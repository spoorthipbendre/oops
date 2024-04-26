#operator_overloading:  (error)
class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
c1=ComplexNumber(real:2,imaginary:2)
c2=ComplexNumber(real:1,imaginary:2)
print(c1+c2)


#correct:
class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
        
c1=complex(2,2)
c2=complex(1,2)
print(c1+c2)


#correct code:
class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self,other):
        return(f"{self.real+other.real}+{self.imaginary+self.imaginary}")
    
c1=ComplexNumber(real=2,imaginary=2)
c2=ComplexNumber(real=1,imaginary=2)

print(c1+c2)


