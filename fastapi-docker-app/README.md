# 🚀 FastAPI + Docker Project

## ✅ Project Goal
Build a simple FastAPI app with:
- **GET** `/` → Returns `"Hello World"`
- **POST** `/hello` → Accepts a name and returns `"Hello {name}"`

---

## 📁 Project Structure
```
fastapi-docker-app/
├── app/
│   └── main.py
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── .venv/  (virtual environment, auto-ignored)
```

---

## 📜 Step-by-Step Setup

### 1. Initialize FastAPI App

**`app/main.py`**
```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/hello")
async def say_hello(request: Request):
    body = await request.json()
    name = body.get("name", "stranger")
    return {"message": f"Hello {name}"}
```

---

### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv .venv
.venv\Scripts\activate  # For Windows
```

---

### 3. Install FastAPI & Uvicorn
```bash
pip install fastapi uvicorn
```

---

### 4. Generate `requirements.txt`
```bash
pip freeze > requirements.txt
```

---

### 5. Create `.dockerignore`
```dockerignore
__pycache__/
*.pyc
.venv/
.env
```

---

### 6. Create `Dockerfile`
```Dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### 7. Build Docker Image
```bash
docker build -t fastapi-app .
```

---

### 8. Run Docker Container
```bash
docker run -d -p 8000:8000 fastapi-app
```

---

### 9. Test the API

#### ✅ GET `/`
```bash
curl http://127.0.0.1:8000/
```
**Response:**
```json
{
  "message": "Hello World"
}
```

#### ✅ POST `/hello`
```bash
curl -X POST http://127.0.0.1:8000/hello \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Umesh\"}"
```
**Response:**
```json
{
  "message": "Hello Umesh"
}
```

---

## 🏁 Done!
You’ve just containerized a FastAPI app with Docker. 🎉  
Let me know if you want to extend it with database support, Docker Compose, or serverless deployment!