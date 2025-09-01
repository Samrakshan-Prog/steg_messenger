# 🔐 Steganography + Encryption Messenger

**Live Demos:**

* **Vercel:** https://steg-messenger.vercel.app

---

## 📝 Project Overview

Steganography + Encryption Messenger is a web application that hides secret messages inside images and reveals them with a unique key. It combines **steganography** (hiding data in an image without visible changes) and **encryption** (securing the hidden message with a key).

**Use Case:** You can send confidential information via images without anyone noticing, and the recipient can decrypt it using the key.

---

## ⚙️ Features

* **Encrypt & Hide:** Upload an image (PNG/JPG/BMP), type a secret message, and generate a stego image with a unique key.
* **Extract & Reveal:** Upload a stego image, paste the key, and reveal the hidden message.
* **Web-Based & Cross-Platform:** Accessible from any modern browser on Windows, Mac, or Linux.
* **Preview Images:** See a preview of your image before processing.
* **Deployment Ready:** Easily deployable on cloud platforms like Vercel and Render.

---

## 💻 Technology Stack

* **Frontend:** AngularJS, HTML, CSS, JavaScript
* **Backend:** Python 3 + Flask
* **Image Handling:** Pillow (Python Imaging Library)
* **CORS Support:** Flask-CORS

---

## 📂 File Structure
```sh
steg_messenger/
├── backend/
│   ├── crypto_utils.py      # Encryption and decryption logic
│   ├── app.py               # Flask backend main application
│   └── stegano_utils.py     # Steganography logic
├── frontend/
│   ├── index.html           # AngularJS frontend
│   └── assets/css/style.css # Styles
└── requirements.txt         # Python dependencies
```


## 🔧 Installation & Setup (Local)

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Samrakshan-Prog/steg_messenger.git](https://github.com/Samrakshan-Prog/steg_messenger.git)
    cd steg_messenger
    ```
2.  **Set up the environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate    # Use `venv\Scripts\activate` on Windows
    pip install -r requirements.txt
    ```
3.  **Run the backend:**
    ```sh
    python backend/app.py
    ```
4.  **Open the frontend:**
    Open `frontend/index.html` in your browser and update the backend URL in the AngularJS code to `http://localhost:5000`.

---

## 🌐 Deployment

Update the backend URL in `frontend/index.html` to your deployed URL (e.g., `https://steg-messenger.vercel.app`). Ensure **CORS** is enabled in your Flask app.

---

## 🖱️ How to Use (Step-by-Step)

### 1️⃣ Encrypt & Hide

1.  Go to the **Encrypt & Hide** tab.
2.  Select your image.
3.  Enter your secret message.
4.  Click **“Create Stego Image”**.
5.  Copy the generated **key** and download the image.

**⚠️ Note:** Do not compress or edit the downloaded image, as this may corrupt the hidden message.

### 2️⃣ Extract & Reveal

1.  Go to the **Extract & Reveal** tab.
2.  Select the stego image.
3.  Paste the key.
4.  Click **“Reveal Message”** to view the decrypted message.

---

## 🤝 Contribution

* Feel free to **fork** the repository and submit pull requests with improvements.
* Report issues or suggest features via the **GitHub issues** page.

---

## 📜 License
This project is licensed under the **MIT License**. For more details, see the `LICENSE` file in the repository.
