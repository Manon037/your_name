import requests
import json
import random
import csv
import time

# 음악 자판기
def music_vending_machine():
    drinks = {
        "칠성사이다": ["青と夏 (Mrs. GREEN APPLE)", "怪獣の花唄 (VAUNDY)", "虹を編めたら (fhána)", "Universe (Official髭男dism)", "Grand Escape (RADWIMPS feat. 三浦透子)"],
        "칸타타 커피": ["merry-go-round (優里)", "たぶん (YOASOBI)", "フィナーレ (eill)", "W/X/Y (たにゆうき)", "NEKO (DISH//)"],
        "오로나민씨": ["沈丁花 (DISH//)", "Mela! (緑黄色社会)", "心海 (Eve)", "Souvenir (BUMP OF CHICKEN)", "シュガーソングとビターステップ (UNISON SQUARE GARDEN)"],
        "딸기우유": ["好すきだから｡ (『ユイカ』)", "LADY (米津玄師)", "好きだ (YOASOBI)", "ハルノヒ (あいみょん)", "トリセツ (西野カナ)"],
        "솔의 눈": ["ロメオ (LIPxLIP)", "DAYS of DASH (鈴木このみ)", "ギターと孤独と蒼い惑星 (結束バンド)", "チューリングラブ (ナナヲアカリ)", "ヒミツ恋ゴコロ (CHiCO with HoneyWorks)"]
    }
    
    print("------------------------------------------------------------------------------------------")
    print("음악 자판기를 선택해주셔서 감사합니다!")
    print("------------------------------------------------------------------------------------------")
    print("여기 5종류의 음료가 있습니다:")
    print("                        ")
    for index, drink in enumerate(drinks.keys(), start=1):
        print(f"{index}. {drink}")
    
    while True:
        print("                        ")
        chosen_drink = input("마음에 드는 음료의 번호를 입력해주세요! (1-5): ")
        
        if chosen_drink.isdigit():
            drink_index = int(chosen_drink)
            if 1 <= drink_index <= len(drinks):
                selected_drink = list(drinks.keys())[drink_index - 1]
                print("------------------------------------------------------------------------------------------")
                print(f"{selected_drink}을 고르셨군요! 어울리는 음악을 추천 중입니다...")
                time.sleep(time_delay)
                recommended_song = random.choice(drinks[selected_drink])
                print(f"어울리는 음악: [{recommended_song}]")
                break
            else:
                print("해당 번호의 음료는 품절되었습니다. (1-5) 사이의 번호로 다시 입력해주세요.")
        else:
            print("Invalid input. Please enter a number or 'r' to refresh.")


# 오늘의 날씨
apiKey = "9f86204ec43f8634cddd428b5049c79b"
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
    lang = 'en' 
    units = 'metric' 
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
    print("------------------------------------------------------------------------------------------")
    print("오늘의 날씨를 선택해주셔서 감사합니다!")
    print("------------------------------------------------------------------------------------------")
    city = input("현재 계신 도시를 영문으로 입력해주세요: ")
    weather_data = fetch_weather(city)
    if weather_data:
        name = weather_data['name']
        lon = weather_data['coord']['lon']
        lat = weather_data['coord']['lat']
        weather = weather_data['weather'][0]['main']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        
        print(f"위치: {name}")
        print(f"현재 날씨: {weather}")
        print(f"온도: {temperature}°C")
        print(f"습도: {humidity}%")
        
        print("------------------------------------------------------------------------------------------")
        time.sleep(time_delay)
        print(f"{city}에 계시군요! {city}의 현재 날씨인 {weather}와 어울리는 음악을 추천 중입니다...")
        time.sleep(time_delay)
        recommended_song = recommend_song(weather)
        print(f"어울리는 음악: [{recommended_song}]")
    else:
        print("날씨 정보를 불러오는 데 실패했습니다.")


