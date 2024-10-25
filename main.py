from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
  return {'data': {'name': 'Sarthak'}}

# FastAPI đọc theo từng hàng từ đầu đến cuối, match đến cái nào là sẽ vào cái đó

@app.get('/blog/unpublished')
def unpublished():
  return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
  # fetch blog with id = id
  return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int):
  # fetch comments of blog with id = id
  return {'data': ['1', '2']}


if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)
