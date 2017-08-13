#!/bin/bash/python
def insertion(l1,l2) :

        if type(l1) != list or type(l2) != list :
                print("Sorry!Please enter a valid list ")
                return 0
        if len(l1) != len(l2) :
                print("Please check the lenth of both list")
                return 0
        l1.sort;
        l2.sort;i=0;j=0;l3=[]
        while i<len(l1) or j<len(l2) :
                if l1[i] == l2[j] :
                        l3.append(i)
                        i=i+1
                else :
                        j+=1
        for k in l3:
                print l3[k]
def main() :
        l1=input("please enter the number in list format i.e[ , ] for first list :")
        l2=input("please enter the number in list format i.e[ , ] for second list :")
#       i=0;j=0;
        a=insertion(l1,l2)
        print a
if __name__ == '__main__' :
        main()
~
