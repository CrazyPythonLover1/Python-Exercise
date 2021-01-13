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

# enumerate

for i, char in enumerate(list(range(100))):
  # print(i,char)
  if char == 50:
    print(f"the index of 50 {i}")



# DRAW A PICTURE 

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0],
]

for row in picture:
  for pixel in row:
    if pixel == 1:
      print("*", end="")
    else:
      print(" ", end="")
  print('')

  ## Scope, List method, set, dictionary, for loop, while loop, if else, function.