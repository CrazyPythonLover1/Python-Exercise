# Error Handling

while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('Please enter a number')
        continue # Trying again from the top
    except ZeroDivisionError:
        print('Please enter age higher than 0')
        break # Getting out from the loop but finally block will run
    else:
        print('Thank you')
        break # Getting out from the loop but finally block will run
    finally:
        print('ok, I am finally done')
    print('can you hear me?')