 #!/bin/bash/python
def intersection(l1,l2,m,n) :
	
	if type(l1) != list or type(l2) != list :
		print("Sorry!Please enter a valid list ")
		return 0
	if len(l1) != len(l2) :
		print("Please check the lenth of both list")
		return 0
	l1.sort;
	count=0;l2.sort;i=0;j=0;o=0
	l3=list()
	while i<m:
		j=o
		print("First loop %s:%s" %(i,l1[i]))
		while j<n and  l2[j]<=l1[i] :
                        #print("Check is %s == %s" %(l1[i],l2[j]))
			if l1[i] == l2[j] :
				print("Matched %s : %s "%( l2[j] ,l1[i] ))
				o=j+1
				l3.append(l1[i])
				break;
			print("second loop loop %s: %s" %(j,l2[j]))
			j+=1
		i+=1
	print l3

		#if l1[i] == l2[j] :
	#		l3.append(l1[i])
#		elif l2[j] == l1[i] :
#			l3.append(l2[j])
#			j+=1
#		count+=1
#	print(count) 
#	for k in l3:
#		print k 	
def main() :
#	l1=input("please enter the number in list format i.e[ , ] for first list :")
#	l2=input("please enter the number in list format i.e[ , ] for second list :")
#	i=0;j=0;
	l1=[1,2,3,4]
	l2=[2,3,4,5]
	m=len(l1);
	n=len(l2); 
	a=intersection(l1,l2,m,n) 
	print a
if __name__ == '__main__' :
	main()
