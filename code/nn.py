#Artificial Neural Network Backpropagation

#initialize outputs
o = [0, 1, 2, 0.7311, 0.0179, 0.9933, 0.8387]
#set true output value and learning rate
t6= 0
l = 10
#initialize error array
err = [0,0,0,0,0,0,0]
#initialize weights
w = [[0, 0, 0, 0, 0, 0, 0],
[0, 0,	0,	-3,	2,	4,	0],
[0, 0,	0,	2,	-3,	0.5, 0],
[0, 0,	0,	0,	0,	0,	0.2],
[0, 0,	0,	0,	0,	0,	0.7],
[0, 0,	0,	0,	0,	0,	1.5]]

#state hidden and input nodes
hidden = [5,4,3]
inputl = [2,1]

#calculate error for each unit in output layer
err[6] = o[6]*(1-o[6])*(t6-o[6])
print "err_6: " , err[6]

#calculate error for each unit in hidden layers
for i in hidden:
	j = 6
	err[i] = o[i]*(1-o[i])*(err[j]*w[i][j])
	print "err_",i, ": ",err[i]

#update weight for each weight in network
for i in hidden:
	j = 6
	w[i][j] = w[i][j] + l*err[j]*o[i]
	print "w_",i,j,": ",w[i][j]

for i in inputl:
	for j in hidden:
		w[i][j] = w[i][j] + l*err[j]*o[i]
		print "w_",i,j,": ",w[i][j]


print err
print w