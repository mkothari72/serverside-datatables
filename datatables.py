from flask import Flask, render_template, request
import logging
import json

app=Flask(__name__)

@app.route("/",methods=["GET"])
def hello_world():
    return render_template('index.html')

@app.route("/update", methods=["POST"]) 
def update_data():
    print("Start update_data")
    error=None
    request_data=request.get_json()
    discard_keys=["context","length","selector","ajax"]
    for key in discard_keys:
        request_data.pop(key, None)

    for key, value in request_data.items():
        print(value)        
    data=json.dumps(request_data)
    render_template('success.html', error=error)
    print("End update_data")
    return 'ok'