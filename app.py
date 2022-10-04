import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('forms.html')

@app.route('/api/chato', methods=['POST'])
def chato():

    json = request.get_json()
    first_name = json['first']
    last_name = json['last']
    time_name = json['time']
    combo = json['combo']
    return jsonify(first=first_name, last=last_name, time=time_name, combo=combo)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5500))
    app.run(host='0.0.0.0', port=port)