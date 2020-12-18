import telebot
from telebot import types


bot = telebot.TeleBot("1325280140:AAEOHn_YQLqm611f_0oZgtDJA9aSoU-ErKc")

chats = {}
questions = []

class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
        questions.append(self)

    def generate_markup(self):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for answer in self.answers.keys():
            markup.add(answer)
        return markup


question1 = Question('Ali: Mehmet nereye gitti? Oya: Mehmet …… gitti.',
    {
        'hastaneye': True,
        'okulda': False,
        "sınıftan": False,
        "pazar": False
    })

question2 = Question('Ahmet: Nerelisiniz? Funda: …..',
    {
        'Ben Türk': False,
        'Biz Ankara': False,
        "Ben Ankaralıyım": True,
        "Siz Türk": False
    })

question3 = Question(' Okul …..?',
    {
        'nerededir': True,
        'buradadır': False,
        "gidelim": False,
        "geldim": False
    })

question4 = Question('O…….arkadaşın mı',
    {
        'Siz': False,
        'Senin': True,
        "Sen": False,
        "Sizin": False
    })

question5 = Question('….. adı nedir?',
    {
        'O': False,
        'Siz': False,
        "Sen": False,
        "Babanızın": True
    })

question6 = Question('Öğretmenimiz ve …. geziye katılıyoruz.',
    {
        'Onlar': False,
        'BiZ': True,
        "O": False,
        "Ali": False
    })

question7 = Question('Yaşınız ….?',
    {
        'nasıldır': False,
        'nerededir': False,
        "kaçtır": True,
        "kaçadır": False
    })

question8 = Question('Kaç yaşındasınız? - On….',
    {
        'otuz': False,
        'yüz': False,
        "dokuz": True,
        "onüç": False
    })

question9 = Question('Antalya’ya kimle gidiyorsunuz? - ',
    {
        'Ben': False,
        'O': False,
        "Üçü": False,
        "Onunla": True
    })

question10 = Question('Mustafa: Mehmet Bey tatile kiminle çıkacak? Hilal: ….',
    {
        'Arabasıyla': False,
        'Köpeği': False,
        "Ailesiyle": True,
        "Uçakla": False
    })

question11 = Question('Çiçekleri ….. üzerine bırak!',
    {
        'sağa': False,
        'üstünde': True,
        "masanın": False,
        "saksıdan": False
    })
question12 = Question('Bu ….. okul var mı?',
    {
        'çarda': False,
        'çaydanlıkta': False,
        "çayda": False,
        "civarda": True
    })

question13 = Question('Filiz: Dün işe gitmedin. Neden? Özge: Çünkü dün …..',
    {
        'hastaydım': True,
        'başım ağrıyor': False,
        "halsizim": False,
        "gitmeyeceğim": False
    })

question14 = Question(' Ne zaman ……? - Dün',
    {
        'gidelim': False,
        'gideceğiz': False,
        "gittin": True,
        "gidiyoruz": False
    })

question15 = Question('Marina: Siz şimdi ne ……? Olga: Ders çalışıyoruz.',
    {
        'gidelim': False,
        'nereye': False,
        "yapıyorsunuz": True,
        "gidiyorsunuz": False
    })
@bot.message_handler(commands=['start','back'])
def send_echo(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    button = types.KeyboardButton("Start learning the language")
    button2 = types.KeyboardButton("Test your knowledge of Turkish")
    markup.add(button,button2)
    bot.send_message(message.chat.id, "Welcome to the courses of Turkish!\n\nThis bot can perform 2 functions:\n", reply_markup=markup)
    bot.send_message(message.chat.id, "𝟏)Determine your knowledge of Turkish")
    bot.send_message(message.chat.id, "𝟐)It can help you to learn Turkish.")
    bot.send_message(message.chat.id, "So let's start, choose the buttons!:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def learn(message):
    if message.text == 'Start learning the language':
        markup = types.ReplyKeyboardMarkup(True, row_width=3)
        button3 = types.KeyboardButton("Temel")
        button4 = types.KeyboardButton("Orta")
        button5 = types.KeyboardButton("Yüksek")
        button6 = types.KeyboardButton("/back")
        markup.add(button3, button4, button5, button6)
        bot.send_message(message.from_user.id, 'Choose your lvl', reply_markup=markup)
    elif message.text == 'Test your knowledge of Turkish':
        markup = types.ReplyKeyboardMarkup(True, row_width=1)
        btn7 = types.KeyboardButton("test")
        btn8 = types.KeyboardButton("/back")
        markup.add(btn7, btn8)
        bot.send_message(message.from_user.id, 'Choose the button start',reply_markup=markup)
    elif message.text == 'Temel':
        bot.send_message(message.from_user.id, 'https://lingust.ru/t%C3%BCrk%C3%A7e/t%C3%BCrk%C3%A7e-dersleri')
    elif message.text == 'Orta':
        bot.send_message(message.from_user.id, 'https://www.lingo-play.com/ru/%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D1%82%D1%83%D1%80%D0%B5%D1%86%D0%BA%D0%B8%D0%B9-%D1%8F%D0%B7%D1%8B%D0%BA-%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD/')
    elif message.text == 'Yüksek':
        bot.send_message(message.from_user.id, 'http://www.de-fa.ru/dersonline.htm')
    elif message.text.lower() == 'test':
        chats[message.chat.id] = [0, 0]
        bot.send_message(message.chat.id, 'Тест начался')
        markup = questions[0].generate_markup()
        bot.send_message(message.chat.id, questions[0].question, reply_markup=markup)
    else:
        try:
            stage = questions[chats[message.chat.id][0]]
            if stage.answers.get(message.text):
                bot.send_message(message.chat.id, 'TRUE')
                chats[message.chat.id][1] += 1
            else:   
                bot.send_message(message.chat.id, 'FALSE')
            if len(questions)-1 > chats[message.chat.id][0]:
                chats[message.chat.id][0] += 1
                stage = questions[chats[message.chat.id][0]]
                markup = stage.generate_markup()
                bot.send_message(message.chat.id, stage.question, reply_markup=markup)
            else:
                keyboard_hider = types.ReplyKeyboardRemove()
                num1 = chats[message.chat.id][1]
                num2 = len(questions)
                bot.send_message(message.chat.id, 'Test ended', reply_markup=keyboard_hider)
                bot.send_message(message.chat.id, f'YOu answered {num1} of {num2}')
                precent = int(num1 / num2 * 100)
                bot.send_message(message.chat.id, f'{precent}%')
                del chats[message.chat.id]
        except:
            pass

print('start bot')
bot.polling(none_stop=True)