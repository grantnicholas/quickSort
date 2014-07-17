from random import randrange
import datetime

def randArr(length, maxval):	
	b = [];
	for i in range(length):
		b.append(randrange(maxval));
	return b;

def partition(arr):
	l = []; r= []; m = [];
	for i in range(len(arr)):
		if(arr[i]>arr[0]):
			r.append(arr[i]);
		elif(arr[i]<arr[0]):
			l.append(arr[i]);
		elif(arr[i] == arr[0]):
			m.append(arr[i]);
	return (l,m,r);

def quickSort(arr):
	if(len(arr) ==0):
		return [];
	if(len(arr) ==1):
		return arr;
	else:
		(l,m,r) = partition(arr);
		return quickSort(l)+ m + quickSort(r);


b = randArr(10000,100);
#print b;
start = datetime.datetime.now()
b = quickSort(b);
finish = datetime.datetime.now()
#print b;
print finish-start;

