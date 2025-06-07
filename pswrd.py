from numpy import *
import random
class Ps:
    def gen(self):
        self.may=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.min=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.num=["0","1","2","3","4","5","6","7","8","9"]
        self.sim="!#$%&'()*+,-./:;<=>?@[\]_{}"
        
        self.med=int(input("Pass size: "))
        #self.cantpss=int(input("Which ones? "))
        self.pp=""
                
        def add(al_list):
            if al_list==1:
                alea=random.randrange(0,25)
                car=str(self.may[alea])
                self.pp=self.pp+car
            elif al_list==2:
                alea=random.randrange(0,25)
                car=str(self.min[alea])
                self.pp=self.pp+car
            elif al_list==3:
                alea=random.randrange(0,9)
                car=str(self.num[alea])
                self.pp=self.pp+car
            elif al_list==4:
                al=random.randrange(0,26)
                car=str(self.sim[al:al+1])
                self.pp=self.pp+car
    
        def generate(pp):
            al_list=random.randrange(1,200)
            add(al_list)            
            try:
                medida=len(self.pp)
                if medida==self.med:
                    print("Your pass is: ",self.pp)
                else:
                    generate(self.pp)
            except RecursionError as err:
                print(f"Ha ocurrido un error! :( Vuelve a ejecutar el programa ({err})")

        generate(self.pp)
p=Ps()
p.gen()
