#os with python 3.7 installed.
FROM python:3.7   

#copy all the files from the cwd ie. "." to the app folder.
COPY  .  /app

WORKDIR /app

RUN pip install -r requirements.txt

#port would be specified while running the dockerfile
EXPOSE $PORT  

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app


