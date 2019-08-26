
def words():
    wordCount = 1
    wordLength = 0
    sameWords = False
    userWords = []
    word = ''
    
    dataBase = ['Good Morning', 'All of the Lights', 'Chain Smoker', 'gud Morneng', 'I like to eat beans']
    userSearch  = "hood mOrning".lower()
    
    for char in userSearch:
        word = word.join(char)
        wordLength+=1
        print(word)
        if char == ' ':
            userWords.append('Guac')
            wordCount +=1
            print(userWords)
            
    for i in dataBase:
        dataWords = []
        result = i
        resultWordCount = 1
        
        for n  in result:
            if  n == ' ':
                resultWordCount +=1   
    
    wordCount +=1
    resultWordCount +=1 
    
def deletion():
    charDel = 0
    charDel +=1
    
def insertion():
    charIns = 0
    
def substitution():
    charSub = 0
        
    
    