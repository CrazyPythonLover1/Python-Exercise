# Ternary Operator 
# SYNTAX
# Do_something if condition_true else do_something_if_condition_false

is_friend = True
can_message = " message allowed " if is_friend else " message not allowed "

print(can_message)

# Short Circuiting 

is_Friend = False
is_User = True

if is_Friend and is_User:
  print("best friend forever")