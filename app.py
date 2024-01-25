from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])

def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        # float bc youre receiving a text but you need it to be a number
        return(render_template("index.html",result=(rate * -50.6) + 90.2))
    else:
        return(render_template("index.html",result="waiting for exchange rate..........."))
if __name__ == "__main__":
    
    app.run()
