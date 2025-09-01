# Steganography + Encryption Messenger

**Live Demos:**

* **Vercel:** https://steg-messenger.vercel.app

---

## Project Overview

Steganography + Encryption Messenger is a web-based application that lets you hide secret messages inside images and reveal them later using a unique key.

The project combines:

* **Steganography:** Hiding data inside an image without noticeable changes.
* **Encryption:** Securing the hidden message with a key.

**Use Case:** You can send confidential information via images without anyone noticing, and the recipient can decrypt it using the key.

---

## Features

* **Encrypt & Hide:**
    * Upload a cover image (PNG/JPG/BMP).
    * Type your secret message.
    * Click “Create Stego Image”.
    * Copy the generated key.
    * Download the stego image safely.
* **Extract & Reveal:**
    * Upload the stego image.
    * Paste the key.
    * Click “Reveal Message”.
    * The hidden message is decrypted and displayed.
* **Preview Images:** See your image before sending it to the backend.
* **Web-Based:** Accessible from any browser.
* **Cross-Platform:** Works on Windows, Mac, Linux.
* **Deployment Ready:** Deploy on Render, Vercel, or any cloud hosting.

---

## Technology Stack

* **Frontend:** AngularJS, HTML, CSS, JavaScript
* **Backend:** Python 3 + Flask
* **Image Handling:** Pillow (Python Imaging Library)
* **CORS Support:** Flask-CORS

---

## File Structure
## 📂 File Structure

```sh
```
steg_messenger/
├── backend/
│   ├── crypto_utils.py     # Encryption and decryption logic
│   ├── app.py              # Flask backend main application
│   └── stegano_utils.py    # Steganography logic
├── frontend/
│   ├── index.html          # AngularJS frontend
│   └── assets/css/style.css # Styles
└── requirements.txt        # Python dependencies

```


---


## Installation & Setup (Local)

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/Samrakshan-Prog/steg_messenger.git](https://github.com/Samrakshan-Prog/steg_messenger.git)
    cd steg_messenger
    ```
2.  **Create a virtual environment and install dependencies**
    ```sh
    python -m venv venv
    source venv/bin/activate        # On Windows use: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  **Run the Flask backend**
    ```sh
    python app.py
    ```
4.  **Open the frontend**
    Open `templates/index.html` in your browser. Update the backend URL in the AngularJS controller:
    ```javascript
    vm.backendBase = 'http://localhost:5000';
    ```
---

## Deployment on Render / Vercel

1.  **Update AngularJS controller:**
    ```javascript
    vm.backendBase = '[https://steg-messenger.onrender.com](https://steg-messenger.onrender.com)'; 
    ```
2.  **Ensure CORS is enabled in Flask backend:**
    ```python
    from flask_cors import CORS
    CORS(app)
    ```
3.  Deploy the Flask backend on Render.
4.  Open your live URL in any browser.

---

## How to Use (Step-by-Step)

### Encrypt & Hide

1.  Go to the **Encrypt & Hide** tab.
2.  Click **“Choose File”** to select your cover image (PNG/JPG/BMP).
3.  Enter your secret message in the text area.
4.  Click **“Create Stego Image”**.
5.  After processing:
    * Copy the generated key (required for decryption).
    * Download the stego image.

**Note:** Always download the stego image exactly as generated; do not compress or edit it.

### Extract & Reveal

1.  Go to the **Extract & Reveal** tab.
2.  Click **“Choose File”** to select the stego image.
3.  Paste the key you received from the sender.
4.  Click **“Reveal Message”**.
5.  The hidden message will be decrypted and displayed.

**Common Errors:**

* `No valid stego header found (MAGIC mismatch)`: The image was modified after encryption, or the wrong key was used.

---

## Tips for Sharing

* Send the stego image **as-is**, do not compress it.
* Share the key **exactly** as shown, including all characters.
* Recommended file transfer: ZIP the image or use cloud storage links (Google Drive, Dropbox).

---

## Contribution

* Fork the repo and make improvements.

## 📜 License

This project is licensed under the **MIT License**. For more details, see the `LICENSE` file in the repository.
