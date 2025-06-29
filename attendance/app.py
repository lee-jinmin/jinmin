from flask import Flask, request, jsonify
from datetime import datetime
import requests
import os

from database import init_db, add_attendance
from config import KAKAO_API_TOKEN, KAKAO_API_URL

app = Flask(__name__)
init_db()


def send_kakao_message(student_id, timestamp):
    """Send attendance notification via KakaoTalk."""
    headers = {
        "Authorization": f"Bearer {KAKAO_API_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "template_object": f"{{'object_type':'text','text':'{student_id} checked in at {timestamp}','link':{{}}}}"
    }
    try:
        response = requests.post(KAKAO_API_URL, headers=headers, data=data)
        response.raise_for_status()
    except Exception as e:
        app.logger.error(f"Failed to send KakaoTalk message: {e}")

@app.route('/attendance')
def attendance():
    student_id = request.args.get('student_id')
    if not student_id:
        return jsonify({'error': 'student_id is required'}), 400
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    add_attendance(student_id, timestamp)
    send_kakao_message(student_id, timestamp)
    return jsonify({'status': 'success', 'student_id': student_id, 'timestamp': timestamp})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
