from sshtunnel import SSHTunnelForwarder
import paramiko
from time import sleep
# Kết nối đến máy chủ 192.168.1.178 đóng vai trò là máy SSH SOCK PROXY ta kiếm được
# Sau khi kết nối thành công tạo máy tính Listen ở localhost port 8888
# Thực hiện kết nối đến trang web icanhazip.com để kiểm tra địa chỉ IP
publicserver = SSHTunnelForwarder(    
	'192.168.1.178',    
	ssh_username="root",    
	ssh_password="123456",    
	local_bind_address=('127.0.0.1',8888),    
	remote_bind_address=('icanhazip.com',80))

server.start()
print(server.local_bind_port)

while True:    
	sleep(1)
	print("test")