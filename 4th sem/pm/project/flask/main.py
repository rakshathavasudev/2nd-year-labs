from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
from app import app
from db_config import mysql

@app.route('/add', methods=['POST'])
def add_user():
	try:
			# Parse the arguments
			parser = reqparse.RequestParser()
			parser.add_argument('name', type=str, help='name of the user')
			parser.add_argument('email', type=str, help='Email address to create user')
			parser.add_argument('password', type=str, help='Password to create user')

			args = parser.parse_args()

			_userName = args['name']
			_userEmail = args['email']
			_userPassword = args['password']

			conn = mysql.connect()
			cursor = conn.cursor()

			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
			data = (_name, _email, _hashed_password,)
			conn = mysql.connect()
			cursor = conn.cursor()
			res=cursor.execute(sql, data)
			conn.commit()
			if len(res) is 0:
				conn.commit()
				return {'StatusCode':'200','Message': 'User creation success'}
			else:
				return {'StatusCode':'1000','Message': str(data[0])}


			#return {'Email': args['email'], 'Password': args['password'] }

	except Exception as e:
		return {'error': str(e)}

@app.errorhandler(404)
def not_found(error=None):
	message = {
		'status': 404,
		'message': 'Not Found: ' + request.url,
	}
	resp = jsonify(message)
	resp.status_code = 404

	return resp
		
if __name__ == "__main__":
	app.run()