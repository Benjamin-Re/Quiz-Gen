# Import sql
import sqlite3

# import flask
from flask import Flask, render_template, jsonify, json

# create app object
app = Flask(__name__)

# Connect to db
connection = sqlite3.connect("questions.db")

# Create cursor object
crsr = connection.cursor()

# Execute a statement
crsr.execute("SELECT * FROM quest WHERE id = 1;")

# store fetched data in variable
myResult = crsr.fetchall()
print(myResult)

# convert into JSON:
myJson = json.dumps(myResult)
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
