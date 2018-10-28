from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def bmi(weight, height):
    result = weight/((height/100)**2)
    return 
if __name__ == '__main__':
    app.run(debug=True)