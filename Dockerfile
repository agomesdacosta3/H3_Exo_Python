FROM python:3.8.10

EXPOSE 8501

WORKDIR /app

COPY . .

ENTRYPOINT ["streamlit", "run", "football.py", "--server.port=8501", "--server.address=0.0.0.0"]
