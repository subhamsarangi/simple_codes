def drawLine(tick_len, tick_label=''):
	line = '-'*tick_len
	if tick_label:
		line+=' '+ tick_label
	print(line)

def drawInterval(cent_len):
	if cent_len >0 :
		drawInterval(cent_len-1)	#RECUSIVELY TOP TICKS
		drawLine(cent_len)	#CENTER TICK
		drawInterval(cent_len-1)	#RECURSIVELY BOTTOM TICKS

def drawRuler (num_inch, maj_len):
	drawLine (maj_len, '0')		#INCH 0 LINE
	for j in range(1,1+num_inch):
		drawInterval (maj_len-1)	#CALL function to draw INTERIOR TICKS
		drawLine (maj_len, str(j))	#INCH j LINE

print('Enter the size of the Ruler in inches and the major tick length, separated by spaces: ')
num, maj=input().split(' ')		#tuple packing
drawRuler(int(num), int(maj))	#unpacking and subsequent function call
