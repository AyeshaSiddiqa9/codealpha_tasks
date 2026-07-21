import random
print("=== Welcome to Hangman ===")
print("Category: Smartphone Brands")
#list of predefined smartphone brands
my_list=["Samsung","Apple","Xiaomi","Realme","Vivo"]
#A random word is selected from my_list
word=random.choice(my_list).lower()
blanks=[]
for i in range(len(word)):
    blanks.append("_")#creates blank space holders for the words
guessed_letters=[]
wrong_guesses=0
max_wrong_guesses=6 #6chances are given to guess the correct word
print(f"You have {max_wrong_guesses} chances to guess the word.")
print(f"The word has {len(word)} letters")
to_be_guessed=" ".join(blanks)
print(to_be_guessed)
while wrong_guesses<max_wrong_guesses:
    single_letter=input().lower()#user enters a letter
    #checks if input is valid
    if not single_letter.isalpha() or len(single_letter)!=1:
        print("Invalid input: Please enter single alphabet")
        continue
    #checks if the input has already been entered or not
    if single_letter in guessed_letters:
        print("This letter has already been entered")
    elif single_letter in word:
        guessed_letters.append(single_letter)
        for i in range(len(word)):
            if single_letter==word[i]:
                blanks[i]=single_letter
    #if the input is not matched with the any letter in the word                
    else:
        guessed_letters.append(single_letter)
        wrong_guesses+=1
        remaining_chances=max_wrong_guesses-wrong_guesses
        print("Wrong guess!")
        print(f"Remaining chances: {remaining_chances}")
    result=" ".join(blanks)
    print(result)
    #if player wins
    if "_" not in blanks:
        print("Congarulations! you won")
        break
#if player losses    
if wrong_guesses == max_wrong_guesses::
    print("You lost!")
    print(f"The word was: {word}")
            
        
            
    
