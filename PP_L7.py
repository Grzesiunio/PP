# squares = []
# for x in range(10):
#     squares.append(x ** 2)
#
# print(squares)
#
# squares = list(map(lambda x: x ** 2, range(10)))
# print(squares)
#
# squares = [x**2 for x in range(10)]
# print(squares)
import functools
from collections import Counter

tab = [1, 2, 3, 4]


def increment(iterable):
    iterable = [x + 1 for x in iterable]
    return iterable


print(increment(tab))
tab = [1, 2, 3, 4]


def iloczyn(ciag_liczb):
    return functools.reduce(lambda x, y: x * y, ciag_liczb)


print(iloczyn(tab))


def palindrom(text):
    final_text = ''
    text = text.lower()
    if text.isalpha():
        print(text)
    else:
        for char in text:
            if char.isalpha():
                final_text = final_text + char
    if final_text == final_text[::-1]:
        return True
    else:
        return False


print(palindrom("Tolo ma samolot"))


def tokenize(text):
    final_text = ''
    znaki = [",", ".", ":", ";", "!", "?", "-", "[", "]"]
    # usuwanie znakow interpunkcyjnych
    for x in text:
        if x in znaki:
            text = text.replace(x, "")
    text = text.lower()
    text = text.split()
    return text


print(tokenize("To be, or not to be - that is the question [...]"))


def remove_stop_words(text):
    with open('pl.stopwords.txt', encoding='UTF-8') as input_file:
        stop_words = input_file.read()
        final_text = ''
        # usuwanie znakow interpunkcyjnych
        for x in text:
            for y in x.split(" "):
                if y not in stop_words and len(y) >= 2:
                    final_text = final_text + y + ' '

        return final_text


print("Zadanie 5")
tab_zad5 = ["Siema a fajnie by było aby gdyby że coś się stało"]
print(remove_stop_words(tab_zad5))
print("Zadanie 6")


def count_most_frequent(text, n):
    text = tokenize(text)
    text = remove_stop_words(text)
    text = text.split()
    cnt = Counter()
    for word in text:
        cnt[word] += 1
    print(cnt.most_common(n))


with open('trurl.txt', encoding='UTF-8') as input_file:
    text_zad6 = input_file.read()
    count_most_frequent(text_zad6, 20)

print("Zadanie 7")

chars_of_anagram = []


def anagrams(s1, s2):
    # s1 = sorted(s1.lower())
    # s2 = sorted(s2.lower())
    for x in range(len(s2)):
        if s2[x] not in chars_of_anagram:
            return False
    return True


def longest_anagrams(text):
    with open('unixdict.txt', encoding='UTF-8') as input_file:
        najdluzszy = 0
        anagrams_list = []
        for x in range(len(text)):
            chars_of_anagram.append(text[x])
        for line in input_file:
            word = line.strip()
            if anagrams(text, word):
                anagrams_list.append(word)
    for x in anagrams_list:
        if len(x) > najdluzszy:
            najdluzszy = len(x)
    for x in anagrams_list:
        if len(x) == najdluzszy:
            print(x)


print("Najdluzsze anagramy to: ")
longest_anagrams("talerz")
