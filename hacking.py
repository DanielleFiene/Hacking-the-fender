# Importing the csv module to work with CSV files
import csv

# Creating an empty list to store usernames of compromised users
compromised_users = []

# Opening the 'passwords.csv' file in read mode and assigning it to the variable 'password_file'
with open('passwords.csv') as password_file:
  # Creating a DictReader object to read the CSV file as dictionaries
  password_csv = csv.DictReader(password_file)
  
  # Iterating through each row in the CSV file
  for password_row in password_csv:
    # Uncomment the following line to print each username
    # print(password_row['Username'])
    
    # Appending the 'Username' from each row to the 'compromised_users' list
    compromised_users.append(password_row['Username'])

# Initializing an empty list to store lines for the 'compromised_users.txt' file
compromised_user_file = []

# Opening (or creating) the 'compromised_users.txt' file in write mode and assigning it to the variable 'compromised_user_file'
with open('compromised_users.txt', 'w') as compromised_user_file:
  # Iterating through each user in the 'compromised_users' list
  for each_user in compromised_users:
    # Writing each username followed by a newline character to the 'compromised_users.txt' file
    compromised_user_file.write(each_user + '\n')

# Importing the json module to work with JSON data
import json

# Opening (or creating) the 'boss_message.json' file in write mode and assigning it to the variable 'boss_message'
with open('boss_message.json', 'w') as boss_message:
  # Creating a dictionary with the recipient and message
  boss_message_dict = {
    'recipient': 'The Boss', 
    'message': 'Mission Success'
  }
  
  # Writing the dictionary to the 'boss_message.json' file as JSON
  json.dump(boss_message_dict, boss_message)

# Opening (or creating) the 'new_passwords.csv' file in write mode and assigning it to the variable 'new_passwords_obj'
with open('new_passwords.csv', 'w') as new_passwords_obj:
  # Creating a multi-line string with a null signature art
  slash_null_sig = ''' 
                      _  _     ___   __  ____             
                      / )( \   / __) /  \(_  _)            
                      ) \/ (  ( (_ \(  O ) )(              
                      \____/   \___/ \__/ (__)             
                      _  _   __    ___  __ _  ____  ____  
                      / )( \ / _\  / __)(  / )(  __)(    \ 
                      ) __ (/    \( (__  )  (  ) _)  ) D ( 
                      \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
                              ____  __     __   ____  _  _ 
                      ___   / ___)(  )   / _\ / ___)/ )( \
                      (___)  \___ \/ (_/\/    \\___ \) __ (
                            (____/\____/\_/\_/(____/\_)(_/
                      __ _  _  _  __    __                
                      (  ( \/ )( \(  )  (  )               
                      /    /) \/ (/ (_/\/ (_/\             
                      \_)__)\____/\____/\____/'''
  
  # Writing the multi-line string to the 'new_passwords.csv' file
  new_passwords_obj.write(slash_null_sig)
