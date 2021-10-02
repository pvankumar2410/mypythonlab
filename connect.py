def fun():
  f=1
  print("-----------------------------------------------------------")
  print("-\t \t\t\t \t ENGLISH LINGUIST    \n\n\t\t\t\t      press e to exit   -")
  print("-----------------------------------------------------------")
  while f == 1:
      words=[]
      total_words=input("no of words do you want to connect :")
      if total_words.isdigit():
          total_words=int(total_words)
          print("\nEnter the word to be connected : ")
          for i in range(0, total_words):
              w=input()
              words.append(w)
          connect=""
          connect=connect.join(words)

          order_connect=""
          for i in connect:
              if(i in order_connect):
                  pass
              else:
                  order_connect=order_connect+i
          print("---------------------------------")
          print("CONNECTED WORD : ",order_connect)
          print("---------------------------------")
    
      elif total_words  == "e":
          choice=input("Are sure want to exit y/n :")
          if choice == "y":
              print("----------------------------")
              print("-      exited              -")
              print("----------------------------")
              f=0
            
          elif choice == "n":
              continue
             
          else:
              print("wrong choice")      
      
      else:
          print("Only Number is allowed....")
          print("-----------------------------------------------------------")

        

if  __name__=='__main__':
  fun()




