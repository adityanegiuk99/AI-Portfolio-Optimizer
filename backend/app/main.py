from fastapi import FastAPI

app = FastAPI(
    title="AI Portfolio Optimizer",
    description="Machine Learning powered portfolio optimization system",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "Portfolio Optimizer API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}