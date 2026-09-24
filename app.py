from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Welcome to My Flask Application!</h1>
    <p>Your Flask application is running successfully.</p>
    <a href="/about">About</a>
    """


@app.route("/about")
def about():
    return """
    <h1>About This Application</h1>
    <p>This is a simple web application created using Python and Flask.</p>
    <a href="/">Go Home</a>
    """


if __name__ == "__main__":
    app.run(debug=True)