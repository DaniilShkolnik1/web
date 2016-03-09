git config --global user.email "subfear@mail.ru"                              
git config --global user.name "pteacher"   

sudo service mysql start
mysql -uroot -e "create database qadb"
sudo /home/box/web/ask/manage.py syncdb

