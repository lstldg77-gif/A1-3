# 서비스 기획서 — 오늘 뭐 먹지?

## 1. 서비스 개요
- 서비스명: 오늘 뭐 먹지?
- 목적: 식사 선택이 어려운 사용자가 몇 가지 조건만 입력하여 AI의 메뉴 선택 아이디어를 받는다.
- 타겟: 직장인, 가족 외식 사용자, 혼밥 사용자 등
- 핵심 가치: 검색 시간을 줄이고 선택 기준을 정리한다.

## 2. 페이지/섹션
1. 홈: 서비스 소개와 AI 추천 시작
2. AI 추천: 입력 폼과 AI 결과
3. 이용 안내: 동작 흐름과 주의사항

## 3. AI 기능
입력: 지역, 음식, 예산, 분위기
출력: 요약, 메뉴 3개, 추천 이유, 선택 팁

## 4. 실패 처리
- 빈 입력: 필수값 안내
- API 오류: 서버 오류 안내
- 지연: 25초 타임아웃 안내
- 너무 큰 입력: 413 안내

## 5. 기술 구조
사용자 → HTML/CSS/JavaScript → fetch('/api/recommend') → Vercel Python Serverless Function → Google Gemini API → JSON → JavaScript 화면 출력

## 6. 보안
API 키는 브라우저 코드에 넣지 않고 서버 환경변수 OPENAI_API_KEY로 관리하며 .env는 .gitignore에 포함한다.

## 7. 반응형
CSS media query로 모바일/태블릿/데스크톱에 맞게 레이아웃을 변경한다.

## 8. 발표 설명
HTML은 구조, CSS는 디자인/반응형, JavaScript는 입력·fetch·결과 표시, Python Function은 API 키를 숨기고 AI를 호출하는 백엔드 역할을 한다.
