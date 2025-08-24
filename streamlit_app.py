import streamlit as st
import random
import time
from datetime import datetime

# 🎮 Налаштування сторінки
st.set_page_config(
    page_title="🎮 Розважальний Чат-Бот",
    page_icon="🤖",
    layout="wide"
)

# 📊 Ініціалізація статистики користувача
def init_stats():
    if 'stats' not in st.session_state:
        st.session_state.stats = {
            'games_played': 0,
            'jokes_told': 0,
            'movies_recommended': 0,
            'start_time': datetime.now()
        }

# 🎯 Ігри
def rock_paper_scissors():
    """Гра Камінь-Ножиці-Папір"""
    st.subheader("🎯 Камінь-Ножиці-Папір")
    
    choices = {'🪨': 'Камінь', '✂️': 'Ножиці', '📄': 'Папір'}
    
    col1, col2, col3 = st.columns(3)
    
    user_choice = None
    with col1:
        if st.button("🪨 Камінь", use_container_width=True):
            user_choice = 'Камінь'
    with col2:
        if st.button("✂️ Ножиці", use_container_width=True):
            user_choice = 'Ножиці'
    with col3:
        if st.button("📄 Папір", use_container_width=True):
            user_choice = 'Папір'
    
    if user_choice:
        bot_choice = random.choice(['Камінь', 'Ножиці', 'Папір'])
        
        st.write(f"**Ваш вибір:** {user_choice}")
        st.write(f"**Вибір бота:** {bot_choice}")
        
        # Логіка гри
        if user_choice == bot_choice:
            st.info("🤝 Нічия!")
        elif (user_choice == 'Камінь' and bot_choice == 'Ножиці') or \
             (user_choice == 'Ножиці' and bot_choice == 'Папір') or \
             (user_choice == 'Папір' and bot_choice == 'Камінь'):
            st.success("🎉 Ви виграли!")
        else:
            st.error("😅 Ви програли!")
        
        st.session_state.stats['games_played'] += 1

def guess_number_game():
    """Гра вгадай число"""
    st.subheader("🔢 Вгадай число від 1 до 50")
    
    # Ініціалізація гри
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 50)
        st.session_state.attempts = 0
        st.session_state.game_over = False
    
    if not st.session_state.game_over:
        guess = st.number_input("Введіть число:", min_value=1, max_value=50, step=1)
        
        if st.button("Перевірити"):
            st.session_state.attempts += 1
            target = st.session_state.number_to_guess
            
            if guess == target:
                st.success(f"🎉 Вітаю! Ви вгадали за {st.session_state.attempts} спроб!")
                st.balloons()
                st.session_state.game_over = True
                st.session_state.stats['games_played'] += 1
            elif guess < target:
                st.info("📈 Моє число більше!")
            else:
                st.info("📉 Моє число менше!")
            
            st.write(f"Спроб: {st.session_state.attempts}")
    
    if st.button("🔄 Нова гра"):
        for key in ['number_to_guess', 'attempts', 'game_over']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

def simple_quiz():
    """Проста вікторина"""
    st.subheader("🧠 Вікторина")
    
    questions = [
        {
            "question": "Яка мова програмування має логотип з змією?",
            "options": ["Java", "Python", "JavaScript", "C++"],
            "correct": 1
        },
        {
            "question": "Скільки біт в одному байті?",
            "options": ["4", "8", "16", "32"],
            "correct": 1
        },
        {
            "question": "Що означає WWW?",
            "options": ["World Wide Web", "World Web Wide", "Web Wide World", "Wide World Web"],
            "correct": 0
        }
    ]
    
    if 'quiz_question' not in st.session_state:
        st.session_state.quiz_question = 0
        st.session_state.quiz_score = 0
    
    if st.session_state.quiz_question < len(questions):
        q = questions[st.session_state.quiz_question]
        st.write(f"**Питання {st.session_state.quiz_question + 1}:** {q['question']}")
        
        answer = st.radio("Оберіть відповідь:", q['options'])
        
        if st.button("Відповісти"):
            if q['options'].index(answer) == q['correct']:
                st.success("✅ Правильно!")
                st.session_state.quiz_score += 1
            else:
                st.error(f"❌ Неправильно! Правильна відповідь: {q['options'][q['correct']]}")
            
            st.session_state.quiz_question += 1
            time.sleep(1)
            st.rerun()
    else:
        st.write("### 🏆 Результати вікторини")
        score = st.session_state.quiz_score
        total = len(questions)
        
        if score == total:
            st.success(f"🎉 Відмінно! {score}/{total}")
        elif score >= total // 2:
            st.info(f"👍 Добре! {score}/{total}")
        else:
            st.warning(f"📚 Можна краще! {score}/{total}")
        
        if st.button("🔄 Пройти знову"):
            st.session_state.quiz_question = 0
            st.session_state.quiz_score = 0
            st.session_state.stats['games_played'] += 1
            st.rerun()

