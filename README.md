## Secret Message Web App with Flask

This Flask application allows users to send encrypted messages with an image attachment through email.

**Features:**

* Encrypts messages using a simple Caesar cipher (shift by 3).
* Generates an image with the encrypted message embedded.
* Sends the encrypted message and image as an email attachment.
* User enters recipient's email address and message to send.

**Technical Stack:**

* Flask: Web framework for building web applications in Python.
* Pillow (PIL Fork): Python Imaging Library for image processing.
* smtplib: Python library for sending emails.
* Email MIME classes: Used to construct email messages with text and attachments.

**Usage:**

1. **Prerequisites:**
    * Python 3
    * Flask (`pip install Flask`)
    * Pillow (`pip install Pillow`)
    * smtplib (included in standard library)
2. **Setup:**
    * Replace `'YourEmail@gmail.com'` in the code with your actual email address.
    * Ensure you have enabled "Less secure app access" in your Gmail settings if necessary.
    * Place two image files in the project directory:
        * `Secret Message.png`: The background image for the encrypted message.
        * `secret.png` (temporary file): This will be overwritten with the generated image.
3. **Run the application:**
    * Open a terminal and navigate to the project directory.
    * Run `python app.py`. This will start the Flask development server.

**Security Considerations:**

* This project uses a simple Caesar cipher for encryption, which is not secure for real-world scenarios. It's intended for educational or entertainment purposes only.
* Store email credentials securely using environment variables (`os.environ.get('EMAIL')`, `os.environ.get('PASS_KEY')`).
* Consider implementing more robust encryption methods and user authentication for a production application.

**Further Enhancements:**

* Implement stronger encryption algorithms.
* Allow users to customize the image background or add watermarks.
* Integrate with a password reset mechanism for the recipient to decrypt the message.

**Disclaimer:**

This project is provided for educational purposes only. The author is not responsible for any misuse or security vulnerabilities associated with the code.
