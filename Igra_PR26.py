# коллекции игрока

inventory = []            # список: инвентарь
clues_found = set()       # множество: улики
visited_rooms = set()     # множество: посещённые комнаты
asked_questions = set()   # множество: заданные вопросы дворецкому
opened_objects = set()    # множество: открытые объекты


# словари

item_descriptions = {
    "разбитая чашка":
        "Фарфоровая чашка, разбитая на кусочки. На дне — бурые пятна.",
    "порванное письмо":
        "Обрывок письма. Читается: «Код сейфа: 5_ _7». Остальное оторвано.",
    "старый фонарь":
        "Тяжёлый железный фонарь. Он ещё работает.",
    "записка с цифрами":
        "Клочок бумаги с надписью: «средние цифры: 3 и 1».",
    "пятно на ковре":
        "Тёмное пятно на ковре. Похоже на кровь. Вы сфотографировали его.",
    "дневник Аркадия":
        "Дневник хозяина усадьбы. Последняя запись: «Кузьма что-то скрывает...».",
    "ключ от подвала":
        "Тяжёлый железный ключ с биркой «Подвал».",
}

character_info = {
    "кузьма": {
        "имя": "Дворецкий Кузьма",
        "описание": "Пожилой дворецкий. Слишком спокоен для такой ситуации.",
        "реплики": [
            "Добрый вечер, господа. Хозяин... уехал по делам.",
            "Я ничего не знаю о его исчезновении.",
            "В подвал? Туда давно никто не спускался.",
        ],
    },
}

safe_codes = {
    "кабинет": "5317",
}

room_params = {
    "холл":     ("Холл",     3, True),
    "гостиная": ("Гостиная", 4, True),
    "кабинет":  ("Кабинет",  2, False),
    "подвал":   ("Подвал",   1, False),
}

topics_for_kuzma = {
    "аркадий":       "Где сейчас хозяин усадьбы?",
    "исчезновение":  "Что вы знаете об исчезновении Аркадия Соколова?",
    "подвал":        "Что находится в подвале?",
}


# вспомогательные функции

def separator():
    """Вывести разделитель."""
    print("=" * 60)


def show_inventory():
    """Показать инвентарь и улики."""
    if not inventory:
        print("\nИнвентарь пуст.")
    else:
        print("\nИнвентарь:")
        for item in inventory:
            print(f"  - {item}")

    if clues_found:
        print(f"Собрано улик: {len(clues_found)} из 7")
        print("  Улики:", ", ".join(sorted(clues_found)))
    else:
        print("Улик пока нет.")


def add_item(item):
    """Добавить предмет и засчитать улику, если надо."""
    if item in inventory:
        print(f"«{item}» уже есть в инвентаре.")
        return

    inventory.append(item)
    print(f"Вы взяли: «{item}»")
    print(f"  {item_descriptions.get(item, '...')}")

    clue_items = {
        "разбитая чашка", "порванное письмо", "записка с цифрами",
        "пятно на ковре", "дневник Аркадия", "ключ от подвала",
    }
    if item in clue_items:
        clues_found.add(item)
        print(f"Улика добавлена. Всего улик: {len(clues_found)}.")


def remove_item(item):
    """Удалить предмет из инвентаря."""
    if item in inventory:
        inventory.remove(item)
        return True
    return False


def show_actions(actions):
    """Показать нумерованный список доступных действий."""
    print("\n" + "-" * 60)
    print("Доступные действия:")
    for i, a in enumerate(actions, start=1):
        print(f"  {i}) {a}")
    print("-" * 60)


def choose_action(actions):
    """
    Показать действия и вернуть выбранное действие (строку).
    Возвращает None, если ввод некорректен.
    """
    show_actions(actions)
    raw = input("Введите номер действия: ").strip()

    if not raw.isdigit():
        print("Нужно ввести число — номер действия из списка.")
        return None

    num = int(raw)
    if 1 <= num <= len(actions):
        return actions[num - 1]

    print(f"Нет действия с номером {num}. В списке {len(actions)} пунктов.")
    return None


# уровень 1. холл

