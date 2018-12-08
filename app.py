import sqlite3 # Import sql
from flask import Flask, render_template, request

app = Flask(__name__) # create app object

# Database: Read Data
connection = sqlite3.connect("questions.db") # Connect to db
crsr = connection.cursor() # Create cursor object
myResult = crsr.execute("SELECT * FROM quest;") # Execute a statement

# Generieren der Frage-Liste
items = []
for row in myResult:
	items.append({'Index': row[0], 'q': row[1], 'a': row[2], 'b': row[3], 'c': row[4], 'd': row[5], 'ans': row[6], 'id': row[7]})


# Request-Handler --> Alle Anfragen gehen derzeit über die Root
@app.route("/")
def index():
    currentQuestion = request.args.get('cq', 0, type=int)
    # Es wird noch nicht geprüft ob die gegebene Antwort korrekt ist :)

    if currentQuestion >= 0 and currentQuestion < len(items):
        nextQuestion = -1 if currentQuestion + 1 >= len(items) else currentQuestion + 1
        return render_template('index.html', myVariable = items[currentQuestion], nq = nextQuestion)
    if currentQuestion == -1:
        return "feddisch"
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
## Gegebene Antworten prüfen
## Weitere Fragen in die DB importieren (wie ist das passiert ?)