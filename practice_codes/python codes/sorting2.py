n="merry and you"
words=n.split() #["merry","and","you"]
final=[]
for  w in words: # visit each word 1 at a time to do sort so loop
    sort=''.join(sorted(w)) #sorted(w) → sorts the letters → ['e','m','r','r','y']
                            # ''.join(...) → glues them with no space → "emrry"  
    final.append(sort) 
    result=' '.join(final) #"emrry" + " " + "adn" + " " + "ouy" → "emrry adn ouy"
print(result)

# output
emrry adn ouy