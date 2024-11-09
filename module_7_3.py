class  WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words (self, *file_names, word):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = file.read().lower()
                    for p in file_names.punctuation:
                        if p in line:
                            line = line.replace(p, '')
                            words = line.split()
                            all_words = file_names.append(), words.append()
                            line = line.lower()
                            punctuation = [',', '.', '=', '!', '?', ';', ':']
                            for punct in punctuation:
                                line = line.replace(punct, '')
                                line = line.replace(' - ', ' ')
                                words.extend(line.split())
                                all_words[file_name] = words
                    return all_words

    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1

        return places
    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count

        return counters
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего




finder2 = WordsFinder('test_file.txt')
#print(finder2.get_all_words()) # Все слова
#print(finder2.find('TEXT')) # 3 слово по счёту
#print(finder2.count('teXT')) # 4 слова teXT в тексте всего
