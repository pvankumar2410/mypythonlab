# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:09:26 2021

@author: Admin
"""

import re
class myregex:

    def LoveForFrenchFries(self,stringinput,find):
        self.regex=""+find+""
        match = re.findall(self.regex,stringinput) 
        print(match)
        print("No of Occurences {} ".format(len(match)))
    
    def MyScottishAccent(self,rep,withthis,full):
        a=full.replace(rep,withthis) 
        print("After Replacing : {}".format(a))
        
    def LinkVowels(self,words):
       self.regex2=re.compile(r'([aeiouAEIOU])+(\s*)+([aeiouAEIOU])')
       mo=self.regex2.search(words)
       if mo:
           print("LINK BETWEEN {}".format(mo.group()))
           self.value=True
           print(self.value)
       else :
           print("NO LINK WORDS ")
           self.value=False
           print(self.value)
           
    def LonelyOne(self,lone):
        self.val="\\b([a-zA-Z0-9])\\1+\\b"
        self.lonely="1+"
        g=re.findall(self.val,lone)
        m=re.findall(self.lonely,lone)
        if g:
            g="0"
            m="0"
            print(m)
        else: 
           print("no of times 1 is alone ",len(m))
        
         


    
myobj=myregex()
#1
while 1:
  print("__________________________________________________________________________")
  a=int(input("Enter the option\n1.search word count\n2.replace char\n3.link\n4.lonely  : "))
  print("__________________________________________________________________________")

  if(a==1):
    str=input("Enter the Main string")
    str2=input("Enter the full string to find main string  :  ")
    myobj.LoveForFrenchFries(str2,str)
#2
  elif(a==2):
    replacingchar=input("Enter the replacing char : ")
    withwhich=input("Enter the char to replace {} : ".format(replacingchar))
    fullword=input("enter the full word to replace : ")
    myobj.MyScottishAccent(replacingchar,withwhich,fullword)
#3
  elif(a==3):
    words=input("Enter the word : ")
    myobj.LinkVowels(words)
#4
  elif(a==4):
    lone=input("Enter the word : ")
    myobj.LonelyOne(lone)
  else :
      print("Wrong input ")
      break;
    

       
       
       