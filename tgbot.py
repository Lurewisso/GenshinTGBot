import telebot
import webbrowser
from telebot import types


tgbot = telebot.TeleBot('6765355665:AAEdvM8xudcNEAMnMAsTThMhExUyZrZDw60')


@tgbot.message_handler(commands=['start'])
def chat(messages):
    tgbot.send_message(messages.chat.id,
                       f'Привет, путешественник, Мона подсказала мне, что тебя зовут: {messages.from_user.first_name} {messages.from_user.last_name}')


@tgbot.message_handler(content_types=['photo'])
def get_pic(messages):
    mark = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('А я смотрю картинки вот тут', url='https://ru.pinterest.com')
    mark.row(button1)
    button2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    mark.row(button2)
    button3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    mark.row(button3)
    tgbot.reply_to(messages, 'Очень красиво! Паймон нравится!', reply_markup=mark)


@tgbot.callback_query_handler(func=lambda callback: True)
def action_message(callback):
    if callback.data == 'delete':
        tgbot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        tgbot.edit_message_text('Ты магии ждал? Я начинающий программист, я не всё умею', callback.message.chat.id,
                                callback.message.message_id)


@tgbot.message_handler(content_types=['audio'])
def get_music(messages):
    tgbot.reply_to(messages, 'Секундочку, сейчас...Вау! звучит потрясно!')


@tgbot.message_handler(content_types=['video'])
def get_video(messages):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Последний шанс удалить видео!', callback_data='delete')
    markup.row(btn)
    tgbot.reply_to(messages, 'Я надеюсь, что там ничего плохого нет! Иначе больше не буду смотреть твои видео!',
                   reply_markup=markup)


@tgbot.callback_query_handler(func=lambda callback: True)
def action_video(callback2):
    if callback2.data == 'delete':
        tgbot.delete_message(callback2.message.chat.id, callback2.message.message_id - 1)


@tgbot.message_handler(commands=['mona'])
def chat(messages):
    tgbot.send_message(messages.chat.id,
                       'Ох, Мона это таинственный молодой астролог, которая представляется как «великий астролог Мона Мегистус» и на самом деле достойна этого звания.')


@tgbot.message_handler(commands=['teivat'])
def chat(messages):
    tgbot.send_message(messages.chat.id,
                       'Тейват — фантастический мир, где в гармонии существуют семь элементов. В далёком прошлом могущественные Архонты научили людей управлять стихиями. С помощью этих навыков люди смогли превратить безжизненную пустыню в свой дом. 500 лет назад крах древней цивилизации перевернул весь мир с ног на голову... И хоть было давно, мир до сих пор не до конца оправился от катастрофы.')


@tgbot.message_handler(commands=['aboutbot'])
def chat(messages):
    tgbot.send_message(messages.chat.id,
                       'Меня зовут <b>Паймон</b>, я <u>бот</u>, который создан, чтобы помогать новичкам!',
                       parse_mode='html')


@tgbot.message_handler(commands=['map'])
def map(messages):
    tgbot.send_message(messages.chat.id,
                       "Эта карта поможет тебе с поиском необходимых предметов!                                 https://act.hoyolab.com/ys/app/interactive-map/index.html?lang=ru-ru#/map/2?shown_types=&center=2008.50,-1084.00&zoom=-3.00")


@tgbot.message_handler(commands=['news'])
def news(messages):
    tgbot.send_message(messages.chat.id, 'Здесь ты можешь узнать актуальные новости по нашей любимой игре!                                               https://genshin.hoyoverse.com/m/ru/news')

@tgbot.message_handler(commands=['buy_gems'])
def gen_drop(messages):
    tgbot.send_message(messages.chat.id,
                       "Закупиться гемами по самым вкусным ценам можно тут! ---> https://genshindrop.com")


