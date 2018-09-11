from django.http import HttpResponse
from django.shortcuts import  render
from codechef_mayukh45.conf import access_token,refresh_token
from codechef_mayukh45.MAIN import get_contests


def index(request):
    contests = get_contests(access_token,refresh_token)

    context = {'contests':contests}
    return render(request,"home_page.html", context)







	
