with open('/Users/hwangjeong-a/Documents/python/lect/your_name/data/Japanese_Music_Quiz_List.csv', 'r', encoding='utf-8') as file:
    for line in file:
        print(repr(line))  # This will display the representation of each line, showing tabs as '\t'