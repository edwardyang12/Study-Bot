word = "two"

def magic(word):
    try:
        intN = int(word)
        return intN
    except:
        bigList = ["zero","one","two","three","four","five","six","seven", "eight", "nine","ten"]
        for i in range(len(bigList)):
            if(bigList[i]==word):
                return i
        return "number not found"

#print(type(magic(word)))
