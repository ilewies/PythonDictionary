import json
from difflib import get_close_matches
data = json.load(open("dicc.json"))
print("----------------------------------------")
user = str(input("Enter name to search: "))

user1 = user.lower()
def tran(user1):
    if user1 in data:
         data1 = data[user1]
         return data1
        
    elif user1.title() in data:
         data1 = data[user1.title()]
         return data1
        

    
    else:
       # print("Word Not Found... these are the close match..")
        close_match = get_close_matches(user1, data.keys())
        return close_match
      #  print("please see and enter aginn..")

out = tran(user1)
if len(out) > 0:
    print("-------Output / Possible Matches-------")
    if type(out) == list:
    
        for i in out:
            print(":-"+i)
    else:
       # for i in out:
            print(":-" +i + "\n")
    print("----------------------------------------")        
else:
    print("can't find...")            
    print("Try New Keyword")
