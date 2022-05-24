import random
from stat import FILE_ATTRIBUTE_SPARSE_FILE


words = ['Coffee','Cancer','Zebra','microwave','nightclub','nowadays','ovary','oxygen','pneumonia','quixotic','whomever','yachtsman','kilobyte','strength','flopping','stymied','zombie']
lifes = 10

intro = '''
Hey this is Hangman game
    You have to guess the  correct word in 5 lifes|

'''
word = random.choice(words).lower()
noOfDash = list('_'*len(word))



def find(ltr,word):
    itrPlace = []
    x = 0
    if ltr in word:
        for i in word:
            if i == ltr:
                itrPlace.append(x)
            x +=1
        return itrPlace
    else:
        return(None)
        
def dash(list,ltr):
    for x in range(len(noOfDash)):
        if x in list:
            noOfDash[x]=ltr
    return noOfDash

def check():
    if noOfDash == list(word):
        return True
    else:
        return False      
        
            

    
i=0
print(noOfDash)
while i < lifes:
    letter = input("Enter the letter: ")
    a = find(letter,word)
    if a == None:
        i += 1
        print("Oops wrong word\nLifes left = {}".format(lifes-i))
        continue
    else:
        dash(a,letter)
        print(noOfDash)
        if check()== True:
            print("you won")
            break


print('word was ',word)
    