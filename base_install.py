#!/usr/bin/python

import os,time


####### Goals v0.1 ######
#Mudar Hostname
#Mudar Bash Shell
#Mudar Banner SSH
#Mudar MotD
#Mudar Vim Configs
####### Goals v0.2 ######
#Create backup old configs
#Create Git interface
#Log managment

UBUNTU_MOTD="/etc/update-motd.d/"
CENTOS_MOTD="/etc/motd"


print """
Linux Initial Script Install	

v0.1

"""

###### Entra na Home e muda Configs #######
print ("\n Configurar Bash profile,rc e aliases...\n ")

opc0=raw_input("Download bash profile? (y/n)\n")

if opc0 == "y":
	print("Entering in Home Dir...\n")
	os.system("cd $USER")
	os.system('rm .bash*')
	print("\nDownloading Bash Profile FIles...\n")
	os.system("wget https://raw.githubusercontent.com/RubenFilipe/TuxStuff/master/.bash_aliases --no-check-certificate")
	os.system("wget https://raw.githubusercontent.com/RubenFilipe/TuxStuff/master/.bashrc --no-check-certificate")
	print("Done :)")

elif opc0 == "n":
	print("\n Jumping to the next config...\n")
	time.sleep(2)



#### Configure MotD #####

print('\n Downloading MotD File...\n')

opc1=raw_input("Download MotD file? (y/n)")

if opc1 == "y":
	print("""
		1 --> CentOS
		2 --> Ubuntu
		3 --> Arch (soon)

		""")
	osopc=raw_input('Choose OS : ')
	if osopc =="1":
		print('Downloading file from Git to CentOS...')
		os.system('cd /tmp && wget https://raw.githubusercontent.com/RubenFilipe/TuxStuff/master/motd --no-check-certificate')
		os.system('mv -f motd ' + CENTOS_MOTD)
		print('MotD changed...\n')
	elif osopc== "2":
		print('Downloading file from Git to Ubuntu...')
		os.system('cd /tmp && wget https://raw.githubusercontent.com/RubenFilipe/TuxStuff/master/motd --no-check-certificate')
		os.system('mv motd ' + UBUNTU_MOTD + '01-mydefault')
		print('MotD changed...\n')		
	else:
		print('\nMore soon...')


#Modificar VIM COnfigs
print("\n Configurar opcoes VIM e adicionar templates...\n")

viopc = raw_input("\nDownload VIM Files? (y/n)\n")

if viopc == "y":
	print("\nEntering in .vim config dir...\n")
	os.system("cd $USER/.vim")
	os.system("wget http://www.#/vim_profile.tar.gz")
	os.system("tar xvfz vim_profile.tar.gz") 
elif viopc == "n":
        print("\n Jumping to the next config...\n")
        time.sleep(3)



################### SSH Configs  ####################
#Entra na Dir, Sacar Ficheiro da Web
print("Configurar parametros SSH...")

opc3=raw_input("\nDownload SSH Files? (y/n)\n")

if opc3=="y":
	print("Entering SSH Config Dir...\n")
	os.system("cd $USER/.ssh")
	print("\nDownload Files...\n")
	try:
		os.system("wget http://www.#/ssh_profile.tar.gz")
	except Exception, e:
		raise e
		print('Error downloading package!')
	try:
		os.system("tar xvfz ssh_profile.tar.gz")
	except Exception, e:
		raise e
		print('Nothing to extract!')
	
	os.system("echo 'Banner /etc/banner' >> /etc/ssh/sshd_config")
	os.system("cd /etc && wget https://raw.githubusercontent.com/RubenFilipe/TuxStuff/master/banner --no-check-certificate")
elif opc3=="n":
	print("\nJumping to the next config...\n")
	time.sleep(3)
else :
	print("Option Invalid...")



############# FIM SSH CONFIGS ########################

#Init Bash
opc = raw_input("Bash Reload? (y/n)\n")
if opc == "y":
	os.system("bash")
elif opc == "n":
	print("Nothing to do, move along!")

else:
	print("\nOption Wrong!")


