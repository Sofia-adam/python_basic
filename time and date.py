import datetime
now = datetime.datetime.now() # Get the current date and time
print("Current date and time : ") # Display a message indicating what is being printed


print(now.strftime("%Y-%m-%d %H:%M:%S")) # Print the current date and time in a specific format

# Use the 'strftime' method to format the datetime object as a string with the desired format
