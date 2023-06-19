from flask import Flask, render_template, request, jsonify
import logging
import json

app=Flask(__name__)

@app.route("/",methods=["GET"])
def hello_world():
    return render_template('index.html')

@app.route("/ss",methods=["GET"])
def get_data():
    return render_template('index1.html')

@app.route("/data/json",methods=["GET"])
def get_json_data():
    data=None
    draw=None
    # draw=request.
    f=open('json_data.json')
    if f:
        data=json.load(f)
        f.close()
        print(f"record count : {len(data)}")
        response = {
            'draw': draw,
            'iTotalRecords': len(data),
            'iTotalDisplayRecords': len(data),
            'aaData': data
        }
    return jsonify(response)

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

        data_list=list(request_data.values())
        print(data_list)        
        data=json.dumps(data_list)
        print(data)        
        results = {
            'processed': 'true',
            'data': data
        }
        print("End update_data")
        return jsonify(results)
    # return render_template('index.html')