@tgbot.message_handler(commands=['promo_free'])
def promo(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("NA88ANTJL5SD")
    item2 = types.KeyboardButton("JB95D2V5XGJ5")
    item3 = types.KeyboardButton("NNDFKSKEX6TH")
    item4 = types.KeyboardButton("HJGDJA2FW7FH")
    markup.add(item1, item2, item3, item4)
    tgbot.send_message(message.chat.id, f'<b>Актуальные промокоды</b> :) нажмите на них, а затем скопируйте. ',
                       reply_markup=markup, parse_mode='html')


@tgbot.message_handler(commands=['creator'])
def creatorr(messages):
    tgbot.send_message(messages.chat.id, "https://t.me/lurewisso")



@tgbot.message_handler(commands=['weapon_guide'])
def weapon(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("★ Одноручное оружие")
    item2 = types.KeyboardButton("★ Двуручное оружие")
    item3 = types.KeyboardButton("★ Древковое оружие")
    item4 = types.KeyboardButton("★ Стрелковое оружие")
    item5 = types.KeyboardButton("★ Катализатор оружие")
    markup.add(item1, item2, item3, item4, item5)
    tgbot.send_message(message.chat.id, 'Выберите тип вашего оружия', reply_markup=markup)


@tgbot.message_handler(func=lambda message: message.text.find("★") != -1)
def message_reply_weapon(message):
    if message.text == "★ Одноручное оружие":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Блеск тихих вод (5★)")
        item2 = types.KeyboardButton("Драгоценный омут (5★)")
        item3 = types.KeyboardButton("Ключ Хадж-нисут (5★)")
        item4 = types.KeyboardButton("Клятва свободы (5★)")
        item5 = types.KeyboardButton("Кромсатель пиков (5★)")
        item6 = types.KeyboardButton("Меч Сокола (5★)")
        item7 = types.KeyboardButton("Харан гэппаку фуцу (5★)")
        item8 = types.KeyboardButton("Свет лиственного разреза (5★)")
        item9 = types.KeyboardButton("Рассекающий туман (5★)")
        item10 = types.KeyboardButton("Небесный меч (5★)")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
        tgbot.send_message(message.chat.id, 'Выберите ваше оружие', reply_markup=markup)

    elif message.text == "Блеск тихих вод (5★)":
        file = open('weapon/1handweapon/blesktihihvod/blesk.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Когда текущее HP экипированного персонажа увеличивается или снижается, наносимый урон элементального навыка повышается на 8% на 6 сек. Эффект возникает не чаще 1 раза в 0,2 сек. и складывается до 3 раз. Когда текущее HP других членов отряда увеличивается или снижается, макс. HP экипированного персонажа повышается на 14% на 6 сек. Эффект возникает не чаще 1 раза в 0,2 сек. и складывается до 2 раз. Эффект срабатывает, даже когда экипированный персонаж находится вне поле боя.")
        # file2 = open('gidro/furina/furina.png', 'br')
        # tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Подходит персонажу: Фурина")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 Крит. урон: 19.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Драгоценный омут (5★)":
        file = open('weapon/1handweapon/drogocenomut/dragonomut.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Увеличивает HP на 20%. Также даёт бонус атаки, равный 1,2% от макс. HP экипированного этим оружием персонажа.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Албедо, Джинн, Аято, Кэ Цин, Кирара")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 Шанс крит. попадания: 9.6 Уровень: 1 Вознесение: 0")

    elif message.text == "Ключ Хадж-нисут (5★)":
        file = open('weapon/1handweapon/keyhadjnisut/keyhadj.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Увеличивает НР на 20%. Попадание элементальным навыком на 20 сек. создаёт Великое сказание, которое повышает мастерство стихий экипированного этим оружием персонажа на 0,12% от его макс. HP. Эффект может возникнуть не чаще 1 раза в 0,3 сек. и складывается до 3 раз. После получения 3 уровней или обновления длительности 3 уровня мастерство стихий всех персонажей поблизости увеличится на 0,2% от макс. HP экипированного этим оружием персонажа на 20 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу:Кирара, Куки Синобу, Нилу, Лайла ")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 HP%: 14.4 Уровень: 1 Вознесение: 0")

    elif message.text == "Клятва свободы (5★)":
        file = open('weapon/1handweapon/klyatvafreedom/klyatvafr.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Часть Тысячелетней симфонии, что блуждает среди ветров. Увеличивает наносимый урон на 10%. Вызов элементальной реакции даёт персонажу один Талисман воодушевления. Он может возникнуть раз в 0,5 сек., даже когда персонаж в отряде, но не активен. Два собранных Талисмана воодушевления пропадают, на 12 сек. наделяя ближайших членов отряда эффектом «Тысячелетняя симфония: Гимн восстания», который увеличивает урон, наносимый обычной атакой, заряженной атакой и атакой в падении, на 16%, а силу атаки - на 20%. В течение 20 сек. после активации эффекта Талисманы воодушевления появляться не будут. Тысячелетняя симфония с эффектами, влияющими на те же навыки, не складывается.")
        tgbot.send_message(message.chat.id, "Подходит персонажу:Куки Синобу, Кадзуха")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Мастерство стихий: 43 Уровень: 1 Вознесение: 0")

    elif message.text == "Кромсатель пиков (5★)":
        file = open('weapon/1handweapon/kromsatelpikov/kromsatelpikov.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Увеличивает прочность щита на 20%. При попадании увеличивает силу атаки на 4% в течение 8 сек. Эффект может складываться до 5 раз и возникнуть раз в 0,3 сек. Кроме того, под защитой щита бонус силы атаки данного эффекта увеличивается на 100%.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Универсальное оружие")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Сила атаки%: 10.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Меч Сокола (5★)":
        file = open('weapon/1handweapon/mechsokola/mechsokola.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Увеличивает силу атаки на 20%. При получении урона пробуждается душа Сокола Запада, несущего знамя сопротивления. Восстанавливает HP, равное 100% от силы атаки, и наносит 200% урона окружающим врагам. Может возникнуть раз в 15 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу:Кэйя, Джинн, Альбедо, Ци Ци")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Бонус физ. урона: 9 Уровень: 1 Вознесение: 0")

    elif message.text == "Харан гэппаку фуцу (5★)":
        file = open('weapon/1handweapon/harangappaku/harangappaku.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Даёт 12% бонус урона всеми элементами. Когда другие члены отряда поблизости активируют элементальные навыки, экипированный этим оружием персонаж получает 1 уровень Волны-шипа. Эффект возникает не чаще, чем один раз в 0,3 сек. Всего можно получить не более 2 уровней. Когда персонаж с этим оружием применяет элементальный навык, все уровни Волны-шипа тратятся, и он получает Хаос волн, который повышает урон обычной атаки согласно количеству уровней. Каждый уровень этого эффекта повышает урон обычной атаки на 20% в течение 8 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Аято")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Шанс крит. попадания: 7.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Свет лиственного разреза (5★)":
        file = open('weapon/1handweapon/lightleafrazrez/lightleaf.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Шанс крит. попадания увеличивается на 4%. Когда обычная атака наносит элементальный урон, она даёт эффект Лиственного выреза: урон обычных атак и элементальных навыков повышается на 120% от мастерства стихий. После 28 активаций или через 12 сек. эффект исчезнет. Лиственный вырез можно получить не чаще одного раза в 12 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Аль-Хайтам")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 Крит. урон: 19.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Рассекающий туман (5★)":
        file = open('weapon/1handweapon/rassekayatuman/rassekayatuman.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Все типы элементального урона получают 12% бонуса урона, а также силу Эмблемы рассекателя тумана. На уровнях эмблемы 1, 2 или 3 персонаж получает 8%, 16% или 28% бонуса к элементальному урону своей стихии соответственно. Персонаж получает 1 уровень Эмблемы рассекателя тумана в каждом из следующих случаев: при нанесении элементального урона обычной атакой, эмблема действует 5 сек.; при применении взрыва стихии, эмблема действует 10 сек.; когда элементальная энергия персонажа ниже 100%, полученная таким образом эмблема действует до тех пор, пока персонаж не восстановит всю свою элементальную энергию. Продолжительность действия каждого уровня эмблемы рассчитывается индивидуально.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Кэйя, Аято, Кэ Цин, Аяка")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Крит. урон: 9.6 Уровень: 1 Вознесение: 0")

    elif message.text == "Небесный меч (5★)":
        file = open('weapon/1handweapon/heavensword/heavensword.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Увеличивает шанс крит. попадания на 4%. Взрыв стихии пробуждает силу небес, которая увеличивает скорость передвижения и атаки на 10%, а обычные и заряженные атаки при попадании наносят дополнительный урон, равный 20% от силы атаки. Все эффекты длятся 12 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Беннет, Син Цю, Джинн")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Восст. энергии: 12 Уровень: 1 Вознесение: 0")

    if message.text == "★ Двуручное оружие":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Вердикт (5★)")
        item2 = types.KeyboardButton("Волчья погибель (5★)")
        item3 = types.KeyboardButton("Краснорогий камнеруб (5★)")
        item4 = types.KeyboardButton("Маяк тростникового моря (5★)")
        item5 = types.KeyboardButton("Небесное величие (5★)")
        item6 = types.KeyboardButton("Некованый (5★)")
        item7 = types.KeyboardButton("Песнь разбитых сосен (5★)")
        markup.add(item1, item2, item3, item4, item5, item6, item7)
        tgbot.send_message(message.chat.id, 'Выберите ваше оружие', reply_markup=markup)

    elif message.text == "Вердикт (5★)":
        file = open('weapon/2handweapon/verdikt/verdikt.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Повышает силу атаки на 20%. Когда члены отряда подбирают элементальные осколки, созданные реакцией Кристалл, экипированный персонаж получает 1 Печать, которая увеличивает урон элементального навыка на 18%. Печать действует 15 сек. Одновременно можно иметь 2 Печати. Все Печати экипированного персонажа пропадут через 0,2 сек. после нанесения урона его элементальным навыком.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Навия")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Шанс крит. попадания: 4.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Волчья погибель (5★)":
        file = open('weapon/2handweapon/wolfdeath/wolfdeath.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает силу атаки на 20%. При попадании по цели с HP меньше 30% увеличивает силу атаки всех членов отряда на 40% в течение 12 сек. Может возникнуть не чаще 1 раза за 30 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Бэй Доу, Дэхья, Дилюк, Эола, Фремине, Кавех, Навия, Рэйзор, Саю, Синь Янь")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Сила атаки%: 10.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Краснорогий камнеруб (5★)":
        file = open('weapon/2handweapon/redhorn/redhorn.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Защита повышается на 28%, урон обычных и заряженных атак повышается на 40% защиты.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Фремине, Итто, Ноэлль, Синь Янь ")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 Крит. урон: 19.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Маяк тростникового моря (5★)":
        file = open('weapon/2handweapon/mayak sea/mayak.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"После попадания элементальным навыком по противнику сила атаки увеличится на 20% на 8 сек. При получении урона сила атаки увеличится на 20% на 8 сек. Эти эффекты срабатывают, даже если персонаж не на поле боя. Кроме того, если экипированный персонаж не защищён щитом, его макс. HP увеличится на 32%.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Бэй Доу, Кавех, Дори")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Шанс крит. попадания: 7.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Небесное величие (5★)":
        file = open('weapon/2handweapon/heaven velichie/heaven velichie.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает наносимый урон на 8%. После активации взрыва стихий попадания обычными или заряженными атаками запускают неосязаемое лезвие, которое наносит 80% урона всем врагам на своём пути. Длится 20 сек. или 8 неосязаемых лезвий.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Бэй Доу, Итто, Фремине, Эола, Чун Юнь")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Восст. энергии: 8 Уровень: 1 Вознесение: 0")

    elif message.text == "Некованый (5★)":
        file = open('weapon/2handweapon/nekovanniy/nekovanniy.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает прочность щита на 20%. При попадании увеличивает силу атаки на 4% в течение 8 сек. Эффект может складываться до 5 раз и возникнуть раз в 0,3 сек. Кроме того, под защитой щита бонус силы атаки данного эффекта увеличивается на 100%.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Навия, Синь Янь")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Сила атаки%: 10.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Песнь разбитых сосен (5★)":
        file = open('weapon/2handweapon/song of broken woods/song of broken woods.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Часть Тысячелетней симфонии, что блуждает среди ветров. Увеличивает силу атаки на 16% и при попадании обычной или заряженной атакой даёт персонажу Печать шёпота. Этот эффект может возникнуть раз в 0,3 сек. После получения 4-ой Печати шёпота все они тратятся, и все окружающие члены отряда получают эффект «Тысячелетняя симфония: Гимн знамени» на 12 сек. «Тысячелетняя симфония: Гимн знамени» увеличивает скорость обычной атаки на 12% и силу атаки на 20%. После активации этого эффекта вы не сможете получать Печати шёпота в течение 20 сек. При наличии нескольких эффектов Тысячелетней симфонии усиления одного типа не складываются.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Эола")
        tgbot.send_message(message.chat.id, "Базовая атака: 49 Бонус физ. урона: 4.5 Уровень: 1 Вознесение: 0")

    if message.text == "★ Древковое оружие":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Небесная ось (5★)")
        item2 = types.KeyboardButton("Нефритовый коршун (5★)")
        item3 = types.KeyboardButton("Покоритель вихря (5★)")
        item4 = types.KeyboardButton("Посох алых песков (5★)")
        item5 = types.KeyboardButton("Посох Хомы (5★)")
        item6 = types.KeyboardButton("Сияющая жатва (5★)")
        item7 = types.KeyboardButton("Усмиритель бед (5★)")
        markup.add(item1, item2, item3, item4, item5, item6, item7)
        tgbot.send_message(message.chat.id, 'Выберите ваше оружие', reply_markup=markup)

    elif message.text == "Небесная ось (5★)":
        file = open('weapon/woodweapon/heaven os/heaven os.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает шанс крит. попадания на 8% и скорость обычной атаки на 12%. При попадании обычной или заряженной атакой есть 50% шанс активировать неосязаемое лезвие, которое наносит 40% урона в небольшом радиусе. Может возникнуть раз в 2 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Кандакия, Райдэн, Розария, Шэнь Хэ, Сян Лин, Сяо")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Восст. энергии: 8 Уровень: 1 Вознесение: 0")

    elif message.text == "Нефритовый коршун (5★)":
        file = open('weapon/woodweapon/nefrit korsh/nefrit korsh.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"При попадании увеличивает силу атаки на 3,2% в течение 6 сек. Эффект может складываться до 7 раз и возникает не чаще чем раз в 0,3 сек. На 7 уровне складывания увеличивает урон на 12%.")
        tgbot.send_message(message.chat.id, "Подходит персонажу:Сайно, Ху Тао, Райдэн, Розария, Шэнь Хэ, Тома, Сяо, Яо Яо ")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Шанс крит. попадания: 4.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Покоритель вихря (5★)":
        file = open('weapon/woodweapon/pokoritel vihrya/pokoritel vihrya.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает прочность щита на 20%. При попадании увеличивает силу атаки на 4% в течение 8 сек. Эффект может складываться до 5 раз и возникнуть раз в 0,3 сек. Кроме того, под защитой щита бонус силы атаки данного эффекта увеличивается на 100%.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Чжун Ли")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Сила атаки%: 10.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Посох алых песков (5★)":
        file = open('weapon/woodweapon/posoh peskov/posoh peskov.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Экипированный этим оружием персонаж получает бонус атаки, равный 52% от его мастерства стихий. Попадание по врагу элементальным навыком на 10 сек. наделяет Сном алых песков: экипированный этим оружием персонаж получает бонус атаки, равный 28% от мастерства стихий. Эффект складывается до 3 раз.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Сайно, Сян Лин")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 Шанс крит. попадания: 9.6 Уровень: 1 Вознесение: 0")

    elif message.text == "Посох Хомы (5★)":
        file = open('weapon/woodweapon/posoh homi/posoh homi.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает HP на 20%. Также даёт бонус атаки, равный 0,8% от макс. HP экипированного этим оружием персонажа. Когда HP экипированного этим оружием персонажа опускается ниже 50%, его сила атаки дополнительно увеличивается на 1% от его макс. HP.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Кандакия, Ху Тао, Сяо, Чжун Ли ")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Крит. урон: 14.4 Уровень: 1 Вознесение: 0")

    elif message.text == "Сияющая жатва (5★)":
        file = open('weapon/woodweapon/siyaushaya jatva/jatva.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает силу атаки на 28% от показателя восстановления энергии свыше 100%. Вы можете получить бонус силы атаки до 80%. Также даёт 30% восстановления энергии на 12 сек. после активации взрыва стихии.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Мика, Райдэн, Юнь Цзинь ")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Восст. энергии: 12 Уровень: 1 Вознесение: 0")

    elif message.text == "Усмиритель бед (5★)":
        file = open('weapon/woodweapon/usmiritel bed/usmiritel bed.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Даёт 12% бонус урона всеми элементами. Запуск элементального навыка накладывает Совершенствование на 20 сек., в результате чего сила атаки увеличивается на 3,2% в секунду. Может складываться до 6 раз. Когда персонаж, экипированный этим оружием, не на поле боя, бонус атаки от Совершенствования удваивается.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Шэнь Хэ")
        tgbot.send_message(message.chat.id, "Базовая атака: 49 Сила атаки%: 3.6 Уровень: 1 Вознесение: 0")

    if message.text == "★ Стрелковое оружие":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Аква симулякрум (5★)")
        item2 = types.KeyboardButton("Громовой пульс (5★)")
        item3 = types.KeyboardButton("Лук Амоса (5★)")
        item4 = types.KeyboardButton("Небесное крыло (5★)")
        item5 = types.KeyboardButton("Охотничья тропа (5★)")
        item6 = types.KeyboardButton("Первый великий фокус (5★)")
        item7 = types.KeyboardButton("Полярная звезда (5★)")
        item8 = types.KeyboardButton("Элегия погибели (5★)")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
        tgbot.send_message(message.chat.id, 'Выберите ваше оружие', reply_markup=markup)

    elif message.text == "Аква симулякрум (5★)":
        file = open('weapon/scouts/aqua simka/aqua simka.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает HP на 16%. Когда рядом есть враги, урон, наносимый персонажем, экипированным этим оружием, увеличивается на 20%. Эффект срабатывает, даже когда персонаж не на поле боя.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Элой, Фарузан, Фишль, Гань Юй, Горо, Лини, Тарталья, Ёимия, Е Лань")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 Крит. урон: 19.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Громовой пульс (5★)":
        file = open('weapon/scouts/thunder pulse/thunder pilse.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает силу атаки на 20% и дарует мощь Громовой эмблемы. На уровнях эмблемы 1, 2 или 3 урон обычной атаки увеличивается на 12%, 24% или 40% соответственно. Персонаж получает 1 уровень Громовой эмблемы в каждом из следующих случаев: при нанесении урона обычной атакой (эмблема действует 5 сек.); при применении элементального навыка (эмблема действует 10 сек.); когда элементальная энергия персонажа ниже 100% (эмблема исчезнет, когда элементальная энергия полностью восстановится). Продолжительность действия каждого уровня эмблемы рассчитывается индивидуально.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Элой, Ёимия, Тарталья, Эмбер ")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Крит. урон: 14.4 Уровень: 1 Вознесение: 0")

    elif message.text == "Лук Амоса (5★)":
        file = open('weapon/scouts/luk amosa/luk amosa.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает урон обычной и заряженной атаки на 12%. Каждые 0,1 сек. полёта стрелы, выпущенной обычной или заряженной атакой, увеличивают её урон на 8%. Эффект может складываться до 5 раз.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Эмбер, Гань Юй, Лини, Ёимия")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Сила атаки%: 10.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Небесное крыло (5★)":
        file = open('weapon/scouts/heaven krilo/heaven wing.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает крит. урон на 20%. При попадании есть 60% шанс нанести 125% физ. урона в небольшом радиусе. Может возникнуть раз в 4 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Элой, Эмбер, Фарузан, Фишль, Гань Юй, Горо, Сара, Лини, Тарталья, Тигнари, Венти, Ёимия")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Шанс крит. попадания: 4.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Охотничья тропа (5★)":
        file = open('weapon/scouts/hunter road/hunter road.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Даёт 12% бонус урона всеми элементами. Попадание заряженной атакой наделяет персонажа эффектом Непрестанной охоты, который увеличивает урон заряженных атак на 160% от мастерства стихий. Через 10 сек. либо после 12 активаций эффект исчезает. Может возникнуть один раз в 12 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Тигнари ")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 Шанс крит. попадания: 9.6 Уровень: 1 Вознесение: 0")

    elif message.text == "Первый великий фокус (5★)":
        file = open('weapon/scouts/first grand focus/first grand.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает урон заряженной атаки на 16%. Предоставляет 1 уровень Уловки за каждого персонажа того же элемента в отряде, что и экипированный персонаж (включая экипированного персонажа). За каждого персонажа отряда с другим элементом предоставляет 1 уровень Актёрского мастерства. Когда действуют 1/2/3 и более уровня Уловки, сила атаки повышается на 16%/32%/48%. Во время действия 1/2/3 и более уровней Актёрского мастерства скорость передвижения увеличивается на 4%/7%/10%.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Лини")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Крит. урон: 14.4 Уровень: 1 Вознесение: 0")

    elif message.text == "Полярная звезда (5★)":
        file = open('weapon/scouts/polar star/polar star.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Урон, наносимый элементальным навыком и взрывом стихии, увеличивается на 12%. Когда обычная атака, заряженная атака, элементальный навык или взрыв стихии попадают по врагу, возникает 1 ур. эффекта Звезда полярной ночи, который длится 12 сек. При 1/2/3/4 ур. эффекта Звезда полярной ночи сила атаки повышается на 10/20/30/48%. Уровни эффекта Звезда полярной ночи, созданные обычной атакой, заряженной атакой, элементальным навыком и взрывом стихии, существуют независимо.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Тарталья, Элой")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Шанс крит. попадания: 7.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Элегия погибели (5★)":
        file = open('weapon/scouts/eligia of death/eligia of death.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Часть Тысячелетней симфонии, что блуждает среди ветров. Увеличивает мастерство стихий на 60 ед. При попадании элементальным навыком или взрывом стихии по противнику персонаж получает один Талисман воспоминаний. Он может возникнуть раз в 0,2 сек., даже когда персонаж в отряде, но не активен. Четыре собранных Талисмана воспоминаний пропадают, на 12 сек. наделяя ближайших членов отряда эффектом «Тысячелетняя симфония: Прощальный гимн». Их мастерство стихии повышается на 100 ед., а сила атаки - на 20%. В течение 20 сек. после активации эффекта Талисманы воспоминаний появляться не будут. Тысячелетняя симфония с эффектами, влияющими на те же навыки, не складывается.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Коллеи, Диона, Фарузан, Горо, Венти, Е Лань")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Восст. энергии: 12 Уровень: 1 Вознесение: 0")

    if message.text == "★ Катализатор оружие":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Великолепие лазурного свода (5★)")
        item2 = types.KeyboardButton("Вечное лунное сияние (5★)")
        item3 = types.KeyboardButton("Воспоминания Тулайтуллы (5★)")
        item4 = types.KeyboardButton("Истина кагура (5★)")
        item5 = types.KeyboardButton("Казначейский надзор (5★)")
        item6 = types.KeyboardButton("Молитва святым ветрам (5★)")
        item7 = types.KeyboardButton("Небесный атлас (5★)")
        item8 = types.KeyboardButton("Обряд вечного течения (5★)")
        item9 = types.KeyboardButton("Память о пыли (5★)")
        item10 = types.KeyboardButton("Сновидения тысячи ночей (5★)")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
        tgbot.send_message(message.chat.id, 'Выберите ваше оружие', reply_markup=markup)

    elif message.text == "Великолепие лазурного свода (5★)":
        file = open('weapon/catalyst/velokolepie lasur/velikolepie lasur.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Когда экипированный персонаж активирует взрыв стихии или создаёт щит, он на 3 сек. получает эффект Камня воли: каждые 2,5 сек. восстанавливается 4,5 ед. энергии, а бонус урона соответствующего элемента повышается на 0,3% за каждую 1000 ед. макс. HP персонажа, максимум 12%. Эффект Камня воли активируется, даже если экипированный персонаж не на поле боя.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Кокоми, Бай Чжу")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 HP%: 10.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Вечное лунное сияние (5★)":
        file = open('weapon/catalyst/infinity Moonlight/infinity moon.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает бонус лечения на 10%, а также повышает урон обычной атаки на 1% от макс. HP экипированного этим оружием персонажа. В течение 12 сек. после использования взрыва стихии попадания обычной атакой по противнику восстанавливают 0,6 ед. энергии. Энергию можно восстановить не чаще чем раз в 0,1 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Кокоми, Бай Чжу")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 HP%: 10.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Воспоминания Тулайтуллы (5★)":
        file = open('weapon/catalyst/remember tulaitul/remember tulaitul.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Скорость обычной атаки повышается на 10%. После активации экипированным этим оружием персонажем элементального навыка урон обычной атаки будет повышаться на 4,8% в секунду в течение 14 сек. Пока этот эффект активен, каждое попадание по противнику мгновенно увеличивает урон обычной атаки на 9,6%. Увеличение может возникнуть один раз в 0,3 сек. Во время действия одного такого эффекта урон обычной атаки может быть увеличен максимум на 48%. Эффект будет снят, если персонаж покинет поле боя, а повторная активация элементального навыка сбросит увеличение урона.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Ризли, Странник")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Крит. урон: 9.6 Уровень: 1 Вознесение: 0")

    elif message.text == "Истина кагура (5★)":
        file = open('weapon/catalyst/istina kagura/istina kagura.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Использование элементального навыка наделяет экипированного этим оружием персонажа эффектом «Танец кагура», который увеличивает урон его элементального навыка на 12%. Этот эффект длится 16 сек. и может складываться до 3 раз. На 3 уровне эффекта персонаж получает 12% бонус урона всеми элементами.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Яэ Мико, Хэйдзо, Лиза")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Крит. урон: 14.4 Уровень: 1 Вознесение: 0")

    elif message.text == "Казначейский надзор (5★)":
        file = open('weapon/catalyst/kaznachei/kaznachei.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает силу атаки на 16%. Когда текущее HP персонажа повышается или понижается, на 4 сек. урон обычной атаки увеличивается на 16%, а заряженной атаки - на 14%. Эффект складывается до 3 раз и возникает не чаще, чем 1 раз в 0,3 сек. При получении экипированным персонажем 3 уровней скорость атаки увеличивается на 8%.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Ризли")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Шанс крит. попадания: 4.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Молитва святым ветрам (5★)":
        file = open('weapon/catalyst/pray saint winds/pray saint winds.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает скорость передвижения на 10%. Во время битвы даёт 8% бонус элементального урона каждые 4 сек. Может складываться до 4 раз. Эффект оканчивается, если персонаж погибает или покидает поле боя.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Кли, Лиза, Мона, Нёвиллет, Нин Гуан, Хэйдзо, Странник, Ризли, Яэ Мико, Янь Фэй ")
        tgbot.send_message(message.chat.id, "Базовая атака: 46  Шанс крит. попадания: 7.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Небесный атлас (5★)":
        file = open('weapon/catalyst/heaven atlas/heaven atlas.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает бонус элементального урона на 12%. При попадании обычной атакой есть 50% шанс получить благословение облаков, которые в течение 15 сек. атакуют ближайших врагов и наносят им 160% урона. Может возникнуть раз в 30 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Кли, Нин Гуан, Хэйдзо, Странник, Ризли, Яэ Мико, Янь Фэй, Шарлотта, Мона4 ")
        tgbot.send_message(message.chat.id, "Базовая атака: 48 Сила атаки%: 7.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Обряд вечного течения (5★)":
        file = open('weapon/catalyst/obryad infinity stream/obryad infin.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает HP на 16%. Когда текущее HP персонажа повышается или понижается, урон заряженной атаки увеличивается на 14% на 4 сек. Эффект складывается до 3 раз и возникает не чаще, чем 1 раз в 0,3 сек. При получении 3 уровней или обновлении времени длительности 3 уровня восстанавливается 8 ед. энергии. Восстанавливать энергию таким образом можно 1 раз в 12 сек.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Нёвиллет")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 Крит. урон: 19.2 Уровень: 1 Вознесение: 0")

    elif message.text == "Память о пыли (5★)":
        file = open('weapon/catalyst/remember of dust/remember of dust.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Увеличивает прочность щита на 20%. При попадании увеличивает силу атаки на 4% в течение 8 сек. Эффект может складываться до 5 раз и возникнуть раз в 0,3 сек. Кроме того, под защитой щита бонус силы атаки данного эффекта увеличивается на 100%.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Универсальное")
        tgbot.send_message(message.chat.id, "Базовая атака: 46 Сила атаки%: 10.8 Уровень: 1 Вознесение: 0")

    elif message.text == "Сновидения тысячи ночей (5★)":
        file = open('weapon/catalyst/1001 nights/1001 nights.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,"Другие члены отряда предоставляют экипированному этим оружием персонажу усиления в зависимости от того, совпадают их элементы, или нет. Если элементы совпадают, мастерство стихий повышается на 32 ед. Если не совпадают, экипированный этим оружием персонаж получает 10% бонус урона своего элемента. Данные эффекты складываются до 3 раз. Вдобавок мастерство стихий всех персонажей отряда поблизости (кроме экипированного этим оружием персонажа) увеличивается на 40 единиц. Если этим оружием обладают и другие члены отряда, эффект суммируется.")
        tgbot.send_message(message.chat.id, "Подходит персонажу: Нахида")
        tgbot.send_message(message.chat.id, "Базовая атака: 44 Мастерство стихий: 58 Уровень: 1 Вознесение: 0")






@tgbot.message_handler(commands=['build_guide'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Анемо")
    item2 = types.KeyboardButton("Крио")
    item3 = types.KeyboardButton("Гео")
    item4 = types.KeyboardButton("Электро")
    item5 = types.KeyboardButton("Пиро")
    item6 = types.KeyboardButton("Дендро")
    item7 = types.KeyboardButton("Гидро")
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    tgbot.send_message(message.chat.id, 'Выберите элемент вашего персонажа', reply_markup=markup)


@tgbot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Анемо":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Сяо")
        item2 = types.KeyboardButton("Кадзуха")
        item3 = types.KeyboardButton("Путешественник анемо")
        item4 = types.KeyboardButton("Джинн")
        item5 = types.KeyboardButton("Венти")
        item6 = types.KeyboardButton("Сахароза")
        item7 = types.KeyboardButton("Саю")
        item8 = types.KeyboardButton("Хэйдзо")
        item9 = types.KeyboardButton("Странник")
        item10 = types.KeyboardButton("Фарузан")
        item11 = types.KeyboardButton("Линетт")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
        tgbot.send_message(message.chat.id, 'Выберите вашего героя!', reply_markup=markup)

    elif message.text == "Сяо":
        file = open('anemo/syo/syo.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id, "Сяо (魈 Xiāo) – играбельный 5-звездочный Анемо-персонаж в Genshin Impact.")
        file2 = open('anemo/syo/build.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Универсальная сборка по урону и полезности. Оптимально для нанесения большого урона.")

    elif message.text == "Кадзуха":
        file = open('anemo/Kadzuha/Kadzuha.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Кадзуха (枫原万叶 Fēngyuán Wànyè) – играбельный Анемо-персонаж в Genshin Impact.")
        file2 = open('anemo/Kadzuha/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Хорошая сборка для роли поддержки.")
        file3 = open('anemo/Kadzuha/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Повышает урон Кадзухи, а не реакции.Отлично подходит для DPS-сборки, которая фокусируется на навыках и взрыве. Также возможна комбинация двух данных сетов")

    elif message.text == "Путешественник анемо":
        file = open('anemo/traveleranemo/traveleranemo.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Путешественник – главный герой Genshin Impact. Пришедший из другого мира в поисках семи Архонтов путешественник(ца), пытающийся вернуть свою сестрёнку(брата).")
        file2 = open('anemo/traveleranemo/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Хорошая синергия с другими элементами. Сокрушайте мобов с помощью широкого диапазона атак с высоким уроном.")
        file3 = open('anemo/traveleranemo/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Увеличенный урон.")

    elif message.text == "Джинн":
        file = open('anemo/Jinn/Jinn.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Джинн (琴Qín) – играбельный Анемо-персонаж в Genshin Impact. Справедливый и искренний Рыцарь Одуванчик, действующий магистр Ордо Фавониус.")
        file2 = open('anemo/Jinn/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Полезно для Джинн, она полагается на исцеление при нанесении урона врагам. Отличная поддержка от дополнительного исцеления.")
        file3 = open('anemo/Jinn/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Подойдёт до получения полного комплекта Конца гладиатора. В качестве альтернативы можно использовать Душу храбреца.")

    elif message.text == "Венти":
        file = open('anemo/Wenti/Wenti.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Венти (温蒂 wēn dì, собирательное название римских богов ветра) – играбельный 5-звездочный Анемо персонаж в Genshin Impact. Обычный бард, слоняющийся по улочкам Мондштадта.")
        file2 = open('anemo/Wenti/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Ослабляет врагов, увеличивая урон. Быстро убивайте врагов с помощью Стихийных реакций.")
        file3 = open('anemo/Wenti/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Увеличивает урон от Элементального взрыва. Усиливает Венти как основного DPS персонажа.")

    elif message.text == "Сахароза":
        file = open('anemo/Saharoza/Saharoza.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Сахароза (砂糖 Shātáng) – играбельный Анемо-персонаж в Genshin Impact. Алхимик, преисполненная любопытством по отношению ко всему на свете. Она занимается исследованием биоалхимии.")
        file2 = open('anemo/Saharoza/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Распространяйте дебаффы (ослабление) на врагов, увеличивая урон.Предоставляет отличную поддержку.")
        file3 = open('anemo/Saharoza/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Подойдёт если нет Изумрудной тени.Подходит для роли DPS персонажа поддержки.")

    elif message.text == "Саю":
        file = open('anemo/Sayu/Sayu.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Саю (早柚 Zǎoyòu) – играбельный Анемо-персонаж в Genshin Impact. Особый ниндзя Сиюмацу-бан. Маленькая и необычайно ловкая.")
        file2 = open('anemo/Sayu/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Отлично подходит для роли поддержки. Увеличивает Рассеивание при сборке в урон.")
        file3 = open('anemo/Sayu/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Усиливает не только Саю, но и всю команду.")

    elif message.text == "Хэйдзо":
        file = open('anemo/Heidzo/Heidzo.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Сиканоин Хэйдзо (鹿野院平藏 Lùyěyuàn Píngzàng) – играбельный Анемо-персонаж в Genshin Impact. Талантливый молодой детектив из комиссии Тэнрё. Отличается ясным умом и острым восприятием.")
        file2 = open('anemo/Heidzo/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Отлично подходит для Мейн-ДПС")
        file3 = open('anemo/Heidzo/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Можно разбавить первый билд данным сетом, это повышает собственный урон Хэйдзо и больше подходит для усиления Анемо-урона, а не реакций.")

    elif message.text == "Странник":
        file = open('anemo/wanderer/wanderer.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Странник (流浪者 Liúlàng-zhě) – играбельный 5-звездочный Анемо-персонаж в Genshin Impact. Скиталец, личность которого остаётся загадкой. Носит одежды сюгэндзя, но высказываниями и действиями на ищущих просветления сюгэндзя совсем не похож.")
        file2 = open('anemo/wanderer/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Идеальный и лучший сет для роли Мейн-ДПС")
        file3 = open('anemo/wanderer/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('anemo/wanderer/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс из этих двух билдов, повышает Анемо-урон и силу атаки, подойдет в качестве временной замены, пока не соберете Хроники.")

    elif message.text == "Фарузан":
        file = open('anemo/Faruzan/Faruzan.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Фарузан (珐露珊 Fàlùshān) – играбельный 4-звездочный Анемо-персонаж в Genshin Impact. Исследовательница из «прошлого века». Ей нравится считать себя старше всех, при этом она обладает обширными познаниями о старинных письменах и древних механизмах.")
        file2 = open('anemo/Faruzan/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Лучший вариант для роли саппорта")

    elif message.text == "Линетт":
        file = open('anemo/Linett/Linett.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Линетт (琳妮特 Línnītè) – играбельный 4-звездочный Анемо-персонаж в Genshin Impact. Немногословная ассистентка иллюзиониста, редко выражающая эмоции. Похожа на кошку своим сложным характером.")
        file2 = open('anemo/Linett/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Хорошая синергия с другими элементами. Подходит для Линетт в любой роли.")

    if message.text == "Крио":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Кэйя")
        item2 = types.KeyboardButton("Гань Юй")
        item3 = types.KeyboardButton("Аяка")
        item4 = types.KeyboardButton("Ци Ци")
        item5 = types.KeyboardButton("Эола")
        item6 = types.KeyboardButton("Розария")
        item7 = types.KeyboardButton("Чун Юнь")
        item8 = types.KeyboardButton("Шэнь Хэ")
        item9 = types.KeyboardButton("Диона")
        item10 = types.KeyboardButton("Лайла")
        item11 = types.KeyboardButton("Мика")
        item12 = types.KeyboardButton("Фремине")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        tgbot.send_message(message.chat.id, 'Выберите вашего героя!', reply_markup=markup)

    elif message.text == "Кэйя":
        file = open('crio/keya/keya.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Кэйа Альберих (凯亚 Kǎiyà) – играбельный Крио-персонаж в Genshin Impact.Капитан Ордо Фавониус выглядит довольно экзотично. Несмотря на дружелюбие и приветливость, от него веет странным холодком.")
        file2 = open('crio/keya/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Билд персонажа поддержки. Хороший бонус от элементального взрыва.")
        file3 = open('crio/keya/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Хорошо сочетается с высоким критическим уроном.")

    elif message.text == "Гань Юй":
        file = open('crio/Gan yui/gan yui.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Гань Юй (甘雨 Gānyǔ) – играбельный Крио-персонаж в Genshin Impact. Главный секретарь павильона Лунного моря. В её жилах течёт кровь мифического зверя цилиня.")
        file2 = open('crio/Gan yui/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Хорошо сочетается с силой Гань Юй. Подходит для роли поддержки.")
        file3 = open('crio/Gan yui/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Сборка персонажа поддержки. Подходит для элементального взрыва. Данную сборку можно разбавить предметами из первого сета.")

    elif message.text == "Аяка":
        file = open('crio/Gan yui/gan yui.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Камисато Аяка (神里绫华 Shénlǐ Línghuá) – играбельный Крио-персонаж в Genshin Impact. Наследница клана Камисато комиссии Ясиро. Благородна и изящна, мудра и сильна.")
        file2 = open('crio/Gan yui/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Хорошо сочетается с силой Гань Юй. Подходит для роли поддержки.")
        file3 = open('crio/Gan yui/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Сборка персонажа поддержки. Подходит для элементального взрыва. Данную сборку можно разбавить предметами из первого сета.")

    elif message.text == "Ци Ци":
        file = open('crio/Chi Chi/chi chi.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Ци Ци (七七 Qīqī) – играбельный Крио-персонаж в Genshin Impact. Ученица и сборщица трав из хижины Бубу. Зомби с бледным лицом, разговаривает или проявляет эмоции очень редко…")
        file2 = open('crio/Chi Chi/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Подходит для Ци Ци, чья атака увеличивает лечение. Повышенный урон также помогает в поддержке.")
        file3 = open('crio/Chi Chi/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Превращает Ци Ци в супер целителя. Позволяет не возиться с едой или сэкономить её.")

    elif message.text == "Эола":
        file = open('crio/Eola/eola.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Эола (优菈 Yōu lā) – играбельный Крио-персонаж в Genshin Impact. Рыцарь Морская пена из старинного рода аристократов Мондштадта, капитан разведывательного отряда рыцарей Ордо Фавониус.")
        file2 = open('crio/Eola/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Лучший выбор для физ. сборки Эолы.")
        file3 = open('crio/Eola/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Данную сборку можно разбавить первым сетом, и будет меньший, но более стабильный урон без необходимости выполнения условий.")

    elif message.text == "Розария":
        file = open('crio/Rozaria/rozaria.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Розария (罗莎莉亚 Luō shā lì yà) – играбельный Крио-персонаж в Genshin Impact.Кроме её одеяния ничто не напоминает о её принадлежности церкви. Известна своими холодными речами и резкими поступками. ")
        file2 = open('crio/Rozaria/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('crio/Rozaria/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов ,Билд сконцентрирован на физическом уроне. Отлично, если Розария будет назначена главным DPS.")
        file4 = open('crio/Rozaria/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        file5 = open('crio/Rozaria/build4.png', 'br')
        tgbot.send_photo(message.chat.id, file5)
        tgbot.send_message(message.chat.id, "Микс двух сетов,отлично подходит для крио поддержки.")

    elif message.text == "Чун Юнь":
        file = open('crio/Chun yun/chun yun.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Чун Юнь (重云 Zhòng yún) – играбельный 4-звездочный Крио-персонаж в Genshin Impact. Молодой экзорцист из семьи экзорцистов. Изо всех сил старается подавить свою энергию Ян.")
        file2 = open('crio/Chun yun/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Набор более эффективен с высоким крит. уроном. Подходит для персонажа поддержки.")
        file3 = open('crio/Chun yun/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Если нет полного комплекта Заблудшего в метели. Отличный сет с повышенным уроном.")

    elif message.text == "Шэнь Хэ":
        file = open('crio/Shan He/shan he.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Шэнь Хэ (申鹤 Shēnhè) – играбельный Крио-персонаж в Genshin Impact. Ученица Адептов, утратившая связь с внешним миром. Годы затворнической жизни в горах Ли Юэ сделали её такой же отстранённой и холодной, как сами Адепты.")
        file2 = open('crio/Shan He/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Фокусируется на увеличении собственного урона. Баффы будут слабее, но урон, наносимый Шэнь Хэ, будет выше.")
        file3 = open('crio/Shan He/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('crio/Shan He/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id, "Микс двух сетов,фокусируется на усилении команды вместо урона Шэнь Хэ.")

    elif message.text == "Диона":
        file = open('crio/Diona/diona.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Диона (迪奥娜 Dí’ào nà) – играбельный Крио персонаж в Genshin Impact. Молодая девушка, унаследовавшая остаточную долю нечеловеческой крови. Она невероятно популярный бармен таверны “Кошкин хвост”.")
        file2 = open('crio/Diona/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Подходит для роли поддержки.Увеличивает урон элементального взрыва и усиливает союзников.")
        file3 = open('crio/Diona/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('crio/Diona/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов, усиливает собственный урон Дионы. Усиливает элементальный взрыв.")

    elif message.text == "Лайла":
        file = open('crio/Layla/layla.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Лайла (莱依拉 Láiyīlā) – играбельный 4-звездочный Крио-персонаж в Genshin Impact. Студентка, которая изучает теоретическую астрологию в даршане Ртавахист. Нередко ходит во сне и страдает от хронического недосыпания.")
        file2 = open('crio/Layla/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Отлично походит для роли поддержки и дает самый прочный щит.")
        file3 = open('crio/Layla/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('crio/Layla/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов, увеличивает урон всех навыков Лайлы. Больше подойдет для роли Саб-ДПС.")

    elif message.text == "Мика":
        file = open('crio/Mika/ mika.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Мика (米卡 Mǐkǎ) – играбельный 4-звездочный Крио-персонаж в Genshin Impact. Молодой рыцарь из обычной семьи, который служит передовым геодезистом отряда. Он застенчив и осторожен.")
        file2 = open('crio/Mika/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Лучше всего для баффа ATK при использовании в качестве поддержки")
        file3 = open('crio/Mika/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Увеличивает исцеление Мики и позволяет наносить дополнительный урон")

    elif message.text == "Фремине":
        file = open('crio/Fremine/fremine.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Фремине (菲米尼 Fēimǐní) – играбельный 4-звездочный Крио-персонаж в Genshin Impact. Сдержанный молодой человек, мастер подводного плавания. За его отстранённой, ледяной наружностью скрывается чистая душа без единого порока.")
        file2 = open('crio/Fremine/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('crio/Fremine/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов,универсальный билд для Саб-ДД Фремине. В зависимости от сборки можно использовать любой полный набор")

    if message.text == "Гео":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Альбедо")
        item2 = types.KeyboardButton("Путешественник гео")
        item3 = types.KeyboardButton("Чжун Ли")
        item4 = types.KeyboardButton("Нин Гуан")
        item5 = types.KeyboardButton("Ноэлль")
        item6 = types.KeyboardButton("Горо")
        item7 = types.KeyboardButton("Итто")
        item8 = types.KeyboardButton("Юнь Цзинь")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
        tgbot.send_message(message.chat.id, 'Выберите вашего героя!', reply_markup=markup)

    elif message.text == "Альбедо":
        file = open('geo/albedo/albedo.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Альбедо (阿贝多 Ā bèiduō) – играбельный Гео-персонаж в Genshin Impact. Гений, именуемый Принцем мела. Главный алхимик и глава исследовательской команды Ордо Фавониус.")
        file2 = open('geo/albedo/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('geo/albedo/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Подходит для персонажа поддержки. Увеличенный урон по всем направлениям.")
        file4 = open('geo/albedo/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id, "Микс двух сетов. Самый стабильный сет и для поддержки, и для урона.")


    elif message.text == "Путешественник гео":
        file = open('geo/travelergeo/travelergeo.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Путешественник (По-китайски: 旅行者 Lǚxíng zhě, “Путешественник”) – главный герой Genshin Impact. Пришедший из другого мира в поисках семи Архонтов путешественник(ца), пытающийся вернуть свою сестрёнку(брата).")
        file2 = open('geo/travelergeo/build1.png', 'br')
        tgbot.send_message(message.chat.id,
                           "Подходит для роли поддержки. Усиливает союзников с помощью элементального взрыва.")
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('geo/travelergeo/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('geo/travelergeo/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов,увеличенный урон с помощью элементального навыка и элементального взрыва.")


    elif message.text == "Чжун Ли":
        file = open('geo/jun li/jun li.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Чжун Ли (钟离 Zhōnglí) – играбельный Гео персонаж в Genshin Impact. Приглашённый специалист ритуального бюро “Ваншэн”. Необычайно загадочен и сведущ во всех делах.")
        file2 = open('geo/jun li/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Сет для поддержки при помощи стихийного взрыва. Усиливает союзников с помощью стихийного взрыва.")
        file3 = open('geo/jun li/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('geo/jun li/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Увеличенный урон с помощью элементального навыка и элементального взрыва.")

    elif message.text == "Нин Гуан":
        file = open('geo/ninguan/ninguan.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Нин Гуан (Níng guāng) – играбельный Гео-персонаж в Genshin Impact.Воля Небес группировки Цисин. Её богатство несравнимо ни с кем на континенте Тейват.")
        file2 = open('geo/ninguan/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('geo/ninguan/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Частые элементальные взрывы с увеличенным уроном. Поддержка союзников.")
        file4 = open('geo/ninguan/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Хорошо подходит для роли поддержки.Увеличивает элементальный урон союзников.")

    elif message.text == "Ноэлль":
        file = open('geo/noell/noell.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Ноэлль (诺伊尔 Nuò yī ěr) – играбельный Гео персонаж в Genshin Impact. Горничная Ордо Фавониус, которая страстно мечтает однажды пополнить ряды ордена.")
        file2 = open('geo/noell/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Повышает атаку и защиту. Может работать как главный DPS.")
        file3 = open('geo/noell/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('geo/noell/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов,этот билд нацелен на универсальность. Превращает Ноэлль в хороший танк.")


    elif message.text == "Горо":
        file = open('geo/goro/goro.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Горо (五郎 Wǔláng) – играбельный Гео-персонаж в Genshin Impact. Великий генерал армии Ватацуми, пользуется безграничным доверием своих подчинённых.")
        file2 = open('geo/goro/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('geo/goro/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Оптимальный вариант для Гео-поддержки команды.")

    elif message.text == "Итто":
        file = open('geo/itto/itto.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Аратаки Итто (荒泷一斗 Huānglóng Yīdǒu) – играбельный Гео-персонаж в Genshin Impact. Первый и величайший предводитель банды Аратаки, прославленной по всей Ханамидзаке города Инадзумы.")
        file2 = open('geo/itto/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Идеальный вариант сборки для роли главного дамагера команды.")

    elif message.text == "Юнь Цзинь":
        file = open('geo/yun chin/yun chin.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Юнь Цзинь (云堇 Yún Jǐn) – играбельный Гео-персонаж в Genshin Impact. Прославленная оперная певица Ли Юэ, которая искусна как в написании пьес, так и в пении. Её неповторимый стиль, изысканный и нежный, — это отражение глубин её души.")
        file2 = open('geo/yun chin/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Увеличивает усиление обычной атаки Юнь Цзинь, а также собственный урон.")

    if message.text == "Пиро":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Ху Тао")
        item2 = types.KeyboardButton("Дэхья")
        item3 = types.KeyboardButton("Лини")
        item4 = types.KeyboardButton("Ёимия")
        item5 = types.KeyboardButton("Дилюк")
        item6 = types.KeyboardButton("Кли")
        item7 = types.KeyboardButton("Беннет")
        item8 = types.KeyboardButton("Янь Фэй")
        item9 = types.KeyboardButton("Сян Лин")
        item10 = types.KeyboardButton("Синь Янь")
        item11 = types.KeyboardButton("Эмбер")
        item12 = types.KeyboardButton("Тома")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        tgbot.send_message(message.chat.id, 'Выберите вашего героя!', reply_markup=markup)

    elif message.text == "Ху Тао":
        file = open('piro/hu tao/hu tao.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Ху Тао (胡桃 Hútáo) – играбельный Пиро-персонаж в Genshin Impact. Хозяйка ритуального бюро «Ваншэн» в семьдесят седьмом поколении. Она унаследовала этот бизнес в достаточно юном возрасте.")
        file2 = open('piro/hu tao/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Значительно увеличивает Пиро-урон. Отлично подходит для игры через реакции.")
        file3 = open('piro/hu tao/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('piro/hu tao/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов, Увеличивает HP Ху Тао и ее общий урон. Немного слабее, чем полный сет Ведьмы, но неплохой вариант.")

    elif message.text == "Дэхья":
        file = open('piro/dehia/dehia.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Дэхья (迪希雅 Díxīyǎ) – играбельный 5-звездочный Пиро-персонаж в Genshin Impact. Член Пустынников, группы наёмников из Сумеру. Сильная и смелая, она пользуется безупречной репутацией среди Пустынников.")
        file2 = open('piro/dehia/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Значительно увеличивает Пиро-урон. Отлично подходит для игры вне Моно-Пиро команды.")
        file3 = open('piro/dehia/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Позволяет дополнительно баффать АТК команде.")

    elif message.text == "Лини":
        file = open('piro/lini/lini.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Лини (林尼 Línní) – играбельный 5-звездочный Пиро-персонаж в Genshin Impact. Маг-иллюзионист из Фонтейна, завораживающий публику ловкостью рук и красноречием.")
        file2 = open('piro/lini/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Лучший вариант для любой из сборок Лини. Повышает Крит. шанс на 36%")

    elif message.text == "Ёимия":
        file = open('piro/eimia/eimia.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Ёимия (宵宮 Xiāogōng) – играбельный Пиро-персонаж в Genshin Impact. Владелица «Фейерверков Наганохары», так же известна как «Королева праздника лета». Будучи мастером своего дела, она воплощает надежды и мечты людей в своих фейерверках.")
        file2 = open('piro/eimia/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Отлично подходит для Мейн-ДД Ёимии. Увеличивает общий урон и урон от обычных атак.")
        file3 = open('piro/eimia/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('piro/eimia/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Более гибкая сборка для Мейн-ДД Ёимии. Ёимии легче набирать энергию для Взрыва стихий, если сравнивать с Симэнавой.")

    elif message.text == "Дилюк":
        file = open('piro/dilyuk/dilyuk.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Дилюк (迪卢克 Dí lú kè) – играбельный Пиро-персонаж в Genshin Impact. Магнат, построивший непревзойдённую винную империю в Мондштадте.")
        file2 = open('piro/dilyuk/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Значительно увеличивает Пиро-урон.")
        file3 = open('piro/dilyuk/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('piro/dilyuk/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Увеличивает и Элементальный, и Физический урон. Более гибкая сборка.")

    elif message.text == "Кли":
        file = open('piro/kli/kli.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Кли (可莉 Kě lì) – играбельный 5-звездочный Пиро-персонаж в Genshin Impact. Эксперт по взрывчатке и частый гость темницы Ордо Фавониус. Также известна, как «Ускользающее солнце».")
        file2 = open('piro/kli/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Значительно увеличивает Пиро-урон.")
        file3 = open('piro/kli/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('piro/kli/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Отлично усиляет все типы атак Кли. Чуть слабее полного сета Ведьмы, но подойдет как альтернатива.")

    elif message.text == "Беннет":
        file = open('piro/bennet/bennet.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Беннет (班尼特 Bānnítè) – играбельный Пиро-персонаж в Genshin Impact. Добросердечный и порядочный искатель приключений из Мондштадта, который, к несчастью, сказочно невезуч.")
        file2 = open('piro/bennet/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Идеально подходит для Беннета в роли поддержки, чтобы усилять всю команду.")
        file3 = open('piro/bennet/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Увеличивает урон Беннета, больше подойдет для роли Саб-ДД")

    elif message.text == "Янь Фэй":
        file = open('piro/yan fai/yan fai.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Янь Фэй (烟绯 Yān fēi) – играбельный Пиро-персонаж в Genshin Impact. Известный консультант по юридическим вопросам из Ли Юэ. Проницательная девушка, в чьих венах течёт кровь Божественного зверя.")
        file2 = open('piro/yan fai/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Значительно увеличивает Пиро-урон. Усиливает заряженные атаки и урон от реакций.")
        file3 = open('piro/yan fai/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Значительно увеличивает Пиро-урон. Может плохо сочетаться с большим временем отката навыков Янь Фэй.")

    elif message.text == "Сян Лин":
        file = open('piro/syan lin/syan lin.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Сян Лин (香菱 Xiānglíng) – играбельный Пиро-персонаж в Genshin Impact. Знаменитый шеф-повар из Ли Юэ. Она относится к готовке со всей страстью. Её фирменным рецептам острых блюд нет равных на всём Тейвате.")
        file2 = open('piro/syan lin/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('piro/syan lin/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Микс двух сетов. Больше подходит для роли Поддержки или Саб-ДД.")
        file4 = open('piro/syan lin/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id, "Идеально подойдет для Саб-ДД с фокусом на Взрыв стихий.")

    elif message.text == "Синь Янь":
        file = open('piro/sin yan/sin yan.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Синь Янь (По-китайски: 辛焱 Xīn yàn) – играбельный пиро-персонаж в Genshin Impact. Единственный рок-музыкант Ли Юэ. Своей вдохновляющей музыкой и пением она выражает протест предубеждениям.")
        file2 = open('piro/sin yan/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Увеличивает урон и силу щита. Универсальная сборка для большинства ситуаций.")
        file3 = open('piro/sin yan/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('piro/sin yan/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Особенно подходит для ситуаций с большим количеством противников. Сборка для максимального физического урона.")

    elif message.text == "Эмбер":
        file = open('piro/ember/ember.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Эмбер (По-китайски: 安柏 Ān bǎi) – играбельный Пиро персонаж в Genshin Impact. Энергичная и весёлая Эмбер. Лучший и единственный скаут Ордо Фавониус.")
        file2 = open('piro/ember/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Подходит для персонажей поддержки. Обеспечивает усиление товарищей по команде.")
        file3 = open('piro/ember/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Подходит для некоторых ситуаций. Увеличивает мощь элементального взрыва.")

    elif message.text == "Тома":
        file = open('piro/toma/toma.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Тома – играбельный Пиро-персонаж в Genshin Impact. Управляющий клана Камисато. Известный в Инадзуме “местный авторитет”")
        file2 = open('piro/toma/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('piro/toma/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Подходит для роли поддержки-щита. Увеличивает щит персонажа.")
        file4 = open('piro/toma/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id, "Увеличивает урон от взрыва стихий.")

    if message.text == "Электро":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Кэ Цин")
        item2 = types.KeyboardButton("Фишль")
        item3 = types.KeyboardButton("Бэй Доу")
        item4 = types.KeyboardButton("Лиза")
        item5 = types.KeyboardButton("Рэйзор")
        item6 = types.KeyboardButton("Сёгун Райдэн")
        item7 = types.KeyboardButton("Сара Кудзё")
        item8 = types.KeyboardButton("Путешественник электро")
        item9 = types.KeyboardButton("Яэ Мико")
        item10 = types.KeyboardButton("Куки Синобу")
        item11 = types.KeyboardButton("Дори")
        item12 = types.KeyboardButton("Сайно")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        tgbot.send_message(message.chat.id, 'Выберите вашего героя!', reply_markup=markup)

    elif message.text == "Кэ Цин":
        file = open('electro/kecin/kecin.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Кэ Цин (刻晴 Kè qíng) – играбельный Электро-персонаж в Genshin Impact. Нефритовое Равновесие группировки Цисин в Ли Юэ.")
        file2 = open('electro/kecin/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Цепочка массового комбо урона. Хороший набор для физического урона.")
        file3 = open('electro/kecin/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('electro/kecin/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Подходит для стихийного DPS.Отличный баланс с приличным уроном.")

    elif message.text == "Фишль":
        file = open('electro/fishle/fishle.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Фишль – играбельный 4-звездочный Электро-персонаж в Genshin Impact. Таинственная девушка, называющая себя «Принцессой осуждения» и путешествующая в сопровождении ворона по имени Оз.")
        file2 = open('electro/fishle/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Хороший комплект для урона и элементальных реакций.Должен работать в паре с персонажем Пиро / Гидро / Крио.")
        file3 = open('electro/fishle/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('electro/fishle/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id, "Микс двух сетов. Усиливает Оза. Легко получить и использовать.")

    elif message.text == "Бэй Доу":
        file = open('electro/baidou/baidou.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Бэй Доу (北斗 Běidǒu) – играбельный Электро персонаж в Genshin Impact. Капитан флота Южного Креста. Она весьма рисковая и прямолинейная леди.")
        file2 = open('electro/baidou/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Хорошо работает с обычной и заряженной атакой. Сборка для максимального физического урона.")
        file3 = open('electro/baidou/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Подходит для роли поддержки. Усиливает элементальный взрыв.")

    elif message.text == "Лиза":
        file = open('electro/lisa/lisa.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Лиза (丽莎 Lìshā) – играбельный Электро-персонаж в Genshin Impact. Ленивый, но безгранично эрудированный библиотекарь Ордо Фавониус. Лучшая выпускница академии Сумеру за последние несколько веков.")
        file2 = open('electro/lisa/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Подходит для роли поддержки. Усиливает элементальный взрыв.")
        file3 = open('electro/lisa/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Билд для усиления элементальных реакций.")

    elif message.text == "Рэйзор":
        file = open('electro/razor/razor.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Рэйзор (雷澤 Léi zé) – играбельный Электро-персонаж в Genshin Impact. Мальчик, живущий среди волков в Вольфендоме у Мондштадта, вдали от цивилизации. Ловок как молния.")
        file2 = open('electro/razor/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Хорошо работает с атаками Рэйзора.Сборка основного DPS.")
        file3 = open('electro/razor/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('electro/razor/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Отличный набор для физического урона. Хорошо подходит для Рэйзора.")

    elif message.text == "Сёгун Райдэн":
        file = open('electro/segunraiden/segunraiden.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Сёгун Райдэн – играбельный Электро-персонаж в Genshin Impact. Известна как Баал, Электро Архонт Инадзумы.")
        file2 = open('electro/segunraiden/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('electro/segunraiden/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов.Подходит для роли поддержки.Увеличивает основной и Электро-урон персонажа.")
        file4 = open('electro/segunraiden/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Лучший сет для Райдэн, так как он обеспечивает достаточно Восстановления энергии и дополнительный урон в зависимости от него.")

    elif message.text == "Сара Кудзё":
        file = open('electro/sarakudze/sarakudze.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Сара Кудзё – играбельный Электро-персонаж в Genshin Impact. Действующий генерал комиссии Тэнрё. Решительный убийца и храбрый воин.")
        file2 = open('electro/sarakudze/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('electro/sarakudze/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Увеличит урон от Взрыва стихий и общий Электро-урон. Лучше всего подойдет для Burst-cборки.")
        file4 = open('electro/sarakudze/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id, "Билд для усиления элементальных реакций и Электро-урона.")

    elif message.text == "Путешественник электро":
        file = open('electro/travelerelectro/travelerelectro.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Путешественник(ца) — играбельный персонаж и протагонист Genshin Impact. В начале повествования игры брат и сестра, путешествующие по разным мирам, попадают в ловушку Неизвестного божества.")
        file2 = open('electro/travelerelectro/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Увеличивает Электро урон. Подойдет как для роли поддержки, так и для урона.")


    elif message.text == "Яэ Мико":
        file = open('electro/yaemiko/yaemiko.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Яэ Мико (八重神子 Bāchóng Shénzǐ) – играбельный Электро-персонаж в Genshin Impact. Гудзи Великого храма Наруками, а также главный редактор издательского дома Яэ.")
        file2 = open('electro/yaemiko/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('electro/yaemiko/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Подходит для увеличения общего урона Яэ. При этой сборке понадобится персонаж-батарейка.")
        file4 = open('electro/yaemiko/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        file5 = open('electro/yaemiko/build4.png', 'br')
        tgbot.send_photo(message.chat.id, file5)
        tgbot.send_message(message.chat.id, "Микс двух сетов. Лучше всего подойдет для Burst-cборки Яэ.")

    elif message.text == "Куки Синобу":
        file = open('electro/kukisinobu/kukisinobu.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Куки Синобу (久岐忍 Jiǔqí Rěn) – играбельный Электро-персонаж в Genshin Impact. Способная и надёжная помощница главаря банды Аратаки.")
        file2 = open('electro/kukisinobu/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Позволяет Куки повышать атаку и щита, обеспечивая при этом приличное исцеление.")
        file3 = open('electro/kukisinobu/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('electro/kukisinobu/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Увеличивает урон от Взрыва стихий. Все еще обеспечивает хорошее исцеление, но бафф уменьшен.")

    elif message.text == "Дори":
        file = open('electro/dori/dori.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Дори (多莉) – играбельный Электро-персонаж в Genshin Impact. Неуловимая негоциантка из Сумеру, которая очень любит блеск монет.")
        file2 = open('electro/dori/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('electro/dori/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Позволяет чаще использовать Взрыв стихий и больше исцелять.")


    elif message.text == "Сайно":
        file = open('electro/saino/saino.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Сайно (赛诺 Sàinuò) – играбельный 5-звездочный Электро-персонаж в Genshin Impact. Генерал махаматра, который осуществляет надзор над всеми учёными Академии. ")
        file2 = open('electro/saino/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Увеличивает общий Электро-урон и урон от реакций. Лучший вариант без сигнатурного копья.")
        file3 = open('electro/saino/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Сильно увеличивает Мастерство стихий и общий урон Сайно. Идеальный вариант при использовании с сигнатурным копьем.")

    if message.text == "Дендро":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Путешественник дендро")
        item2 = types.KeyboardButton("Тигнари")
        item3 = types.KeyboardButton("Коллеи")
        item4 = types.KeyboardButton("Нахида")
        item5 = types.KeyboardButton("Яо Яо")
        item6 = types.KeyboardButton("Кавех")
        item7 = types.KeyboardButton("Аль-Хайтам")
        item8 = types.KeyboardButton("Бай Чжу")
        item9 = types.KeyboardButton("Кирара")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
        tgbot.send_message(message.chat.id, 'Выберите вашего героя!', reply_markup=markup)

    elif message.text == "Путешественник дендро":
        file = open('dendro/travelerdendro/travelerdendro.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Путешественник (旅行者 Lǚxíng zhě) – главный герой Genshin Impact. Пришедший из другого мира в поисках семи Архонтов путешественник(ца), пытающийся вернуть свою сестрёнку(брата).")
        file2 = open('dendro/travelerdendro/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Хорошо подходит для роли поддержки. Увеличивает урон реакций от навыков.")
        file3 = open('dendro/travelerdendro/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Подходит для частого Взрыва стихий.")

    elif message.text == "Тигнари":
        file = open('dendro/tignari/tignari.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Тигнари (提纳里 Tínàlǐ) – играбельный 5-звездочный Дендро-персонаж в Genshin Impact. Молодой учёный, хорошо разбирающийся в ботанике. В настоящее время служит лесным стражем в лесу Авидья")
        file2 = open('dendro/tignari/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Самый большой Дендро-урон и лучший сет для Тигнари.")
        file3 = open('dendro/tignari/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Сфокусирован на заряженных атаках и реакциях. Подойдет, если пока нет хороших Воспоминаний дремучего леса.")

    elif message.text == "Коллеи":
        file = open('dendro/kollei/kollei.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Коллеи (柯莱 Kēlái) – играбельный 4-звездочный Дендро-персонаж в Genshin Impact. Стажёр Лесного дозора в лесу Авидья. За её энергичной речью и действиями скрывается довольно закрытая личность.")
        file2 = open('dendro/kollei/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Хорошо подходит для увеличения общего урона.")
        file3 = open('dendro/kollei/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Подходит для частого Взрыва стихий и помогает справиться с его высокой стоимостью.")

    elif message.text == "Нахида":
        file = open('dendro/nahida/nahida.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Нахида (纳西妲 Nàxīdá) – играбельный 5-звездочный Дендро-персонаж в Genshin Impact. Узница глубин Храма Сурастаны, которая созерцает мир только в сновидениях.")
        file2 = open('dendro/nahida/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Максимально увеличивает Мастерство стихий. Отлично подходит для усиления реакций Нахиды и команды.")
        file3 = open('dendro/nahida/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Увеличивает собственный урон от навыков. Используйте его, если никто из персонажей в команде еще не носит этот сет.")

    elif message.text == "Яо Яо":
        file = open('dendro/yaoyao/yaoyao.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Яо Яо (瑶瑶 Yáoyao) – играбельный 4-звездочный Дендро-персонаж в Genshin Impact. Младшая ученица Владыки Песен и Скитаний, добрый и заботливый «маленький взрослый».")
        file2 = open('dendro/yaoyao/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Отлично подходит для роли хиллера. Дополнительный бафф к АТК для команды.")
        file3 = open('dendro/yaoyao/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Выбирайте этот сет, если Яо Яо в команде с другим Дендро персонажем. Увеличивает урон Яо Яо и Дендро вне поля.")

    elif message.text == "Кавех":
        file = open('dendro/kaveh/kaveh.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Кавех (卡维 Kǎwéi) – играбельный 4-звездочный Дендро-персонаж в Genshin Impact. Знаменитый архитектор из Сумеру, поглощённый заботами. Эстет, обеспокоенный реальностью.")
        file2 = open('dendro/kaveh/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Универсальный набор для Кавеха. Желательно иметь персонажа с сетом Воспоминаний в команде.")
        file3 = open('dendro/kaveh/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Подходит для игры через реакции с Гидро. Повышает МС и урон от реакций.")

    elif message.text == "Аль-Хайтам":
        file = open('dendro/alhaitam/alhaitam.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Аль-Хайтам (艾尔海森 Ài’ěrhǎisēn) – играбельный 5-звездочный Дендро-персонаж в Genshin Impact. Нынешний секретарь Академии Сумеру, наделённый выдающимся умом и способностями.")
        file2 = open('dendro/alhaitam/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Лучший сет, если в команде есть саппорт с сетом Воспоминаний. Увеличивает урон Хайтама и МС.")
        file3 = open('dendro/alhaitam/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Увеличивает общий урон. Используйте его, если никто из персонажей в команде еще не носит этот сет.")

    elif message.text == "Бай Чжу":
        file = open('dendro/baiju/baiju.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Бай Чжу (白术 Báizhú) – играбельный 5-звездочный Дендро-персонаж в Genshin Impact. Владелец хижины «Бубу» в Ли Юэ. На его плечах всегда возлежит белая змея по имени Чан Шэн. Искусный лекарь со своими скрытыми намерениями.")
        file2 = open('dendro/baiju/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Больше подойдет для роли саппорта под Дендро. Рекомендуется выбирать HP для артефактов, чтобы максимально увеличить баффы от него.")
        file3 = open('dendro/baiju/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Идеально подойдет для хиллера.")

    elif message.text == "Кирара":
        file = open('dendro/kirara/kirara.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Кирара (绮良良 Qǐliángliáng) – играбельный 4-звездочный Дендро-персонаж в Genshin Impact. Курьер инадзумской компании доставки «Комания экспресс». Эта нэкомата обожает свою работу и общество людей.")
        file2 = open('dendro/kirara/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Отлично подойдет для роли саппорта или щитовика. Повышает урон Кирары.")

    if message.text == "Гидро":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Мона")
        item2 = types.KeyboardButton("Тарталья")
        item3 = types.KeyboardButton("Барбара")
        item4 = types.KeyboardButton("Син Цю")
        item5 = types.KeyboardButton("Кокоми")
        item6 = types.KeyboardButton("Е Лань")
        item7 = types.KeyboardButton("Аято")
        item8 = types.KeyboardButton("Кандакия")
        item9 = types.KeyboardButton("Нилу")
        item10 = types.KeyboardButton("Путешественник гидро")
        item11 = types.KeyboardButton("Нёвиллет")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
        tgbot.send_message(message.chat.id, 'Выберите вашего героя!', reply_markup=markup)

    elif message.text == "Мона":
        file = open('gidro/mona/mona.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Мона (莫娜 Mò nà) – играбельный 5-звездочный Гидро-персонаж в Genshin Impact. Таинственный молодой астролог, которая представляется как «великий астролог Мона Мегистус» и на самом деле достойна этого звания. Эрудирована и горделивая.")
        file2 = open('gidro/mona/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Увеличивает урон от элементального взрыва. Оказывает хорошую поддержку остальным членам отряда.")
        file3 = open('gidro/mona/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Усиливает урон элементального взрыва. Обеспечивает хороший постоянный урон.")

    elif message.text == "Тарталья":
        file = open('gidro/tartar/tartar.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Тарталья (達達利亞 Dá dálì yǎ) – играбельный Гидро-персонаж в Genshin Impact. Номер одиннадцать из Предвестников Фатуи, искусный воин, также известный под титулом Чайльд.")
        file2 = open('gidro/tartar/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Постоянная прибавка к урону. Универсальная сборка.")
        file3 = open('gidro/tartar/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('gidro/tartar/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           " Микс двух сетов. Больше подходит для усиления элементального взрыва. Мощная сборка для уничтожения слабых мобов.")

    elif message.text == "Барбара":
        file = open('gidro/barbara/barbara.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Барбара (芭芭拉 Bā bā lā) – играбельный Гидро-персонаж в Genshin Impact. Все жители Мондштадта боготворят Барбару, но слово «идол» она узнала из модного журнала.")
        file2 = open('gidro/barbara/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Лучший выбор для персонажа целителя. Позволяет не возиться с едой или сэкономить её.")
        file3 = open('gidro/barbara/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Подходит для некоторых ситуаций. Наносит большой взрывной урон.")

    elif message.text == "Син Цю":
        file = open('gidro/sincu/sincu.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Син Цю (行秋 Xíng qiū) – играбельный Гидро-персонаж в Genshin Impact. Молодой любитель книг с благородным сердцем и длинным мечом.")
        file2 = open('gidro/sincu/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Оптимально для роли поддержки. Увеличивает атаку для товарищей по команде после элементального взрыва")
        file3 = open('gidro/sincu/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('gidro/sincu/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Сборка подходит для использования с Церемониальным мечом.")

    elif message.text == "Кокоми":
        file = open('gidro/kokomi/kokomi.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Сангономия Кокоми (珊瑚宮心海 Shānhúgōng Xīnhǎi) – играбельный Гидро-персонаж в Genshin Impact. Божественная Жрица острова Ватацуми. Все дела острова находятся в руках этой молодой леди.")
        file2 = open('gidro/kokomi/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Идеально подходит для роли хиллера.")
        file3 = open('gidro/kokomi/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('gidro/kokomi/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id, "Микс двух сетов. Увеличивает HP, а также увеличивает лечение.")

    elif message.text == "Е Лань":
        file = open('gidro/elan/elan.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Е Лань (夜兰 Yèlán) – играбельный Гидро-персонаж в Genshin Impact. Незнакомка, якобы работающая в Департаменте по делам граждан.")
        file2 = open('gidro/elan/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id,
                           "Увеличивает урон от взрыва стихий. Обеспечивает Е Лань восстановлением энергии.")
        file3 = open('gidro/elan/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('gidro/elan/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id, "Микс двух сетов. Увеличивает общий урон. Отлично подходит для Мейн-ДПС.")

    elif message.text == "Аято":
        file = open('gidro/ayato/ayato.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Камисато Аято (神里绫人 Shénlǐ Língrén) – играбельный 5-звездочный Гидро-персонаж в Genshin Impact. Молодой и всесторонне одарённый глава комиссии Ясиро из клана Камисато. Он вежливый и предупредительный человек, у которого для любой проблемы найдётся множество решений.")
        file2 = open('gidro/ayato/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Сильно увеличивает атаку. Отлично подходит для ДПС-Аято.")
        file3 = open('gidro/ayato/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('gidro/ayato/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id, "Микс двух сетов. Больший фокус на Взрыв стихий.")

    elif message.text == "Кандакия":
        file = open('gidro/kandakia/kandakia.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Кандакия (坎蒂丝 Kǎndìsī) – играбельный Гидро-персонаж в Genshin Impact. Защитница деревни Аару, наследница царя Дешрета. Её левый глаз сияет подобно янтарю.")
        file2 = open('gidro/kandakia/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Отлично подходит для усиления всей команды.")
        file3 = open('gidro/kandakia/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        file4 = open('gidro/kandakia/build3.png', 'br')
        tgbot.send_photo(message.chat.id, file4)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Позволяет чаще использовать Взрыв стихий и наносить больше урона.")

    elif message.text == "Нилу":
        file = open('gidro/nilu/nilu.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Нилу (妮露 Nīlù) – играбельный Гидро-персонаж в Genshin Impact. Знаменитая танцовщица Театра Зубаира. Изящная красавица с чистой и открытой душой.")
        file2 = open('gidro/nilu/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('gidro/nilu/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id,
                           "Микс двух сетов. Лучшая сборка для увеличения HP и урона. Ансамбль можно заменить на другой сет с мастерством стихий.")

    elif message.text == "Путешественник гидро":
        file = open('gidro/travelergidro/travelergidro.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Путешественник (旅行者 Lǚxíng zhě) – главный герой Genshin Impact. Пришедший из другого мира в поисках семи Архонтов путешественник(ца), пытающийся вернуть свою сестру (брата).")
        file2 = open('gidro/travelergidro/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        file3 = open('gidro/travelergidro/build2.png', 'br')
        tgbot.send_photo(message.chat.id, file3)
        tgbot.send_message(message.chat.id, "Микс двух сетов. Отлично подходит для усиления Взрыва стихий.")

    elif message.text == "Нёвиллет":
        file = open('gidro/nevillet/nevillet.png', 'br')
        tgbot.send_photo(message.chat.id, file)
        tgbot.send_message(message.chat.id,
                           "Нёвиллет (那维莱特 Nàwéiláitè) – играбельный 5-звездочный Гидро-персонаж в Genshin Impact. Верховный судья Фонтейна, или же юдекс, прославился своей безукоризненной беспристрастностью.")
        file2 = open('gidro/nevillet/build1.png', 'br')
        tgbot.send_photo(message.chat.id, file2)
        tgbot.send_message(message.chat.id, "Универсальный набор для Гидро-ДД. Максимизирует собственный урон.")

    if message.text.lower() == 'привет':
        tgbot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

    if message.text.lower() == 'пока':
        tgbot.send_message(message.chat.id,
                           f'До скорых встреч, {message.from_user.first_name} {message.from_user.last_name}!')

    if message.text.lower() == 'как дела?':
        tgbot.send_message(message.chat.id, f'У меня всё отлично, ведь ты здесь!')





tgbot.polling(none_stop=True, interval=0)
