# Attendance Automation System

This repository contains a simple QR-based attendance system for academies. Students scan a QR code that opens a URL like:

```
http://<server-address>/attendance?student_id=<STUDENT_ID>
```

When the endpoint is hit, the server records the attendance in a local SQLite database and sends a KakaoTalk notification to the registered channel.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Edit `attendance/config.py` and insert your KakaoTalk API token.
3. Run the server:
   ```bash
   python attendance/app.py
   ```

## Files

- `attendance/app.py` – Flask application handling attendance events.
- `attendance/database.py` – SQLite helpers.
- `attendance/config.py` – KakaoTalk API configuration (fill in your token).

## Usage

Generate QR codes that point to the `/attendance` endpoint with the `student_id` query parameter. When a student scans their code, their attendance will be stored and a notification sent.
