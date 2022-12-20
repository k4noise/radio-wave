﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Артём', color="#c8ffc8")
define n = Character('Никита', color="#ffff00")
define asy = Character('Ася', color="#42aaff")
define p = Character('Полина', color="#8b00ff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

default stay_home = True
default write_today = True
# Игра начинается здесь:
label start:

    scene artem_room
    "8:30. Первые мысли после пробуждения сразу врезаются в голову с неистовой скоростью. Пара секунд и приходит осознание, что начался ещё один день. Снова."
    "*звон будильника*"

    show artem at left with dissolve:
        xalign 0.1

    a "Чёрт! Не стоило мне так долго играть этой ночью. Как бы я быстро не собирался все равно опоздаю. Сил нет снова выслушивать упреки в мою сторону. Думаю, у меня отличный повод никуда сегодня не пойти."
    a "Все равно этот день ничем не будет отличаться от предыдущих. Ничего нового. Скука."
    hide artem

    "Посмотрев по сторонам, я увидел в углу пыльную гитару, которая как будто плачет  от того, что ей никто не хочет пользоваться."
    "На шкафу лежит волейбольный мяч, там же расположены недочитанные мной книги, а около жужжащего компьютера аккуратно стоят нетронутые холсты и запечатанные кисти."

    "Я сгреб все лишнее со стола в небольшую кучу, освободив место для рук, и, как обычно, первым делом открыл ютуб.  Процесс пробуждения почти подходил к концу, мой живот издал резкий урчащий звук. "

    show artem at left with dissolve:
        xalign 0.1
    a "Пора бы и перекусить."
    hide artem with dissolve

    'Я прошел по коридору сначала в ванную, а после на кухню, где обнаружил записку на столе, написанную почерком мамы: "Доброе утро, еда в холодильнике. Удачной учебы <3".'
    "Будет грустно видеть ее лицо после звонка из школы. Закончив прием пищи, я отправился обратно к себе."

    "Осенний ветер колышет ветки за окном, листья, медленно кружась, падают на подоконник, а лучи солнца изо всех сил стараются проникнуть через тонкие шторы в эту невеселую комнату."
    "Это заворожило меня, я даже подумал, что еще могу улавливать что то прекрасное в таких мелочах."

    show artem at left with dissolve:
        xalign 0.1
    a "Будь я музыкантом или художником,именно сейчас меня должно было посетить вдохновение для создания чего-то великого. Однако я не Вивальди и не Левитан."
    "Я могу лишь просто наслаждаться этой красотой, чтобы хоть как-то скрасить серость обыденных дней."

    hide artem with dissolve

    "Доделав остаток утренних процедур, я, как обычно, не знал чем заняться дальше. В любой другой день я бы просто открыл стим и запустил одну из игр, просидевших в ней до ночи. Но в этот раз даже играть не хотелось."
    "Я завязал волосы в хвост и лег на уже заправленную постель. Никогда не любил так делать, ведь ты остаешься наедине со своими мыслями. Один на один."

    "Я даже не помню когда именно это началось. Год назад? Два? Когда я потерял всяческий интерес ко всему, что я делаю? И ведь пробовал снова найти то, что будет затягивать с головой, и не раз."
    "Сейчас уже поздно искать себя, попробовать что-то новое, бросать, а затем браться за другое. Одиннадцатый класс, экзамены, выбор вуза. Почему я не ушел после девятого... "

    'Я не хочу прожить жизнь так ничего и не сделав, пока я только потребляю, то что создали другие. Бесит. Мне нужно нечто большее от жизни, но как найти это "большее"?'
    "Я всегда терял искру интереса в том, чем увлекался. Это какой-то барьер, который я не могу преодолеть в силу недостатка мотивации или чего-то еще..."

    show artem at left with dissolve:
        xalign 0.1

    a "Мне определенно нужен какой то толчок."

    hide artem with dissolve

    "Я встал с кровати, сел за компьютер и включил рандомную шугейз-группу. Было здорово, когда мы собирались с друзьями и играли что-то подобное."
    "Помню как вчера: приносил заготовки к песне, парни ее разучивали, и мы с наслаждением играли, чувствуя каждую нотку и качаясь в ритм барабанов."
    "Сейчас мы не поддерживаем общение: один переехал, другой бросил музыку ради учебы. Остался только Саня, с которым мы иногда играем что-то на гитарах, но это уже совсем не то, что было раньше."

    "Я до сих пор иногда пишу мелодии, правда уже на синтезаторе. Однако, то что я делаю не звучит как серьезная музыка, которую играют в филармониях. На хит городских дискотек тоже не тянет."
    "Мои наработки похожи на легкие саундтреки к игре, однако, меня это ни капли не расстраивает."

    "Мысли в голове путаются, руки и ноги тяжелеют, в глазах начинает темнеть, кажется я совсем сегодня не выспался."
    scene thinking_in_room
    "Проснувшись в полной темноте, я еще долго не решался взглянуть на время. Просто тупил в пустоту, не имея ни одной мысли в голове. Просидев так минут десять, я включил монитор. 23:11."
    "Мать видимо решила, что я устал после учебы и не стала беспокоить. Оно и к лучшему."
    "Открыв личные сообщения, я увидел, что мне написал Никита, хотя лучше сказать настрочил. Сколько помню нашу дружбу, он всегда был непоседлив и нетерпелив. Моя полная противоположность. Наверное, от этого мы так и сдружились с ним. "
    "В сообщениях он рассказал о том, что было в школе, скинул домашку и конспекты, а также отправил ссылку на какую-то статью, с подписью: “ты обязательно должен прочитать это”."
    "Планов у меня на сегодняшние ночные посиделки не было, поэтому отписавшись Никите, я пошел смотреть, что же такого он мне кинул."
    show artem at left
    a "Так и знал!"
    hide artem
    "Никита был очень вовлечен в эту сферу и постоянно скидывал мне интересные и не очень статьи об этом, но никогда не прикреплял такие подписи к этим ссылкам."
    "Скорее просто делился тем, чем увлекается, как и положено хорошим друзьям. Это была статья про геймдев, а конкретно про какую-то маленькую инди-студию, которая в этом году всех удивила своими проектами."
    "В одну из тех игр мне удалось поиграть и самому. Не сказать, что она была шедевром, но учитывая их бюджет и количество людей, вышло и правда хорошо. "
    "Прочитав все от начала и до конца, даже я был немного вдохновлен. Не представляю, что сейчас чувствовал впечатлительный Никита. Отписавшись, о том, что я прочитал все, мне сразу поступает звонок в дискорде."
    "Это был кудрявый. Только приняв его, на меня свалился невероятный словесный понос, я с трудом разбирал слова, которые выстреливал из себя этот идиот."

    show artem at left with dissolve:
        xalign 0.1
    show nikita at right with dissolve:
        zoom 0.85
        xalign 0.9

    a "Так, эминем еврейских кровей, ты можешь немного помедленнее?"
    n "НЕТ"
    a "Успокоишься, позвонишь"
    n "Пойдем прогуляемся?"
    hide nikita
    with dissolve

    menu:
        a "Я уже давно никуда не выходил, и это не казалось такой плохой идеей, однако моя лень и нежелание, что-либо делать магическим образом никуда не исчезали."
        "Остаться дома":
            jump sit_at_home
        "Выйти на улицу":
            jump go_outside

    label sit_at_home:
        "Мои отрицательные стороны и качества оказались сильнее, ничего нового."
        show nikita at right with dissolve:
            zoom 0.85
            xalign 0.9
        a "Давай не сегодня, дружище, в школе расскажешь, то что хочешь"
        n "Ты как всегда"
        a "Добрых снов"
        n "Спокойной ночи"
        hide nikita with dissolve
        hide artem with dissolve

        "Я не знаю, что на меня опять нашло. Он же мой друг и явно хотел поделиться чем-то ценным для него. Как будто я отстраняюсь от людей, потому что завидую их стремлениям и желаниям"
        "А может это и к лучшему, хотя-бы меньше поводов для беспокойства и самокопаний. С такими мыслями. Просидев до 4 ночи, меня окончательно начало клонить в сон."
        show artem at left with dissolve:
            xalign 0.1

        a "Ну хоть режим на место встанет"
        hide artem with dissolve
        "И вот я уже окончательно погрузился в свой трехчасовой отдых перед учебой."
        jump cont1

    label go_outside:
        $stay_home = False
        "Мне явно нужно немного подышать свежим воздухом."
        show nikita at right with dissolve:
            zoom 0.85
            xalign 0.9
        a "На площадке в 0:20, не опаздывай. Убью"
        n "Уже одеваюсь!"
        hide nikita with dissolve
        hide artem with dissolve
        "Прокравшись на цыпочках до прихожей, я накинул куртку и выбежал во двор. "
        scene city
        show artem at left with dissolve:
            xalign 0.1
        a "Все-таки, хорошо, что мы живем в домах напротив"
        "На качели уже стоял Никита с улыбкой на все лицо. Я не мог не улыбнуться в ответ. Существует только один человек, который улыбается также ярко и во все зубы как он…"
        show nikita at right with dissolve:
            zoom 0.85
            xalign 0.9
        n "Ты точно все прочел?"
        a "Абсолютно"
        n "НУ И? Ничего не почувствовал?"
        a "Красивая история, но к сожалению лишь сплошная удача"
        n "Да это же просто нечто, их было всего четверо, а они смогли так много сделать имея так мало."
        a "Только не говори мне, что…"
        n "Мы будем делать игру!"
        a "Черт"
        "Ну как же так. Без объявления войны. Вот так просто. Он всегда был таким, подначивал на всяческие авантюры с поводом и без, а я отнекиваюсь."
        "Хотя по итогу все равно соглашаюсь… Возможно только из-за него я окончательно не превратился в амёбу."
        a "Так ладно. У тебя хоть идеи есть?"
        n "Ты даже не станешь спорить? Тебя машина недавно не сбивала? Где Артем, признавайся!"
        a "Улетел на другой край света. Подальше от надоедливого придурка."
        n "Ну есть парочка, но нам нужна команда. Как минимум еще 2 человека – сценарист и художник"
        a "Вот и ищи, на меня не надейся."
        n "Ну, пожалуйста!"
        a "..."
        "Никита попытался состроить гримасу кота в сапогах из “шрека”."
        a "Ты в курсе, что являешься той еще занозой?"
        n "Угу"
        "Мы поговорили еще пару минут о разных мелочах, я почувствовал, что начинаю замерзать. Посмотрев на осеннее небо, а потом на Никиту. Мне почему-то взбрело сказать это."
        a "Я что-нибудь придумаю, а теперь давай по домам."
        n "Ура! До встречи!"
        a "Ага"
        hide artem with dissolve
        hide nikita with dissolve
        scene artem_room
        "Придя домой, я еще долго не мог уснуть. Неужели меня и правда вдохновила вся эта история с маленькой студией или же дело в чем-то другом."
        "Точно не могу ответить на этот вопрос, по крайней мере сейчас. Кажется становится не так скучно…"
        jump cont1

        label cont1:
            scene artem_room
            "Утро в этот раз не задалось: все валилось из рук, медлительные действия, чувство разбитости. Явное проявление отсутствия здорового сна."
            "С этим нужно что-то делать, хоть мне и нравится ночная жизнь, но оставлять все так в учебное время грозит большими проблемами для организма."
            "Собравшись в школу, я кое-как приготовил себе завтрак и удалился из дома."
            scene city
            "В наушниках играли Radiohead, а я наблюдал за падающими листьями."
            "Мне очень нравится подобное спокойствие на улице, когда каждый человек идет по своим делам и думает о сегодняшнем дне, о том, что ему предстоит сделать сегодня."
            "Именно в это время большинство людей остаются наедине с собой, обдумывают свое бытие, погружаются в себя."
            scene classroom
            "Когда я зашел в класс, то понял, что чего-то не хватает. Никита еще не пришел. Это было странно, потому что он всегда приходил раньше меня на пару минут."
            "В сети он не появлялся, а значит что-то стряслось, иначе Никита точно бы предупредил."
            "Где-то на уроке третьем, я сказал, что у меня болит живот, и меня спокойно отпустили."
            scene city
            "Проходит буквально десять минут, а я уже стою у его домофона."
            "Немного постояв на месте, набираю его квартиру, на той стороне, как не странно, отвечает Никита в явно приподнятом настроении. "

            show nikita at left with dissolve:
                zoom 0.85
            n "Заходи скорее. Ты не поверишь, кто у меня сейчас дома!"
            hide nikita with dissolve

            "По правде говоря, он меня заинтересовал. Я поднялся быстрым шагом на третий этаж, открыл дверь и... замер."
            scene nikita_room_day
            "Как будто окунулся на семь лет назад. В коридоре стояла Ася, которая почти не изменилась внешне."

            "Мы были друзьями в то время. Даже больше, чем друзьями, она была нам как старшая сестра. Как и все дети, мы часто бегали во дворе, где были, как друзья, так и враги."
            "Однажды нам с Никитой повезло увидеть картину, как маленькая девочка издевалась над главным хулиганом и неприятелем всех ребят. "
            "Это была Ася. Она тогда только переехала в наш район. После такого неожиданного, для всех детей, случая, мы и сдружились с ней."
            "Из всех других ребят именно мы заинтересовали ее. Вечно унылый и невероятно гиперактивный. Для нее, видимо, это стало интересным сочетанием."
            "К сожалению, наша дружба не продлилась долго, и ее семья опять переехала в другой город, конечно, взяв с собой Асю. "
            "О ней остались множество теплых воспоминаний, я даже сейчас помню, как переживал, о том, что она уезжает. Это был второй человек в моей жизни, который мог сподвигнуть меня на всяческие активности."

            show nikita at left with dissolve:
                zoom 0.85
            show artem at center with dissolve
            show asya at right with dissolve:
                zoom 0.8
            a "Но как? Ты же уехала. Почему снова здесь?"
            asy "Может хотя-бы  “привет” выдавишь из себя?"
            asy "Ой, ладно. Родители снова решили переехать в город покрупнее для работы, а я с ними, потому что хочу попробовать себя в творческих проектах."
            asy "Здесь их явно будет больше, чем в той глухомани, в которой мы были."
            "Я простоял молча еще пару секунд и не мог поверить своим глазам. Она подошла ближе."
            asy "Быть таким высоким не честно. Пригнись."
            "Я послушался. Она обняла меня со всей силой, что было в этом маленьком человечке. Я ответил тем же."
            asy "Как же я скучала по вам!"
            n "А мы то как!"

            "Еще проболтав так в коридоре минут двадцать, Никита предложил выпить чаю, на что мы с радостью согласились."
            "Оказалось, что он встретил ее по пути в школу, отложил все свои дела, а мне не написал, потому что знал, что я прибегу к нему домой."
            asy "Никита, кстати, рассказал о ваших планах. Я в деле!"
            a "Это не что-то грандиозное, я не думаю, что ты имела в виду такие несерьезные проекты."
            if stay_home:
                n "Еще как серьезный! И нам как раз нужен художник. А вообще-то это ты должен был людей искать, так что спасибо должен сказать. "
            else:
                n "Еще как серьезный! А вообще я хотел тебя попросить найти людей для этого дела. Справишься?"

            a "Получается нам остался лишь геймдизайнер?"
            n "Угу. Я не знаю, как ты это сделаешь, но постарайся, пожалуйста. Мне уже не терпится начать."
            a "Так сколько тебе уже лет? Ты же нас на пару лет старше, насколько я помню."
            asy "О таком не прилично спрашивать вообще-то! В душе до сих пор тринадцать."
            a "Да просто по тебе и не скажешь, каков твой настоящий возраст."
            asy "Так это же не я вымахала до 190 за семь лет. И хватит с темы сходить. Мы обязаны сделать что-то крутое."
            n "К сожалению мы не можем начать создавать концепцию игры таким составом. Нужен геймдизайнер. Срочно."
            a "Ладно, Ладно. Я вас понял. Есть у меня один человек в знакомых. Сегодня же спишусь с ним."
            asy "Вот и договорились."
            "Тема разработки игры ушла куда-то назад, и мы продолжили разговор на отвлеченные темы. Давно я так ни с кем не беседовал в компании."
            "Ася рассказывала про свою жизнь, мы про нашу, таким образом, не заметно для всех, наступил вечер."
            scene nikita_room_night
            a "Кажется пора по домам. Ася, я тебя провожу."
            n "Удачи, ребят"
            hide nikita with dissolve
            hide artem with dissolve
            scene city
            show artem at left with dissolve
            show asya at right with dissolve:
                zoom 0.8
            "Мы вышли на улицу. Уже неплохо так стемнело"
            a "Ты же понимаешь, что в этом проекте не будет ничего серьезного. Он не пойдет куда-то далеко, не будет финансироваться."
            asy "Конечно, я все понимаю. Дело же не в этом, глупый. Да, я сказала, что хочу поучаствовать в серьезной работе, но почему я должна отказываться от опыта, который предоставит мне этот маленький инди-проект."
            asy "Артем, бери от этой жизни то, что тебе дают, не упускай возможности. Мы все от него, что-то получим для себя. Я в это верю."
            a "И ты, конечно, настроена серьезно."
            asy "А иначе зачем браться за дело?"
            "Я проводил ее прямо до двери и поплелся домой. Никита и Ася всегда хорошо ладили, а тут еще и совместная работа."
            hide asya with dissolve

            menu:
                a "Возможно, мне тоже нужно отнестись к этому посерьезнее."
                "Отложить дело":
                    jump postpone
                "Написать знакомой сегодня":
                    jump writetoday

        label postpone:
            $write_today = False
            hide artem with dissolve
            scene thinking_in_room
            "Сегодня произошло и так много событий. Думаю, это может подождать. Приду и рухну в постель, а дела не такие уж и срочные."
            "Поужинав, я быстро умылся и без сил лег спать. Надо будет как-то объясниться перед Никитой. Подумаю об этом завтра."
            scene artem_room
            "Утро было не слишком добрым. Будильники я не любил, а звонки с утра еще больше. Это был Никита, который сразу же начал расспрашивать об еще одном участнике."
            show artem at left with dissolve
            show nikita at right with dissolve:
                zoom 0.85
            n "Ну что? Нашел?"
            a "А это не может подождать? Я только проснулся."
            n "Как я и подозревал... Ладно, я уже позвал Полину к нам в команду. Встречаемся у меня через 2 часа."
            a "Прости"
            n "Ничего страшного, просто приходи вовремя."
            hide artem with dissolve
            hide nikita with dissolve
            "Это и не удивительно, он знал ее также, как я, поэтому нам обоим пришла на ум именно она. Мы познакомились с ней в какой-то MOBe, уже и не вспомню в какой."
            "Она материла союзника, который, по ее словам, сделал, что-то “максимально бездарное”. По общению она была довольна активной девушкой."
            "После того, как мы довольно сильно разговорились, оказалось, что живем в одном городе, но дальше интернет-общения не пошло."
            "Вместе с ней и Никитой играли какое-то время, но потом общение сошло на нет. По всей видимости с ним она еще продолжила общаться."
            "Вспомнили мы ее, потому что она участвовала в ролевиках и писала кампании для настольных игр."
            jump artem_mind

        label writetoday:
            hide artem with dissolve
            scene thinking_in_room
            "Я обещал Никите, а значит сделаю. Когда пришел домой, мама уже спала. Тихо поужинав, я сел за компьютер, открыл страницу Полины и долго думал, что написать."
            "Мы познакомились с ней в какой-то MOBe, уже и не вспомню в какой. Она материла союзника, который, по ее словам, сделал, что-то “максимально бездарное”."
            "По общению она была довольна активной девушкой. После того, как мы довольно сильно разговорились, оказалось, что живем в одном городе, но дальше интернет-общения не пошло."
            "Вместе с ней и Никитой играли какое-то время, но потом общение сошло на нет. Вспомнил я именно ее, потому что она участвовала в ролевиках и писала кампании для настольных игр."
            "Вместе с ней и Никитой играли какое-то время, но потом общение сошло на нет. Вспомнил я именно ее, потому что она участвовала в ролевиках и писала кампании для настольных игр."
            show artem at left with dissolve
            a "Не попробуешь - не узнаешь."
            "И я написал. Самая тяжелая минута ожидания, после прочтения сообщения в моей жизни."
            show polina at right with dissolve:
                zoom 0.85
            p "Да, почему нет. Звучит интересно, а если учесть, что за сюжетную составляющую буду отвечать я, то может выйдет не так плохо."
            a "Тогда может встретимся завтра всей компанией для небольшого брейншторма?"
            p "Договорились"
            hide artem with dissolve
            hide polina with dissolve
            "У меня получилось. Я был несказанно рад, потому что впервые я зову кого-то принять участие, а не меня. С чувством выполненного долга, я лег в кровать, и сон не заставил себя долго ждать."
            scene artem_room
            "Сегодня я проснулся гораздо раньше обычного."
            "Было это связанно с тем, что мой режим встал на место или же мне просто было невтерпеж начать думать над нашим совместным проектом, пока не ясно, но настроение у меня было явно приподнятое."
            "Скорее всего я просто до сих пор гордился тем, что самостоятельно заманил человека на какую-то авантюру. Предстоял тяжелый день общения в большой компании людей."
            hide polina with dissolve
            hide artem with dissolve
            jump artem_mind


        label artem_mind:
            "Сделав все утренние дела, я начал собираться к Никите. Волнуюсь. Первый опыт давал о себе знать. Вдруг, что-то пойдет не так и мы не придем к общим соглашениям? Но ведь для этого мы и собираемся."
            show artem at left with dissolve
            a "Надо взять себя в руки"
            hide artem with dissolve
            "Ася попросила взять меня треногу, так как оставила свою в том городе. Полностью собравшись, я пулей вылетел до Никиты."
            scene city
            if write_today:
                jump meet_polina_with_write
            else:
                jump meet_polina



        label meet_polina_with_write:
            show artem at left with dissolve:
                zoom 0.85
            show nikita at right with dissolve:
                zoom 0.75
            show asya at center with dissolve:
                zoom 0.7
            n "Ты что-то рано"
            a "Ну значит вместе встретим Полину и Асю, давай собирайся"
            n "А не слишком ты активный сегодня?"
            a "Я такой же как обычно"
            n "Ты меня не проведешь. Все-таки тебе нравится вся эта затея!"
            a "Может немного."
            n "Ты не представляешь, как я рад это услышать!"
            "Никита собрался довольно быстро, и мы поспешили встретить других сокомандников. Сначала зашли за Асей, а потом пошли встречать Полину на остановку."
            asy "Вы хоть знаете, как она выглядит?"
            a "Неа"
            n "Неа"
            a "Я написал, что мы стоим компанией из трех человек прямо у остановки, думаю найдет"
            hide asya with dissolve
            show asya at center with dissolve:
                zoom 0.75
                xalign 0.33
            show polina at center with dissolve:
                zoom 0.75
                xalign 0.68
            "И вот выходит она. Я многое ожидал от нее: крепкие объятия сразу при встрече, повышенный тон голоса, возможно даже снисходительность и высокомерность общения."
            "Но нет. Мы слышим робкое “П-привет” и сразу понимаем, что некоторые люди совершенно отличаются от своего представления в интернете. "
            n "Это точно она?"
            a "Сам не уверен, может опаздывает?"
            n "Проверь телефон"
            a "Заткнитесь и не смущайте человека! Привет, меня зовут Ася"
            p "П-приятно познакомиться. Полина."
            "И этот человек считался мной самым агрессивным игроком, которого я встречал. Обратный путь давался нам с Никитой тяжело, мы не могли отойти от шока."
            "Зато Ася очень хорошо разговорилась с Полиной, хотя было видно, что ей это тяжело дается, но она старалась втянуться в разговор."
            scene nikita_room_day
            show artem at left with dissolve:
                zoom 0.85
            show nikita at right with dissolve:
                zoom 0.75
            show asya at center with dissolve:
                zoom 0.75
                xalign 0.33
            show polina at center with dissolve:
                zoom 0.75
                xalign 0.68
            "Наконец-то мы дошли до Никиты и стали проходить в его комнату для того, чтобы обсудить игру."
            jump meeting

        label meet_polina:
            scene nikita_room_day
            show nikita at left with dissolve:
                zoom 0.75
            show asya at center with dissolve:
                zoom 0.7
                xalign 0.33
            show polina at center with dissolve:
                zoom 0.7
                xalign 0.68
            show artem at right with dissolve:
                zoom 0.85
            n "Наконец-то пришел."
            a "Да вы все в сборе уже, извините, что опоздал."
            n "Ну Полину ты уже знаешь, однако лично я понял, что похоже не так уже и хорошо."
            "На кровати сидела явно смущенная Полина. И это наш сценарист??? Ладно, я просто совсем по-другому представлял этого человека, а Ася с Никитой кажется уже привыкли."
            "Все-таки некоторые люди в отрыве от интернета ведут себя иначе."
            jump meeting

        label meeting:
            n "Итак, сегодня нам предстоит создать общую концепцию игры: обсудить сеттинг, механики, жанр, конкурентов."
            a "Сразу же хотелось бы уточнить, что бюджета у нас нет и не будет. Вывозим на чистом энтузиазме."
            asy "Раз так, то круг жанров сужается. Может визуальная новелла?"
            n "Мы, конечно, не профессионалы, но хотелось бы запрогать, что-то реально инетересное."
            asy "У меня есть опыт в графическом дизайне и анимации. Есть куда разогнаться."
            a "Я бы для начала обратился к успешным проектам других инди-студий. Super Meat Boy, Five Nights at Freddy’s, Hotline Maiami."
            "И тут начала говорить она. Уверенно, без запинки. Так, как будто уже думала об этом."
            p "Все равно в нашей игре главным воздействием на игрока будет являться сюжет, потому что как бы вы хорошо не делали свою работу, для нее нужен не один человек, а книги пишутся чаще одним автором."
            "Все уставились на нее."
            p "К-как-то так..."
            asy "А что вы молчите? Она права. У тебя уже есть какие-то идеи?"
            p "Не то что бы..."
            n "Давай не стесняйся. Ты же наш геймдизайнер!"
            p "Я всегда хотел написать какой-то хоррор, психологический триллер. Историю, заставляющую чувствовать животный страх, но без визуала такое довольно трудно сделать..."
            n "А как насчет игр, в которых подоплека сюжета проходит через сами механики."
            n "В той же “Hotline Maiami” драйвовая музыка резко прекращается, после каждого пройденного уровня, и остается только шум в ушах героя, что указывает на его состояния во время всей этой жестокости, что он совершает. "
            asy "Мы что-то углубились в детали, не имея ничего из заготовок. Я предлагаю взять графику как в “Dead cells”, “Katana zero”, “Hotline Maiami”."
            asy "Кто-то против? А теперь выдвигайте свои идеи по поводу сюжета и сеттинга. Начинать двигаться надо от этого."
            a "Хорошая идея."
            "Именно после слов Аси обсуждения пошло быстрее. Возможно, она и правда прирожденный лидер."
            "Остановились наши размышления на нуар сеттинге, а именно детективная история с ужасающим убийцей. Таким образом мы учли предпочтения Полины, она была рада, что ей дали прописать такой сюжет."
            "Чтобы его хорошо подать, мы выбрали жанр ролевой игры с добавлением платформинга и экшена в определнные моменты психологического состояния героя."
            "На этом мы решили закончить обсуждения и ждать прописанного сюжета и героев, для их отрисовки и добавления в игру."
            asy "Хорошо поработали, ребята! Полина тебе понравилось?"
            p "Было весело..."
            n "Ждем от тебя наброски сюжета и начинаем приступать к работе!"
            p "Я постараюсь."
            a "Долго же мы сидели. Уже стемнело."
            scene nikita_room_night
            show nikita at left with dissolve:
                zoom 0.75
            n "Зато как много всего обсудили, а теперь идите отдыхайте."
            hide nikita with dissolve
            "Мы благополучно вышли из дома Никиты и побрели до остановки."
            scene city
            "Проводив Полину, по пути домой Ася безостановочно рассказывала о своих дизайнерских решениях по поводу локаций, а я слушал так внимательно, что не упустил ни одну деталь."
            show artem at left with dissolve
            show asya at right with dissolve:
                zoom 0.8
            asy "Все таки я рада, что мы занялись этим делом. Я чувствую командный дух!"
            a "Получилось и правда неплохо, надеюсь так пойдет и дальше. Что-то типа плана уже составлено, осталось ему следовать."
            asy "А этот проект у тебя тоже был по плану?"
            a "Конечно нет."
            asy "Главное, что мы получаем удовольствие от этого дела."
            a "И то верно. До скорого!"
            asy "Удачи"
            hide asya with dissolve
            hide artem with dissolve
            "Хорошо, что до дома было не так далеко. С этими обсуждениями я был совсем без сил."
            scene thinking_in_room
            "Наконец-то придя домой, я сразу лег в кровать. Мне и правда было весело сегодня."
            "Раньше я только наблюдал за тем, как создают, что-то свое, а теперь сам участвую в таком деле. От усталости мысли путались, и сон пришел быстрее обычного."
            scene artem_room
            "Работа над проектом шла полным ходом: Полина писала сценарий, Ася накидывала концепт-арты персонажей и лвлов, а мы с Никитой уже выбрали движок на котором станем писать игру."
            "Подготовка к основной части разработки уже подходила к концу и настал этап прототипирования, поэтому мы решили собраться, дабы обсудить дальнейшие действия команды."
            "В этот раз принимать гостей пришлось мне, так как у Никиты в гостях были родственники, а моя мать как раз уехала к бабушке на все выходные."
            "Я встал пораньше, потому что приводить Никиту в неубранную комнату себе дороже."
            "Помню, как в детстве я пригласил его в гости поиграть в приставку, а потом пойти гулять, но вместо этого мы целый день прибирались и никуда не пошли."
            "После этого в гости я звал его редко. Очень редко."
            "Вычистив все по полной программе, уже подходило время встречи, и я услышал звонок в дверь. Никита первый ворвался в мою комнату и начал все судорожно осматривать. "

            show artem at left with dissolve:
                zoom 0.85
            show nikita at right with dissolve:
                zoom 0.75
            show asya at center with dissolve:
                zoom 0.75
                xalign 0.33
            show polina at center with dissolve:
                zoom 0.75
                xalign 0.68

            a "Ну как тебе?"
            n "Не идеально, но тебе пойду на уступки. Это что моя фигурка человека паука?"
            a "Давайте приступим к работе."
            n "Я ее с 8 лет не видел!"
            asy "Полина сказала, что основная часть сюжета готова и можно начинать работать над ветвлениями истории, диалогами, и отношениями персонажей."
            asy "Я же нарисовала множество концепт-артов, которые уже можно моделировать и создавать скелет игры."
            "В этот день мы наконец-то закрепили позиции и обязанности каждого в проекте."
            "Полина отвечает за все сюжетные части игры, нарративы, взаимоотношения персонажей, подсказывает дизайнеру оформление локаций и героев."
            "Ася занимается анимацией и моделированием. Я прописываю поведение персонажей в программе и помогаю в работе дизайнера.
            "Никита же отвечает за геймплей и механики игры."
            "Следующей целью мы выбрали создание макета игры. Добавить какие-то базовые механики, чтобы побегать и опробовать как будет выглядеть игра."
            asy "Не хочется медлить, давайте начнем сейчас."
            "Кажется, я совсем не ожидал, что мы начнем над этим работу в ту же секунду после обсуждения."
            "По концепт-артам Ася начала моделировать персонажа и добавлять к нему анимации. С первым помогала Полина, а со вторым я."
            n "Работа над локацией будет происходить долго, так что давайте просто создадим платформу, на которой персонаж может побегать."
            "Уже подключился Никита, который оживил нашего героя."
            p "Создать локацию и уже будет выглядеть, как настоящая игра!"
            asy "Я думаю мы с Артемом можем подзадержаться сегодня. Так ведь?"
            a "Не думаю, что у меня есть выбор, когда ты так спрашиваешь."
            asy "И правильно думаешь."
            "Полина дала некоторые рекомендации по оформлению первой локации Асе, а Никита на доступном языке объяснил мне как работает его геймплейный код, чтобы мы могли добавить его на новую локацию."
            hide nikita with dissolve
            hide polina with dissolve
            hide artem with dissolve
            hide asya with dissolve

            show artem at left with dissolve
            show asya at right with dissolve:
                zoom 0.8

            "И вот мы остались вдвоем. Я принес нам чая с печеньками, и началась работа над оформлением лвла."
            "Пока Ася занималась локацией и ей не требовалась моя помощь, мой ум был занят оформлением диалогового окна - одной из главных составляющих ролевой игры."
            "Был выходной поэтому мы решили работать до отказа. А точнее это решила Ася."
            "Наконец-то макет локации был готов. Мы добавили одного болванчика и создали с ним один из сценарных диалогов с вариантами ответов."
            a "Пока выходит неплохо. Надо доработать окружение, добавить персонажей из сюжета, механик, которые придумал Никита, и будет полноценный пролог игры. Ася?"
            "Я так увлекся, что не заметил, как Ася тихо задремала прямо за столом. Оно и не удивительно, время было позднее.
            scene thinking_in_room
            show artem at left with dissolve
            show asya at right with dissolve:
                zoom 0.8
            "Я выключил компы, свет,  пернес Асю на свою кровать, а сам расположился на полу. Спустя некоторое время молчания Ася вдруг заговорила"
            asy "И не думай ничего постыдного, я просто устала сегодня."
            a "Ни в коем случае. Спи."
            asy "Мог и разбудить, чтобы я пошла домой."
            a "Уже поздно, а мне лень тебя провожать. Не переживай, просто спи."
            "Кажется, Ася окончательно уснула. Оказывается, она говорит во сне. Этого я точно не ожидал. Бормотала, что-то про анимацию, а мне пришлось включить музыку, чтобы спокойно уснуть. "

            jump good_continue


        label good_continue:
            "Хороший конец"
            jump end

        label bad_continue:
            "Плохой конец"
            jump end

        label end:
            return
