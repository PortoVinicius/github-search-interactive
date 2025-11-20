FROM python:3.12-slim

WORKDIR /app

COPY search.py .

RUN pip install requests

CMD ["python", "search.py"]
