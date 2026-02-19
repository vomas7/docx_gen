from core.ui_objects.base.base_attribute import SimpleAttribute


class Prst(SimpleAttribute):
    """Enum для всех предустановленных геометрических форм DrawingML"""

    # class Options(Enum):
    #     # ========== ОСНОВНЫЕ ФИГУРЫ ==========
    #     rect = "rect"  # Прямоугольник (по умолчанию)
    #     roundRect = "roundRect"  # Прямоугольник со скругленными углами
    #     snip1Rect = "snip1Rect"  # Прямоугольник с одним срезанным углом
    #     snip2Rect = "snip2Rect"  # Прямоугольник с двумя срезанными углами
    #     snipRoundRect = "snipRoundRect"  # Прямоугольник со скругленными и срезанными
    #     углами
    #     frame = "frame"  # Рамка
    #     halfFrame = "halfFrame"  # Полурамка
    #
    #     # Овалы и круги
    #     ellipse = "ellipse"  # Эллипс/овал
    #     circle = "circle"  # Круг
    #
    #     # Треугольники
    #     triangle = "triangle"  # Равносторонний треугольник (вершиной вверх)
    #     rtTriangle = "rtTriangle"  # Прямоугольный треугольник
    #     isoTriangle = "isoTriangle"  # Равнобедренный треугольник
    #
    #     # Другие многоугольники
    #     diamond = "diamond"  # Ромб
    #     parallelogram = "parallelogram"  # Параллелограмм
    #     trapezoid = "trapezoid"  # Трапеция
    #     hexagon = "hexagon"  # Шестиугольник
    #     octagon = "octagon"  # Восьмиугольник
    #     decagon = "decagon"  # Десятиугольник
    #     dodecagon = "dodecagon"  # Двенадцатиугольник
    #     pentagon = "pentagon"  # Пятиугольник
    #     heptagon = "heptagon"  # Семиугольник
    #     nonagon = "nonagon"  # Девятиугольник
    #
    #     # Объемные формы
    #     can = "can"  # Цилиндр/банка
    #     cube = "cube"  # Куб
    #     bevel = "bevel"  # Скошенный прямоугольник
    #
    #     # Специальные основные
    #     homePlate = "homePlate"  # Бейсбольная "база"
    #     chevron = "chevron"  # Шеврон
    #     pie = "pie"  # Сектор круга (пирог)
    #     chord = "chord"  # Сегмент круга
    #     teardrop = "teardrop"  # Капля
    #     blockArc = "blockArc"  # Блочная дуга
    #     donut = "donut"  # Пончик/тороид
    #
    #     # ========== СТРЕЛКИ ==========
    #     # Простые стрелки
    #     rightArrow = "rightArrow"  # Стрелка вправо
    #     leftArrow = "leftArrow"  # Стрелка влево
    #     upArrow = "upArrow"  # Стрелка вверх
    #     downArrow = "downArrow"  # Стрелка вниз
    #     leftRightArrow = "leftRightArrow"  # Двусторонняя стрелка
    #     upDownArrow = "upDownArrow"  # Вертикальная двусторонняя стрелка
    #     quadArrow = "quadArrow"  # Четырехсторонняя стрелка
    #     leftRightUpArrow = "leftRightUpArrow"  # Трехсторонняя стрелка
    #     bentArrow = "bentArrow"  # Изогнутая стрелка
    #     uturnArrow = "uturnArrow"  # Стрелка разворота
    #
    #     # Круговые стрелки
    #     circularArrow = "circularArrow"  # Круговая стрелка
    #     leftCircularArrow = "leftCircularArrow"  # Левая круговая стрелка
    #     leftRightCircularArrow = "leftRightCircularArrow"  # Двусторонняя круговая
    #     стрелка
    #     curvedRightArrow = "curvedRightArrow"  # Изогнутая стрелка вправо
    #     curvedLeftArrow = "curvedLeftArrow"  # Изогнутая стрелка влево
    #     curvedUpArrow = "curvedUpArrow"  # Изогнутая стрелка вверх
    #     curvedDownArrow = "curvedDownArrow"  # Изогнутая стрелка вниз
    #
    #     # ========== БЛОК-СХЕМЫ ==========
    #     flowChartProcess = "flowChartProcess"  # Процесс
    #     flowChartDecision = "flowChartDecision"  # Решение
    #     flowChartInputOutput = "flowChartInputOutput"  # Ввод/вывод
    #     flowChartPredefinedProcess = "flowChartPredefinedProcess"  # Предопределенный
    #     процесс
    #     flowChartInternalStorage = "flowChartInternalStorage"  # Внутреннее хранилище
    #     flowChartDocument = "flowChartDocument"  # Документ
    #     flowChartMultidocument = "flowChartMultidocument"  # Множество документов
    #     flowChartTerminator = "flowChartTerminator"  # Терминатор
    #     flowChartPreparation = "flowChartPreparation"  # Подготовка
    #     flowChartManualInput = "flowChartManualInput"  # Ручной ввод
    #     flowChartManualOperation = "flowChartManualOperation"  # Ручная операция
    #     flowChartConnector = "flowChartConnector"  # Соединитель
    #     flowChartOffpageConnector = "flowChartOffpageConnector"  # Соединитель на
    #     другую страницу
    #     flowChartPunchedCard = "flowChartPunchedCard"  # Перфокарта
    #     flowChartPunchedTape = "flowChartPunchedTape"  # Перфолента
    #     flowChartSummingJunction = "flowChartSummingJunction"  # Суммирующий переход
    #     flowChartOr = "flowChartOr"  # ИЛИ
    #     flowChartCollate = "flowChartCollate"  # Подборка
    #     flowChartSort = "flowChartSort"  # Сортировка
    #     flowChartExtract = "flowChartExtract"  # Извлечение
    #     flowChartMerge = "flowChartMerge"  # Слияние
    #     flowChartOnlineStorage = "flowChartOnlineStorage"  # Онлайн-хранилище
    #     flowChartDelay = "flowChartDelay"  # Задержка
    #     flowChartMagneticTape = "flowChartMagneticTape"  # Магнитная лента
    #     flowChartMagneticDisk = "flowChartMagneticDisk"  # Магнитный диск
    #     flowChartMagneticDrum = "flowChartMagneticDrum"  # Магнитный барабан
    #     flowChartDisplay = "flowChartDisplay"  # Дисплей
    #
    #     # ========== ЗВЕЗДЫ ==========
    #     star4 = "star4"  # 4-лучевая звезда
    #     star5 = "star5"  # 5-лучевая звезда (классическая)
    #     star6 = "star6"  # 6-лучевая звезда (звезда Давида)
    #     star7 = "star7"  # 7-лучевая звезда
    #     star8 = "star8"  # 8-лучевая звезда
    #     star10 = "star10"  # 10-лучевая звезда
    #     star12 = "star12"  # 12-лучевая звезда
    #     star16 = "star16"  # 16-лучевая звезда
    #     star24 = "star24"  # 24-лучевая звезда
    #     star32 = "star32"  # 32-лучевая звезда
    #
    #     # ========== ЛЕНТЫ И БАННЕРЫ ==========
    #     ribbon = "ribbon"  # Лента
    #     ribbon2 = "ribbon2"  # Двойная лента
    #     ellipseRibbon = "ellipseRibbon"  # Овальная лента
    #     ellipseRibbon2 = "ellipseRibbon2"  # Двойная овальная лента
    #     verticalScroll = "verticalScroll"  # Вертикальный свиток
    #     horizontalScroll = "horizontalScroll"  # Горизонтальный свиток
    #     wave = "wave"  # Волна
    #     doubleWave = "doubleWave"  # Двойная волна
    #     plaque = "plaque"  # Плакетка
    #     foldedCorner = "foldedCorner"  # Загнутый уголок
    #     burst = "burst"  # Взрыв/сияние
    #
    #     # ========== ВЫНОСКИ ==========
    #     wedgeRectCallout = "wedgeRectCallout"  # Прямоугольная выноска
    #     wedgeRoundRectCallout = "wedgeRoundRectCallout"  # Выноска со скругленными
    #     углами
    #     wedgeEllipseCallout = "wedgeEllipseCallout"  # Овальная выноска
    #     cloudCallout = "cloudCallout"  # Облачная выноска
    #     lineCallout1 = "lineCallout1"  # Линейная выноска 1
    #     lineCallout2 = "lineCallout2"  # Линейная выноска 2
    #     lineCallout3 = "lineCallout3"  # Линейная выноска 3
    #     borderCallout1 = "borderCallout1"  # Выноска с рамкой 1
    #     borderCallout2 = "borderCallout2"  # Выноска с рамкой 2
    #     borderCallout3 = "borderCallout3"  # Выноска с рамкой 3
    #     accentCallout1 = "accentCallout1"  # Акцентная выноска 1
    #     accentCallout2 = "accentCallout2"  # Акцентная выноска 2
    #     accentCallout3 = "accentCallout3"  # Акцентная выноска 3
    #     callout1 = "callout1"  # Выноска 1 (с заливкой)
    #     callout2 = "callout2"  # Выноска 2 (с заливкой)
    #     callout3 = "callout3"  # Выноска 3 (с заливкой)
    #
    #     # ========== МАТЕМАТИЧЕСКИЕ СИМВОЛЫ ==========
    #     plus = "plus"  # Плюс (+)
    #     mathPlus = "mathPlus"  # Математический плюс
    #     mathMultiply = "mathMultiply"  # Умножение (×)
    #     mathDivide = "mathDivide"  # Деление (÷)
    #     mathEqual = "mathEqual"  # Равно (=)
    #     mathNotEqual = "mathNotEqual"  # Не равно (≠)
    #     minus = "minus"  # Минус (-)
    #
    #     # ========== КНОПКИ И ТАБЫ ==========
    #     cornerTabs = "cornerTabs"  # Угловые вкладки
    #     squareTabs = "squareTabs"  # Квадратные вкладки
    #     plaqueTabs = "plaqueTabs"  # Плакетки-вкладки
    #     round1Rect = "round1Rect"  # Прямоугольник с одним скругленным углом
    #     round2SameRect = "round2SameRect"  # Прямоугольник с двумя одинаково
    #     скругленными углами
    #     round2DiagRect = "round2DiagRect"  # Прямоугольник с диагонально скругленными
    #     углами
    #
    #     # ========== СПЕЦИАЛЬНЫЕ СИМВОЛЫ ==========
    #     noSmoking = "noSmoking"  # Знак "Не курить"
    #     seal4 = "seal4"  # Печать 4-сторонняя
    #     seal8 = "seal8"  # Печать 8-сторонняя
    #     seal16 = "seal16"  # Печать 16-сторонняя
    #     seal32 = "seal32"  # Печать 32-сторонняя
    #     heart = "heart"  # Сердце
    #     lightningBolt = "lightningBolt"  # Молния
    #     sun = "sun"  # Солнце
    #     moon = "moon"  # Луна
    #     smileyFace = "smileyFace"  # Смайлик
    #     irregularSeal1 = "irregularSeal1"  # Неправильная печать 1
    #     irregularSeal2 = "irregularSeal2"  # Неправильная печать 2
    #
    #     # ========== ГРАФИКИ И ДИАГРАММЫ ==========
    #     chartPlus = "chartPlus"  # График с плюсом
    #     chartStar = "chartStar"  # Звездный график
    #     chartX = "chartX"  # X-график
    #
    #     # ========== СОЕДИНИТЕЛИ ==========
    #     straightConnector1 = "straightConnector1"  # Прямой соединитель 1
    #     bentConnector2 = "bentConnector2"  # Изогнутый соединитель 2
    #     bentConnector3 = "bentConnector3"  # Изогнутый соединитель 3
    #     bentConnector4 = "bentConnector4"  # Изогнутый соединитель 4
    #     bentConnector5 = "bentConnector5"  # Изогнутый соединитель 5
    #     curvedConnector2 = "curvedConnector2"  # Кривой соединитель 2
    #     curvedConnector3 = "curvedConnector3"  # Кривой соединитель 3
    #     curvedConnector4 = "curvedConnector4"  # Кривой соединитель 4
    #     curvedConnector5 = "curvedConnector5"  # Кривой соединитель 5
    #
    #     # ========== ДОПОЛНИТЕЛЬНЫЕ МНОГОУГОЛЬНИКИ ==========
    #     hendecagon = "hendecagon"  # Одиннадцатиугольник
    #     tridecagon = "tridecagon"  # Тринадцатиугольник
    #     tetradecagon = "tetradecagon"  # Четырнадцатиугольник
    #     pentadecagon = "pentadecagon"  # Пятнадцатиугольник
    #     hexadecagon = "hexadecagon"  # Шестнадцатиугольник
    #     heptadecagon = "heptadecagon"  # Семнадцатиугольник
    #     octadecagon = "octadecagon"  # Восемнадцатиугольник
    #     enneadecagon = "enneadecagon"  # Девятнадцатиугольник
    #     icosagon = "icosagon"  # Двадцатиугольник
    #
    #     # ========== АКЦЕНТЫ И РАМКИ ==========
    #     accentBorderCallout1 = "accentBorderCallout1"  # Акцентная выноска с рамкой 1
    #     accentBorderCallout2 = "accentBorderCallout2"  # Акцентная выноска с рамкой 2
    #     accentBorderCallout3 = "accentBorderCallout3"  # Акцентная выноска с рамкой 3
    #     actionButtonBack = "actionButtonBack"  # Кнопка "Назад"
    #     actionButtonForward = "actionButtonForward"  # Кнопка "Вперед"
    #     actionButtonBeginning = "actionButtonBeginning"  # Кнопка "В начало"
    #     actionButtonEnd = "actionButtonEnd"  # Кнопка "В конец"
    #     actionButtonHome = "actionButtonHome"  # Кнопка "Домой"
    #     actionButtonInformation = "actionButtonInformation"  # Кнопка "Информация"
    #     actionButtonMovie = "actionButtonMovie"  # Кнопка "Фильм"
    #     actionButtonReturn = "actionButtonReturn"  # Кнопка "Возврат"
    #     actionButtonSound = "actionButtonSound"  # Кнопка "Звук"
    #     actionButtonHelp = "actionButtonHelp"  # Кнопка "Помощь"
    #     actionButtonBlank = "actionButtonBlank"  # Пустая кнопка действия
    #
    #     # ========== КАРАНДАШ И СВОБОДНАЯ ФОРМА ==========
    #     line = "line"  # Линия (особый случай)
    #     pencil = "pencil"  # Карандаш/свободная форма
    #     freeform = "freeform"  # Произвольная форма
    #
    #     # ========== ТЕКСТОВЫЕ БОКСЫ ==========
    #     textPlain = "textPlain"  # Простой текстовый блок
    #     textStop = "textStop"  # Текстовый блок "Стоп"
    #     textTriangle = "textTriangle"  # Треугольный текстовый блок

    #     textTriangleInverted = "textTriangleInverted"  # Инвертированный треугольный
    #     текстовый блок
    #     textChevron = "textChevron"  # Текстовый блок-шеврон
    #     textChevronInverted = "textChevronInverted"  # Инвертированный текстовый
    #     блок-шеврон
    #     textRing = "textRing"  # Кольцевой текстовый блок
    #     textWave = "textWave"  # Волнообразный текстовый блок
    #     textFade = "textFade"  # Текстовый блок с затуханием
    #     textSlant = "textSlant"  # Наклонный текстовый блок
    #     textCan = "textCan"  # Цилиндрический текстовый блок
    #
    #     # ========== ФЛАГИ И СИГНАЛЫ ==========
    #     flag = "flag"  # Флаг
    #     pennant = "pennant"  # Вымпел
    #     banner = "banner"  # Баннер
    #
    #     # ========== ГЕОМЕТРИЧЕСКИЕ УКРАШЕНИЯ ==========
    #     gear6 = "gear6"  # 6-зубая шестеренка
    #     gear9 = "gear9"  # 9-зубая шестеренка
    #     funnel = "funnel"  # Воронка
    #     mathParenthesis = "mathParenthesis"  # Математическая скобка
    #     mathBrace = "mathBrace"  # Математическая фигурная скобка
    #     mathBracket = "mathBracket"  # Математическая квадратная скобка
    #
    #     # ========== БАЛЛОНЫ И ОБЛАКА ==========
    #     balloon = "balloon"  # Воздушный шар/балабон
    #     cloud = "cloud"  # Облако
    #     multiColorCloud = "multiColorCloud"  # Разноцветное облако
    #
    #     # ========== БИОЛОГИЧЕСКИЕ ФОРМЫ ==========
    #     leaf = "leaf"  # Лист
    #     flower = "flower"  # Цветок
    #     tree = "tree"  # Дерево
    #     animal1 = "animal1"  # Животное 1
    #     animal2 = "animal2"  # Животное 2
    #     animal3 = "animal3"  # Животное 3
    #     animal4 = "animal4"  # Животное 4
    #     animal5 = "animal5"  # Животное 5
    #
    #     # ========== МУЗЫКАЛЬНЫЕ СИМВОЛЫ ==========
    #     musicNote = "musicNote"  # Музыкальная нота
    #     musicAccidental = "musicAccidental"  # Музыкальный знак альтерации
    #     musicClef = "musicClef"  # Музыкальный ключ
    #     musicRest = "musicRest"  # Музыкальная пауза
    #
    #     # ========== ТРАНСПОРТ ==========
    #     car = "car"  # Автомобиль
    #     truck = "truck"  # Грузовик
    #     bus = "bus"  # Автобус
    #     airplane = "airplane"  # Самолет
    #     ship = "ship"  # Корабль
    #     train = "train"  # Поезд
    #     bicycle = "bicycle"  # Велосипед
    #     motorcycle = "motorcycle"  # Мотоцикл
    #
    #     # ========== АРХИТЕКТУРА И СТРОИТЕЛЬСТВО ==========
    #     house = "house"  # Дом
    #     building = "building"  # Здание
    #     factory = "factory"  # Завод
    #     bridge = "bridge"  # Мост
    #     tower = "tower"  # Башня
    #     arch = "arch"  # Арка
    #     dome = "dome"  # Купол
    #
    #     # ========== ОФИСНЫЕ ПРЕДМЕТЫ ==========
    #     desk = "desk"  # Письменный стол
    #     chair = "chair"  # Стул
    #     computer = "computer"  # Компьютер
    #     phone = "phone"  # Телефон
    #     printer = "printer"  # Принтер
    #     folder = "folder"  # Папка
    #     fileCabinet = "fileCabinet"  # Картотека
    #     book = "book"  # Книга
    #
    #     # ========== ПИЩЕВЫЕ ПРОДУКТЫ ==========
    #     apple = "apple"  # Яблоко
    #     banana = "banana"  # Банан
    #     bread = "bread"  # Хлеб
    #     cheese = "cheese"  # Сыр
    #     pizza = "pizza"  # Пицца
    #     coffeeCup = "coffeeCup"  # Чашка кофе
    #     wineGlass = "wineGlass"  # Бокал вина
    #
    #     # ========== СПОРТИВНЫЙ ИНВЕНТАРЬ ==========
    #     basketball = "basketball"  # Баскетбольный мяч
    #     football = "football"  # Футбольный мяч
    #     baseball = "baseball"  # Бейсбольный мяч
    #     tennisRacket = "tennisRacket"  # Теннисная ракетка
    #     golfClub = "golfClub"  # Клюшка для гольфа
    #     ski = "ski"  # Лыжа
    #     snowboard = "snowboard"  # Сноуборд

    def __init__(self, value: str = "rect"):
        super().__init__(value=value, xml_name="a:prst")
