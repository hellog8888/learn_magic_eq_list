class Morph:
    def __init__(self, *args):
        self.words_list = [x.strip(' ,.!?:;').lower() for x in args]

    def add_word(self, word):
        w = word.lower()
        if w not in self.words_list:
            self.words_list.append(w)

    def get_words(self):
        return (self.words_list)

    def __eq__(self, other):
        return other.lower() in self.words_list

dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

text = input()

print(sum(word.strip(' ,.!?:;').lower() == morph for word in text.split() for morph in dict_words))

