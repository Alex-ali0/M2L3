import telebot
from config import token
from logic import quiz_questions
user_points =  {}
user_responses = {} 

bot = telebot.TeleBot(token)

def send_question(chat_id):
    bot.send_photo(chat_id, open('3524032.png', 'rb'))
    bot.send_message(chat_id, quiz_questions[user_responses[chat_id]].get_text, reply_markup=quiz_questions[user_responses[chat_id]].gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id

    if chat_id not in user_points:
        user_points[chat_id] = 0

    if call.data == "correct":
        user_points[chat_id] += 1
        bot.answer_callback_query(call.id, "✅ Правильно!")
    elif call.data == "wrong":
        bot.answer_callback_query(call.id, "❌ Неправильно!")
        

    user_responses[chat_id] += 1
    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
    if user_responses[call.message.chat.id]>=len(quiz_questions):
        bot.send_message(chat_id, f"Конец.Вы набрали: {user_points[chat_id]} очков.✅")
    else:
        send_question(call.message.chat.id)

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        send_question(message.chat.id)


bot.infinity_polling()