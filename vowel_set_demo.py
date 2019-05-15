#checking vowels in a word using set

word=input("enter the word to check for vowels :: ")

vowels=set("aeiou")
found=set(word).intersection(vowels)

for i in found:
    print(i)
