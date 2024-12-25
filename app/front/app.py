from flask import Flask
from flask import render_template

print(f"Name is {__name__}")
app = Flask(__name__, template_folder=".")

@app.route('/')
def hello_world():
    return render_template("index.html", title="FDSFJSLFJKSDF")

if __name__ == '__main__':
    app.run(debug=True)
