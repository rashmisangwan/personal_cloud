def is_email_valid( email ):
	if len(email) == 0:
		return False
	else:
		return True

def is_password_valid(password):
	if ( password and len(password) <= 15 and len(password) >= 6 ):
		return True
		
	else:
		return False

def is_username_valid(uname):
	if len(uname) == 0:
		return False
	else:
		return True

def is_retypepass_valid(retype, password):
	if retype == password:
		return True
	else:
		return False