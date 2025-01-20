import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    text = re.sub(r'[,\.\=\!\?\;\:\-\s]', ' ', text)
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        found_positions = {}
        for file_name, words in self.get_all_words().items():
            try:
                index = words.index(word) + 1  # +1 to start from 1
                found_positions[file_name] = index
            except ValueError:
                pass
        return found_positions


    def count(self, word):
        word = word.lower()
        word_counts = {}
        for file_name, words in self.get_all_words().items():
             count = words.count(word)
             if count > 0 :
                 word_counts[file_name] = count
        return word_counts


# Пример использования:

# Создаем тестовый файл
with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("It's a text for task Найти везде,\n")
    f.write("Используйте его для самопроверки.\n")
    f.write("Успехов в решении задачи!\n")
    f.write("text text text text")


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))