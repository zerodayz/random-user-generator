from flask import Flask, render_template
from apps.create import create

app = Flask("Random User generator")


@app.route('/')
def hello():
    welcome_text = "Hello world!"
    return render_template("hello.html", welcome_text=welcome_text)


app.route('/create', methods=["POST"])(create)


@app.route('/world')
def world():
    welcome_text = "World hello!"
    return welcome_text


if __name__ == "__main__":
    app.run(port=5555)
