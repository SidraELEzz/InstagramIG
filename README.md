<h1 align="center">InstagramIG</h1>
<p align="center">It is a useful project for developers that includes useful tools for Instagram</p>

![](https://img.shields.io/badge/SidraELEzz-orange?style=for-the-badge&logo=python.svg) 
<p align="center">
<a href="#"><img title="Made in UAE" src="https://img.shields.io/badge/MADE%20IN-UAE-red.svg?style=for-the-badge&logo=github"></a>

</p>
<p align="center">
<img alt="SidraELEzz' Github Stats" src="https://github-readme-stats.vercel.app/api?username=SidraELEzz&show_icons=true&include_all_commits=true&hide_border=true" />

</p>
<p align="center">
<a href="#"><img title="telegram Num" src="https://img.shields.io/badge/telegram%20Num-SidtaTools-red.svg?style=for-the-badge&logo=telegram"></a>
</p>
<p align="center">
<a href="https://github.com/SidraELEzz/followers"><img title="Followers" src="https://img.shields.io/github/followers/SidraELEzz?color=blue&style=flat-square"></a>
</p>

## Installation :
```
pip install InstagramIG
```
### Logan Usage

``` python
from InstagramIG import SidraELEzz

username = "<your email or phone or username>"
password ="<your password >"
Logan = SidraELEzz.Instalogin(str(username),str(password))

if Logan ==True:
	print ("login successful")
	
elif Logan ==False:
	print("Error account is security")
elif deta ==None:
	print("Error account is bad")
	
```
### To get the number of followers

``` python
from InstagramIG import SidraELEzz

username = "< username >"

followers = SidraELEzz.followers(str(username))
print (followers)
	
```
### To get the number of following

``` python
from InstagramIG import SidraELEzz

username = "< username >"

following = SidraELEzz.following(str(username))
print (following)
	
```
### To get the number of posts

``` python
from InstagramIG import SidraELEzz

username = "< username >"

post = SidraELEzz.posts(str(username))
print (post)
	
```
### To get the  id

``` python
from InstagramIG import SidraELEzz

username = "< username >"

id = SidraELEzz.id(str(username))
print (id)
	
```
### To get the  name

``` python
from InstagramIG import SidraELEzz

username = "< username >"

name = SidraELEzz.name(str(username))
print (name)
	
```
### To get the target account creation date

``` python
from InstagramIG import SidraELEzz

username = "< username >"

data = SidraELEzz.data(str(username))
print (data)
	
```
### Log in with a phone number or email with all the information

``` python
from InstagramIG import SidraELEzz

username = "<your email or phone >"
password ="<your password >"
Logan = SidraELEzz.Instalogin(str(username),str(password))

if Logan ==True:
	sessionid = 'sessionid.txt'
	file = open(sessionid, "r").readline().split('\n')[0]
	username = SidraELEzz.username(str(file))
	print ("login successful")
	print(username)
	followers = SidraELEzz.followers(str(username))
	print (followers)
	following = SidraELEzz.following(str(username))
	print (following)
	post = SidraELEzz.posts(str(username))
	print (post)
	ID = SidraELEzz.id(str(username))
	print (ID)
	name = SidraELEzz.name(str(username))
	print(name)
	deat = SidraELEzz.data(str(username))
	print (deat)
elif Logan ==False:
	print("Error account is security")
elif Logan ==None:
	print("Error account is bad")
	
	
```
## Follow us on social media
[![Github](https://img.shields.io/badge/Github-SidraELEzz-orange?style=for-the-badge&logo=github)](https://github.com/SidraELEzz/)
[![Telegram](https://img.shields.io/badge/Telegram-SidraELEzz-orange?style=for-the-badge&logo=Telegram)](https://t.me/SidraTools)


