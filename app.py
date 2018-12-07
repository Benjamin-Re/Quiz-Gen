# Import sql
import sqlite3

# import flask
from flask import Flask, render_template, jsonify, json

# create app object
app = Flask(__name__)
# json = FlaskJSON(app)		notwendig?

# Connect to db
connection = sqlite3.connect("questions.db")

# Create cursor object
crsr = connection.cursor()

# Execute a statement
myResult = crsr.execute("SELECT * FROM quest WHERE id = 1;")

# store fetched data in variable
# myResult = crsr.fetchall()
#print(myResult)

items = []
# (hardcoded) solution to get description along with result
for row in myResult:
	items.append({'Index': row[0], 'q': row[1], 'a': row[2], 'b': row[3], 'c': row[4], 'd': row[5], 'ans': row[6], 'id': row[7]})
print(items)


# convert into JSON:
myJson = json.dumps(items[0])
print(myJson)

# route to index
@app.route("/")
def index():
    return render_template('index.html', myVariable = myJson)

if __name__ == '__main__':
    app.run(debug=True)


# To save changes
connection.commit()

# Close the connection
connection.close()
