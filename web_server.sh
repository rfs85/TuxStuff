
###Apache
sudo apt-get install apache2
sudo service apache2 restart

###PHP
sudo apt-get install php5 libapache2-mod-php5
sudo apt-get install php5-cli
sudo apt-get install php5-mysql

###SSH Server
sudo apt-get install openssh-server
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.original
sudo chmod a-w /etc/ssh/sshd_config.original
ssh-keygen -t rsa

