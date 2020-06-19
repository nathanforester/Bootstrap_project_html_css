from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def render_static():
    return render_template("bootstrap_new.html")


@app.route("/static")
def render():
    return render_template("static/about_me.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')