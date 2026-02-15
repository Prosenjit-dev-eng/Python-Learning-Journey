file = open('youtube.txt', 'w')
# The try block lets you test a piece of code for errors.
# If an error (exception) occurs, the program won’t crash — instead, it moves to the except block.
try:
    file.write('chai aur code')
finally:
    file.close()
# This is best with
with open('youtube.txt','w') as file:
    file.write('Chai aur python')