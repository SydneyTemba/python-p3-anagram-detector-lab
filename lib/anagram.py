# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagram = []
        for word in words:
            if sorted(word) == sorted(self.word) and word!= self.word:
                anagram.append(word)
        return anagram