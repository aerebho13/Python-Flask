from flask import Flask  
# from the flask module import the Flask class.


app = Flask(__name__)  
#create an instance of "Flask" into app.
# the "app" variable is also considered an "object".

@app.get("/")  
# flask decorator that allows us to map "/" to index
def index(): 
#python function - in flask this is a "view function"

    me = {   
#python dictionary containing key-value pairs.
        "first_name": "Aaron",
        "last_name": "Erebholo",
        "hobbies": "Basketball",
        "active": True
    }
    return me     
#returns statement. flask converts dict to JSON