class complex:
    def __init__(self,real=0,img=0):
        self.real=real
        self.img=img
    def addition(self):
        self.real1=input("enter real part of number to add")
        self.img1 = input("enter img part of num to add")
        self.real2=input("enter second real num to add")
        self.img2 = input("enter second img part")
        addreal = self.real1 + self.real2
        addimg = self.img1 + self.img2
        print("the first comlex number entered by you is %d+%di" %(self.real1,self.img1))
        print("the second comlex number entered by you is %d+%di" %(self.real2,self.img2))
        print("the addition of complex number is %d+%di" %(addreal,addimg))
    def subtraction(self):
        self.real1=input("enter real part of number to sub")
        self.img1 = input("enter img part of num to sub")
        self.real2=input("enter second real num to sud")
        self.img2 = input("enter second img part")
        subreal = self.real1 - self.real2
        subimg = self.img1 - self.img2
        print("the first comlex number entered by you is %d+%di" %(self.real1,self.img1))
        print("the second comlex number entered by you is %d+%di" %(self.real2,self.img2))
        print("the addition of complex number is %d+%di" %(subreal,subimg))
    def multiplication(self):
        self.real1=input("enter real part of number to mul")
        self.img1 = input("enter img part of num to mul")
        self.real2=input("enter second real num to mul")
        self.img2 = input("enter second img part")
        mulreal= self.real1 * self.real2 - self.img1 * self.img2
        mulimg=self.real1 * self.img2 + self.img1 * self.real2
        print("the first comlex number entered by you is %d+%di" %(self.real1,self.img1))
        print("the second comlex number entered by you is %d+%di" %(self.real2,self.img2))
        print("the addition of complex number is %d+%di" %(mulreal,mulimg))
    def compare(self):
        self.real1=input("enter real part of number ")
        self.img1 = input("enter img part of num to mul")
        self.real2=input("enter second real num to mul")
        self.img2 = input("enter second img part")
        print("the first comlex number entered by you is %d+%di" %(self.real1,self.img1))
        print("the second comlex number entered by you is %d+%di" %(self.real2,self.img2))
        if self.real1 == self.real2 and self.img1 == self.img2 :
            print("both complex number are same")
        else:
            print("number are not same")
def main():
    complex1=complex(1,2)
    complex1.addition()
    complex1.subtraction()
    complex1.multiplication()
    complex1.compare()
if __name__ == '__main__':
    main()