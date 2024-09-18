FROM python:3.9-slim-bookworm

RUN apt-get update && apt-get install -y graphviz

WORKDIR /app

COPY . /app

RUN pip install streamlit graphviz

CMD ["python","-m","streamlit","run","./main.py"] 
