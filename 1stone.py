import re

def myfunction():
   pattern="^[a-zA-Z\s]+$"; #first and last name pattern
   pattern3 = "^[a-zA-Z0-9_]*$";
   pattern2="^[\s{2,*}]$";
   a=list();
   a=input();
  
   if a.isdigit():#identifies if its digit
     print("Orange")
   elif re.search(pattern,a): 
     print("Apple")
   elif re.search(pattern3,a): 
     print("Bannana")
   elif a.isalpha() :
     print("Bannana")
   elif re.search(pattern2,a):
     print("Bannana")
   else :
     print("Bannana")

def b(str):
    gerund=str[:-3]
    if str[-3:]=="ing":
      print("to "+gerund)
    else :
      print("Not a gerund")
def c(str):
    valid_dna = "ACGT"
    sequence = str.replace(" ", "")
    for i in sequence:
      if i in valid_dna:
            count = 1
      else:
            count=0
    if count==1:
      print("This is a valid DNA sequence.") 
      print(str.replace("t", "u"))
    else:
      print("This is an invalid DNA sequence")  
if __name__ == "__main__":
  #1a
   myfunction()
  #1b
   stri=list()
   stri = input('Enter the Tring ')
   b(stri)
  #1c
   dna=list()
   dna=input("Enter Dna Strand ( A(Adanine) C(Cytosine) G(Guanine ) T(Tymine))").upper()
   c(dna)
   