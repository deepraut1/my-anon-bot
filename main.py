import telebot
import os

# Railway पर टोकन हम Environment Variables में डालेंगे
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    try:
        if message.chat.type in ['group', 'supergroup']:
            user_id = message.from_user.id
            text = message.text
            fake_name = f"User_{str(user_id)[-4:]}"
            bot.delete_message(message.chat.id, message.message_id)
            
            if message.reply_to_message:
                bot.send_message(message.chat.id, f"👤 **{fake_name}**: {text}", reply_to_message_id=message.reply_to_message.message_id)
            else:
                bot.send_message(message.chat.id, f"👤 **{fake_name}**: {text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("बॉट चालू हो गया है...")
    bot.infinity_polling()
