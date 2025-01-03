from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random

# Тексты для кнопки "СЕКРЕТИК!"
secret_texts = [
    """Ты наполняешь мою жизнь светом, и даже в самые трудные моменты твоя любовь придает мне сил. С тобой не страшно, потому что я знаю, что мы всегда будем вместе. Ты — моя опора и вдохновение. Я мечтаю о нашем будущем, о каждом моменте, который мы проведем вместе. Ты — та, с кем я хочу расти и развиваться, строить дом, создавать воспоминания. Каждый день с тобой — это новый шанс быть счастливыми, и я не могу дождаться, что будет дальше. Ты — мое солнце, и я буду оберегать тебя, любить и поддерживать, несмотря ни на что. Мы с тобой — команда, и нет ничего, что могло бы нас разлучить. С тобой я готов на всё, потому что ты — моя любовь, и в этом мире нет ничего более важного для меня!""",
    """Ты — моя причина верить в чудеса. Каждый твой взгляд, каждое слово дарит мне ощущение тепла и любви. С тобой я чувствую себя дома, несмотря на любые трудности. Ты — моя сила и моя слабость одновременно. В моменты счастья и в моменты грусти, ты всегда рядом, и это самое важное для меня. Ты — человек, с которым я хочу делить каждое мгновение жизни. С тобой я готов идти в огонь и в воду, потому что ты — моя уверенность, мой источник вдохновения и моя вечность.""",
    """С тобой не существует невозможного. Ты — моя муза, моя поддержка, моя радость. Ты даешь мне силы, когда я сомневаюсь, ты рядом, когда мне тяжело. Твоя любовь — это свет, который освещает мой путь. Ты моя звезда, которая ведет меня через темные времена. Я готов на всё ради твоего счастья, потому что ты — это самое важное, что есть в моей жизни. Вместе с тобой я чувствую себя живым, потому что ты — моя жизнь, моя душа, мое вдохновение!""",
    """Ты — это мой космос, моя вселенная, все, о чем я когда-либо мечтал. Ты даришь мне покой в мире хаоса и радость в моменты грусти. Быть рядом с тобой — значит ощущать любовь, которая меня наполняет. Ты — моя невероятная, уникальная и неповторимая звезда. Моя жизнь с тобой становится ярче, и я готов пройти все испытания, чтобы быть рядом с тобой!""",
    """Каждый момент, проведенный с тобой, для меня бесценен. Ты — как дыхание, которое мне нужно, как свет, что освещает путь в темные времена. Ты — мой лучший друг и любовь всей моей жизни. Когда ты рядом, я чувствую, что все возможно. В мире, полном перемен, ты — мое постоянство и опора. Я горжусь тем, что могу любить тебя""",
    """Ты — моя реальность, моя мечта и мой самый драгоценный дар. В твоих глазах я нахожу смысл жизни, в твоих руках — уют и тепло. Ты — не просто человек, ты — целый мир, в котором я хочу остаться навсегда. Я люблю тебя не за то, кто ты, а за то, что ты даришь мне любовь, заботу и счастье. Ты — всё, что мне нужно.""",
    """С тобой я научился ценить каждое мгновение. Ты как светлый лучик в моей жизни, который разгоняет темные тучи. Ты делаешь меня лучше, сильнее, увереннее. Ты моя нежность, моя поддержка, моя гордость. Вместе с тобой я могу достичь всего. Ты — мой идеал, и я не перестану восхищаться тобой каждый день.""",
    """Ты — моя сила и моя нежность, моя нежность и моя опора. Ты даешь мне силы верить в себя и в нас. С тобой мне не страшны ни беды, ни испытания. Ты и есть мое счастье. Ты — тот самый человек, с которым я готов строить будущее, создавать моменты счастья и прожить всю свою жизнь. Ты — моя любовь и мой смысл""",
    """Когда я смотрю в твои глаза, я вижу весь мир. Ты — то, что делает мою жизнь полной, яркой и счастливой. Ты — мой свет в темном мире, мой компас, который всегда указывает правильный путь. С тобой я научился жить, смеяться и любить. Ты — причина, по которой я просыпаюсь с улыбкой и засыпаю с миром в сердце.""",
    """Ты — источник моего вдохновения, мой идеал красоты и любви. В тебе сочетаются силы и слабости, страсть и спокойствие. Я горжусь тем, что ты есть в моей жизни. Ты — моя звезда, моя жизнь, моя душа. Вместе с тобой я чувствую себя не просто человеком, а целым миром, в котором я могу быть собой."""
]

