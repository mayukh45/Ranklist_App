from django.shortcuts import  render
from codechef_mayukh45.conf import access_token,refresh_token
from codechef_mayukh45.MAIN import get_contests,get_college,get_ranklist
import sys
from operator import itemgetter
own_college = 0

def index(request):
    global own_college
    friends = []
    f = True


    username = str(request.GET.get('username'))
    ranklist = []
    if len(str(username)) > 0 and str(username) != "None":
        own_college = get_college(access_token, str(username))
    #print(request.method)
    #print("*"*20)

    contest_code = str(request.GET.get('contest_code'))

    from database import data
    del sys.modules['database']
    keys = list(data.keys())
    #print(keys)
 #   print(username)
  #  print(contest_code)

    if keys.count(username)>0:
        friends = data[username]['friends']
        #print("AM HERE")
        ranklist = get_ranklist(access_token,refresh_token,friends,contest_code,username,own_college)
            #print("AM IN"+str(friends))

    contests = get_contests(access_token,refresh_token)
   # print(ranklist)
    null = False
    if str(username) =="None":
        null=True
   # print("LOL"*40)
   # print("BEFOREEEE"+str(ranklist))
   # print("\n\n")
    ranklist = sorted(ranklist, key=itemgetter('rank'))
   # print("AFTERRR"+str(ranklist))
    context = {'contests':contests,'friends' : friends,'username':username,'ranklist':ranklist,'null':null}
    return render(request,"ranklist.html", context)
