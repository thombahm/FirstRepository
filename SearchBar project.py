
def words():
    wordCount = 1
    wordLength = 0
    sameWords = False
    userWords = []
    word = ''
    
    dataBase = ['Good Morning', 'All of the Lights', 'Chain Smoker', 'gud Morneng', 'I like to eat beans']
    userSearch  = "hood mOrning".lower()
    
    ''' any code that needs to filter through each character that the user has typed in'''
    for char in userSearch:
        word = word.join(char)
        wordLength+=1
        print(word)
        
        ''' used to figure out how many words in the users text'''
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
        
    
    
