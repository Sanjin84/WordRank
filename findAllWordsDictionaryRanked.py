trump = '''
1. Arab-Americans cheered the attacks on 9/11. Trump repeatedly claimed
that on 11 September, 2001, there were thousands of Arab-Americans
celebrating in New Jersey after two planes flew into the Twin Towers. He
says such public demonstrations "tell you something" about Muslims
living in the US. However, there are no media reports to back up the
claim. 2. There should be surveillance on US mosques. Trump believes
Muslims should be tracked by law enforcement as a counterterrorism
initiative. He has walked back some comments about keeping a database on
all American Muslims, but says he doesn't care if watching mosques is
seen as "politically incorrect".
'''
trump = trump.split()
print('what word would you like to search for?')
length = len(trump)
word_counter = {}

for x in range(0,length):
    keyword = trump[x]
    word_counter[keyword] = 0
    for i in range(0,length):
        if keyword == trump[i]:
            word_counter[keyword] += 1
    print(keyword +' repeats ' + str(word_counter[keyword]) + ' times') 

popular_words = sorted(word_counter, key = word_counter.get, reverse = True )


for i in range(0,length):
    print(popular_words[i] + ' : ' + str(word_counter[popular_words[i]]))

