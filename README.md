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
README의 GitHub URL과 Vercel URL을 실제 값으로 교체하고 docs/evidence에 실제 캡처를 넣으세요.
