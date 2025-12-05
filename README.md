🚀 FastAPI Backend Project

A lightweight, high-performance backend built using FastAPI and Uvicorn, featuring automatic interactive API documentation with Swagger UI

🛠️ Installation

- Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

- Install Dependencies

```bash
pip install -r requirements.txt
```

- Run the Server

```bash
uvicorn app.main:app --reload
```

- Swagger UI

```url
http://127.0.0.1:8000/docs
```

- Before pushing the code, execute the below script on the commandline (inside your virtual environment)

```bash
pip freeze > requirements.txt
```
