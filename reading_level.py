f_open = open("ExistentialismEssay1ErinKiffney.txt","r") #opening a file
essay = f_open.read() #reading a file
f_open.close() #closing a file

words = essay.split() #splitting words into a list
print "Number of words in text document is" 
print len(words) #printing number of words

sentences = essay.split(".")
print "Number of sentences in text document is"
print len(sentences)

syllables = 0
vowels = "aeiou"
for char in essay:
	if char in vowels:
		syllables += 1
print "Number of syllables in text document is"
print syllables

level = ((0.39*len(words)/len(sentences)) + (11.8* syllables/len(words)) - 15.59)
print "Grade level of text file:"
print level