word = "eighty two"

def magic(word):
    try:
        intN = int(word)
        return intN
    except:
        temp = 0
        found = False
        bigList = ["zero","one","two","three","four","five","six","seven", "eight", "nine","ten",
                   "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
        tensList = ["twenty" , "thirty", "forty", "fifty", "sixty"]
        for i in range(len(tensList)):
            if(word[:len(tensList[i])] == tensList[i]):
                temp = temp + (i+2)*10
                word = word[len(tensList[i])+1:]
                found = True
        for i in range(len(bigList)):
            if(bigList[i] == word):
                temp = temp + i
                found = True
        if(found):
            return temp
        else:
            return "number not found"

print(magic(word))
