categories_data = [
 {"name": "Еда"},
 {"name": "Бары"},
 {"name": "Культура"},
 {"name": "Новый опыт"},
 {"name": "Страх"},
 {"name": "Экстрим"},
 {"name": "Животные"},
 {"name": "Мастер-классы"},
 {"name": "Спорт"},
 {"name": "Релакс"},
]

options_data = [
 {"name": "У вас есть аллергия на животных?"},
 {"name": "Боитесь ли Вы высоты?"},
 {"name": "Любите крепкий алкоголь?", "desirable": True},
]

locations_data = [{
    "name": "Мексиканский бар «El Chapo»",
    "coords": [59.93504096272858, 30.347761359920188],
    "address": "Литейный проспект, 57",
    "website": "http://эльчапо.рф/",
    "offers": [{
        "name": "Мексиканский бар «El Chapo»",
        "description": "Блюда",
        "calendar": [
            {"open_time": "18:00", "close_time": "6:00", "only_weekdays": [5, 6]},
            {"open_time": "17:00", "close_time": "3:00", "except_weekdays": [5, 6]},
        ],
        "categories": ["Еда"],
        "grade": 2,
        "price": 500,
    }, {
        "name": "Мексиканский бар «El Chapo»",
        "description": "Кокотейли, шоты",
        "calendar": [
            {"open_time": "18:00", "close_time": "6:00", "only_weekdays": [5, 6]},
            {"open_time": "17:00", "close_time": "3:00", "except_weekdays": [5, 6]},
        ],
        "categories": ["Бары"],
        "grade": 1,
        "price": 300,
    }],
}, {
    "name": "Грузинский ресторан «Mama Georgia»",
    "coords": [59.924456665460305, 30.24194468718984],
    "address": "Кожевенная линия, д. 40",
    "website": "https://mama-georgia.ru/",
    "offers": [{
        "name": "Грузинский ресторан «Mama Georgia»",
        "description": "Блюда",
        "calendar": [
            {"open_time": "12:00", "close_time": "23:00", "except_weekdays": [5, 6]},
            {"open_time": "12:00", "close_time": "1:00", "only_weekdays": [5, 6]},
        ],
        "categories": ["Еда"],
        "grade": 3,
        "price": 1200,
    }],
}, {
    "name": "Кафе русской кухни «Siberika»",
    "coords": [59.93101639522108, 30.271370719701636],
    "address": "наб. Лейтенанта Шмидта, 43",
    "website": "https://restaurantsiberika.ru",
    "offers": [{
        "name": "Кафе русской кухни «Siberika»",
        "description": "Блюда",
        "calendar": [
            {"open_time": "11:00", "close_time": "23:00", "except_weekdays": [6, 7]},
            {"open_time": "12:00", "close_time": "0:00", "only_weekdays": [6, 7]},
        ],
        "categories": ["Еда"],
        "grade": 1,
        "price": 300,
    }],
}, {
    "name": "Арт-Кафе «ArtHall»",
    "coords": [59.9581800021303, 30.30945431179489],
    "address": "Сытнинская улица, 14",
    "website": "https://vk.com/coffeearthall",
    "offers": [{
        "name": "Арт-Кафе «ArtHall»",
        "description": "Блюда",
        "calendar": [
            {"open_time": "15:00", "close_time": "22:00"},
        ],
        "categories": ["Еда"],
        "grade": 2,
        "price": 600,
    }, {
        "name": "Арт-Кафе «ArtHall»",
        "description": "Билет",
        "calendar": [
            {"open_time": "15:00", "close_time": "22:00"},
        ],
        "categories": ["Мастер-классы"],
        "grade": 3,
        "price": 2000,
    }],
}, {
    "name": "Бар «Quokka bar»",
    "coords": [59.96277962893864, 30.30976712684854],
    "address": "Большая Пушкарская, 50",
    "website": "https://vk.com/quokkabar",
    "offers": [{
        "name": "Бар «Quokka bar»",
        "description": "Блюда",
        "calendar": [
            {"open_time": "15:00", "close_time": "0:00"},
        ],
        "categories": ["Еда"],
        "grade": 3,
        "price": 1500,
    }, {
        "name": "Бар «Quokka bar»",
        "description": "Крафтовое пиво",
        "calendar": [
            {"open_time": "15:00", "close_time": "0:00"},
        ],
        "categories": ["Бары"],
        "grade": 2,
        "price": 500,
    }],
}, {
    "name": "Итальянский ресторан «Casa Nostra»",
    "coords": [59.94150275745054, 30.280845827138002],
    "address": "6-я линия В.О. дом 21",
    "website": "https://vk.com/casanostraspb",
    "offers": [{
        "name": "Итальянский ресторан «Casa Nostra»",
        "description": "Блюда",
        "calendar": [
            {"open_time": "12:00", "close_time": "23:00", "except_weekdays": [5, 6]},
            {"open_time": "12:00", "close_time": "0:00", "only_weekdays": [5]},
            {"open_time": "13:00", "close_time": "0:00", "only_weekdays": [6]},
        ],
        "categories": ["Еда"],
        "grade": 1,
        "price": 250,
    }],
}, {
    "name": "Бар-музей скандинавской мифологии «SKAL!»",
    "coords": [59.923285881543755, 30.342374169465167],
    "address": "ул. Правды, 12",
    "website": "https://skalbar.ru/",
    "offers": [{
        "name": "Бар-музей скандинавской мифологии «SKAL!»",
        "description": "Шоты",
        "calendar": [
            {"open_time": "15:00", "close_time": "2:00", "only_weekdays": [1, 2, 3, 4]},
            {"open_time": "15:00", "close_time": "3:00", "only_weekdays": [5]},
            {"open_time": "14:00", "close_time": "3:00", "only_weekdays": [6]},
            {"open_time": "14:00", "close_time": "2:00", "only_weekdays": [7]},
        ],
        "categories": ["Бары"],
        "grade": 2,
        "price": 600,
    }],
}, {
    "name": "Бар «Neon bar»",
    "coords": [59.930120135441385, 30.319414413645426],
    "address": "ул. Гороховая, 31",
    "website": "https://vk.com/31cnbar",
    "offers": [{
        "name": "Бар «Neon bar»",
        "description": "Коктейли, шоты",
        "calendar": [
            {"open_time": "15:00", "close_time": "6:00"},
        ],
        "categories": ["Бары"],
        "grade": 3,
        "price": 800,
    }],
}, {
    "name": "Славянский бар-музей «Пьяна ель»",
    "coords": [59.944202389186295, 30.34784616946618],
    "address": "ул. Пестеля, 21",
    "website": "https://barelspb.ru/",
    "offers": [{
        "name": "Славянский бар-музей «Пьяна ель»",
        "description": "Шоты",
        "calendar": [
            {"open_time": "15:00", "close_time": "2:00", "only_weekdays": [1, 2, 3, 4]},
            {"open_time": "15:00", "close_time": "3:00", "only_weekdays": [5]},
            {"open_time": "14:00", "close_time": "3:00", "only_weekdays": [6]},
            {"open_time": "14:00", "close_time": "2:00", "only_weekdays": [7]},
        ],
        "categories": ["Бары"],
        "grade": 1,
        "price": 250,
    }],
}, {
    "name": "Музей рекордов и фактов «Титикака»",
    "coords": [59.93195973311646, 30.321025913645485],
    "address": "ул. Казанская, 7",
    "website": "https://titiqaqa.ru/",
    "offers": [{
        "name": "Музей рекордов и фактов «Титикака»",
        "description": "Билет",
        "calendar": [
            {"open_time": "10:00", "close_time": "22:00"},
       ],
       "categories": ["Культура", "Новый опыт"],
        "grade": 3,
        "price": 1000,
    }],
}]
