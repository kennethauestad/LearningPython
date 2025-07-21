from flask import Flask, render_template # importerer Flask og render_template fra flask

app = Flask(__name__)  
@app.route("/")

def hei():
    return "Hei Per, velkommen til Flask!"

if __name__ == "__main__":
    app.run()