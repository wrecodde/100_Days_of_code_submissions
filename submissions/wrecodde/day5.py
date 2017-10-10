# Count Vowels
# count the number of vowels in a given string


from collections import Counter


text = input("say the word: ").lower()
# force to lowercase


count = Counter(text)
# count all chars in text

a = count["a"]
e = count["e"]
i = count["i"]
o = count["o"]
u = count["u"]

no_of_vowels = a + e + i + o + u

print(f"total no of vowels: {no_of_vowels}")
print(f"a: {a}")
print(f"e: {e}")
print(f"i: {i}")
print(f"o: {o}")
print(f"u: {u}")
