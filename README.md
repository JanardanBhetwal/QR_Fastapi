# QR FastAPI

## Overview

QR FastAPI is a lightweight and efficient application for generating QR codes. Built with Python and FastAPI, it provides a simple API interface for QR code operations, making it easy to integrate into other applications or use as a standalone service.

## Features

- Generate QR codes with custom text or URLs.
- Fast and scalable API using FastAPI.

---

## How to Run

### Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerized deployment)

### Running Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/JanardanBhetwal/QR_Fastapi.git
   cd QR_Fastapi
   ```

2. Install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   cd backend
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

---

<!-- ### Running with Docker

1. Build the Docker image:

   ```bash
   docker build -t qr-fastapi .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 qr-fastapi
   ```

--- -->

Then open http://127.0.0.1:8000/api/v1/utils/qr?data=https://github.com/JanardanBhetwal/ in your browser.

## Usage

The QR FastAPI application allows you to generate QR codes by passing any value to the `data` query parameter in the API endpoint. For example:

```bash
http://127.0.0.1:8000/api/v1/utils/qr?data=YourCustomValue
```

Replace `YourCustomValue` with any text, URL, or data you want to encode into a QR code. The API will return the QR code image that you can use or download.

### Example

To generate a QR code for a URL:

```bash
http://127.0.0.1:8000/api/v1/utils/qr?data=https://example.com
```

To generate a QR code for custom text:

```bash
http://127.0.0.1:8000/api/v1/utils/qr?data=HelloWorld
```

You can use this feature to create QR codes for links, messages, or any other data you need.

## Configuration and Setup Notes

- **Environment Variables**:
  You can configure the application using the following environment variables:

  - `HOST`: The host address (default: `127.0.0.1`).
  - `PORT`: The port number (default: `8000`).

- **Dependencies**:
  Ensure all dependencies listed in `requirements.txt` are installed if running locally.

- **Testing**:
  Run the test suite using:
  ```bash
  pytest
  ```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

---