def level1_hall():
    """Первый уровень: сбор первых улик в холле."""
    separator()
    print("УРОВЕНЬ 1. ХОЛЛ УСАДЬБЫ")
    separator()
    print("Савва и Александр входят в тёмный холл усадьбы.")
    print("За спиной с грохотом захлопывается дверь.")
    print("Савва: «Обратной дороги нет. Придётся разобраться.»")
    print("Александр: «Тогда осмотримся. Хозяин не мог исчезнуть просто так.»")

    visited_rooms.add("холл")

    room_name, size, has_light = room_params["холл"]
    print(f"\nКомната: {room_name}, размер {size}x{size} шагов,")
    print(f"свет: {'есть' if has_light else 'нет'}.")

    available_items = ["разбитая чашка", "старый фонарь", "порванное письмо"]

    while True:
        actions = ["Осмотреться", "Инвентарь"]
        if available_items:
            actions.append("Взять предмет")
        if "порванное письмо" in inventory:
            actions.append("Идти в гостиную")
        else:
            actions.append("Идти в гостиную (нужно письмо)")

        choice = choose_action(actions)
        if choice is None:
            continue

        if choice == "Осмотреться":
            if available_items:
                print("Савва и Александр видят:")
                for item in available_items:
                    print(f"  - {item}")
            else:
                print("В холле больше ничего интересного.")

        elif choice == "Инвентарь":
            show_inventory()

        elif choice == "Взять предмет":
            print("Что взять?")
            for i, item in enumerate(available_items, start=1):
                print(f"  {i}) {item}")
            raw = input("Номер предмета (0 — отмена): ").strip()
            if not raw.isdigit():
                print("Нужно ввести число.")
                continue
            num = int(raw)
            if num == 0:
                continue
            if 1 <= num <= len(available_items):
                item = available_items.pop(num - 1)
                add_item(item)
            else:
                print("Нет предмета с таким номером.")

        elif choice.startswith("Идти в гостиную"):
            if "порванное письмо" in inventory:
                print("\nАлександр: «Письмо пригодится. Идём дальше.»")
                opened_objects.add("дверь_в_гостиную")
                return True
            else:
                print("Савва: «Сначала осмотрим холл внимательнее.»")
                print("Кажется, здесь есть что-то важное...")


# уровень 2. гостиная

def level2_living_room():
    """Второй уровень: разговор с дворецким и новые улики."""
    separator()
    print("УРОВЕНЬ 2. ГОСТИНАЯ")
    separator()
    print("В гостиной у камина стоит дворецкий Кузьма.")
    print("Он пристально смотрит на вас, но молчит.")

    visited_rooms.add("гостиная")

    room_name, size, has_light = room_params["гостиная"]
    print(f"\nКомната: {room_name}, размер {size}x{size} шагов.")

    print(f"\n{character_info['кузьма']['имя']}:")
    print(f"  {character_info['кузьма']['описание']}")

    available_items = ["пятно на ковре"]
    hidden_items = ["записка с цифрами"]

    required_topics = {"исчезновение", "подвал"}

    while True:
        actions = ["Осмотреться", "Инвентарь", "Поговорить с Кузьмой",
                   "Спросить Кузьму"]
        if available_items:
            actions.insert(1, "Взять предмет")
        if required_topics.issubset(asked_questions):
            actions.append("Идти в кабинет")
        else:
            actions.append("Идти в кабинет (расспросите Кузьму)")

        choice = choose_action(actions)
        if choice is None:
            continue

        if choice == "Осмотреться":
            if available_items:
                print("Савва замечает:")
                for item in available_items:
                    print(f"  - {item}")
            else:
                print("В гостиной больше ничего примечательного.")

        elif choice == "Инвентарь":
            show_inventory()

        elif choice == "Взять предмет":
            print("Что взять?")
            for i, item in enumerate(available_items, start=1):
                print(f"  {i}) {item}")
            raw = input("Номер предмета (0 — отмена): ").strip()
            if not raw.isdigit():
                print("Нужно ввести число.")
                continue
            num = int(raw)
            if num == 0:
                continue
            if 1 <= num <= len(available_items):
                item = available_items.pop(num - 1)
                add_item(item)
            else:
                print("Нет предмета с таким номером.")

        elif choice == "Поговорить с Кузьмой":
            print("\nКузьма говорит:")
            for line in character_info["кузьма"]["реплики"]:
                print(f"  «{line}»")

        elif choice == "Спросить Кузьму":
            topics = list(topics_for_kuzma.keys())
            print("О чём спросить?")
            for i, topic in enumerate(topics, start=1):
                mark = " (уже спрашивали)" if topic in asked_questions else ""
                print(f"  {i}) {topics_for_kuzma[topic]}{mark}")
            raw = input("Номер темы (0 — отмена): ").strip()
            if not raw.isdigit():
                print("Нужно ввести число.")
                continue
            num = int(raw)
            if num == 0:
                continue
            if not (1 <= num <= len(topics)):
                print("Нет темы с таким номером.")
                continue

            topic = topics[num - 1]
            if topic in asked_questions:
                print("Вы уже это спрашивали.")
                continue

            asked_questions.add(topic)
            print(f"\nВаш вопрос: {topics_for_kuzma[topic]}")

            if topic == "аркадий":
                print("Кузьма: «Хозяин уехал. Я не знаю куда.»")
            elif topic == "исчезновение":
                print("Кузьма: «Я ничего не знаю. Уверяю вас.»")
                print("Александр замечает, что Кузьма отводит взгляд.")
            elif topic == "подвал":
                print("Кузьма: «В подвале сыро. Ключ... потерян.»")
                print("Из его кармана выпадает клочок бумаги.")
                if "записка с цифрами" in hidden_items:
                    hidden_items.remove("записка с цифрами")
                    add_item("записка с цифрами")

            if required_topics.issubset(asked_questions):
                if "показание дворецкого" not in clues_found:
                    clues_found.add("показание дворецкого")
                    print("\nСавва: «Он себе противоречит.»")
                    print("Новая улика: «показание дворецкого».")

        elif choice.startswith("Идти в кабинет"):
            if required_topics.issubset(asked_questions):
                print("\nАлександр: «Достаточно. Идём в кабинет.»")
                opened_objects.add("дверь_в_кабинет")
                return True
            else:
                print("Сначала расспросите дворецкого о главном:")
                print("  - исчезновение")
                print("  - подвал")


