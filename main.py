from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
def index():
  return {'data': {'name': 'Sarthak'}}

# FastAPI đọc theo từng hàng từ đầu đến cuối, match đến cái nào là sẽ vào cái đó

@app.get('/blog')
# Optional từ thư viện typing được sử dụng để khai báo rằng một biến có thể nhận giá trị của kiểu dữ liệu đã chỉ định hoặc nếu kh truyền thì nhận giá trị None.
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
  # Chỉ lấy 10 blog đã được xuất bản (published)
  if published:
    return {'data': f'{limit} published blogs from the db'}
  else:
    return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
  return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
  # fetch blog with id = id
  return {'data': id}

@app.get('/blog/{id}/comments')
# FAPI vẫn phân biệt được đâu là path đâu là query mặc dù đặt cạnh nhau
def comments(id: int, limit=10):
  # fetch comments of blog with id = id
  return {'data': ['1', '2'], "limit": limit}


class Blog(BaseModel):
  title: str
  body: str
  published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
  return {'data': f"Blog is created with title: {request.title}"}


if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)
