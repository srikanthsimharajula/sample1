from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/", methods = ['POST'])
def bmi():
    data= request.get_json()
    height = data['h']
    weight = data['w']
    output = round(weight / (height * height),2)
    return(jsonify({'output' :output}))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)