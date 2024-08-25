# Replace 'YOUR_API_TOKEN' with your actual bot token
bot = Bot(token='7123132963:AAGYLROEqoNYQlUu2iOTXC4XiVrAW__vj2I')

# Replace 'CHAT_ID' with the chat ID where you want to send the message
chat_id = '1428483523'



# Replace 'YOUR_API_TOKEN' with your actual bot token
api_token = '7123132963:AAGYLROEqoNYQlUu2iOTXC4XiVrAW__vj2I'
#bot.send_message(chat_id=chat_id, text=message)
# Send a message
url = f'https://api.telegram.org/bot{api_token}/sendMessage'
params = {'chat_id': chat_id, 'text': message}
try:
    response = requests.post(url, data=params)
except:
    print("Connection Error")


def start(update, context):
    pass

def main():
    try:
        updater = Updater('7123132963:AAGYLROEqoNYQlUu2iOTXC4XiVrAW__vj2I', queue.Queue())
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        updater.start_polling()
        updater.shutdown()
    except:
        print("Message not Sent")


if __name__ == '__main__':
    main()