import io;

def printFile():
    filestr= open('words.txt', 'r')
    containt = filestr.read()
    listFile = containt.split(" ")
    sepWord = []
    temp = input("enter the char = ")
    for word in listFile:
        if(word.startswith(temp)):
            sepWord.append(word)
    print(sepWord)
    filestr.close()
printFile()






















