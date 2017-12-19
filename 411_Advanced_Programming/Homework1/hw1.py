#!/usr/local/bin/python
# coding:utf-8

#libraries
import numpy as np
import math

# calculate the value of sample t-test
def sample_t_value(list, n, num):
	# the average of list
	mean=np.array(list).sum()/n
	# the variance of list
	var=0
	for i in range(0,n):
		var+=(list[i]-mean)**2
	var/=n

	# the value of t-test
	t_value=(mean-num)/math.sqrt(var/(n))
	print 'the value of t-test: '+ str(t_value)
	return t_value

# calculate the value of pair-t-test
def paired_t_value(list1, n1, list2, n2):
	d=[]
	d2=[]
	for i in range(0,n1):
		d.append(list2[i]-list1[i])
		d2.append(d[i]**2)
	mean_d=np.array(d).sum()/n1

	sd=(np.array(d2).sum()-np.array(d).sum()**2/n1)/(n1-1)
	t_value=mean_d/math.sqrt(sd/n1)
	print 'the value of t-test: ' + str(t_value)
	return t_value

# find the number in the t_test.dat, which will be used to compared with the value of t-test
def find_t(n):
	target_name='t_test.dat'
	file = open(target_name,'r')
	next(file)
	# print file
	t=0	
	for line in file:
		# n-1 means the degrees of freedom
		if line.split()[0]==str(n-1):
			t=line.split()[1]
			break
	print "critical possibility 0.05, critical t-value "+str(t)
	return t

def sample_t_test():
	# system's processing speed
	list=[11300, 9890, 10400, 9900, 10545, 12334]
	# number of the list
	n=6
	# previous speed
	num=10000
	t=find_t(n)
	t_value=sample_t_value(list,n ,num)
	
	if t_value<t:
		print 'the previous speed and the new system speed do not have obvious difference'
	else:
		print 'the previous speed and the new system speed have obvious difference'

def paired_t_test():
	# two speed
	list1=[11300, 9890, 10400, 9900, 10545, 12334]
	list2=[11400, 9800, 11345, 9739, 10787, 12555]
	n=6
	t=find_t(n)
	t_value=paired_t_value(list1,n,list2,n)
	
	if t_value<t:
		print 'the previous speed and the new system speed do not have obvious difference'
	else:
		print 'the previous speed and the new system speed have obvious difference'

if __name__ == '__main__':
	print "one sample t-test:"
	sample_t_test()
	print "paired t-test:"
	paired_t_test()
	