
inputLineOne = input()
# syntax in input line 1 should be exactly as specified i.e. Starting point: (x, y),
# where x and y could be arbitrary values of choice

lineOneSPlit = inputLineOne.split(' ')

x = int(lineOneSPlit[2][1:(len(lineOneSPlit[2])-1)])
# if we keep the syntax as specified x would be the [2] component if we split the string
# from there we take the length of the string omitting the first and the last symbol
# the result is then caseted to int
y = int(lineOneSPlit[3][0:(len(lineOneSPlit[2])-2)])
# same as for x (ref above)

cipher = input()
# the sequence of the symbols is provided on a separate line as specified

countWarps = 0
# count the occurences of the '~' symbol
for symbol in cipher:
	if symbol == '~':
		countWarps +=1
	if countWarps % 2 == 0: # if we have an even number of '~'s then the imlication of the additional warp action voids
		if symbol == '>':
			x += 1
		elif symbol == '<':
			x -= 1
		elif symbol == '^':
			y -= 1
		elif symbol == 'v':
			y += 1
	else:
		if symbol == '>':
			x -= 1
		elif symbol == '<':
			x += 1
		elif symbol == '^':
			y += 1
		elif symbol == 'v':
			y -= 1
	
# print ('({}, {})'.format(x, y)) # output as formatted string

tupleXY = (x , y) # creating a tuple as the output
print (tupleXY)


