table = 'ivan evnh inav mvvn qrit' # input the required data as a string
word = 'ivan'
wordCount = 0
tableSplit = table.split(' ')

# check right to left
for s in tableSplit:
	if word in s:
		wordCount += 1

# check left to right
contentLeftRigt = []
for w in tableSplit:
	contentLeftRigt.append(w[::-1])

for s in contentLeftRigt:
	if word in s:
		wordCount += 1

# check top to bottom
contentTopBottom =[]
for i in range(0, len(tableSplit[0])):
	ch = []
	for w in tableSplit:
		ch.append(w[i:i+1:])
	x = ''.join(ch)
	contentTopBottom.append(x)

for s in contentTopBottom:
	if word in s:
		wordCount += 1

# check bottom to top
contentBottomTop =[]
for w in contentTopBottom:
	contentBottomTop.append(w[::-1])
for s in contentBottomTop:
	if word in s:
		wordCount += 1

# check diagonalLeftToRight
chars = []
diagLR = []
for i in range(0,1):
	chars.append(tableSplit[i-i][i-i])
	chars.append(tableSplit[i+1-i][i+1-i])
	chars.append(tableSplit[i+2-i][i+2-i])
	chars.append(tableSplit[i+3-i][i+3-i])
	temp = ''.join(chars)
	chars.clear()
	diagLR.append(temp)

for s in diagLR:
	if word in s:
		wordCount += 1

# check diagonalRightToLeft
charsRL = []
diagRL = []
for i in range(0, 1 ):
	charsRL.append(tableSplit[i-i][i-i-1])
	charsRL.append(tableSplit[i+1-i][i+1-i-3])
	charsRL.append(tableSplit[i+2-i][i+2-i-5])
	charsRL.append(tableSplit[i+3-i][i+3-i-7])
	temp = ''.join(charsRL)
	charsRL.clear()
	diagRL.append(temp)
for s in diagRL:
	if word in s:
		wordCount += 1

# final result
print(wordCount) 