#program to check if a word contains a vowel if yes then print that vowel
word="my name is souvik chakraborty"

vowels_list=['a','e','i','o','u']
vowel_count=0
for letter in word:
    if letter in vowels_list:
        print("yes the letter is ",letter," at index ",word.index(letter))
        vowel_count=vowel_count+1
    else:
        print("not a vowel")
print("the total no of vowels in the word are ",vowel_count)
        
