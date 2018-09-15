from django.http import HttpResponse
from django.shortcuts import  render
from codechef_mayukh45.conf import access_token,refresh_token
from codechef_mayukh45.MAIN import get_college
import sys
#username = ""
#friends = []
own_college = 0
friends_college   = 0
import time

def index(request):
    global own_college
    global friends_college
    new_friend = ""
    friends = {}
    username = str(request.GET.get('username'))
    print("username creation "+str(username))
    if len(str(username)) > 0 and str(username) != "None":
        own_college = get_college(access_token,str(username))
    from database import data
    del sys.modules['database']
    #print(str(data))
    keys = list(data.keys())
    if keys.count(username)==0 and username!="None":
        data[username]={'friends':{},"college":own_college}
        keys.append(username)
    if request.method=="POST":
        new_friend = str(request.POST.get('new_friend'))
        print(new_friend)
        if len(str(new_friend))>0 and str(new_friend)!="None" and str(username)!=("None"):
            #print("LOL"*10)
            #print(username)


            friends_college = get_college(access_token,new_friend)
            if friends_college != -1 and own_college!=-1:

                data[username]['friends'][str(new_friend)]=friends_college
                #print(data)
                f = open('database.py','w')
                f.write("data = "+str(data))
                f.close()

   # print("*"*100)
   # print("new_friend"+str(new_friend))
   # print(str(data))
    if keys.count(username)>0:
       # print(username + "io")
        friends = list(data[username]['friends'].keys())


    null = False
    if str(username) == "None" or len(str(username))==0 and friends_college!=-1:
        null = True

    #print("creation"+str(username))
   # print("friends "+str(friends))
    context = {'friends' : friends,'username':username,'own_college':own_college,'friend_college':friends_college,"null":null}
    return render(request,"creation.html", context)


