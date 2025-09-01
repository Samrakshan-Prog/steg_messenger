import struct
from PIL import Image
MAGIC = b"STEG"         
HEADER_FMT = "<I"        
def _ensure_rgb(img: Image.Image) -> Image.Image:
    if img.mode != "RGB":
        return img.convert("RGB")
    return img
def _bits_to_bytes(bits_iter, nbytes: int) -> bytes:
    """Read nbytes from iterator of bits (lsb-first)."""
    out = bytearray()
    try:
        for _ in range(nbytes):
            byte = 0
            for bit_index in range(8):
                bit = next(bits_iter)
                byte |= (bit & 1) << bit_index
            out.append(byte)
    except StopIteration:
        raise ValueError("Not enough data in image to reconstruct message.")
    return bytes(out)
def encode_message_in_image(image_path: str, message: bytes, output_path: str) -> dict:
    img = Image.open(image_path)
    img = _ensure_rgb(img)
    pixels = list(img.getdata())

    # Prepare data: header = MAGIC + length
    header = MAGIC + struct.pack(HEADER_FMT, len(message))
    payload = header + message
    bits = []
    for byte in payload:
        for bit_index in range(8):
            bits.append((byte >> bit_index) & 1)
    capacity = len(pixels) * 3  # 3 channels per pixel
    if len(bits) > capacity:
        raise ValueError("Message too large for this image.")
    flat_channels = []
    for r, g, b in pixels:
        flat_channels.extend([r, g, b])
    for i, bit in enumerate(bits):
        flat_channels[i] = (flat_channels[i] & ~1) | bit
    new_pixels = [tuple(flat_channels[i:i + 3]) for i in range(0, len(flat_channels), 3)]
    img.putdata(new_pixels)
    img.save(output_path)
    return {
        "width": img.width,
        "height": img.height,
        "capacity_bytes": capacity // 8,  # bits → bytes
        "used_bytes": len(payload),
        "saved_as": output_path
    }
def decode_message_from_image(image_path: str) -> bytes:
    img = Image.open(image_path)
    img = _ensure_rgb(img)
    pixels = list(img.getdata())
    flat_channels = []
    for r, g, b in pixels:
        flat_channels.extend([r, g, b])
    def lsb_iter():
        for ch in flat_channels:
            yield ch & 1
    bits = lsb_iter()
    header_len = len(MAGIC) + struct.calcsize(HEADER_FMT)
    header_bytes = _bits_to_bytes(bits, header_len)
    if not header_bytes.startswith(MAGIC):
        raise ValueError("No valid stego header found (MAGIC mismatch).")
    length = struct.unpack(HEADER_FMT, header_bytes[len(MAGIC):])[0]
    if length < 0:
        raise ValueError("Invalid payload length in header.")
    payload = _bits_to_bytes(bits, length)
    return payload

