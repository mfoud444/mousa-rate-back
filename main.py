from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def greet_json():
    return {"Hello": "World!"}

@app.get("/get-rate")
def make_post_request():
    url2 = 'https://sarfonlay.com/upadd.php'
    headers2 = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.12.0'
    }
    data2 = {
        'api': 'fONoY+dZVo2MWqykBBU7aCjoRT5uU0NaLa16KEYPnvo='
    }

    response2 = requests.post(url2, headers=headers2, data=data2)
    return response2.json()

