## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y  # -p means path ie. (the virtual environment's path) called venv gets created in this folder itself. # with -n the virtual environment gets created in the anaconda folder. 
```
```
conda activate venv/ # venv is in the current folder thats why. 
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .  # this adds all the files to the git which has changed. " . " is referring to all files. 
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file -- write like <filename>/ eg. venv/

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github #origin is just a placeholder for this string "https://github.com/NikitaaArora/ML_project1.git"
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = a52@gmail.com
2. HEROKU_API_KEY = 
3. HEROKU_APP_NAME = ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .  # "dot" is for the current working directory ie. the dockerfile is present in the current working directory.
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678  # this number is the id of the docker image created. e is the environment variable usually we run app on 5000. 
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```


# U is for untracked files meaning - those files are still not added in the github repo. to add them simply do git add <filename>
# git commit is to commit that version.
# git log is to read all the commit messages for all the versions you created. 
