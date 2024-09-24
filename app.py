from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    a = 123
    return render_template('base.html')

@app.route("/login", methods=['POST'])
def login():
    u = request.args.get('user')
    p = request.args.get('password')
    return jsonify({'success': True})
