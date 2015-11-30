###.bashrc file ###


#Modificar prompt do Terminal - user@hostname[dir]
export PS1="\[\e[00;33m\]$USER\[\e[0m\]\[\e[00;37m\]@\h:\[\e[0m\]\[\e[00;36m\][\w]:\[\e[0m\]\[\e[00;37m\] \[\e[0m\]"

#Carregar ficheiro de Aliases
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
