
###Apache
sudo apt-get install apache2
sudo service apache2 restart

groupadd webserver
useradd -d /var/www/ -g webserver -s /bin/nologin webserver

###PHP
sudo apt-get install php5 libapache2-mod-php5 php5-cli php5-mysql


###SSH Server
sudo apt-get install openssh-server
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.original
sudo chmod a-w /etc/ssh/sshd_config.original
ssh-keygen -t rsa

