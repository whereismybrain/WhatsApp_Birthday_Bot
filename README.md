# WhatsApp_Birthday_Bot
WhatsApp_Birthday_Bot is a Python Script designed to simplify birthday wishes. It addresses the challenge of sending unique birthday greetings to a growing list of contacts. The script automates the process by retrieving birthdays from your specified database and selecting random birthday messages from a predefined collection.

# Installation 

pip install selenium 
pip install pandas

# Setting up 

Complete the Database.csv with the necessary details:

- **Name**: Contact's name in your WhatsApp.
- **Birthday**: Contact's day/month.
- **Already_Sent**: Tracks contacts messaged.
- **Nickname**: Script's chosen nickname for the contact.

Prepare birthday wishes in .txt format within the messages folder. 

The script automatically adds "Hi {Nickname}" while sending the message, so the format follows with content after "Hi {Nickname}".
A sample template is available for reference.

For script setup, provide the driver/profile path in whatsapp.py.

# Run

Execute the script by running "send_congratulations.py". To schedule it for daily automatic execution at midnight, add the following line in crontab-e: 00 00 * * * python path/to/send_congratulations.py

# Process Flow of Execution

- Retrieving birthdays from the database
- Identifying today's birthdays
- Selecting a random message
- Launching a web browser
- Accessing WhatsApp Web using the default profile
- Sending the message to the respective contact
















