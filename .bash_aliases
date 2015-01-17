###.bash_aliases file ######

alias install='sudo yum -y install'
alias upgrade='sudo yum -y upgrade'
alias update='sudo yum -y update'

##Directorios
alias projectos='cd /run/media/$USER/Data/Projetos'
alias wardrive='cd /run/media/$USER/Data/Projetos/Projecto_WarDriving/Projecto'
alias downloads='cd /home/$USER/Downloads'
alias desk='cd /home/$USER/Desktop'
alias grep='grep --color=auto'
alias ls='ls -aF --color=always'
alias root='sudo su'
alias home='cd ~'
alias cls='clear'
alias untar='tar -xvvf'
alias myip="lynx -dump -hiddenlinks=ignore -nolist http://checkip.dyndns.org:8245/ | awk '{ print \$4 }' | sed '/^$/d; s/^[ ]*//g; s/[ ]*$//g'"
alias androidsdk='cd /home/synman/Android/adt-bundle-linux-x86_64-20140702/eclipse && ./eclipse'
alias who='echo You Chancellor!'
alias forwhat='echo To Rule Them all Chancellor!'
alias when='echo Soon...'
alias ary='cd /run/media/synman/Data/Projetos/Projecto_Ary'
alias aptana='cd /home/synman/Downloads/Aptana_Studio_3 && bash AptanaStudio3.sh'
alias dev='cd /var/www/html'
alias vi='vim'
alias apachetart='sudo apachectl start'
alias apacherestart='sudo apachectl restart'


#Alias de atalhos
alias cls='clear'
alias vi='vim'

#Alias para edição rapidas das configd Bash
alias editbash='cd ~ && vi .bashrc'
alias editalias='cd ~ && vi .bash_aliases'
alias editprofiles='cd ~ && vi .bash_profiles'

#Atalhos
alias home='cd ~'
alias master='sudo su'
alias etc='cd /etc'
alias update='apt-get update'
alias upgrade='apt-get upgrade'
alias install='apt-get install '
alias temp='cd /var/tmp'

#Gestao de Logs
alias logs='cd /var/log'
alias logsh='journalctl -u sshd | tail -100'

##Wifi Networks
alias wifi_mon='sudo airmon-ng start wlp0s19f5u9'
alias wifi_scan='sudo airodump-ng mon0'

##Ligar Servidores
alias tugaspider='ssh tugaspider'
alias tugaweb='ssh tugaweb'
alias tugachat='ssh tugachat '
alias tugamail='ssh tugamail'
