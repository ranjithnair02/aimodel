from flask import Flask
from ab import getresult
app=Flask(__name__)

@app.route('/predict')
def helloWord():
    return getresult()

app.run()