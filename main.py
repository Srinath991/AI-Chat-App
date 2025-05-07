from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import uvicorn
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env
load_dotenv()

app = FastAPI()

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ✅ Initialize Gemini model via LangChain with conversation memory
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory, verbose=False)

# Pydantic model for input message
class Message(BaseModel):
    message: str

# Home route
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Chat route
@app.post("/chat")
async def chat(message: Message):
    reply = chain.run(message.message)
    return JSONResponse(content={"reply": reply})

# Uvicorn server runner
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