# уровень 3. кабинет

def level3_office():
    """Третий уровень: разгадать код сейфа."""
    separator()
    print("УРОВЕНЬ 3. КАБИНЕТ АРКАДИЯ СОКОЛОВА")
    separator()
    print("Кабинет хозяина. На столе — бумаги, в углу — старый сейф.")
    print("Савва: «Чтобы попасть в подвал, нужен ключ,»")
    print("       «а он, скорее всего, в сейфе.»")

    visited_rooms.add("кабинет")

    room_name, size, has_light = room_params["кабинет"]
    print(f"\nКомната: {room_name}, размер {size}x{size} шагов,")
    print(f"свет: {'есть' if has_light else 'нет'}.")

    available_items = ["дневник Аркадия"]

    while True:
        actions = ["Осмотреться", "Инвентарь", "Открыть сейф",
                   "Ввести код сейфа"]
        if available_items:
            actions.insert(1, "Взять предмет")
        if "сейф" in opened_objects and "ключ от подвала" in inventory:
            actions.append("Идти в подвал")
        else:
            actions.append("Идти в подвал (нужен ключ из сейфа)")

        choice = choose_action(actions)
        if choice is None:
            continue

        if choice == "Осмотреться":
            if available_items:
                print("На столе:")
                for item in available_items:
                    print(f"  - {item}")
            else:
                print("Стол пуст.")
            print("В углу — сейф с кодовым замком.")

        elif choice == "Инвентарь":
            show_inventory()

        elif choice == "Взять предмет":
            print("Что взять?")
            for i, item in enumerate(available_items, start=1):
                print(f"  {i}) {item}")
            raw = input("Номер предмета (0 — отмена): ").strip()
            if not raw.isdigit():
                print("Нужно ввести число.")
                continue
            num = int(raw)
            if num == 0:
                continue
            if 1 <= num <= len(available_items):
                item = available_items.pop(num - 1)
                add_item(item)
            else:
                print("Нет предмета с таким номером.")

        elif choice == "Открыть сейф":
            print("\nСейф закрыт. Нужен код из 4 цифр.")
            if "порванное письмо" in inventory and "записка с цифрами" in inventory:
                print("В письме: «Код: 5_ _7».")
                print("В записке: «средние цифры: 3 и 1».")
                print("Похоже, код можно собрать.")
            elif "порванное письмо" in inventory:
                print("В письме: «Код: 5_ _7». Где взять средние цифры?")
            elif "записка с цифрами" in inventory:
                print("В записке: «3 и 1». Но где остальные цифры?")
            else:
                print("Подсказок нет. Возможно, вы что-то упустили.")

        elif choice == "Ввести код сейфа":
            code = input("Введите код из 4 цифр: ").strip()
            if code == safe_codes["кабинет"]:
                print("\nСейф щёлкает и открывается.")
                print("Александр: «Внутри ключ. Тот самый, от подвала.»")
                opened_objects.add("сейф")
                add_item("ключ от подвала")
                if "дневник Аркадия" not in inventory:
                    print("Савва: «И дневник со стола не забудь.»")
            else:
                print("Сейф не открылся. Код неверный.")

        elif choice.startswith("Идти в подвал"):
            if "сейф" in opened_objects and "ключ от подвала" in inventory:
                print("\nВы берёте ключ и спускаетесь в подвал.")
                return True
            elif "сейф" in opened_objects:
                print("Сначала возьмите ключ из сейфа.")
            else:
                print("Дверь в подвал заперта. Сначала откройте сейф.")


