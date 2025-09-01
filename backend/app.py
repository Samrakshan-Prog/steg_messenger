import os
import time
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from stegano_utils import encode_message_in_image, decode_message_from_image  # <- updated names
from crypto_utils import encrypt_message, decrypt_message
from cryptography.fernet import InvalidToken
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
app = Flask(__name__)
CORS(app)
ALLOWED_IMAGE_EXT = {"png", "jpg", "jpeg", "bmp"}
def _allowed(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_IMAGE_EXT
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})
@app.route("/api/hide", methods=["POST"])
def hide():
    if "image" not in request.files:
        return jsonify({"error": "image file is required"}), 400
    if "message" not in request.form:
        return jsonify({"error": "message text is required"}), 400
    file = request.files["image"]
    msg = request.form["message"].strip()
    if not msg:
        return jsonify({"error": "message cannot be empty"}), 400
    if file.filename == "" or not _allowed(file.filename):
        return jsonify({"error": "invalid or missing image file"}), 400
    fname = secure_filename(file.filename)
    ts = int(time.time() * 1000)
    in_path = os.path.join(UPLOAD_DIR, f"{ts}_{fname}")
    file.save(in_path)
    key, token = encrypt_message(msg)
    out_name = f"stego_{ts}.png"
    out_path = os.path.join(OUTPUT_DIR, out_name)
    try:
        encode_message_in_image(in_path, token, out_path)  # <- updated function name
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({
        "message": "success",
        "key": key.decode("utf-8"),
        "download_url": f"/api/download/{out_name}",
    })
@app.route("/api/reveal", methods=["POST"])
def reveal():
    if "image" not in request.files:
        return jsonify({"error": "image file is required"}), 400
    if "key" not in request.form:
        return jsonify({"error": "key is required"}), 400
    key = request.form["key"].strip()
    file = request.files["image"]
    if file.filename == "" or not _allowed(file.filename):
        return jsonify({"error": "invalid or missing image file"}), 400
    fname = secure_filename(file.filename)
    ts = int(time.time() * 1000)
    in_path = os.path.join(UPLOAD_DIR, f"{ts}_{fname}")
    file.save(in_path)
    try:
        token = decode_message_from_image(in_path)
    except ValueError as e:
        return jsonify({"error": f"stego error: {e}"}), 400
    try:
        plaintext = decrypt_message(token, key)
    except InvalidToken:
        return jsonify({"error": "invalid key or corrupted data"}), 400
    return jsonify({
        "message": "success",
        "secret": plaintext
    })
@app.route("/api/download/<path:filename>", methods=["GET"])
def download(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

