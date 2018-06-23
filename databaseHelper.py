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
		user_exist_query = "SELECT * FROM user_auth WHERE email = '" + email + "'"

		c.execute( user_exist_query )
		existing_users = c.fetchall()

		try:
			if len( existing_users ) > 0:
				return {
					'payload': {},
					'status': {
						'code': 400,
						'message': 'User Already Exists'
					}
				}
			else:
				add_user = "INSERT INTO user_auth values (" + email + ", " + password + ")"

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


	
		
