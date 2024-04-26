#thrives operator (>) error:
class Party:
    def __init__(self,name,money):
        self.name=name
        self.money=money
        
p1=Party(name="spoorthi",money=1000)
p2=Party(name="Bhavana",money=2000)

if(p1>p2):
    print(f"{p1.name} will pay the bill.")
else:
    print(f"{p2.name} will pay the bill.")
    

#correct code:
class Party:
    def __init__(self,name,money):
        self.name=name
        self.money=money
        
    def __gt__(self,other):
        if self.money>other.money:
            return True
        else:
            return False
        
p1=Party(name="spoorthi",money=1000)
p2=Party(name="Bhavana",money=2000)

if(p1>p2):
    print(f"{p1.name} will pay the bill.")
else:
    print(f"{p2.name} will pay the bill.")
    
