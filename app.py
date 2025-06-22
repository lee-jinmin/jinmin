import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

SYSTEM_PROMPT = (
    "너는 고등학교 상위권 여학생이 수능 수학에서 1등급을 받을 수 있도록 돕는 AI 수학 튜터야. "
    "친절하고 따뜻하지만, 구조적이고 논리적인 설명을 제공해야 해."
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_prompt = request.form.get('prompt', '')
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ]
        )
        answer = response.choices[0].message['content'].strip()
    except Exception as e:
        answer = f"Error: {e}"
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True)
