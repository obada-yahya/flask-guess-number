from random import randint
from flask import Flask

app = Flask(__name__)
special_number = randint(0, 9)


@app.route("/")
def say_hello():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route("/guess/<int:num>")
def check(num):
    if num == special_number:
        return "<h1 style='color:green'>You Found Me!!!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif num > special_number:
        return "<h1 style='color:green'>Too High, Try Again!!!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color:green'>Too Low, Try Again!!!</h1>" \
               "<img src=' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
