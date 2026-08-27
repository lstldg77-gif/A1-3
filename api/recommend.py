import json
import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from openai import OpenAI

app = FastAPI()
PROJECT_ROOT = Path(__file__).resolve().parent.parent

app.mount("/css", StaticFiles(directory=PROJECT_ROOT / "css"), name="css")
app.mount("/js", StaticFiles(directory=PROJECT_ROOT / "js"), name="js")


@app.get("/", include_in_schema=False)
async def index():
    return FileResponse(PROJECT_ROOT / "index.html")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)

SYSTEM_PROMPT = """당신은 한국어 메뉴 추천 도우미입니다.

사용자가 입력한 지역, 음식, 예산, 분위기를 참고하여 '메뉴 선택 아이디어'를 제안하세요.

특정 식당의 현재 영업 여부, 실제 가격, 재고 등 확인되지 않은 사실은 단정하지 마세요.

반드시 아래 JSON 구조만 반환하세요.

{
  "summary": "한두 문장의 요약",
  "recommendations": [
    {
      "menu": "메뉴 이름",
      "reason": "추천 이유",
      "tips": [
        "선택 팁 1",
        "선택 팁 2"
      ]
    }
  ]
}

추천은 정확히 3개를 만드세요.
"""

@app.post("/api/recommend")
async def recommend(request: Request):
    try:
        # 1. API 키 확인
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return JSONResponse(
                status_code=500,
                content={"error": "서버에 OPENAI_API_KEY가 설정되지 않았습니다."}
            )

        # 2. JSON 데이터 읽기
        try:
            payload = await request.json()
        except Exception:
            return JSONResponse(
                status_code=400,
                content={"error": "요청 데이터가 없거나 올바른 JSON이 아닙니다."}
            )

        # 3. 사용자 입력 추출
        region = str(payload.get("region", "")).strip()
        food = str(payload.get("food", "")).strip()
        budget = str(payload.get("budget", "")).strip()
        mood = str(payload.get("mood", "")).strip()

        # 4. 필수 입력값 확인
        if not region or not food or not budget:
            return JSONResponse(
                status_code=400,
                content={"error": "지역, 음식, 예산은 필수 입력값입니다."}
            )

        # 5. AI에게 전달할 사용자 요청 프롬프트
        prompt = f"""
지역: {region}
먹고 싶은 음식: {food}
1인 예산: {budget}
원하는 분위기: {mood or "특별한 조건 없음"}
"""

        # 6. OpenAI 클라이언트 생성 및 호출
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        output_text = response.choices[0].message.content.strip()
        if not output_text:
            return JSONResponse(
                status_code=502,
                content={"error": "AI가 빈 응답을 반환했습니다."}
            )

        # 7. JSON 변환 및 유효성 검증
        result = json.loads(output_text)
        recommendations = result.get("recommendations")

        if not isinstance(recommendations, list) or len(recommendations) != 3:
            raise ValueError("AI 추천 결과가 올바르지 않거나 3개가 아닙니다.")

        return JSONResponse(status_code=200, content=result)

    except json.JSONDecodeError:
        return JSONResponse(
            status_code=502,
            content={"error": "AI 응답을 JSON으로 처리하지 못했습니다. 다시 시도해주세요."}
        )
    except Exception as error:
        print("SERVER ERROR:", error)
        return JSONResponse(
            status_code=500,
            content={"error": "AI 서버 처리 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요."}
        )

# Vercel이 요구하는 ASGI 애플리케이션 인터페이스 등록
handler = app