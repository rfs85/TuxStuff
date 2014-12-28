###.bash_aliases file ######

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
