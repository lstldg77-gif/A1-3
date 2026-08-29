# 오늘 뭐 먹지? - AI 메뉴 추천 웹 서비스

AI 웹 개발 미션 제출용 프로젝트입니다.

## 서비스 소개
지역, 먹고 싶은 음식, 1인 예산, 분위기를 입력하면 AI가 메뉴 선택 아이디어 3가지를 제안합니다.

실시간 식당 검색 서비스가 아니라 AI 메뉴 선택 도우미이므로 실제 영업시간·가격은 별도로 확인해야 합니다.

## 기술 스택
- Frontend: HTML / CSS / JavaScript
- Backend: Vercel Serverless Functions / Python
- AI: Google Gemini API
- Deployment: Vercel
- Repository: GitHub

## 폴더 구조
```text
index.html
css/style.css
js/app.js
api/recommend.py
docs/service_plan.md
docs/submission_checklist.md
.env.example
.gitignore
requirements.txt
vercel.json
```

## 로컬 실행
Python 3.12 권장.
```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
npm install -g vercel
vercel dev
```
브라우저에서 http://localhost:3000 접속.

## 환경 변수
`.env.example`을 참고해 `GEMINI_API_KEY`를 설정합니다. 실제 키는 GitHub에 올리지 않습니다. Vercel의 Environment Variables에도 등록합니다.

## GitHub
```bash
git init
git add .
git commit -m "feat: initial AI menu recommendation service"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

## Vercel
GitHub 저장소를 Import → Environment Variables에 GEMINI_API_KEY 등록 → Deploy → 실제 URL 테스트.

## 테스트
- 정상: 대전 유성구 / 국밥 / 1~2만원 / 가족 식사
- 빈 입력: 필수값 안내 확인
- API 오류: 잘못된 키를 사용하는 테스트 환경에서 오류 안내 확인
- 지연: 프론트 25초 타임아웃 안내 확인

## 제출 전 수정
README의 GitHub URL https://github.com/lstldg77-gif/A1-3/blob/main/README.md

Vercel URL https://vercel.com/lstldg77-gif

##각 기능별 설명
1. 웹의 뼈대와 데이터가 움직이는 길 (HTML/CSS/JS & Fetch)

설명할 내용:

"웹사이트는 역할이 정확히 나뉘어 있습니다. HTML은 뼈대(건물 구조), CSS는 인테리어(디자인), JavaScript는 스위치나 자동문 같은 '동작'을 담당하죠.
사용자가 웹 화면에 무언가를 입력하고 버튼을 누르면, JavaScript가 그 입력을 가로채서 서버로 던져주는 **fetch(요청)**를 보냅니다. 서버가 그에 맞는 결과를 주면, JavaScript가 다시 받아서 화면을 새로고침 없이 슥 바꿔주는 것이 현대 웹의 흐름입니다."

2. 서버리스와 프론트-백엔드 연결 (Vercel Serverless Functions)

설명할 내용:

"옛날에는 웹사이트를 만들려면 24시간 켜져 있는 커다란 컴퓨터(서버)가 필요했지만, 지금은 Vercel 같은 서버리스(Serverless) 플랫폼을 씁니다.
사용자가 요청할 때만 잠시 컴퓨터(파이썬 코드)가 깨어나서 일하고 사라지는 구조예요. 그래서 프론트엔드 화면에서 파이썬으로 된 백엔드 로직을 아주 가볍고 쉽게 호출할 수 있습니다."

3. API 키와 보안 (환경 변수)

설명할 내용:

"AI 모델이나 외부 서비스를 쓸 때 쓰는 API 키는 내 집의 마스터키와 같습니다. 이걸 코드에 그대로 적어서 인터넷에 올리면 전 세계 사람이 다 보게 돼요.
그래서 키를 소스 코드에서 분리해 **'환경 변수(Environment Variables)'**라는 안전한 금고에 숨겨두고, 시스템 내부에서만 살짝 꺼내 쓰도록 관리해야 합니다."

4. 개발과 실전 서비스 (로컬 환경 vs 배포 환경)

설명할 내용:

"내 컴퓨터에서 테스트할 때는 잘 되던 게 실제 인터넷에 올리면(배포) 안 되는 경우가 있습니다. 이걸 로컬 환경과 배포 환경의 차이라고 하죠.
배포 후 문제가 생기면 로그를 확인해 원인을 찾고, 코드를 고친 뒤 다시 배포(Re-deploy) 버튼을 눌러 서비스를 업데이트하는 사이클을 직접 겪어보며 서비스 운영 감각을 익혔습니다."

5. AI 코딩 도구 활용과 디버깅

설명할 내용:

"코딩을 AI가 다 해준다고 해서 사람이 놀고먹는 게 아닙니다. AI가 짜준 코드에 에러가 나거나 원하는 대로 안 움직일 때, 어느 부분이 잘못됐는지 원인(로그나 에러 메시지)을 파악할 수 있어야 해요.
'여기가 문제니 이렇게 고쳐줘'라고 정확한 방향을 말로 지시하고 협업하는 능력이 진짜 실력입니다."
