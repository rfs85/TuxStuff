#!/usr/bin/python

import os,time


print """
CentOS Initial Script Install   

v0.1

"""

#Mudar Hostname
#/etc/sysconfig/network
#Mudar Banner
#Mudar MotD
os.system("cat /etc/motd")

###### Entra na Home e muda Configs #######
print ("\n Configurar Bash profile,rc e aliases...\n ")

opc1=raw_input("Download bash profile? (y/n)\n")

if opc1 == "y":
        print("Entering in Home Dir...\n")
        os.system("cd $USER")
        print("\nDownloading Bash Profile FIles...\n")
        os.system("wget https://raw.githubusercontent.com/RubenFilipe/TuxStuff/master/.bash_aliases")
        os.system("wget https://raw.githubusercontent.com/RubenFilipe/TuxStuff/master/.bashrc")
        print("Done :)")

elif opc1 == "n":
        print("\n Jumping to the next config...\n")
        time.sleep(3)

#Modificar VIM COnfigs
print("\n COnfigurar opcoes VIM e adicionar templates...\n")

opc2 = raw_input("\nDownload VIM Files? (y/n)\n")

if opc2 == "y":
        print("\nEntering in .vim config dir...\n")
        os.system("cd $USER/.vim")
        os.system("wget http://www.files.binarymedia.pt/vim_profile.tar.gz")
        os.system("tar xvfz vim_profile.tar.gz")
elif opc2 == "n":
        print("\n Jumping to the next config...\n")
        time.sleep(3)



################### SSH Configs  ####################
#Entra na Dir, Sacar Ficheiro da Web
print("Configurar  Acessos SSH...")

opc3=raw_input("\nDownload SSH Files? (y/n)\n")

if opc3=="y":
        print("Entering SSH Config Dir...\n")
        os.system("cd $USER/.ssh")
        print("\nDownload Files...\n")
        os.system("wget http://www.#.pt/ssh_profile.tar.gz")
        os.system("tar xvfz ssh_profile.tar.gz")
        os.system("cd /etc && echo 'Banner /etc/banner' >> /etc/ssh/sshd_config")
        os.system("wget https://raw.githubusercontent.com/RubenFilipe/TuxStuff/master/banner")
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


        
