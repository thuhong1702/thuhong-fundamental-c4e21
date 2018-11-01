from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/input_form", methods= ["GET", "POST"])
def input_form():
    if request.method == "GET":
        return render_template("input_form.html")
    elif request.method == "POST":
        form = request.form
        option1 = form["Option1"]
        option2 = form["Option2"]
        option3 = form["Option3"]
        option4 = form["Option4"]
        option5 = form["Option5"]
        option6 = form["Option6"]
        return "accept"
@app.route("/new_bike", methods= ["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("bike.html")
    elif request.method == "POST":
        form = request.form
        option1 = form["Option1"]
        option2 = form["Option2"]
        option3 = form["Option3"]
        option4 = form["Option4"]
        return "accept"
        print(form)
if __name__ == "__main__":
    app.run(debug=True)