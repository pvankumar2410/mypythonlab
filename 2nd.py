import string

question = input("Ask me something :")

response = ["Whoa, Chill Out!",'""You are, what, like 16?"'  , "Sure", "Whatever", "Fine be that way" ,'""Hi there!")','"WHAT\'S GOING ON?"','   ','"WATCH OUT!"' ,'Calm down, I know what I\'m doing!"',"Invalid Option" ]


def lackdaisical(question):
    if question==response[8]:
        print(response[0])
    elif question==response[1]:
        print(response[2])
    elif question==response[5]:
        print(response[3])
    elif question==response[6]:
        print(response[9])
    elif question=="   ":
        print("Fine be that way")
    else:
        print(response[10])


lackdaisical(question)

  
