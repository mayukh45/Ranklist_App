import requests
import json
count = 0
my_id = '38cb632e20af9e3fcc51b87acdacccbf'
my_secret = '55789839fb85e93e85ac6a20a98c3152'
redirect_uri = 'http://149.129.138.201/'

auth_uri = 'https://api.codechef.com/oauth/token'


def generate_refresh_token(refresh_token):


    headers = {'content-Type': 'application/json', }
    data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'client_id': my_id,
            'client_secret': my_secret}
   # print(refresh_token)
    refresh_token_response = requests.post(auth_uri, headers=headers, data=json.dumps(data))
    print(refresh_token_response.content)
    refresh_token_response = json.loads(refresh_token_response.content.decode("UTF-8"))
   # print(refresh_token_response)
    access_token = refresh_token_response['result']['data']['access_token']
    refresh_token = refresh_token_response['result']['data']['refresh_token']
    f = open('conf.py','w')
    f.write("access_token = '"+access_token+"'\nrefresh_token = '"+refresh_token+"'")
    f.close()


def get_college(access_token,username):
    base_url = "https://api.codechef.com/users/"+username+"?fields=organization"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + access_token
    }
    college_response = requests.get(base_url,headers=headers)
    college_response = json.loads(college_response.content.decode("UTF-8"))

    if college_response['result']['data']['message']=="user does not exists":
        return -1
    return college_response['result']['data']['content']['organization']



def get_contests(access_token,refresh_token):
    #print("lololololololol"*50)
    base_url = "https://api.codechef.com/contests?fields=code&status=present"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + access_token
    }
    contests_response = requests.get(base_url, headers=headers)
   # print("0"*20)

   # print(contests_response.content)
    contests_response = json.loads(contests_response.content.decode("UTF-8"))

    # if access token is expired
    if contests_response['status'] == "error":
        generate_refresh_token(refresh_token)
        contests_response = requests.get(base_url, headers=headers)
        contests_response = json.loads(contests_response.content.decode("UTF-8"))

    temp = contests_response['result']['data']['content']['contestList']
    contest_list = []
    for contests in temp:
        contest_list.append(contests['code'])

    f_contest_list =""
    for contest in contest_list:
        f_contest_list = f_contest_list+contest+"  |  "
    return "| "+f_contest_list









def get_ranklist(access_token,refresh_token,friends_dict,c_code,username,own_college):
    rank_list = []
    base_url = 'https://api.codechef.com/rankings/'
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + access_token
    }
    found = False
    friends_id = list(friends_dict.keys())

    friends_id.append(username)
   # print(friends_id)
    for friend in friends_id:
        if friend==username:
            college = own_college.split(" ")
        else:
            college = str(friends_dict[friend]).split(" ")
        #print(username+"YOYO"+college)
        insti_url = "%20".join(college)
        url = base_url + c_code + "?fields=username%2CtotalScore&institution=" + insti_url+"&limit=25"
    # print(url)
        rank_list_response = requests.get(url, headers=headers)
        rank_list_response = json.loads(rank_list_response.content.decode("UTF-8"))

    # if access token is expired
        if rank_list_response['status'] == 'error':
            generate_refresh_token(refresh_token)
            rank_list_response = requests.get(url, headers=headers)
            rank_list_response = json.loads(rank_list_response.content.decode("UTF-8"))

        content =[]
        # print(rank_list_response)
        if not(rank_list_response['result']['data']['code']==9000):
                content = rank_list_response['result']['data']['content']
        for info in content:
            if info['username']==friend:
                rank_list.append(info)
                found = True
                break
        if not(found):
            url = url+"&sortOrder=asc"
            rank_list_response = requests.get(url, headers=headers)
            rank_list_response = json.loads(rank_list_response.content.decode("UTF-8"))

    # if access token is expired
            if rank_list_response['status'] == 'error':
                generate_refresh_token(refresh_token)
                rank_list_response = requests.get(url, headers=headers)
                rank_list_response = json.loads(rank_list_response.content.decode("UTF-8"))

        #print(rank_list_response)
            if not(rank_list_response['result']['data']['code']==9000):
                content = rank_list_response['result']['data']['content']
            for info in content:
                if info['username']==friend:
                    rank_list.append(info)
                    break
      #  print(str(friend))
       # print(str(rank_list))
    return rank_list
