from flask import Flask
from housing.logger import logging
import sys
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/",methods=["GET","POST"]) #get means the parametrs appear in the url and in post it goes to the headers and it doesnt appear in the url. so thats the change. 
def index():
    # try:
    #     raise Exception("We are testing the exception")
    
    # except Exception as e:
    #     # housing = HousingException(e,sys) #created an object of the class
    #     raise HousingException(e,sys) from e

        # logging.info(housing.error_message) #housing is an object and error_message is the attribute of the class HousingException
        # logging.info(" testing logging file")


    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)