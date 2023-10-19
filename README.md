# SMS Sender Flask App

This is a simple Flask web application for sending SMS messages. Users can input the sender's name, recipient's phone number, and message text through a form on the website. The application provides validation hints to guide users in filling out the form correctly. After submitting the form, a status message is displayed, indicating the success or failure of the SMS sending process. The page reloads after 3 seconds.

## Prerequisites
- Python 3.10
- Flask
- Waitress

## Getting Started

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**

   Make sure you have Python 3.10 installed. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   waitress-serve --listen=*:8000 app:app
   ```

   The application will be accessible at `http://localhost:8000`.

## Usage

1. Access the application through your web browser.

2. Fill out the form fields:
   - **Sender Name:** At least two letters and spaces allowed.
   - **Recipient Number:** Numeric, 10 to 15 digits allowed.
   - **Message Text:** Up to 160 characters allowed.

3. Click the "Send SMS" button to submit the form.

4. Wait for the status message to appear. The page will automatically reload after 3 seconds.

## Contributing

If you want to contribute to this project and make it better, feel free to fork and create a pull request. Your contributions are always welcome!

---

