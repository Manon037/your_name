import requests
import json
import random
import csv

# 음악 자판기
def music_vending_machine():
    drinks = {
        "Chilsung Cider": ["青と夏 (Mrs. GREEN APPLE)", "怪獣の花唄 (VAUNDY)", "虹を編めたら (fhána)", "Universe (Official髭男dism)", "Grand Escape (RADWIMPS feat. 三浦透子)"],
        "Cantata Coffee": ["merry-go-round (優里)", "たぶん (YOASOBI)", "フィナーレ (eill)", "W/X/Y (たにゆうき)", "NEKO (DISH//)"],
        "Oronamin Seed": ["沈丁花 (DISH//)", "Mela! (緑黄色社会)", "心海 (Eve)", "Souvenir (BUMP OF CHICKEN)", "シュガーソングとビターステップ (UNISON SQUARE GARDEN)"],
        "Strawberry Milk": ["好すきだから｡ (『ユイカ』)", "LADY (米津玄師)", "好きだ (YOASOBI)", "ハルノヒ (あいみょん)", "トリセツ (西野カナ)"],
        "Sol's Eye": ["ロメオ (LIPxLIP)", "DAYS of DASH (鈴木このみ)", "ギターと孤独と蒼い惑星 (結束バンド)", "チューリングラブ (ナナヲアカリ)", "ヒミツ恋ゴコロ (CHiCO with HoneyWorks)"]
    }
    
    print("Welcome to the Music Vending Machine!")
    print("Here are five drinks:")
    for index, drink in enumerate(drinks.keys(), start=1):
        print(f"{index}. {drink}")
    
    while True:
        chosen_drink = input("Enter the number of the drink you like (1-5) or 'r' to refresh: ")
        
        if chosen_drink.lower() == 'r':
            # Refresh drinks
            print("Refreshing drinks...")
            for drink_list in drinks.values():
                random.shuffle(drink_list)
            print("Drinks refreshed!")
        elif chosen_drink.isdigit():
            drink_index = int(chosen_drink)
            if 1 <= drink_index <= len(drinks):
                selected_drink = list(drinks.keys())[drink_index - 1]
                print(f"You chose {selected_drink}. Now recommending a song...")
                recommended_song = random.choice(drinks[selected_drink])
                print(f"Recommended song: {recommended_song}")
                break
            else:
                print("Invalid drink number. Please try again.")
        else:
            print("Invalid input. Please enter a number or 'r' to refresh.")

# 오늘의 날씨
# Your OpenWeatherMap API key
apiKey = "9f86204ec43f8634cddd428b5049c79b"

# Define songs for each weather type in Japanese
songs = {
    "Clear": ["ふわり春（あさぎーにょ）", "ロマンチシズム(Mrs. GREEN APPLE)", "もう少しだけ(YOASOBI)", "葵(あいみょん)", "サラバ(SEKAI NO OWARI)"],
    "Mist": ["LADY(米津玄師)", "奏（スキマスイッチ）", "Answer(幾田りら)", "喜劇（星野源）", "レオ（優里）"],
    "Clouds": ["LADY(米津玄師)", "奏（スキマスイッチ）", "Answer(幾田りら)", "喜劇（星野源）", "レオ（優里）"],
    "Rain": ["ランデヴー(shy taupe)", "ガリレオは恋をする（優里）", "虹（菅田将暉）", "水平線(back number)", "森の小さなレストラン（手嶌葵）"],
    "Drizzle": ["ランデヴー(shy taupe)", "ガリレオは恋をする（優里）", "虹（菅田将暉）", "水平線(back number)", "森の小さなレストラン（手嶌葵）"],
    "Snow": ["クリスマスソング(back number)", "WISH(嵐)", "粉雪(レミオロメン)", "ヒロイン(back number)", "白い恋人達（桑田佳祐）"],
    "Thunderstorm": ["inferno(Mrs. GREEN APPLE)", "ピーターパン（優里）", "Cry Baby(Official髭男dism)", "スターマイン(Da-iCE)", "サムライハート(SPYAIR)"]
}

def fetch_weather(city):
    lang = 'en'  # Language preference
    units = 'metric'  # Temperature units preference (metric for Celsius)
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"
    
    result = requests.get(api)
    if result.status_code == 200:
        weather_data = json.loads(result.text)
        return weather_data
    else:
        return None

