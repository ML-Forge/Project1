from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET","POST"]) #get means the parametrs appear in the url and in post it goes to the headers and it doesnt appear in the url. so thats the change. 
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)