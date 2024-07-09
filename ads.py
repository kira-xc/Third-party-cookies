from flask import Flask,render_template,request,make_response

app=Flask(__name__)

@app.route("/")
def index():
    visit=request.referrer
    if visit is not None:
        if visit.find("fasi9.com")!=-1:
            res=make_response("set cookie")
            res.set_cookie(key="user",value="fas9",samesite="None",secure=True,
                           max_age=24*60*60*365)
            return res
        if visit.find("islam.com")!=-1:
            res=make_response("set cookie")
            res.set_cookie(key="user",value="islam",samesite="None",secure=True,
                           max_age=24*60*60*365)
            return res
    return render_template("ads.html")

if __name__=="__main__":
    app.run(debug=True,port=4449,host="ads.localhost")