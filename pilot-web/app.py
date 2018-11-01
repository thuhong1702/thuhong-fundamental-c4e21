from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/new_poll", methods=["GET", "POST"])
def new_poll():
    if request.method == "GET":
        return render_template("new_poll.html")
    elif request.method == "POST":
        # 1. Unpack data (form)
        form = request.form
        question= form['question']
        options = []
        for k,v in form.items():
            if k != "question":
                options.append(v)
        return "Gotcha"
@app.route("/find_friend", methods= ["GET", "POST"])
def find_friend():
    if request.method == "GET":
        return render_template("nisekoi.html")
    elif request.method == "POST":
        form = request.form
        option1 = form["Opton1"]
        option2 = form["Opton2"]
        option3 = form["Opton3"]
        option4 = form["Opton4"]
        option5 = form["Opton5"]
        option6 = form["Opton6"]
        return "accept"
if __name__ == "__main__":
    app.run(debug=True)