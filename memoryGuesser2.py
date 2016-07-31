import random, time, sys, os


wordList = ['book','cook','table','car','pen','stand',
            'carpet','computer','soap', 'ball','van','tub',
'bat','bed','book','boy','bun','can','cake','cap','cat',
'cow','cub','cup','dad','day','dog','doll','dust','fan','feet',
'girl','gun','hall','hat','hen','jar','kite','man','map','men',
'mom','pan','pet','pie','pig','pot','rat','son','sun','toe',
'marshmallow','steak','butterfly', 'fire','chocolate','banana',
'bunny','bubbles','rock','panda','kitten','meerkat', 'crazy',
'dinosaur', 'coffee']
random.shuffle(wordList)

points = 0
print("how many words do you want to test yourself on")
testLength = int(input()) # how many words do tou want to test?
print("how many seconds per word")
timePerWord = int(input()) # how much time do you want per word
print("These are the words that you have to memorise:")


def spaceOut():
   for i in range(0,14):
      print('*')


for i in range(0,testLength):
   spaceOut()
   print(wordList[i])
   spaceOut()
   time.sleep(timePerWord)

print("now its your turn to guess all the words in the correct sequence")   
for i in range(0,testLength):
    yourGuess = input()
    if yourGuess ==wordList[i]:
        points = points + 1
        print("Correct!!")
    else:
       print("Nope, the answer is " + wordList[i])
         
print("your scored " + str(points) + " out of " + str(testLength))
time.sleep(6)

   




   
