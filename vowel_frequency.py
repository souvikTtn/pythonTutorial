#program to count frequency of vowel in a given word
word_input=input("enter the word to perform the check :: ")
print(word_input)

vowels=['a','e','i','o','u']

my_dict={}
for i in vowels:
    my_dict[i]=0

for i in word_input:
    if i in vowels:
            my_dict[i]+=1

for k,v in my_dict.items():
    if v!=0:
        print(k," has appeared ",v," time(s)" )
