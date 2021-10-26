try:
	import requests  ,re, os , sys , random , uuid , user_agent , json,secrets
	from uuid import uuid4
	from user_agent import generate_user_agent
	
except ImportError:
	os.system('pip install requests')
	os.system('pip install user_agent')
	
class SidraELEzz:
	
	def Instalogin(email,password):
		
		url = "https://i.instagram.com/api/v1/accounts/login/"
		
		headers = {
        'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
        'Accept':'*/*', 
        'Cookie':'missing', 
        'Accept-Encoding':'gzip, deflate', 
        'Accept-Language':'en-US', 
        'X-IG-Capabilities':'3brTvw==', 
        'X-IG-Connection-Type':'WIFI', 
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
        'Host':'i.instagram.com'}
        
		data = {
		'uuid':str(uuid4()),
		'password':password,
		'username':email, 
		'device_id':str(uuid4()),
		'from_reg':'false', 
		'_csrftoken':'missing', 
		'login_attempt_countn':'0'}
		
		login = requests.post(url,headers=headers,data=data,allow_redirects=True,verify=True)
		
		if str("logged_in_user") in login.text:
			
			
			os.system('rm -rf sessionid.txt')
			
			APK = login.cookies['sessionid']
			
			f = open('sessionid.txt','a')
			
			f.write(APK+"\n")
			
			f.close()
			
			return True
			
		if str('"message":"challenge_required","challenge"') in login.text:
			
			return False
			
		else:
			
			return None
			
	def username(sessionid):
		
		headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Zc4tm5D7QNL1hiMGJ1caLT7DNPTYHqH0; ds_user_id=45334757205; sessionid='+str(sessionid)+'; rur=VLL','referer': 'https://www.instagram.com/accounts/edit/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
         'User-Agent': str(generate_user_agent()),
         'x-ig-app-id': '936619743392459',
         'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9Ncl',
         'x-requested-with': 'XMLHttpRequest'}
         
		url = "https://www.instagram.com/accounts/edit/?__a=1"
		
		data = {'__a': '1'} 
		
		response = requests.get(url, data=data, headers=headers)
		
		try:
			
			return str(response.json()['form_data']['username'])
			
		except:
			
			return ("Error account is security")
			
        
    
    
	def followers(user):
		
		vpn = generate_user_agent()
		
		headers = {
		
        "content-type" : "application/json",
        
        "User-agent" :str(vpn)}
       
		URL = 'https://www.instagram.com/'+str(user)+'/?__a=1'
		
		response = requests.get(url=URL, headers=headers).json()
		
		try:
			
			return str(response['graphql']['user']['edge_followed_by']['count'])
			
		except:
			
			return ("Error account is security")
			
	def following(user):
		
		vpn = generate_user_agent()
		
		headers = {
		
        "content-type" : "application/json",
        
        "User-agent" :str(vpn)}
       
		URL = 'https://www.instagram.com/'+str(user)+'/?__a=1'
		
		response = requests.get(url=URL, headers=headers).json()
		
		try:
			
			return str(response['graphql']['user']['edge_follow']['count'])
			
		except:
			
			return ("Error account is security")
		
	def posts(user):
		
		vpn = generate_user_agent()
		
		headers = {
		
        "content-type" : "application/json",
        
        "User-agent" :str(vpn)}
       
		URL = 'https://www.instagram.com/'+str(user)+'/?__a=1'
		
		response = requests.get(url=URL, headers=headers).json()
		
		try:
			
			return str(response['graphql']['user']['edge_owner_to_timeline_media']['count'])
			
		except:
			
			return ("Error account is security")
			
	def id(user):
		
		vpn = generate_user_agent()
		
		headers = {
		
        "content-type" : "application/json",
        
        "User-agent" :str(vpn)}
       
		URL = 'https://www.instagram.com/'+str(user)+'/?__a=1'
		
		response = requests.get(url=URL, headers=headers).json()
		
		try:
			
			return str(response['graphql']['user']['id'])
			
		except:
			
			return ("Error account is security")
			
	def name(user):
		
		vpn = generate_user_agent()
		
		headers = {
		
        "content-type" : "application/json",
        
       "User-agent" :str(vpn)}
       
		URL = 'https://www.instagram.com/'+str(user)+'/?__a=1'
		
		response = requests.get(url=URL, headers=headers).json()
		
		try:
		
			return str(response['graphql']['user']['full_name'])
			
		except:
			
			return ("Error account is security")
		
	def data(user):
		
		vpn = generate_user_agent()
		
		headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cookie': 'csrftoken='+str(secrets.token_hex(8)*2)+'; sessionid='+str(secrets.token_hex(8)*2)+';',
        'user-agent': str(vpn)}
       
		URL = 'https://www.instagram.com/'+str(user)+'/?__a=1'
		
		response = requests.get(url=URL, headers=headers).json()
		
		idd = str(response['logging_page_id']).split('_')[1]
		
		urld = "https://o7aa.pythonanywhere.com/?id="+str(idd)
		
		hadd = {
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
       'Connection': 'keep-alive',
       'Host': 'o7aa.pythonanywhere.com',
       'User-Agent': str(vpn)} 
      
		GOOD = requests.get(urld,headers=hadd).json() 
		
		
		
		try:
			
			return str(GOOD["data"])
			
		except:
			
			return ("Error account is security")
			
	#print
	