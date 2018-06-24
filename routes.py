from flask import Flask, request, render_template, make_response
import json

from databaseHelper import authHelpers
from validation import is_email_valid, is_password_valid, is_username_valid, is_retypepass_valid

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signupHandler():
	if request.method == 'POST':
		name = request.form.get("username")
		email = request.form.get("email")
		password_hash = request.form.get("password")
		retypepass = request.form.get("retypePassword")
		
		emailCheckUp = is_email_valid( email )
		passCheckUp = is_password_valid(password_hash)
		nameCheckUp = is_username_valid(name)
		retypeCheckUp = is_retypepass_valid(retypepass, password_hash)

		if emailCheckUp == False:
			return json.dumps({
													'payload': {},
													'status': {
																			'code': 400,
																			'message': 'please enter your email address'
																		}
												})
		elif passCheckUp == False:
			return json.dumps({
													'payload': {},
													'status': {
																			'code': 400,
																			'message': 'password length should be in between 6 to 15 characters'
																		}
												})
		elif nameCheckUp == False:
			return json.dumps({
													'payload': {},
													'status': {
																			'code': 400,
																			'message': 'please enter your username'
																		}
												})
		elif retypeCheckUp == False:
			return json.dumps({
													'payload': {},
													'status': {
																			'code': 400,
																			'message': 'please match your password'
																		}
												})

		else:
			response = authHelpers.signup(name, password_hash, email)
			return json.dumps( response )
	else:
		return render_template('sign_up.html')


@app.route('/signin', methods = ['GET', 'POST'])
def signinHandler():
	if request.method == 'GET':
		return render_template('sign_in.html')
	else:
		email = request.form.get("email")
		password_hash = request.form.get("password")

		emailCheckUp = is_email_valid( email )
		passCheckUp = is_password_valid(password_hash)
		if emailCheckUp == False:
			return json.dumps({
													'payload': {},
													'status': {
																			'code': 400,
																			'message': 'please enter your email address'
																		}
												})
		elif passCheckUp == False:
			return json.dumps({
													'payload': {},
													'status': {
																			'code': 400,
																			'message': 'password length should be in between 6 to 15 characters'
																		}
												})
		else:
			databaseResponse = authHelpers.signin(email, password_hash)
			if( databaseResponse.meta_data && databaseResponse.meta_data.cookie_data ):
				resp = make_response(json.dumps( databaseResponse ))
		    resp.set_cookie('cookie_data', databaseResponse.meta_data.cookie_data)
				return resp
		  else:
				return json.dumps({
														'payload': {},
														'status': {
																				'code': 400,
																				'message': 'Not logged in.. idk why'
																			}
													})
		  	

if __name__ == "__main__":
	app.run(debug = True)