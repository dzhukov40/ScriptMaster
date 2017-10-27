# ScriptMaster
это пример реализации ботика телеграм

- отправка работает
- прикрутили тесты
- в указанной функции для принятия сообщений надо проверять тип
  для удобной работой с сообщением
  - [ if isinstance(msg, Update): ]
  
  
# TODO:  
1) чтобы определить набор команд бота их надо задать через [ @BotFather ]  
   C таким описанием, если пользователь наберет /, 
   Telegram услужливо покажет список всех доступных команд.
  
2) посмотреть как отправить кнопочки в сообщении 
  - смотри [ reply_markup ] (*) есть во всех сендах!     
  - :
    inlineKeyboardButton1 = {'text': 'текст1', 'url': 'http://ya.ru'}
    inlineKeyboardButton2 = {'text': 'текст2', 'url': 'http://ya.ru'}
    inlineKeyboardButton3 = {'text': 'текст3', 'url': 'http://ya.ru'}
    inlineKeyboardButton4 = {'text': 'текст4', 'url': 'http://ya.ru'}
    arrayButtons1 = [inlineKeyboardButton1, inlineKeyboardButton2]
    arrayButtons2 = [inlineKeyboardButton3, inlineKeyboardButton4]
    inlineKeyboardMarkup = {'inline_keyboard': [arrayButtons1, arrayButtons2]}
    inlineKeyboardMarkup = json.dumps(inlineKeyboardMarkup)

    bot.sendMessage(chatId, chatText, reply_markup=inlineKeyboardMarkup)