def recommend_song(weather):
    if weather in songs:
        return random.choice(songs[weather])
    else:
        return "No recommendation"

def today_weather():
    city = input("Enter your city: ")
    weather_data = fetch_weather(city)
    if weather_data:
        name = weather_data['name']
        lon = weather_data['coord']['lon']
        lat = weather_data['coord']['lat']
        weather = weather_data['weather'][0]['main']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        
        print(f"Location: {name}")
        print(f"Longitude: {lon}, Latitude: {lat}")
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        
        recommended_song = recommend_song(weather)
        print(f"We recommend a song that matches the weather: {recommended_song}")
    else:
        print("Failed to fetch weather data.")

# 슬롯 머신
def recommend_song_from_number(number):
    # Logic for recommending songs based on the number
    songs = {}
    with open('/Users/hwangjeong-a/Documents/python/lect/your_name/data/Slot_Machine_List.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader, start=1):
            songs[idx] = row[0]

    return songs.get(number, "No song recommendation for this number")

def slot_machine():
    print("Welcome to the Slot Machine!")
    print("This slot machine generates random numbers from 1 to 30.")
    print("Let's start!")

    while True:
        input("Press Enter to spin the slot machine...")
        generated_number = random.randint(1, 30)  # Generate a random number between 1 and 30
        print(f"Your number is: {generated_number}")

        recommended_song = recommend_song_from_number(generated_number)
        print(f"We recommend a song that matches the number: {recommended_song}")

        refresh = input("Type 'r' to spin again or any key to exit: ")
        if refresh.lower() != 'r':
            print("Thank you for playing the Slot Machine!")
            break

# 일본 음악 퀴즈
lyrics_dict = {}

def load_quiz_data():
    with open('/Users/hwangjeong-a/Documents/python/lect/your_name/data/Japanese_Music_Quiz_List.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            song_name = row[0]
            korean_lyrics = row[1]
            japanese_hint = row[2]
            lyrics_dict[song_name] = {"Korean": korean_lyrics, "Japanese_hint": japanese_hint}

def get_random_song():
    song_keys = list(lyrics_dict.keys())
    return random.choice(song_keys)

def generate_options(correct_song):
    options = [correct_song]
    while len(options) < 4:
        random_song = get_random_song()
        if random_song not in options:
            options.append(random_song)
    random.shuffle(options)
    return options

def show_lyrics(song):
    print(f"Korean Translated Lyrics: {lyrics_dict[song]['Korean']}")
    return lyrics_dict[song]["Japanese_hint"]

def japanese_music_quiz():
    print("Welcome to the Japanese Music Quiz!")
    print("Try to guess the Japanese music genre based on their Korean translated lyrics.")
    load_quiz_data()

    while True:
        print("Press 's' to start with a random song or 'q' to quit.")
        choice = input("Enter your choice: ")

        if choice.lower() == 's':
            chosen_song = get_random_song()
            options = generate_options(chosen_song)

            print(f"Korean Translated Lyrics: {lyrics_dict[chosen_song]['Korean']}")
            print("Options:")
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")

            hint_shown = False
            while True:
                answer = input("Enter the number corresponding to your choice (1-4): ")

                if answer.isdigit() and 1 <= int(answer) <= 4:
                    guessed_song = options[int(answer) - 1]
                    if guessed_song == chosen_song:
                        print("Correct! You guessed the song.")
                        break
                    else:
                        print("Incorrect! Try again.")
                else:
                    print("Invalid input. Enter a number between 1 and 4.")

        elif choice.lower() == 'q':
            print("Thanks for playing the Japanese Music Quiz!")
            break
        else:
            print("Invalid choice. Please enter 's' to start or 'q' to quit.")
            japanese_music_quiz()

    
# 메인
def main():
    print("Welcome to the Japanese Music Recommendation Program!")
    while True:
        print("[Select an option]")
        print("1. Music Vending Machine")
        print("2. Today's Weather")
        print("3. Slot Machine")
        print("4. Japanese Music Quiz")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            music_vending_machine()
        elif choice == "2":
            today_weather()
        elif choice == "3":
            slot_machine()
        elif choice == "4":
            japanese_music_quiz()
        else:
            print("Invalid choice. Please select again.")
        
        another_round = input("Do you want to continue? (y/n): ")
        if another_round.lower() != 'y':
            print("Thank you for using the Japanese Music Recommendation Program. Goodbye!")
            break

if __name__ == "__main__":
    main()