sentence = input("What is your sentence: ")
word = input("What word do you want to remove: ")

newSentence = ""
#Approach 1
newSentence = sentence.replace(word,"")
print("Sentence is: "+newSentence)
