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
counter = 0 
trump = trump.split()
nrep = []
length = len(trump)
for i in range(0,length):
    if trump[i] not in nrep:
        nrep.append(trump[i])
print(nrep)
print(len(nrep))
    
