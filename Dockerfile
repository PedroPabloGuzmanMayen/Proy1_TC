FROM python:3.9-slim-bookworm

WORKDIR /app

COPY . /app

RUN pip install streamlit

CMD ["python","-m","streamlit","run","./main.py"] 
