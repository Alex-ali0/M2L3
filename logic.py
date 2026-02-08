import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def get_text(self):
            return self.__text
    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)



        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(option, callback_data='correct'))
            else:
                markup.add(InlineKeyboardButton(option, callback_data='wrong'))
            
        return markup

quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, "Спят", "Пишут мемы"),
    Question("Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми"),
    Question("Почему программисты не любят прогулки на свежем воздухе?", 1, "Они боятся потерять курсор","Ветер может сбить их с командной строки","Открытый воздух — это как баг в их коде"),
    Question("Почему коты не любят играть в шахматы?",1,"Они слишком заняты охотой на свою тень","Им мешают буквы Ш и М в названиях"," Они считают, что ферзь — это их личный враг")

]