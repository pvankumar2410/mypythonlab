# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:31:41 2021

@author: Pavan Kumar K

Create a class called “Vehicle” which has attributes brand, model, type, fuel_tank_ size, 
fuel _level. Initialize the variables in the “__init__” method and write the following methods

•	Fulltank()- which fills the entire tank and prints “Tank is Full”
•	Update_fuel_tank()- which updates the amount of fuel which is in the tank.You can pass 
    a variable called “new_level”  and assign  that to  fuel_level. Print a warning if the 
    fuel_level is <=3liters.
•	Get_fuel() – which takes in a variable “amount” and add it to fuel_level.
    Print warning if the fuel_level is exceeding the capacity of the tank.
•	Drive() – which prints a message saying “WOW! I am Driving {model}”. 
    The model is the vehicle should be inserted instead of “{model}”

Create two objects of vehicles and call the functions.

brandd,mod,typee,fuel_cap,capacity,level

"""
class Vehicle:
    def __init__(self,brand,model,typ,fuel_tank,fuel_level):
        self.brand=brand
        self.model=model
        self.type=typ
        self.fuel_tank=fuel_tank
        self.fuel_level=fuel_level
        self.fuelstatus=True
        self.diff=float()
        self.diff2=float()
    def Drive(self):
        self.brand=brand
        self.model=model
        self.type=typ
        self.fuel_tank=fuel_tank
        self.fuel_level=fuel_level
        if(self.fuel_level<3):
            print("Very less fuel")
        else :
            print("")
        print("WOW! I am Driving {} ".format(self.model))
        
        print("----------------------------------------")
        print("brand : ",self.brand)
        print("model : ",self.model)
        print("type : ",self.type)
        print("fueltank : ",self.fuel_tank)
        print("fuel level : ",self.fuel_level)
        
    def Fulltank(self):
        self.fuel_level=self.fuel_tank
        return True
    def Get_fuel(self):
        self.brand=brand
        self.model=model
        self.type=typ
        self.fuel_tank=fuel_tank
        self.fuel_level=fuel_level
        self.diff2=self.fuel_tank-self.fuel_level
        if self.fuel_tank==fuel_level:
           print("-----------Tank full----------")
           print("Tank FUll")
           print("-----------Details--------------")
           print("brand : ",self.brand)
           print("model : ",self.model)
           print("type : ",self.type)
           print("fueltank : ",self.fuel_tank)
           print("fuel level : ",self.fuel_level)
           
        else :
          print("-------------------------------------------------")
          amt=float(input(" present fuel  : {}\nenter the amount to fill more".format(fuel_level)))
          print("-------------------------------------------------")
          self.diff=amt+fuel_level
          while self.diff>self.fuel_tank:
              print("-------------------------------------------------")
              amt=float(input("present fuel  : {}\n Can't exceed more than tank size".format(fuel_level)))
              print("-------------------------------------------------")
              self.diff=amt+fuel_level
          self.diff2=self.fuel_tank-amt
          print("diff : {}".format(self.diff2))
          while self.diff>self.fuel_tank or self.diff <1 :
             self.diff=0
             self.diff2=0
             self.fuel_level=0
             print("-------------------------------------------------")
             amt=float(input("Exceeding fuel capity of ur vehicle plz enter fuel_level less b/w 0-{}".format(self.fuel_tank)))
             print("-------------------------------------------------")
             self.diff=amt+self.fuel_level
             self.diff2=self.fuel_tank-self.fuel_level
          self.fuel_level+=amt
          if(amt==self.fuel_tank):
              print("-------------------------------------------------")
              print("Tank is Full")
              print("-------------------------------------------------")
              return True
          else:
              print("present fuel after filling is : {} liters \nCapacity left is : {} liters".format(self.fuel_level,(self.fuel_tank-self.fuel_level)))
              if self.fuel_tank==self.fuel_level :
                  print("Tank FUll")
              elif self.fuel_level<=3:
                  print("Low fuel <3")
              else :
                  print("manageable fuel in bike")
    def Update_fuel_tank(self):
        self.brand=brand
        self.model=model
        self.type=typ
        self.fuel_tank=fuel_tank
        self.fuel_level=fuel_level
        self.diff2=self.fuel_tank-self.fuel_level

        print("-------------------------------------------------")
        amt=float(input("Update fuel"))
        print("-------------------------------------------------")
        while 1:
            if amt>self.fuel_tank or amt<=0:
                amt=float(input("cant update fuel beyound {} or less than 3 liters \n------Update fuel Again-----".format(self.fuel_tank)))
            else :
                self.fuel_level=amt
                print("present fuel {}".format(self.fuel_level))
                if self.fuel_level<=3:
                   print("less fuel <3 liters")
                else :
                   print("-----------tank full----------")
                   print("Tank FUll")
                   print("-----------Details--------------")
                   print("brand : ",self.brand)
                   print("model : ",self.model)
                   print("type : ",self.type)
                   print("fueltank : ",self.fuel_tank)
                   print("fuel level : ",self.fuel_level)
                break;
                
    
        
          
   # def Get_fuel(self):
        
   # def Drive(self):
        




driving=0
brand=input("enter the name of the brand : ")
model=input("enter the name of the model : ")
typ=input("enter the name of the type : ")
fuel_tank=float(input("Enter the capacity of tank : "))
while fuel_tank<10:
   print("--------------------------------------------------------")
   fuel_tank=float(input("minimum size of tank is 10 !\nplz eneter valid fuel tank : "))
   print("--------------------------------------------------------")
fuel_level=float(input("Enter the capacity of fill : "))
while fuel_level>fuel_tank or fuel_level<=0:
   print("--------------------------------------------------------")
   fuel_level=float(input("YOu cant have more fuel while ur tank size is less !\nplz eneter valid amount : "))
   print("--------------------------------------------------------")
while fuel_level<=0 :
   print("--------------------------------------------------------")
   fuel_level=float(input("cant be 0 or lesser  \nplz eneter valid amount : "))
   print("--------------------------------------------------------")
if fuel_level<=3:
   print("--------------------------------------------------------")
   print("Low fuel < 3liters")
   print("--------------------------------------------------------")
obj=Vehicle(brand,model,typ,fuel_tank,fuel_level)
obj2=Vehicle(brand,model,typ,fuel_tank,fuel_level)
#
while 1 :
    a=int(input("1 to drive \n 2 to get fuel \n 3 to update fuel : ") )
    if a ==1 :
      driving+=1
      if driving>1:
        print("------------------you are already driving {} -------------".format(model))
      else:
        obj2.Drive()
    elif a==2:
      obj.Get_fuel()
    elif a==3:
      obj.Update_fuel_tank()
    else:
        break;



