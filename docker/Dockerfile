FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD app/ /app/
RUN pip install -r requirements.txt

EXPOSE 6050
CMD ["python", "/app/main.py"]
