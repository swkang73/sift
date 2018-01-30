import csv
import numpy as np
import matplotlib.pyplot as plt

# project milestone 2
# this program shows raw mass spec of healthy human breaths
# the csv files are deleted in final submitted version to protect patient's information
# output: figure 2

def getX(file, ion):
	array = []
	with open(file, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)

		for line in csv_reader:
			if(line[0]==ion and int(line[1])<301):
				array.append(float(line[1]))
	return array

def getY(filename, ion, hour):
	with open(filename, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		array = []

		for line in csv_reader:
			if(line[0]==ion and int(line[1])<301):
				array.append(float(line[hour+1])/10000.0)
		return array

def getMaxY(filename, ion):
	with open(filename, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		maxPeak = -1.0

		for line in csv_reader:
			if(line[0]==ion):
				for x in range (2, 9):
					if(maxPeak < float(line[x])):
						maxPeak = float(line[x])

		return maxPeak/10000.0

def localMax(data):
	maximum = 0.0
	index = 0
	m_z = 15
	for x in data:
		if(maximum < x):
			maximum = x
			index = m_z
		m_z += 1
	return 'Max m/z '+ str(index) + ' value '+ str(maximum)



def roundup(x):
	return x if x % 10 == 0 else x + 10 - x % 10

files = ['p_7_20.csv', 'p_7_24.csv', 'p_7_25.csv', 'p_7_26.csv', 'p_7_27.csv', 'p_8_1.csv', 'p_8_2.csv',
'p_8_3.csv', 'p_8_8.csv', 'p_8_9.csv', 'p_8_10.csv', 'p_8_11.csv', 'p_8_15.csv', 'p_8_16.csv', 'p_8_17.csv']

# draw figure for H3O mass specs 
# ions are interchangable: 19/30/32
for file in files:

	ion = '32'
	color = '-g'

	X = getX(file, ion)
	Y1 = getY(file, ion, 1)
	Y2 = getY(file, ion, 2)
	Y3 = getY(file, ion, 3)
	Y4 = getY(file, ion, 4)
	Y5 = getY(file, ion, 5)
	Y6 = getY(file, ion, 6)
	Y7 = getY(file, ion, 7)

	ylimit = roundup(getMaxY(file, ion))
	Y = [Y1, Y2, Y3, Y4, Y5, Y6, Y7]
	for sample in Y:
		print(file)
		print(localMax(sample))
	
	fig = plt.figure(figsize=(10,6))
	ax1 = fig.add_subplot(241)
	ax1.plot(X, Y1, color)
	ax1.set_xlim([15,300])
	ax1.set_ylim([0,ylimit])
	ax1.margins(y=0)
	ax1.set_title('1')
	ax1.set_xlabel('m/z')
	ax1.set_ylabel('ion count (10000)')

	ax2 = fig.add_subplot(242)
	ax2.plot(X, Y2, color)
	ax2.set_xlim([15,300])
	ax2.set_ylim([0,ylimit])
	ax2.margins(y=0)
	ax2.set_title('2')
	ax2.set_xlabel('m/z')

	ax3 = fig.add_subplot(243)
	ax3.plot(X, Y3, color)
	ax3.set_xlim([15,300])
	ax3.set_ylim([0,ylimit])
	ax3.margins(y=0)
	ax3.set_title('3')
	ax3.set_xlabel('m/z')

	ax4 = fig.add_subplot(244)
	ax4.plot(X, Y4, color)
	ax4.set_xlim([15,300])
	ax4.set_ylim([0,ylimit])
	ax4.margins(y=0)
	ax4.set_title('4')
	ax4.set_xlabel('m/z')

	ax5 = fig.add_subplot(245)
	ax5.plot(X, Y5, color)
	ax5.set_xlim([15,300])
	ax5.set_ylim([0,ylimit])
	ax5.margins(y=0)
	ax5.set_title('5')
	ax5.set_xlabel('m/z')
	ax5.set_ylabel('ion count (10000)')


	ax6 = fig.add_subplot(246)
	ax6.plot(X, Y6, color)
	ax6.set_xlim([15,300])
	ax6.set_ylim([0,ylimit])
	ax6.margins(y=0)
	ax6.set_title('6')
	ax6.set_xlabel('m/z')


	ax7 = fig.add_subplot(247)
	ax7.plot(X, Y7, color)
	ax7.set_xlim([15,300])
	ax7.set_ylim([0,ylimit])
	ax7.margins(y=0)
	ax7.set_title('7')
	ax7.set_xlabel('m/z')

	plt.suptitle(file)
	plt.subplots_adjust(wspace=0.2, hspace=0.4)
	fig.savefig('fig2/'+file+'_o2.png')
	plt.show()



