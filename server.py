from flask import Flask, request, jsonify	from flask import Flask
from dataclasses import dataclass

@dataclass
class Result:
    result: int



app = Flask(__name__)	app = Flask(__name__)




@app.route("/calculator/greeting", methods=['GET'])	@app.route("/calculator/greeting", methods=['GET'])
def greeting():	def greeting():
    return 'Hello world!'	    return ''


@app.route("/calculator/add", methods=['POST'])	@app.route("/calculator/add", methods=['POST'])
def add():	def add():
    numbers = request.json	    return ''
    response = Result(numbers['first'] + numbers['second'])
    return jsonify(response)


@app.route("/calculator/subtract", methods=['POST'])	@app.route("/calculator/subtract", methods=['POST'])
def subtract():	def subtract():
    numbers = request.json	    return ''
    response = Result(numbers['first'] - numbers['second'])
    return jsonify(response)


if __name__ == '__main__':	if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')