# Функция, которая вызывается при команде /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("НАЖИМАЙ КИТЯ", callback_data='click')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.edit_message_text(
            "Привет Алина! Чтобы ты не грустила, то нажми на кнопочку ниже солнышко!", 
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "Привет Алина! Чтобы ты не грустила, то нажми на кнопочку ниже солнышко!", 
            reply_markup=reply_markup
        )

# Функция обработки нажатий на кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Инициализация secret_index, если она ещё не установлена в user_data
    secret_index = context.user_data.get('secret_index', 0)


    if query.data == 'click':
        cute_phrases = [
            "Люблю тебя!",
    "Ты самая лучшая!",
    "Моя кисонька, ты прекрасна!",
    "С тобой весь мир становится ярче!",
    "Ты мое счастье!",
    "Ты мое вдохновение!",
    "Ты мое чудо!",
    "Ты самая красивая!",
    "Ты мой смысл жизни!",
    "Я так рад, что ты у меня есть!",
    "Ты делаешь меня счастливым!",
    "Я не могу без тебя!",
    "Ты самая добрая!",
    "Ты мой ангел!",
    "Ты мое сокровище!",
    "Ты моя вселенная!",
    "Ты мое солнышко!",
    "Ты мое сердечко!",
    "Ты моя любовь!",
    "Ты моя радость!",
    "Ты самый дорогой человек в моей жизни!",
    "Ты придаешь смысл моему существованию!",
    "Ты делаешь каждый мой день особенным!",
    "Я обожаю тебя!",
    "Ты самый светлый человек в моей жизни!",
    "Ты мое счастье, моя жизнь!",
    "Ты мой уют!",
    "Ты моя гармония!",
    "Ты мое спокойствие!",
    "Ты мое все!",
    "Ты моя любимая звезда!",
    "Ты самый важный человек для меня!",
    "Ты мое вдохновение каждый день!",
    "Ты мой лучший друг и моя любовь!",
    "Ты делаешь меня лучше!",
    "Ты – это все, что мне нужно!",
    "Ты самый милый человек!",
    "Ты самый умный человек!",
    "Ты самая заботливая!",
    "Ты моя гордость!",
    "Ты самое дорогое, что у меня есть!",
    "Ты мое утешение!",
    "Ты мой компас!",
    "Ты мой дом!",
    "Ты мое счастье, мой друг и моя семья!",
    "Ты самое нежное создание на свете!",
    "Ты моя надежда!",
    "Ты моя опора!",
    "Ты моя любовь навсегда!",
    "Ты мое будущее!",
    "Ты мое настоящее!",
    "Ты самый прекрасный человек на земле!",
    "Ты мое вдохновение на всю жизнь!",
    "Ты мой космос!",
    "Ты моя галактика!",
    "Ты моя нежность!",
    "Ты моя звезда!",
    "Ты моя луна!",
    "Ты мое счастье каждую минуту!",
    "Ты мой маяк в темноте!",
    "Ты мой свет!",
    "Ты моя сила!",
    "Ты мое счастье утром, днем и ночью!",
    "Ты мое счастье на всю жизнь!",
    "Ты мой лучший подарок судьбы!",
    "Ты мое сердце!",
    "Ты мое счастье, которым я горжусь!",
    "Ты мое все, что мне нужно!",
    "Ты мой рай!",
    "Ты мой любимый человек!",
    "Ты мое счастье, мое сокровище!",
    "Ты мое вдохновение, моя муза!",
    "Ты моя жизнь!",
    "Ты мое чудо света!",
    "Ты мой бриллиант!",
    "Ты мое счастье на земле!",
    "Ты моя роскошь!",
    "Ты мой мир!",
    "Ты мое бесконечное счастье!",
    "Ты моя радость каждый день!",
    "Ты мое счастье с первого взгляда!",
    "Ты моя любовь, которая только растет!",
    "Ты моя мечта!",
    "Ты мое счастье на всю жизнь!",
    "Ты моя фантазия!",
    "Ты моя жизнь, моя любовь и мое счастье!",
    "Ты мое счастье, мой дом!",
    "Ты моя половинка!",
    "Ты мой свет в конце туннеля!",
    "Ты моя улыбка!",
    "Ты мое счастье, мой мир и моя жизнь!",
    "Ты мое бесценное сокровище!",
    "Ты моя радость и мое вдохновение!",
    "Ты мое счастье, мое вдохновение!",
    "Ты мой рассвет и мой закат!",
    "Ты моя сладкая мечта!",
    "Ты мой лучший выбор!",
    "Ты мое лучшее решение!",
    "Ты моя вечность!",
    "Ты моя любовь и мой покой!",
    "Ты моя красота в этом мире!",
    "Ты мое блаженство!",
    "Ты мое сокровенное желание!",
    "Ты мой восторг!",
    "Ты мое счастье на этой земле!",
    "Ты моя душа!",
    "Ты мой ангелочек!",
    "Ты мое лучшее утро!",
    "Ты мое любимое время дня!",
    "Ты мое счастье в мелочах!",
    "Ты мой фейерверк эмоций!",
    "Ты мой мягкий плед зимой!",
    "Ты моя прохлада летом!",
    "Ты мой уютный дом!",
    "Ты мое отражение любви!",
    "Ты моя самая светлая мысль!",
    "Ты мое вдохновение и радость!",
    "Ты моя самая заветная мечта!",
    "Ты моя улыбка на губах!",
    "Ты мое удивительное приключение!",
    "Ты мое тихое счастье!",
    "Ты мой светлый лучик!",
    "Ты мое счастье без границ!",
    "Ты моя мелодия сердца!",
    "Ты мой праздник каждый день!",
    "Ты мое утро с чашкой кофе!",
    "Ты мой закат на берегу!",
    "Ты моя вторая половинка!",
    "Ты мое счастье, которое со мной!",
    "Ты мое вдохновение на подвиги!",
    "Ты мой теплый плед в холода!",
    "Ты моя легкость бытия!",
    "Ты мой смысл и мотив!",
    "Ты мое счастье, моя жизнь и любовь!",
    "Ты мое дыхание!",
    "Ты мой блеск в глазах!",
    "Ты моя самая сладкая мечта!",
    "Ты мой навсегда!",
    "Ты моя тихая гавань!",
    "Ты мой огонек в ночи!",
    "Ты мое счастье, которое только растет!",
    "Ты мое вдохновение в каждый день!",
    "Ты мой самый любимый человек на свете!",
    "Ты мой смысл просыпаться утром!",
    "Ты моя радость и надежда!",
    "Ты мой луч света в темноте!",
    "Ты мое счастье без условий!",
    "Ты моя гармония в жизни!",
    "Ты мой маяк в океане!",
    "Ты мое утро и ночь!",
    "Ты мой каждый вдох!",
    "Ты мое самое светлое чувство!",
    "Ты мой смысл и мечта!",
    "Ты мое настоящее и будущее!",
    "Ты мой самый главный человек!",
    "Ты - моя душа и сердце!",
    "Ты - мой смысл в жизни!",
    "Ты - мой яркий луч в темной ночи!",
    "Ты - моя родная душа!",
    "Ты - мой единственный смысл!",
    "Ты - мое сердце, мое дыхание!",
    "Ты - моя надежда, моя сила!",
    "Ты - моя любовь, которая светит!",
    "Ты - мое дыхание и моя жизнь!",
    "Ты - мой смысл жить!",
    "Ты - моя лучшая половина!",
    "Ты - моя душевная гармония!",
    "Ты - мой уют и радость!",
    "Ты - моя первая и последняя любовь!",
    "Ты - мой смысл каждого дня!",
    "Ты - моя маленькая вселенная!",
    "Ты - мой лучик счастья!",
    "Ты - мой источник вдохновения!",
    "Ты - моя гармония и мир!",
    "Ты - мой смысл и моя жизнь!",
    "Ты - моя вечная любовь!",
    "Ты - мой мир, моя крепость!",
    "Ты - мой свет в темные моменты!",
    "Ты - моя мечта, ставшая реальностью!",
    "Ты - мой ангел и мой защитник!",
    "Ты - моя любовь и мой смысл!",
    "Ты - мой смысл радости!",
    "Ты - мой цветок, который расцветает!",
    "Ты - мое вдохновение и счастье!",
    "Ты - мой компас и моя опора!",
    "Ты - моя любовь, мой смысл быть!",
    "Ты - моя реальность, мои мечты!",
    "Ты - мой свет в облаках!",
    "Ты - мой лучший выбор в жизни!",
    "Ты - мой рай на земле!",
    "Ты - мой светлый момент!",
    "Ты - мой теплый уголок!",
    "Ты - моя радость на все времена!",
    "Ты - мой комфорт и счастье!",
    "Ты - мой любимый человек!",
    "Ты - мой смех и радость!",
    "Ты - мой мир в твоих глазах!",
    "Ты - мое счастье в сердце!",
    "Ты - мой нежный свет!",
    "Ты - мой теплый лучик в холодные дни!",
    "Ты - моя любовь, мое счастье!",
    "Ты - моя цель и смысл!",
    "Ты - мое дыхание и жизнь!",
    "Ты - моя звезда в ночном небе!",
    "Ты - моя светлая мечта!",
    "Ты - мой лучший момент!",
    "Ты - мой светлый путь!",
    "Ты - мой рай на Земле!",
    "Ты - моя вселенная и мир!",
    "Ты - мой источник счастья и вдохновения!",
    "Ты - моя гармония и любовь!",
    "Ты - мой смысл существования!",
    "Ты - мой светлый луч в темные моменты!",
    "Ты - моя радость и мир!",
    "Ты - мой компас, который ведет меня!",
    "Ты - мой светлый лучик на горизонте!",
    "Ты - моя душа и сердце!",
    "Ты - мой ангел, мой защитник!",
    "Ты - моя любовь и опора!",
    "Ты - мой взгляд на мир!",
    "Ты - мое счастье и поддержка!",
    "Ты - мой смысл и счастье!",
    "Ты - моя радость и светлый путь!",
    "Ты - мой свет, мое вдохновение!",
    "Ты - мое утешение в трудные моменты!",
    "Ты - моя гармония и поддержка!",
    "Ты - моя поддержка и сила!",
    "Ты - мой самый лучший друг и любовь!",
    "Ты - моя вторая половинка, мой ангел!",
    "Ты - мой светлый луч в жизни!",
    "Ты - мой уют и родная душа!",
    "Ты - моя любовь, которая светит!",
    "Ты - моя поддержка и мой смысл!",
    "Ты - мое вдохновение и радость!",
    "Ты - мой источник счастья!",
    "Ты - мой светлый момент!",
    "Ты - мое счастье с каждым днем!",
    "Ты - моя гармония и смысл!",
    "Ты - моя любовь, мое счастье!",
    "Ты - мой лучший выбор!",
    "Ты - моя любовь, которая согревает!",
    "Ты - моя вселенная!",
    "Ты - моя радость, мой свет!",
    "Ты - мой единственный смысл!",
    "Ты - мое вдохновение и моя любовь!",
    "Ты - мой рай, мой мир!",
    "Ты - мой уют в этой жизни!",
    "Ты - моя жизнь, моя радость!",
    "Ты - мой лучший момент в жизни!",
    "Ты - моя маленькая звезда!",
    "Ты - мой светлый путь в жизни!",
    "Ты - мой самый главный человек!",
    "Ты - моя жизнь, мой смысл и любовь!",
    "Ты - мой первый и последний взгляд!",
    "Ты - мое счастье и мое вдохновение!",
    "Ты - моя любовь, мой свет!",
    "Ты - мой смысл в этом мире!",
    "Ты - моя поддержка в жизни!",
    "Ты - мое счастье с каждым днем!",
    "Ты - мой смысл жизни, моя любовь!",
    "Ты - мой лучший выбор и счастье!",
    "Ты - моя лучшая половинка!",
    "Ты - мое вдохновение и поддержка!",
    "Ты - мой светлый и радостный день!",
    "Ты - мой смысл быть с тобой!",
    "Ты - моя любовь и радость!",
    "Ты - мой компас и вдохновение!",
    "Ты - моя душевная гармония!",
    "Ты - мой светлый и нежный момент!",
    "Ты - моя жизнь, мой свет!",
    "Ты - моя радость, мой смысл!",
    "Ты - мой уют и моя любовь!",
    "Ты - моя цель и мечта!",
    "Ты - мой смысл существования!",
    "Ты - моя любовь, мой мир!",
    "Ты - мой светлый взгляд на жизнь!",
    "Ты - мой смысл и моя любовь!",
    "Ты - мое счастье на всю жизнь!",
    "Ты - моя любовь и поддержка!",
    "Ты - мой лучший выбор в жизни!",
    "Ты - моя звезда и мир!",
    "Ты - мой светлый лучик!",
    "Ты - моя поддержка и опора!",
    "Ты - мой уют и мой смысл!",
    "Ты - моя жизнь, моя любовь!",
    "Ты - мой фейерверк в сердце!",
    "Ты - мой смысл и вдохновение!",
    "Ты - мой светлый уголок в жизни!",
    "Ты - моя радость и смысл!",
    "Ты - мое вдохновение на всю жизнь!",
    "Ты - мой смысл и любовь на всю жизнь!",
    "Ты - моя светлая мечта!",
    "Ты - мой идеал в жизни!",
    "Ты - мой лучший выбор!",
    "Ты - моя самая сильная любовь!",
    "Ты - мой смысл быть!",
    "Ты - моя любовь, мой свет!",
    "Ты - моя любовь, мой смысл!",
    "Ты - мой смысл и мой путь!",
    "Ты - мой смысл жизни и любовь!",
    "Ты - мой ангел, моя звезда!",
    "Ты - моя мечта, которая сбылась!",
    "Ты - мой светлый момент в жизни!",
    "Ты - моя радость, моя жизнь!",
    "Ты - мой смысл существования!",
    "Ты - мой лучший момент в жизни!",
    "Ты - моя любовь, мой светлый уголок!",
    "Ты - моя светлая радость!",
    "Ты - мой смысл на каждый день!",
    "Ты - мой лучший выбор и любовь!",
    "Ты - мое счастье и радость!",
    "Ты - моя звезда, мой свет!",
    "Ты - мое вдохновение и моя любовь!",
    "Ты - мой лучший момент в жизни!",
    "Ты - мой смысл в жизни, моя любовь!"
        ]
        message = random.choice(cute_phrases)
        keyboard = [
            [
                InlineKeyboardButton("Назад", callback_data='back'),
                InlineKeyboardButton("Нажми еще <3", callback_data='click')
            ],
            [InlineKeyboardButton("СЕКРЕТИК!", callback_data='secret')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(message, reply_markup=reply_markup)

    elif query.data == 'secret':
        # Получаем текущий секретный текст
        secret_message = secret_texts[secret_index]

        # После показа текста, увеличиваем индекс для следующего нажатия
        secret_index = (secret_index + 1) % len(secret_texts)
        context.user_data['secret_index'] = secret_index  # Сохраняем новый индекс

        # Кнопки, которые остаются после перехода к секретному сообщению
        keyboard = [
            [
                InlineKeyboardButton("Назад", callback_data='back'),
                InlineKeyboardButton("Анука еще!", callback_data='next_secret')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(secret_message, reply_markup=reply_markup)

    elif query.data == 'next_secret':
        # Меняем текст на следующий
        secret_index = (secret_index + 1) % len(secret_texts)
        context.user_data['secret_index'] = secret_index  # Сохраняем новый индекс
        secret_message = secret_texts[secret_index]

        # Обновляем кнопки
        keyboard = [
            [
                InlineKeyboardButton("Назад", callback_data='back'),
                InlineKeyboardButton("Анука еще!", callback_data='next_secret')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(secret_message, reply_markup=reply_markup)

    elif query.data == 'back':
        await start(update, context)

# Основной код для запуска бота
if __name__ == "__main__":
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    application = ApplicationBuilder().token("7573634465:AAE9VDxM8_fR47rMKWWub0mzL7n-SiK7wSM").build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    # Регистрируем обработчик нажатий на кнопки
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запускаем бота
    application.run_polling()