import MySQLdb

# database connection method
def connection():
		conn = MySQLdb.connect(
				host 	= "localhost",
				user 	= "root",
				passwd 	= "1234",
				db 		= "personal_cloud"
		)

		c = conn.cursor()
		return c, conn

c, con = connection()

class authHelpers:
	def signup(uname, password, email):
		try:
			user_exist_query = "SELECT * FROM user_auth WHERE email = '" + email + "'"
			c.execute( user_exist_query )
			existing_users = c.fetchall()

			if len( existing_users ) > 0:
				return {
					'payload': {},
					'status': {
						'code': 400,
						'message': 'User Already Exists'
					}
				}
			else:
				add_user = "INSERT INTO user_auth(email, password_hash) values ('" + email + "', '" + password + "')"
				c.execute(add_user)
				con.commit()

				return {
					'payload': {},
					'status': {
						'code': 200,
						'message': 'Account Created Successfully'
					}
				}
		except:
			return {
				'payload': {},
				'status': {
					'code': 500,
					'message': 'Database Error'
				}
			}


	def signin(name, email, password):
		try:
			user_check_email_query = "select * from user_auth where email = '" +email+ "'"
			c.execute(user_check_email_query)
			existing_users = c.fetchall()
			if len(existing_users) == 0:
				return {
					'payload': {},
					'status': {
						'code': 400,
						'message': 'this email does not Exists'
					}
				}
			else:
				if existing_users[2] == password:
					cookie_code = existing_users[0]
					add_user_info = "insert into user_info(cookie_code, forget_pass_code) values ('" +cookie_code+ "') where user_id == " +existing_users[0]
					c.execute(add_user_info)
					con.commit()

					return {
						'payload': {},
						'metadata': {
							'cookie_code': cookie_code
						}
						'status': {
							'code': 200,
							'message': 'logged in Successfully'
						}
					}
				else:
					return {
						'payload': {},
						'status': {
							'code': 400,
							'message': 'please enter right password or click on forgot password'
						}
					}

		except:
			return {
				'payload': {},
				'status': {
					'code': 500,
					'message': 'Database Error'
				}
			}





				 