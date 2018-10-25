from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return "you are mine"
@app.route("/hello")
def homepag():
    return "hi"
@app.route("/praise/pep")
def lala():
    return "somethings"
@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    s = x + y
    return str(s)
@app.route("/question")
def show_question():
    return render_template("question.html")

@app.route("/about-me")
def me():
    return render_template("about-me.html")

@app.route("/school")
def school():
    return redirect(http://techkids.vn)

@app.route("/bmi/<int:weight>/<int:height_cm>")
def bmi_someone(weight, height_cm):
    height = height_cm/100
    bmi = weight/(height*height)
    return str(bmi)

if __name__ == "__main__":
    app.run(debug=True)