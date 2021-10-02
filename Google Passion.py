def function():
  f=1
  flag=1
  dot=0


  print("-----------------------------------------------------------")
  print("    \t\t\t    GOOGLE PASSION            \n        \t\t\tpress e to exit    ")
  print("-----------------------------------------------------------")
  while f == 1:  
      final_string=[]    
      google_string=""
      Googlenumber = input("Enter Numbers (1 to 8 ) ")
      Google_number=list(Googlenumber.split())   
    
      for i in range(0,len(Googlenumber)):
          if Googlenumber[i] == "0" or Googlenumber[i] == "9" : 
              flag=0
              break 
          else :
              flag=1
  
      if Googlenumber.isdigit() and flag == 1  :
          for i in range(0,len(Googlenumber)):
              if Googlenumber[i] == "1": 
                  final_string.append('g')
              elif Googlenumber[i] == "2":
                  final_string.append('o')
              elif Googlenumber[i] == "3":
                  final_string.append('l')
              elif Googlenumber[i] == "4":
                  final_string.append('e')
              elif Googlenumber[i] == "5":
                  final_string[i-1]=final_string[i-1].upper()
              elif Googlenumber[i] == "6":
                  dot=1;
              elif Googlenumber[i] == "7":
                  if final_string[0].isupper():
                      final_string[0]=final_string[0].lower()
                  else:
                      final_string[0]=final_string[0].upper()
              elif Googlenumber[i] == "8":
                  final_string=final_string[::-1]
                   
            
                
          print("-----------------------------------------------------------")
          print("                     String")   
          if dot == 1:
               final_string.append('.')
          for a in final_string:
              google_string+=a
          print(google_string)
          print("-----------------------------------------------------------")
        
      elif Googlenumber  == "e":
          choice=input("press - y to exit /n  press -n to continue :")
          if choice == "y":
              print("----------------------------")
              print("-      bye!!    -")
              print("----------------------------")
              f=0
            
          elif choice == "n":
              continue
             
          else:
              print("Invalid choice")      
      
      else:
          print("Invalid choice (enter no between 1-8)")
          print("-----------------------------------------------------------")

if __name__ == '__main__' :

  function()



