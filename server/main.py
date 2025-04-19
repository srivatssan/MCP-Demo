from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
import json
import asyncio

app = FastAPI()

@app.post("/rpc")
async def handle_rpc(request: Request):
    data = await request.json()
    method = data.get("method")
    if method == "tools/list":
        return JSONResponse({
            "jsonrpc": "2.0",
            "result": [
                {
                    "name": "greet",
                    "description": "Greets the user",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}
                        },
                        "required": ["name"]
                    }
                }
            ],
            "id": data.get("id")
        })
    elif method == "tools/call":
        params = data.get("params", {})
        name = params.get("name", "world")
        result = {"message": f"Hello, {name}!"}
        return JSONResponse({
            "jsonrpc": "2.0",
            "result": result,
            "id": data.get("id")
        })
    else:
        return JSONResponse({
            "jsonrpc": "2.0",
            "error": {
                "code": -32601,
                "message": "Method not found"
            },
            "id": data.get("id")
        })

@app.get("/events")
async def sse():
    async def event_stream():
        while True:
            await asyncio.sleep(5)
            yield f"data: {{'event': 'heartbeat'}}\n\n"
    return StreamingResponse(event_stream(), media_type="text/event-stream")
