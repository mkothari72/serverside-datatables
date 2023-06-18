from flask import Flask, render_template, request, jsonify
import logging
import json

app=Flask(__name__)

@app.route("/",methods=["GET"])
def hello_world():
    return render_template('index.html')

@app.route("/update", methods=["GET","POST"]) 
def update_data():
    content_type = request.headers.get('Content-Type')
    print(f"content_type: {content_type}")
    print(f"method: {request.method}")
    if request.method=="POST":
        print("Start update_data")
        error=None
        request_data=request.get_json()
        discard_keys=["context","length","selector","ajax"]
        for key in discard_keys:
            request_data.pop(key, None)

        for key, value in request_data.items():
            print(value)        
        data=json.dumps(request_data)
        results = {
            'processed': 'true',
            'data': data
        }
        print("End update_data")
        return jsonify(results)
    # return render_template('index.html')