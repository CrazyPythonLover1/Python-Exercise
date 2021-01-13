username = input('what is your username?')
password = input("what is your password?")
password_length =  len(password)
hide_password = "*" * password_length

print(f"Hi {username} your password is {hide_password} , {password_length} letters long ")