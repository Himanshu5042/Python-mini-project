
# 📱 QR Code Generator Using Python

A simple and interactive QR Code Generator built using Python and Streamlit.

This application allows users to generate customized QR codes for website URLs, text, email addresses, phone numbers, and Wi-Fi networks. Users can customize QR code colors and download the generated image in PNG format.

## 🚀 Features

- Generate QR codes for website URLs.
- Convert text into QR codes.
- Generate email QR codes.
- Create phone number QR codes.
- Generate Wi-Fi connection QR codes.
- Customize QR code colors.
- Customize background colors.
- Adjust QR code size and border.
- Download QR codes as PNG images.
- Simple and user-friendly interface.

## 🛠️ Technologies Used

- Python
- Streamlit
- qrcode
- Pillow

## 📦 Python Libraries

| Library | Purpose |
|---|---|
| Streamlit | Create the web interface |
| qrcode | Generate QR codes |
| Pillow | Process and save QR images |

## 📁 Project Structure

```text
qr-code-generator/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 💻 Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/himanshu-verma/qr-code-generator.git
```

### Step 2: Open the project folder

```bash
cd qr-code-generator
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install required libraries

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
streamlit run main.py
```

The application will open in your default web browser.

## 📖 How to Use

1. Open the QR Code Generator application.
2. Select the QR code type.
3. Enter your information.
4. Choose your QR code color.
5. Select a background color.
6. Adjust the QR code size and border.
7. Click Generate QR Code.
8. Preview your QR code.
9. Click Download QR Code to save it as a PNG image.

## 🎯 Example Uses

- Website links
- Contact information
- Email addresses
- Wi-Fi network access
- Event information
- Personal messages
- Business cards

## 🧠 Learning Outcomes

By completing this project, you will learn:

- Python functions and conditional statements.
- Working with third-party Python libraries.
- Generating QR codes programmatically.
- Processing images using Pillow.
- Handling image data using BytesIO.
- Creating interactive applications with Streamlit.
- Providing downloadable files in a web application.

## 🔮 Future Improvements

- Add logo insertion in QR codes.
- Add QR code history.
- Generate QR codes in SVG format.
- Support bulk QR code generation.
- Add QR code scanning functionality.
- Add downloadable QR code PDF files.

## ⚠️ Important Note

Test your generated QR code with a QR scanner before sharing it.

Avoid putting confidential information, passwords, or sensitive personal data into QR codes that may be shared publicly.

## 👨‍💻 Developer

**Himanshu Verma**

GitHub: https://github.com/himanshu-verma

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you like this project, consider giving it a star on GitHub!