# 😄 Анекдоти та жарти
def show_jokes():
    """Показ анекдотів"""
    st.subheader("😄 Анекдоти")
    
    ukrainian_jokes = [
        "Програміст приходить додому:\n- Дорогий, купи хліба, а якщо будуть яйця - візьми десяток.\nПовертається з 10 буханками:\n- Яйця були!",
        
        "Дружина програміста:\n- Сходи в магазин за молоком.\n- Добре.\n(через 3 години)\n- Ти де?\n- У нескінченному циклі біля молочного відділу.",
        
        "Чому програмісти плутають Різдво і Хеловін?\nБо 25 DEC = 31 OCT!",
        
        "Програміст лежить вмираючи:\n- Дорогий, останні слова?\n- Так... Error 404: life not found.",
        
        "Зустрічаються два програмісти:\n- Як справи?\n- Як в UTF-8: іноді один байт, іноді чотири."
    ]
    
    programmer_jokes = [
        "There are only 10 types of people: those who understand binary and those who don't.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "A SQL query goes into a bar, walks up to two tables and asks: 'Can I join you?'"
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🇺🇦 Український анекдот", use_container_width=True):
            joke = random.choice(ukrainian_jokes)
            st.info(joke)
            st.session_state.stats['jokes_told'] += 1
    
    with col2:
        if st.button("🇺🇸 Programming Joke", use_container_width=True):
            joke = random.choice(programmer_jokes)
            st.info(joke)
            st.session_state.stats['jokes_told'] += 1

# 🎬 Рекомендації фільмів
def movie_recommendations():
    """Рекомендації фільмів"""
    st.subheader("🎬 Рекомендації фільмів")
    
    movies = {
        "Комедія": [
            {"title": "Маска", "year": 1994, "rating": "7.9/10"},
            {"title": "Один вдома", "year": 1990, "rating": "8.2/10"},
            {"title": "Брюс Всемогутній", "year": 2003, "rating": "6.8/10"}
        ],
        "Бойовик": [
            {"title": "Матриця", "year": 1999, "rating": "8.7/10"},
            {"title": "Джон Вік", "year": 2014, "rating": "7.4/10"},
            {"title": "Месники", "year": 2012, "rating": "8.0/10"}
        ],
        "Драма": [
            {"title": "Втеча з Шоушенка", "year": 1994, "rating": "9.3/10"},
            {"title": "Форест Гамп", "year": 1994, "rating": "8.8/10"},
            {"title": "Хрещений батько", "year": 1972, "rating": "9.2/10"}
        ]
    }
    
    genre = st.selectbox("Оберіть жанр:", list(movies.keys()))
    
    if st.button("🎲 Рекомендувати фільм"):
        movie = random.choice(movies[genre])
        
        st.success(f"**{movie['title']}** ({movie['year']})")
        st.write(f"⭐ Рейтинг: {movie['rating']}")
        
        st.session_state.stats['movies_recommended'] += 1

# 📊 Статистика
def show_statistics():
    """Показ статистики"""
    st.subheader("📊 Ваша статистика")
    
    stats = st.session_state.stats
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🎮 Ігор зіграно", stats['games_played'])
    
    with col2:
        st.metric("😄 Жартів розказано", stats['jokes_told'])
    
    with col3:
        st.metric("🎬 Фільмів рекомендовано", stats['movies_recommended'])
    
    # Час у додатку
    time_spent = datetime.now() - stats['start_time']
    minutes = int(time_spent.total_seconds() / 60)
    st.write(f"⏱️ Час у чат-боті: {minutes} хвилин")
    
    if st.button("🗑️ Очистити статистику"):
        st.session_state.stats = {
            'games_played': 0,
            'jokes_told': 0,
            'movies_recommended': 0,
            'start_time': datetime.now()
        }
        st.success("Статистика очищена!")
        st.rerun()

# 🎨 Цікаві факти
def interesting_facts():
    """Цікаві факти"""
    st.subheader("🧐 Цікаві факти")
    
    facts = [
        "🐙 Восьминоги мають три серця і блакитну кров!",
        "🍯 Мед - єдиний продукт, який ніколи не псується.",
        "🌙 Місяць віддаляється від Землі на 3.8 см щорічно.",
        "🐧 Пінгвіни можуть стрибати на висоту до 3 метрів!",
        "🧠 Людський мозок споживає 20% енергії тіла.",
        "🌍 День на Венері довший за рік на Венері.",
        "🔥 Блискавка в 5 разів гарячіша за поверхню Сонця.",
        "🐝 Бджоли можуть розпізнавати людські обличчя."
    ]
    
    if st.button("💡 Цікавий факт", use_container_width=True):
        fact = random.choice(facts)
        st.info(fact)

# 🏠 Головна функція
def main():
    """Головна функція додатку"""
    
    # Ініціалізація
    init_stats()
    
    # Заголовок
    st.title("🤖 Розважальний Чат-Бот")
    st.markdown("---")
    
    # Бокова панель з навігацією
    with st.sidebar:
        st.header("🧭 Навігація")
        
        menu_options = [
            "🏠 Головна",
            "🎮 Ігри", 
            "😄 Анекдоти",
            "🎬 Фільми",
            "🧐 Цікаві факти",
            "📊 Статистика"
        ]
        
        choice = st.radio("Оберіть розділ:", menu_options)
        
        st.markdown("---")
        st.write("**Швидка статистика:**")
        st.write(f"🎮 Ігор: {st.session_state.stats['games_played']}")
        st.write(f"😄 Жартів: {st.session_state.stats['jokes_told']}")
        st.write(f"🎬 Фільмів: {st.session_state.stats['movies_recommended']}")
    
    # Основний контент
    if choice == "🏠 Головна":
        st.header("Вітаємо в розважальному чат-боті! 👋")
        
        st.markdown("""
        ### 🎯 Що я можу:
        - 🎮 **Ігри**: Камінь-ножиці-папір, вгадай число, вікторина
        - 😄 **Анекдоти**: Українські та англійські жарти  
        - 🎬 **Фільми**: Рекомендації за жанрами
        - 🧐 **Факти**: Цікаві факти про світ
        - 📊 **Статистика**: Відстеження активності
        
        👈 **Оберіть розділ з бокової панелі!**
        """)
        
        # Швидкі дії
        st.subheader("⚡ Швидкі дії")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎲 Випадковий жарт"):
                jokes = [
                    "Програміст заходить в бар... Ні, це не жарт, він просто п'є після дебагу.",
                    "404: Жарт не знайдено... але ви знайшли цей! 😄"
                ]
                st.info(random.choice(jokes))
                st.session_state.stats['jokes_told'] += 1
        
        with col2:
            if st.button("🎬 Випадковий фільм"):
                movies = ["Матриця", "Форест Гамп", "Маска", "Джон Вік"]
                movie = random.choice(movies)
                st.success(f"Рекомендую: **{movie}**")
                st.session_state.stats['movies_recommended'] += 1
        
        with col3:
            if st.button("💡 Випадковий факт"):
                facts = [
                    "Код 'Hello World' написано мільярди разів!",
                    "Перший комп'ютерний баг був справжнім жуком! 🐛"
                ]
                st.info(random.choice(facts))
    
    elif choice == "🎮 Ігри":
        st.header("🎮 Ігри")
        
        game_tabs = st.tabs(["🎯 Камінь-Ножиці-Папір", "🔢 Вгадай число", "🧠 Вікторина"])
        
        with game_tabs[0]:
            rock_paper_scissors()
        
        with game_tabs[1]:
            guess_number_game()
        
        with game_tabs[2]:
            simple_quiz()
    
    elif choice == "😄 Анекдоти":
        show_jokes()
    
    elif choice == "🎬 Фільми":
        movie_recommendations()
    
    elif choice == "🧐 Цікаві факти":
        interesting_facts()
    
    elif choice == "📊 Статистика":
        show_statistics()
    
    # Футер
    st.markdown("---")
    st.markdown("*Створено з ❤️ для навчання програмування*")

if __name__ == "__main__":
    main()