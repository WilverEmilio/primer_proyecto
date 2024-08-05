import fastapi as _fastapi

app = _fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