# уровень 4. подвал

def handle_accusation():
    """Разоблачение дворецкого."""
    key_clues = {
        "разбитая чашка", "порванное письмо", "записка с цифрами",
        "пятно на ковре", "дневник Аркадия", "ключ от подвала",
        "показание дворецкого",
    }
    if key_clues.issubset(clues_found):
        print("\nСавва и Александр предъявляют улики по очереди.")
        print("Кузьма бледнеет: «Хорошо... это был я. Я хотел его усадьбу.»")
        return "accused_full"
    else:
        missing = key_clues - clues_found
        print("\nКузьма усмехается: «У вас нет доказательств, господа.»")
        print(f"Не хватает улик: {', '.join(sorted(missing))}.")
        print("Поищите больше улик или выберите другой вариант.")
        return None


def handle_deal():
    """Сделка с дворецким."""
    print("\nКузьма достаёт конверт с деньгами.")
    print("«Возьмите. Забудьте про этот вечер — и разойдёмся.»")
    print("Александр молча берёт деньги, Савва отворачивается.")
    return "deal"


def handle_leave():
    """Уйти, не разобравшись."""
    print("\nСавва и Александр разворачиваются и уходят из усадьбы.")
    print("Тайна осталась нераскрытой.")
    return "leave"


def level4_basement():
    """Четвёртый уровень: развязка в подвале."""
    separator()
    print("УРОВЕНЬ 4. ПОДВАЛ")
    separator()
    print("Савва и Александр спускаются по скрипучей лестнице.")
    print("В свете фонаря видны очертания связанного человека.")
    print("Рядом — дворецкий Кузьма с конвертом в руках.")

    visited_rooms.add("подвал")

    room_name, size, has_light = room_params["подвал"]
    print(f"\nКомната: {room_name}, размер {size}x{size} шагов,")
    print(f"свет: {'есть' if has_light else 'нет'}.")

    while True:
        actions = ["Осмотреться", "Инвентарь", "Уличить Кузьму",
                   "Взять деньги и уйти", "Уйти"]
        choice = choose_action(actions)
        if choice is None:
            continue

        if choice == "Осмотреться":
            print("Вы видите связанного Аркадия Соколова и Кузьму рядом.")
            print("Аркадий жив, но без сознания.")

        elif choice == "Инвентарь":
            show_inventory()

        elif choice == "Уличить Кузьму":
            result = handle_accusation()
            if result:
                return result

        elif choice == "Взять деньги и уйти":
            return handle_deal()

        elif choice == "Уйти":
            return handle_leave()


# финал

def print_ending(result):
    """Вывести финальную концовку."""
    separator()
    if result == "accused_full":
        print("КОНЦОВКА: «ПРАВДА»")
        print("Савва и Александр раскрыли тайну усадьбы.")
        print("Аркадий Соколов спасён, Кузьма арестован.")
        print("Ваша статья выходит завтра.")
    elif result == "deal":
        print("КОНЦОВКА: «СДЕЛКА»")
        print("Вы взяли деньги и ушли. Тайна осталась нераскрытой.")
        print("Совесть вас ещё долго будет мучить.")
    else:
        print("КОНЦОВКА: «МОЛЧАНИЕ»")
        print("Вы ушли ни с чем. Аркадий Соколов так и не был найден.")

    print()
    print(f"Собрано улик: {len(clues_found)} из 7")
    if clues_found:
        print("  Улики:", ", ".join(sorted(clues_found)))
    else:
        print("  Улик нет.")
    print(f"Пройдено комнат: {len(visited_rooms)}")
    print("  Комнаты:", ", ".join(sorted(visited_rooms)))
    if opened_objects:
        print("Открыто:", ", ".join(sorted(opened_objects)))
    separator()


# запуск игры

def main():
    """Точка входа."""
    separator()
    print("ТАЙНА УСАДЬБЫ СОКОЛОВА")
    print("Текстовая игра-новелла")
    separator()
    print("Два друга-журналиста, Савва и Александр, приезжают")
    print("в старую усадьбу Аркадия Соколова. Хозяин бесследно")
    print("исчез три дня назад, а ворота за гостями закрываются")
    print("сами собой. Нужно собрать улики, найти Аркадия")
    print("и решить, что делать с правдой.")
    print()

    if not level1_hall():
        return
    print("\n[Уровень 1 пройден]")

    if not level2_living_room():
        return
    print("\n[Уровень 2 пройден]")

    if not level3_office():
        return
    print("\n[Уровень 3 пройден]")

    result = level4_basement()
    print_ending(result)


if __name__ == "__main__":
    main()