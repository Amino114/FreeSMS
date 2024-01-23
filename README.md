# SMS Gateway Web Interface

This Python-based web application, "SMS Gateway Web Interface", uses Flask and Mocean's SDK to provide a user-friendly interface for sending SMS messages. It also includes a Discord bot as an additional feature, which listens for commands in a Discord server and sends SMS messages when instructed to do so.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Flask
- Discord bot library (selfcord)
- Mocean's SDK
- A `.env` file with your API key, API secret, and bot token
- Waitress (a WSGI server)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Amino114/FreeSMS.git
   ```
2. Install Python packages
   ```sh
   pip install flask selfcord.py moceansdk python-dotenv waitress
   ```
3. Enter your API in `.env`
   ```sh
   API_KEY = 'ENTER YOUR API'
   API_SECRET = 'ENTER YOUR SECRET'
   TOKEN = 'ENTER YOUR TOKEN'
   ```

## Usage

To run the application, use the command:

```sh
waitress-serve --listen=*:8000 app:app
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
