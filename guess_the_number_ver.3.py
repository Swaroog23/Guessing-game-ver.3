from flask import Flask, request


app = Flask(__name__)

html_start = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Guessing game</title>
</head>
<body>
<h1>'Imagine a number between 1 and 1000!</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}">
    <input type="hidden" name="max" value="{}">
    <button type="submit">OK!</button>
</form>
</body>
</html>
"""
# This is the first page player sees, where he is told what to do

"""First page that player sees, telling him what to do"""

main_game = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guessing game</title>
</head>
<body>
    <p>My guess is: {guess}!</p>
    <form action="" method="POST">

        <input type="submit" name="answer" value="Too big!">
        <input type="submit" name="answer" value="Too small!">
        <input type="submit" name="answer" value="You win!">        
        <input type="hidden" name="min" value="{min}">
        <input type="hidden" name="max" value="{max}">
        <input type="hidden" name="guess" value="{guess}">
        
    </form>
</body>
</html>
"""

# Main game page, where computer tries to guess the number

win_screen = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guessing game</title>
</head>
<body>
    <h1>I guessed! Your number is: {guess}</h1>
</body>
</html>
"""

# Win screen, where computer shows you the number you have chosen

@app.route("/", methods=["POST", "GET"])
def guess_num():

    """Main body of the game."""

    if request.method == "GET":

        # Checks the method and in case of GET returns the first page to the player, and hidden values
        # min and max for the game

        return html_start.format(0, 1000)

    else:

        # The function does all of the operations for the game, checks max and min values, calculates the guess,
        # checks the players answer and sends back to user his guess

        minimum = int(request.form.get('min'))
        maximum = int(request.form.get('max'))
        answer = request.form.get("answer")
        guess = int(request.form.get("guess", 500))

        if answer == "Too big!":
            maximum = guess
        elif answer == "Too small!":
            minimum = guess
        elif answer == "You win!":
            return win_screen.format(guess=guess)

        guess = int((maximum - minimum) / 2) + minimum
        return main_game.format(guess=guess, min=minimum, max=maximum)


if __name__ == "__main__":
    app.run(debug=True)
