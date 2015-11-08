import random
import sys
diff = input('Difficulty (1-5)? ')
myList = []
f = open('enable1.txt', 'r')
if diff == '1':
	n = random.randint(4,5)
	for i in f:
		if len(i)-1 == n:
			myList.append(i.rstrip())
elif diff == '2':
	n = random.randint(6,8)
	for i in f:
		if len(i)-1 == n:
			myList.append(i.rstrip())
elif diff == '3':
	n = random.randint(9,10)
	for i in f:
		if len(i)-1 == n:
			myList.append(i.rstrip())
elif diff == '4':
	n = random.randint(11,12)
	for i in f:
		if len(i)-1 == n:
			myList.append(i.rstrip())
elif diff == '5':
	n = random.randint(13,15)
	for i in f:
		if len(i)-1 == n:
			myList.append(i.rstrip())
wordList = random.sample(myList, random.randint(5,15))
password = random.choice(wordList)
count = 4
print(wordList)
while(count > 0):
	print('Guess? (', count, ' left)')
	guess = input()
	corPos = 0
	charCount = 0
	for i in guess:
		if(i == password[charCount]):
			corPos += 1
		charCount += 1
	print(corPos, '/', n, ' correct')
	if(corPos == n):
		print('You win!')
		sys.exit()
	count -= 1
