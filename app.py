## Flask app routing


from flask import Flask , render_template , request , redirect, url_for,jsonify

## create a simple  flask application

app = Flask(__name__)

@app.route("/" , methods = ["GET"])
def welcome():
    return "<h2>Welcome to flask app</h2>"

@app.route("/index" , methods = ["GET"])
def index():
    return "<h1>Welcome to index page</h1>"

## variable rule
@app.route('/success/<int:score>')
def success(score):
    return "the person has passed and the score is : " + str(score)


@app.route('/fails/<int:score>')
def fails(score):
    return "the person has falis and the score is : " + str(score)

@app.route('/form' , methods = ["GET" , "POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        averagemarks = (maths+science+history)/3

        # return render_template('form.html' , score = averagemarks)
        res = ""
        if averagemarks>=50:
            res="success"
        else:
            res = "fail"

        return redirect(url_for(res, score = averagemarks))


## API 

@app.route('/api' , methods = ['POST'])
def calculatesum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val+b_val)


if __name__ == "__main__":
    app.run(debug = True)

## after this we have to download postman and see krishnaik video 