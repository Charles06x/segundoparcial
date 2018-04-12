from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/')
def name():
	return 'Charles Acevedo Díaz T00039395'


@app.route('/prime/<int:n>/json')
def primeNumber(n):
	list = []
	suma = 0
	for i in range(n):
		if i == 2:
			list.append(i)
		if i < 2:
			for j in range(i-1):
				if i % j == 0 :
					suma = suma + 1
			if suma == 1:
				list.append(j)
	print(list)
	return jsonify(list)

		
