import random
from flask import Flask, render_template, request

app = Flask(__name__)
secret_number = None
attempts = 0

def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    global attempts
    if request.method == 'POST':
        guess = int(request.form['guess'])
        attempts += 1

        if guess < secret_number:
            message = "Too low!"
        elif guess > secret_number:
            message = "Too high!"
        else:
            message = "Congratulations! You guessed the number in {} attempts.".format(attempts)
            start_game()

        if attempts == 10:
            message = "Sorry, you've reached the maximum number of attempts."
            message += " The secret number was: {}".format(secret_number)
            start_game()

        return render_template('index.html', message=message)
    else:
        return render_template('index.html', message='')

if __name__ == '__main__':
    start_game()
    app.run()

