import os
import pandas as pd
import pywhatkit
from datetime import datetime, date
from emoji import emoji
import configparser


def get_config_data(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config['WhatsApp Birthday Bot']


def send_birthday_messages(database, token):
    data = pd.read_csv(database)
    today = date.today().strftime('%#m/%#d')
    for _, row in data.iterrows():
        bday_date = row['Date of Birthday'].split('/')[0]
        if bday_date == today:
            name = row['Name of Person (Birthday)'].replace('birthday', '')
            message = f"Happy birthday {emoji(':birthday_cake:')} {name} {emoji(':partying_face: :party_popper: :party_popper:')}"
            print(message)
            current_time = datetime.now()
            pywhatkit.sendwhatmsg_to_group(token, f"Happy birthday to {name}", current_time.hour,
                                           current_time.minute + 1)
def main():
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "WhatsApp Birthday Bot.ini")

    if os.path.exists(directory):
        config_data = get_config_data(directory)
        api_token = config_data["tokenapi"]
        database_path = config_data["database"]

        if os.path.exists(database_path):
            print("Using token API:", api_token)
            print("Getting ready to send birthday messages...")
            send_birthday_messages(database_path, api_token)
        else:
            print("Database not found. Please update the path in the dashboard.")
    else:
        print("Config file not found.")
        exit(1)


if __name__ == "__main__":
    print("ADG WHATSAPP BIRTHDAY BOT")
    main()
