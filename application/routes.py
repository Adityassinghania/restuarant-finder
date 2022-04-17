from application import app

@app.route("/")
@app.route("/index")
def default():
    return "<h1> Hello! </h1>"