
from django.shortcuts import  render
from codechef_mayukh45.conf import access_token,refresh_token



def index(request):
   return render(request,"home_page.html")







	
