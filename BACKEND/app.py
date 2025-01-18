from flask import Flask

app = Flask(__name__)
port = 3000

@app.route('/')

def home():
    """ 
    Handles the home page route.

     Returns:      None
    """
    return 


if __name__ == '__main__':
    app.run(debug=True, port=port)