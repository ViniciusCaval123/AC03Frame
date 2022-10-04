import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('forms.html')

@app.route('/api/chato', methods=['POST','GET'])
def chato():

    json = request.get_json()
    first_name = json['first'].upper()
    last_name = json['last'].upper()
    time_name = json['time'].upper()
    combo = json['combo'].upper()
    print (first_name)
    return jsonify(first=first_name, last=last_name, time=time_name, combo=combo)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)