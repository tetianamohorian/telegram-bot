import telebot
import webbrowser
import sqlite3
import time
from telebot import types

bot = telebot.TeleBot('6695575458:AAH-EHjF-f_9JCjBuDd02GIO2_WuvvWdP2g')

creator_id = 301457043

@bot.message_handler(commands=['site'])
def site(message):
   webbrowser.open('https://kmti.fei.tuke.sk/')


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('tatyanamogoryan.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), surname varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}! I am Tatyana Mogoryan 😊. This bot is designed for communication with clients 💻. You can learn more about the services I provide. To see the list of available commands, type /help.')
    file = open('./img_about.jpg', 'rb')
    bot.send_photo(message.chat.id, file)

@bot.message_handler(commands=['services'])
def services(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Web Design', callback_data = 'text_web')
    btn2 = types.InlineKeyboardButton('Game Developer', callback_data = 'text_game')
    btn3 = types.InlineKeyboardButton('Neural Network Developer', callback_data = 'text_neural')
    markup.row(btn1);
    markup.row(btn2, btn3);
    bot.reply_to(message, 'I provide these services:', reply_markup = markup) 

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'text_web':
        bot.edit_message_text('\n✅ I develop the user interface.\n✅ Web page development.\n✅ I position your brand.\n', callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'text_game':
        bot.edit_message_text('\n✅ I develop the user interface.\n✅ Game development.\n✅ Keeping the game running after release, adding new content.\n', callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'text_neural':
        bot.edit_message_text('\n✅ Designing neural network models.\n✅ Training neural networks.\n✅ Exploring the latest trends and advances in neural networks, and implementing new methods and techniques to improve model training and performance.\n', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['contactme'])
def contactme(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Telegram', url = 'https://t.me/mogoryan_tatyana')
    btn2 = types.InlineKeyboardButton('Instagram', url = 'https://www.instagram.com/mogoryan.tatyana/')
    btn3 = types.InlineKeyboardButton('Facebook',  url = 'https://www.facebook.com/people/%D0%A2%D0%B0%D1%82%D1%8C%D1%8F%D0%BD%D0%B0-%D0%9C%D0%BE%D0%B3%D0%BE%D1%80%D1%8F%D0%BD/pfbid025UU37DmntB7SPZb64Vp6QpZQTW5Ls6wYdUjtQP8fruYhH1iHc9pmk2Fq8BTbsEWTl/')
    markup.row(btn1);
    markup.row(btn2, btn3);
    bot.reply_to(message, 'I provide these services:', reply_markup = markup) 


@bot.message_handler(commands=['export_users'])
def export_users(message):
    if message.from_user.id == creator_id:
        conn = sqlite3.connect('tatyanamogoryan.sql')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users")
        users = cur.fetchall()

        if users:
            with open('users.txt', 'w') as file:
                for user in users:
                    file.write(f"Name: {user[1]}, Surname: {user[2]}\n")

            bot.send_document(message.chat.id, open('users.txt', 'rb'))
        else:
            bot.send_message(message.chat.id, "No users found.")

        cur.close()
        conn.close()
    else:
        bot.send_message(message.chat.id,"This command is only available for the bot creator.")    


@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(message.chat.id, 'Enter your name, please:')
    bot.register_next_step_handler(message, user_name) 


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Enter your surname, please')
    bot.register_next_step_handler(message, user_surname)

def user_surname(message):
    surname = message.text.strip()

    conn = sqlite3.connect('tatyanamogoryan.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, surname) VALUES (?, ?)", (name, surname))
    conn.commit()

    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Super, wait for a reply, you will be contacted later on 😊❤️')


@bot.message_handler(commands=['id'])
def info(message):
    bot.reply_to(message, f'ID: {message.from_user.id}')

@bot.message_handler(commands=['hello'])
def inf(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}! I am Tatyana Mogoryan 😊. This bot is designed for communication with clients 💻. You can learn more about the services I provide. To see the list of available commands, type /help.')
    file = open('./img_about.jpg', 'rb')
    bot.send_photo(message.chat.id, file)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>Help information</b>. \n - /start - start the bot\n - /contact - leave your contacts\n - /contactme - my contacts\n - /services - provide services\n - /help - list of commands\n - /hello - start the bot\n - /id - user id\n - /site - portfolio ', parse_mode='html')





bot.polling(none_stop=True)


