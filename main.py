from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize Gemini via LangChain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)
memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory, verbose=False)

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(message: Message):
    reply = chain.run(message.message)
    return JSONResponse(content={"reply": reply})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
