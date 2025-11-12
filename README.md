# Gmail API Email Sender

This project allows you to send emails automatically through the Gmail API using Python.

## Setup

1. Enable the Gmail API

- Go to Google Cloud Console.

- Create a new project.

- Enable Gmail API under APIs & Services → Library.

- Create OAuth 2.0 Client ID credentials (type: Desktop app).

- Download the credentials.json file.

2. Place files

- Put credentials.json in your project folder.

- The token.json file will be created automatically after the first authorization.

3. Create a .env file

GMAIL_CREDENTIALS_PATH=/absolute/path/to/credentials.json
GMAIL_TOKEN_PATH=/absolute/path/to/token.json

4. Install dependencies

```bash
poetry install
```

5. Run the script
```bash
poetry run python email_sender.py
```

The browser will open for authentication the first time you run it.
