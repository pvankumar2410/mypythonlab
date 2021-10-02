import datetime 
#from datetime 
class ValueTooLargeError(Exception):
  pass
def zodiac():
  sign=list()
  dict={
     "Aries(ram)": {'UR AWESOME' },
     "Taurus(Bull)": {'UR GREAT'},
     "Gemini(Twins)": {'ur fantastic'},
     "Cancer(Crab)": {'ur pretty talented' },
     "Leo(Lion)": {'CALM AND AWESOME'},
     "Virgo(Virgin)": {'UR THE BEST' },
     "Libra(Balance)": {'PURE SOUL' },
     "Scorpius(Scorpion)": {'ur humane being ' },
     "Sagittarius(Archer)": {'underrated' },
     "Capricornus(Goat)": {'hardworking' },
     "Aquarius(Water Bearer)": {'better than best' },
     "Pisces(Fish)": {'Smart and talented','January' }
  }
  a=int()
  dob=list()
  current = datetime.datetime.now() 
  print("Day :{} Month :{} Year :{}".format(current.day,current.month,current.year ))
  while 1:
    try:
      print("--------------------------------------------------")
      print("\t\t\t\t\tMenu\nEnter Q/q to quit \n? to no the format \nAny other no to enter date :")
      print("-------------------------------------------------")
      choice=input("")
      
      if choice=='Q' or choice=='q':
         raise ValueTooLargeError
      elif choice=='?':
        print("enter day/month/year format")
        print("--------------------------------------")
      else:
        try :
          print("Enter the date ")
          print("----------------------------------------")
          for i in input().split("/"):
              dob.append(int(i))
        except ValueError:
          print("----------Invalid Date :( -----------")
        except ValueTooLargeError:
          print("hello")
    except ValueTooLargeError:
      print("Bye! Hope you run this program again")
      break;
    if(len(dob)==3):
      #length of dateshdnt be more
      if len(dob)>3 :
        dob.clear()
        print("length")
        a=0
      #odd no month logic
      elif (dob[0]>31 or dob[0]<1) and dob[1]%2!=0 :
        dob.clear()
        print("invalid date")
        a=0
      #leap year logic
      elif (dob[0]>28 or dob[0]<1)and (dob[1]==2) and (dob[2]%4!=0):
        dob.clear()
        print("invalid date")
        a=0
      elif  len(str(dob[2]))!=4 or dob[0]<1 or dob[1]<1 or dob[0]<1 or dob[2]>current.year or dob[1]>12 or dob[1]<1 or dob[0]>31:
        print("invalid date")
        dob.clear()
        a=0
      elif (dob[0]>30 or dob[0]<1) and (dob[1]%2==0) or (dob[2]>current.year) or len(str(dob[2]))!=4 or dob[0]<1 or dob[1]<1 or dob[0]<1 or dob[2]>current.year or dob[1]>12 :
        print("invalid date")
        a=0
      elif dob[1]>current.month  and dob[2]>=current.year :
        print("invalid date\ngreater than today's date")
        a=0
      elif (dob[0]>29 or dob[0]<1)and (dob[1]==2) and (dob[2]%4==0):
        print("invalid date \nyour month doesnt have 30 days")
        a=0
      else:
        print("-----------------Displaying Info----------------------")
        print("YOUR DOB :{}/{}/{}".format(dob[0],dob[1],dob[2]))
        #Aries (Ram):             21-3 19-4
        if (dob[0]>=21 and dob[1]==3) or (dob[0]<=19 and dob[1]==4 ):
           sign.append("Aries(ram)")
        #Taurus (Bull):           20-4 20-5
        elif (dob[0]>=20 and dob[1]==4) or (dob[0]<=20 and dob[1]==5 ):
           sign.append("Taurus(Bull)")
        #Gemini (Twins) :         21-5 21-6
        elif (dob[0]>=21 and dob[1]==5) or (dob[0]<=21 and dob[6]==5 ):
           sign.append("Gemini(Twins)")
        #Cancer (Crab):           22-6 22-7
        elif (dob[0]>=22 and dob[1]==6) or (dob[0]<=22 and dob[6]==7 ):
           sign.append("Cancer(Crab)")
        #Leo (Lion):              23-7 22-8
        elif (dob[0]>=23 and dob[1]==7) or (dob[0]<=22 and dob[6]==8 ):
           sign.append("Leo(Lion)")
        #Virgo (Virgin):          23-8 22-9
        elif (dob[0]>=23 and dob[1]==8) or (dob[0]<=22 and dob[6]==9 ):
           sign.append("Virgo(Virgin)")
        #Libra (Balance):         23-9 23-10
        elif (dob[0]>=23 and dob[1]==9) or (dob[0]<=23 and dob[6]==10 ):
           sign.append("Libra(Balance)")
        #Scorpius (Scorpion):     24-10 21-11
        elif (dob[0]>=24 and dob[1]==10) or (dob[0]<=21 and dob[6]==11 ):
           sign.append("Scorpius(Scorpion)")
        #Sagittarius (Archer):    22-11 21-12
        elif (dob[0]>=22 and dob[1]==11) or (dob[0]<=21 and dob[6]==12 ):
           sign.append("Sagittarius(Archer)")
        #Capricornus (Goat):      22-12 19-1
        elif (dob[0]>=22 and dob[1]==12) or (dob[0]<=19 and dob[6]==1 ):
           sign.append("Capricornus(Goat)")
        #Aquarius (Water Bearer): 20-1 18-2
        elif (dob[0]>=20 and dob[1]==1) or (dob[0]<=18 and dob[6]==2 ):
           sign.append("Aquarius(Water Bearer)")
        #Pisces (Fish):               19-2 20-3
        elif (dob[0]>=19 and dob[1]==2) or (dob[0]<=20 and dob[6]==3 ):
           sign.append("Pisces(Fish)")
        else:
          print(" NO Sign")
        res=""
        res=dict.get(sign[0])
        print("YOUR SIGN : ",sign[0])
        print("YOUR QUALITY : ",res)
        a=1
        break;
  
zodiac()