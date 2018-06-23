from flask import Flask, request, render_template
import json

from databaseHelper import authHelpers

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signupHandler():
	if request.method == 'POST':
		name = request.form.get("username")
		email = request.form.get("email")
		password_hash = request.form.get("password")
		
		if ( password_hash and len(password_hash) <= 15 and len(password_hash) >= 6 ):
			response = authHelpers.signup(name, password_hash, email)
			return json.dumps( response )
		
		else:
			return json.dumps({
													'payload': {},
													'status': {
																			'code': 400,
																			'message': 'password length should be in between 6 to 15 characters'
																		}
												})
	else:
		return render_template('sign_up.html')


if __name__ == "__main__":
	app.run(debug = True)