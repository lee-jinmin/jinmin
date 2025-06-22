# AI 수학 튜터 웹 애플리케이션

이 프로젝트는 고등학교 상위권 학생이 수능 수학 1등급을 받을 수 있도록 돕는
AI 튜터 챗봇의 간단한 웹 애플리케이션 예제입니다.

## 주요 기능
- 사용자가 입력한 질문을 OpenAI API로 전송하여 답변을 받아옵니다.
- 한국어 기반의 시스템 프롬프트를 사용하여 친절하고 구조적인 설명을 제공합니다.

## 실행 방법
1. Python 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```
2. 환경 변수 `OPENAI_API_KEY`에 OpenAI API 키를 설정합니다.
   `.env` 파일을 사용해도 됩니다.
3. Flask 개발 서버 실행:
   ```bash
   flask run
   ```
4. 브라우저에서 `http://localhost:5000`에 접속합니다.

## 파일 구조
- `app.py` : Flask 애플리케이션 실행 파일
- `templates/index.html` : 기본 HTML 페이지
- `static/style.css` : 간단한 스타일 시트

개발 용도로 만든 간단한 예제이므로 필요에 맞게 확장해 사용하세요.
