from fastapi import FastAPI

from schemas import Blog
app = FastAPI()


# khi chuyển sang pydantic thì các tham số được gom vào requestbody thay vì query
@app.post('/blog')
def create(request: Blog):
  return request


if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.2", port=9000)
