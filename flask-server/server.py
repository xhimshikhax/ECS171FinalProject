from flask import Flask

app = Flask(__name__)

@app.route("/categories")
def categories():
    return {"categories":['c1','c2','c3','c4','c5','c6']}

if __name__ == "__main__":
    app.run(debug=True)