import csv
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# project milestone 2
# this program runs principal component analysis of healthy human breath mass spectra
# output: figure 4

# import files 
files = ['p_7_20.csv', 'p_7_21.csv', 'p_7_24.csv', 'p_7_25.csv', 'p_7_26.csv', 
'p_7_27.csv', 'p_7_28.csv', 'p_7_31.csv', 'p_8_1.csv', 'p_8_2.csv', 'p_8_3.csv', 
'p_8_4.csv', 'p_8_7.csv', 'p_8_8.csv', 'p_8_9.csv', 'p_8_10.csv', 'p_8_11.csv', 
'p_8_14.csv','p_8_15.csv', 'p_8_16.csv', 'p_8_17.csv', 'p_8_18.csv', 'p_8_22.csv']

data_H3O = []
data_NO = []
data_O2 = []


def avg(line):
	total = 0.0
	limit = len(line)
	for x in range(2, limit):
		total += float(line[x])
	return (total/(len(line)-2.0))

# import data from csv files 
# filter noise by averaging each reading 
for file in files:
	with open(file, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		array1 = []
		array2 = []
		array3 = []
		
		for line in csv_reader:
			if(line[0]=='19' and int(line[1])<301):
				average = avg(line)
				array1.append(average) #averaging
			elif(line[0]=='30' and int(line[1])<301):
				average = avg(line)
				array2.append(average) #averaging	
			elif(line[0]=='32' and int(line[1])<301):
				average = avg(line)
				array3.append(average) #averaging			

		data_H3O.append(array1)
		data_NO.append(array2)
		data_O2.append(array3)

# standardize the values
H3O = StandardScaler().fit_transform(data_H3O)
NO = StandardScaler().fit_transform(data_NO)
O2 = StandardScaler().fit_transform(data_O2)

# PCA analysis 
# source 1: https://plot.ly/ipython-notebooks/principal-component-analysis/
# source 2: https://www.youtube.com/watch?v=EFJhO_6zWm0&t=832s 
# source 3: https://stackoverflow.com/questions/36566844/pca-projecting-and-reconstruction-in-scikit
# source 4: http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
'''# fig 3: each cumulative variances explained 
X = []
# explained variances (1:H30, 2:NO, 3:O2)
Y1 = []
Y2 = []
Y3 = []

pca = PCA(n_components=11)
pca.fit_transform(H3O)
Y1 = pca.explained_variance_ratio_
pca.fit_transform(NO)
Y2 = pca.explained_variance_ratio_
pca.fit_transform(O2)
Y3 = pca.explained_variance_ratio_

fig, ax = plt.subplots()
index = np.arange(1,12)
bar_width = 0.25
opacity = 0.8

rec1 = plt.bar(index-bar_width, Y1, bar_width, 
	alpha=opacity,
	label="Measured by H3O+",
	color='r',
	align='center')

rec2 = plt.bar(index, Y2, bar_width,
	alpha=opacity,
	label="Measured by NO+",
	color='b',
	align='center')

rec3 = plt.bar(index+bar_width, Y3, bar_width,
	alpha=opacity,
	label="Measured by O2+",
	color='g',
	align='center')

plt.xlabel('Number of PCs')
plt.xticks(index)
plt.ylabel('Accounted Variances')
plt.legend(loc=1)
plt.show()'''

'''# fig 4: actual losses (not standardized) by each components
X = []
D = [data_H3O, data_NO, data_O2]
Y1 = []
Y2 = []
Y3 = []

x = 0
for data in D:
	for n in range(1, 14):
		pca = PCA(n_components=n)
		X_trained = pca.fit_transform(data)
		X_projected = pca.inverse_transform(X_trained)
		loss = ((data - X_projected) ** 2).mean()
		if(x==0):
			X.append(n)
			Y1.append(loss)
		elif(x==1):
			Y2.append(loss)
		else:
			Y3.append(loss)
	x+=1

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(131)
ax1.bar(X, Y1, color='red')
ax1.set_xlabel('Number of PCs')
ax1.set_ylabel('losses by each components')
ax1.set_title('H3O+')

ax2 = fig.add_subplot(132)
ax2.bar(X, Y2, color='blue')
ax2.set_xlabel('Number of PCs')
ax2.set_ylabel('losses by each components')
ax2.set_title('NO+')

ax3 = fig.add_subplot(133)
ax3.bar(X, Y3, color='green')
ax3.set_xlabel('Number of PCs')
ax3.set_ylabel('losses by each components')
ax3.set_title('O2+')

plt.subplots_adjust(wspace=0.5)
plt.show()'''

# fig 5A: visualize selected PCA 
pca1 = PCA(n_components=2)
Y1 = pca1.fit_transform(H3O)
pca2 = PCA(n_components=2)
Y2 = pca2.fit_transform(NO)
pca3 = PCA(n_components=2)
Y3 = pca3.fit_transform(O2)


# visualize our first and second principal components 
fig = plt.figure(figsize=(10,6))
plt.scatter(Y1[:,0], Y1[:,1], c='r', marker='o', alpha=0.7, label="Measured by H3O+")
plt.scatter(Y2[:,0], Y2[:,1], c='b', marker='o', alpha=0.7, label="Measured by NO+")
plt.scatter(Y3[:,0], Y3[:,1], c='g', marker='o', alpha=0.7, label="Measured by O2+")
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend(loc=2)
plt.show()

# heat map 
'''fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(311)
ax1 = sns.heatmap(pca1.components_, xticklabels=50, yticklabels=[1,2], cmap='Reds')
ax1.set_ylabel('Number of PCs')
ax2 = fig.add_subplot(312)
ax2 = sns.heatmap(pca2.components_, xticklabels=50, yticklabels=[1,2], cmap='Blues')
ax2.set_ylabel('Number of PCs')
ax3 = fig.add_subplot(313)
ax3 = sns.heatmap(pca3.components_, xticklabels=50, yticklabels=[1,2], cmap='Greens')
ax3.set_ylabel('Number of PCs')
plt.xlabel('mass to charge ratio')
plt.show()'''
