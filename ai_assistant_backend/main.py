from fastapi import FastAPI, Request
from generator import generate_content

app = FastAPI()

@app.post("/generate")
async def run_task(request: Request):
    data = await request.json()
    task_type = data.get("task_type")
    topic = data.get("topic")
    content = generate_content(task_type, topic)
    return {"output": content}