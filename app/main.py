from fastapi import FastAPI


app = FastAPI()

@app.get("/good")
def get_day():
    return "hello world"
