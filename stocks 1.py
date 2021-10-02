class inp:
  def stocks(self):
    l=[]
    l1=[]
    tot=0
    tot2=0
    print("Pavan Kumar K")
    print("RegNo:2147224")
    st=inp()
    while True:
      try:
        n=int(input("Enter the no of inputs :")) 
        if n>0 and n<6:
          print("Validated ")
          break;
        else:
         print("enter range 1-6")      
      except ValueError:
        print("Provide an integer value...")
        continue
      
    for i in range(n):
      print("------------------------------------------")
      print("Entry {}".format(i+1))
      print("------------------------------------------")
      company=str(input("Enter the COmpany Initial : "))
      while True:
        try:
          quantity=float(input("enter the quantity : "))
          if quantity>0:
            print("Validated... ")
            break;
          else:
           print("enter no greater than 0")      
        except ValueError:
          print("Invalid Quatity")
          continue
      
      
      while True:
        try:
          price=float(input("Enter the price : "))
          if price>0:
            print("Validated... ")
            amt=quantity*price
            break;
          else:
           print("enter no greater than 0")      
        except ValueError:
          print("Invalid Quatity")
          continue
      
      status=str(input("enter the Status s/b :"))
      if(status=='s'):
        tot+=amt
        print(tot)
      elif(status=='b'):
        tot2+=amt
        print(tot2)
      else :
        l1.append((company,quantity,price,status))
        print(l1)
        print("! Invalid Input of status")
        break;
      l.append((company,quantity,price,status))
      t=tuple(l)
      print("------------------------------------------")
      print("Results : {}".format(t))
      print("Buys :{} , Sells :{}".format(tot2,tot))
      print("------------------------------------------")
   
    print(t)

       

st=inp()
st.stocks();


