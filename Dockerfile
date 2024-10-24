#os with python 3.7 installed.
FROM python:3.7   

#copy all the files from the cwd ie. "." to the app folder.
COPY  .  /app

WORKDIR /app

RUN pip install -r requirements.txt

#port would be specified while running the dockerfile #usually flask application would run on 5000, this port varibale would be supplied during deploymnet. # This port is a dynamic one and it gets assigned randomly by the heroku side only.
# this is like an environment variable which would be supplied by heroku end only.
# environment variable is the value whose value is set from the operating system side 
EXPOSE $PORT   

#this command is quivalent to python app.py(used for only tessting purpose.) if you run it on local.
# filename:flask_objectname
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app  


