from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("tab5.html")

if __name__=="__main__":
    app.run(debug=True,port=4446,host="tab5.com")