# 슬롯 머신
def recommend_song_from_number(number):
    songs = {}
    with open('/Users/hwangjeong-a/Documents/python/lect/your_name/data/Slot_Machine_List.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader, start=1):
            songs[idx] = row[0]

    return songs.get(number, "No song recommendation for this number")

def slot_machine():
    print("------------------------------------------------------------------------------------------")
    print("슬롯 머신을 선택해주셔서 감사합니다!")

    while True:
        print("------------------------------------------------------------------------------------------")
        input("슬롯을 돌리시려면 Enter를 눌러주세요...")
        time.sleep(time_delay)
        generated_number = random.randint(1, 30)
        print(f"슬롯 번호: ({generated_number})")

        recommended_song = recommend_song_from_number(generated_number)
        print(f"해당 번호의 곡을 추천드립니다: [{recommended_song}]")

        refresh = input("다시 돌리고 싶으시면 'r'을 입력해주세요! 종료를 원하시면 아무 키를 눌러주세요: ")
        if refresh.lower() != 'r':
            print("------------------------------------------------------------------------------------------")
            print("슬롯 머신을 이용해주셔서 감사합니다!")
            print("------------------------------------------------------------------------------------------")
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
    print(f"한국어 번역 가사: {lyrics_dict[song]['Korean']}")
    return lyrics_dict[song]["Japanese_hint"]

def japanese_music_quiz():
    print("------------------------------------------------------------------------------------------")
    print("일본 음악 퀴즈를 선택해주셔서 감사합니다!")
    print("------------------------------------------------------------------------------------------")
    print("한국어 번역 가사를 보고, 일본 곡의 제목을 맞춰주세요! 'h'를 누르시면 힌트로 일본어 발음을 보여드립니다.")
    load_quiz_data()

    while True:
        print("시작하시려면 's'를 눌러주세요.")
        choice = input("입력: ")

        if choice.lower() == 's':
            chosen_song = get_random_song()
            options = generate_options(chosen_song)
            
            print("                        ")
            print("------------------------------------------------------------------------------------------")
            print(f"[한국어 번역 가사: {lyrics_dict[chosen_song]['Korean']}]")
            print("------------------------------------------------------------------------------------------")
            print("다음 중 제시된 가사의 곡을 선택해주세요:")
            print("                        ")
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")

            hint_shown = False
            while True:
                print("                        ")
                answer = input("번호를 선택하여 정답을 입력하세요 1-4 (힌트는 h): ")
        
                if answer.lower() == 'h':
                   print("일본어 가사 힌트: ", show_lyrics(chosen_song))
                   continue

                if answer.isdigit() and 1 <= int(answer) <= 4:
                   guessed_song = options[int(answer) - 1]
                   if guessed_song == chosen_song:
                       print("정답! 축하합니다!")
                       play_again = input("게임을 다시 하시겠습니까? (Y/N): ")
                       if play_again.lower() == 'y':
                          break 
                       else:
                           print("일본 음악 퀴즈를 이용해주셔서 감사합니다!!")
                           return 
                   else:
                       print("                        ")
                       print("땡! 다시 시도해보세요.")
                       
                else:
                    print("                        ")
                    print("해당 번호는 제공되어있지 않습니다. 1부터 4 사이의 번호를 입력해주세요")

    
# 메인
def main():
    print("==========================================================================================")
    print("Japanese Music Recommendation Program(JMP)를 선택해주셔서 감사합니다!")
    while True:
        print("==========================================================================================")
        print("[옵션을 선택해주세요]")
        print("1. 음악 자판기")
        print("2. 오늘의 날씨")
        print("3. 슬롯 머신")
        print("4. 일본 음악 퀴즈")
        choice = input("번호를 입력해주세요! (1-4): ")
        
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
        
        another_round = input("계속하시겠습니까? (y/n): ")
        if another_round.lower() != 'y':
            print("==========================================================================================")
            print("Japanese Music Recommendation Program(JMP)를 이용해주셔서 감사합니다!")
            print("==========================================================================================")
            break

time_delay = 2

if __name__ == "__main__":
    main()