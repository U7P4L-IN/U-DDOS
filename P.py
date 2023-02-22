#!/usr/bin/python2
#coding=utf-8

import os
import sys
import time

def slowprint(s):
    try:
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.001)
    except (KeyboardInterrupt, EOFError):
        run('Nonaktif!!!')

load = ('''
\033[1;92m    __                    ___
   / /   ____  ____ _____/ (_)___  ____ _
  / /   / __ \/ __ `/ __  / / __ \/ __ `/
 / /___/ /_/ / /_/ / /_/ / / / / / /_/ / _ _
/_____/\____/\__,_/\__,_/_/_/ /_/\__, (_|_|_)
                                /____/\033[1;97m
''')

logo = ('''

   ###    ##       ##                                
  ## ##   ##       ##                                
 ##   ##  ##       ##                                
##     ## ##       ##                                
######### ##       ##                                
##     ## ##       ##                                
##     ## ######## ########                          
                                                                                                                    
      ########  #######   #######  ##        ######  
         ##    ##     ## ##     ## ##       ##    ## 
         ##    ##     ## ##     ## ##       ##       
         ##    ##     ## ##     ## ##        ######  
         ##    ##     ## ##     ## ##             ## 
         ##    ##     ## ##     ## ##       ##    ## 
         ##     #######   #######  ########  ######  
                             |lolcat
\033[1;99m╔════════════════════════════════════════════════════════════════════╗    
\033[1;92m█ \033[1;91m##     ##\033[1;93m ######### \033[1;94m########  \033[1;95m##        \033[1;32m##           \033[1;91m#### \033[1;93m##    ## \033[1;92m█
\033[1;93m█ \033[1;91m##     ##\033[1;93m ##    ##  \033[1;94m##     ## \033[1;95m##    ##  \033[1;32m##            \033[1;91m##  \033[1;93m###   ## \033[1;93m█
\033[1;94m█ \033[1;91m##     ##\033[1;93m      ##   \033[1;94m##     ## \033[1;95m##    ##  \033[1;32m##            \033[1;91m##  \033[1;93m####  ## \033[1;94m█ 
\033[1;95m█ \033[1;91m##     ##\033[1;93m     ##    \033[1;94m########  \033[1;95m##    ##  \033[1;32m##       \033[1;94m###  \033[1;91m##  \033[1;93m## ## ## \033[1;95m█
\033[1;96m█ \033[1;91m##     ##\033[1;93m    ##     \033[1;94m##        \033[1;95m######### \033[1;32m##            \033[1;91m##  \033[1;93m##  #### \033[1;96m█ 
\033[1;97m█ \033[1;91m##     ##\033[1;93m   ##      \033[1;94m##        \033[1;95m      ##  \033[1;32m##            \033[1;91m##  \033[1;93m##   ### \033[1;97m█ 
\033[1;91m█  \033[1;91m####### \033[1;93m  ##       \033[1;94m##        \033[1;95m      ##  \033[1;32m#########    \033[1;91m#### \033[1;93m##    ## \033[1;91m█ 
\033[1;99m╚════════════════════════════════════════════════════════════════════╝
[+]====================================================[+]
[+] CREATED BY   :  U7P4L IN                           [+]
[+] COUNTRY      :  BANGLADESH                         [+]
[+] ON GITHUB    :  U7P4L-IN                           [+]
[+] TOOL STATUS  :  MY ALL TARMUX TOOLS                [+]
[+] TOOL VERSION :  V0.0.5G PRO                        [+]
[+]====================================================[+]
-------------\033[1;93m[\033 Menu tools \033[1;93m]\033[1;97m-------------

\033[1;93m[\033[1;97m1\033[1;93m]\033[1;97m  Tramux Besic All Package Set Up
\033[1;93m[\033[1;97m2\033[1;93m]\033[1;97m  Tarmux Header Animation Banner
\033[1;93m[\033[1;97m3\033[1;93m]\033[1;97m  Tarmux Stylish Theme & Front
\033[1;93m[\033[1;97m4\033[1;93m]\033[1;97m  Python To Marshal Encrypting
\033[1;93m[\033[1;97m5\033[1;93m]\033[1;97m  Fb Brute Force Attack 
\033[1;93m[\033[1;97m6\033[1;93m]\033[1;97m  Android Infect Vairus
\033[1;93m[\033[1;97m0\033[1;93m]\033[1;97m  log out

----------------------------------------
''')

def x():
	os.system('clear')
	print(load)
	os.system('git clone --depth=1 https://github.com/U7P4L-IN/SET-UP.git')
	os.chdir('SET-UP')
	os.system('git pull')
	os.system('python SET-ALL.py')
	
def xx():
	os.system('clear')
	print(load)
	os.system('git clone https://github.com/U7P4L-IN/Banner.PHP.git')
	os.chdir('Banner.PHP')
	os.system('git pull')
	os.system('php Adv.php')
	
def xxx():
	os.system('clear')
	print(load)
	os.system('git clone https://github.com/U7P4L-IN/Theme.git')
	os.chdir('Theme')
	os.system('git pull')
	os.system('bash Theme.sh')
	
def xxxx():
	os.system('clear')
	print(load)
	os.system('git clone --depth=1 https://github.com/U7P4L-IN/ENC_PY3.git')
	os.chdir('ENC_PY3')
	os.system('git pull')
	os.system('python2 ENC_PY3.py')
	
def xxxxx():
	os.system('clear')
	print(load)
	os.system('git clone --depth=1 https://github.com/U7P4L-IN/FB-BRUTE.git')
	os.chdir('FB-BRUTE')
	os.system('git pull')
	os.system('python3 FB.py or python FB2.py')
	
def xxxxxx():
	os.system('clear')
	print(load)
	os.system('git clone https://github.com/U7P4L-IN/INFECT.git')
	os.chdir('INFECT')
	os.system('git pull')
	os.system('bash INFECT.sh')
	

def masuk():
	os.system('clear')
	slowprint(logo)
	pilih()
	
def pilih():
	pahrul = raw_input('(+) choose : ')
	if pahrul == "":
		print ("")
		print "(+) What are you typing, man? !!!"
		exit()
	elif pahrul == "1":
		x()
	elif pahrul == "2":
		xx()
	elif pahrul == "3":
		xxx()
	elif pahrul == "4":
		xxxx()
	elif pahrul == "5":
		xxxxx()
	elif pahrul == "6":
		xxxxxx()
	elif pahrul == "0":
		exit()
	else:
		print ("")
		print "(+) What are you typing, man? !!!"
		exit()
		
masuk()
