from starlette.responses import HTMLResponse
from ellie import getTasks
from fastapi import FastAPI, HTTPException
import uvicorn
import os
import nest_asyncio

nest_asyncio.apply()

DFX_API_KEY = os.environ.get("DFX_API_KEY")
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    message = '<h3>Nope.</h3>'
    return message

@app.get('/getTasks')
def getTaskAPI(authkey: str):
    if authkey == DFX_API_KEY:
        taskList = getTasks()
        return taskList
    else:
        raise HTTPException(status_code=403, detail="Invalid auth key")

# uvicorn.run(app, host="0.0.0.0", port=5005)