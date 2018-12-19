import sqlite3  # Import sql
from flask import Flask, render_template, request


app = Flask(__name__)  # create app object


# Database: Read Data
connection = sqlite3.connect("questions.db")  # Connect to db
crsr = connection.cursor()  # Create cursor object
myResult = crsr.execute("SELECT * FROM quest;")  # Execute a statement

# Generieren der Frage-Liste
items = []
for row in myResult:
    items.append(
        {'Index': row[0], 'q': row[1], 'a': row[2], 'b': row[3], 'c': row[4], 'd': row[5], 'ans': row[6], 'id': row[7]})

# Zählt die richtigen Antworten
count = 0

# Request-Handler --> Alle Anfragen gehen derzeit über die Root
@app.route("/")
def index():
    global count
    count = 0
    return render_template('index.html')


@app.route("/quiz")
def quiz():
    # get arguments
    cq = request.args.get('cq', 0, type=int)  # current question
    pq = request.args.get('pq', -1, type=int)  # previous question
    pq_answer = request.args.get('answer', None, type=str)  # previous question
    global count

    # check if answer to previous question was correct
    pq_correct = -1
    if 0 <= pq < len(items):
        if pq_answer == items[pq]['ans']:
            pq_correct = 1
            count += 1

    else:
        pq_correct = 0

    # check if the currently requested question does exist
    if 0 <= cq < len(items):
        nextQuestion = -1 if cq + 1 >= len(items) else cq + 1
        return render_template('quiz.html', cq=cq, myVariable=items[cq], nq=nextQuestion, pq_correct=pq_correct, pq = pq, count = count, answerVar = items[cq]['ans'])
    elif cq == -1:
        return render_template('quiz.html', cq=cq, myVariable=None, nq=None, pq_correct=pq_correct, pq=pq, count = count, answerVar = items[cq]['ans'])
    else:
        return "Question doesn't exist"


if __name__ == '__main__':
    app.run(debug=True)

# To save changes
connection.commit()

# Close the connection
connection.close()

# Referenzen
## http://flask.pocoo.org/docs/1.0/quickstart/#variable-rules
## http://jinja.pocoo.org/docs/2.10/templates/#variables
## http://127.0.0.1:5000

# Offene Tasks
## Layout anpassen
## Animationen hinzufügen
