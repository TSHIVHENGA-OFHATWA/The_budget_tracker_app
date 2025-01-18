from flask import Flask, render_template

app = Flask(__name__)
port = 3000

@app.route('/')
def home():
    """ 
    Handles the home page route.

     Returns: None
    """
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, port=port)