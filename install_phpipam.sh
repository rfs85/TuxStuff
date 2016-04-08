
##Update & Upgrade

apt-get update

apt-get upgrade


## Install Apache , MySQL


apt-get install -y apache2 php5 php5-mysql libapache2-mod-php5 mysql-server libgmp-dev php-pear php5-gmp php5-ldap

## Install PHP

apt-get install -y php-pear php5-dev php5-cli php5-common php5-curl php5-gmp php5-dev php5-ldap php5-gd php5-mcrypt php5-pgsql php5-xdebug

sudo service apache2 restart

aptitude install -y libapache2-mod-php5filter 

sudo service apache2 restart

##Download and move

wget http://downloads.sourceforge.net/project/phpipam/phpipam-1.1.010.tar
tar -xf phpipam-1.1.010.tar 
mv phpipam /var/www/html

a2enmod rewrite
