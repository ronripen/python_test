import paramiko as p
import sys

nbytes = 4096
hostname = '192.168.1.199'
port = 22
username = 'ron'
password = 'rootroot'
command = 'echo "hello :)"'

client = p.Transport(hostname, port)
client.connect(username=username, password=password)
# ssh = p.SSHClient()
# ssh.set_missing_host_key_policy(p.AutoAddPolicy())
# ssh.connect(hostname, port, username, password)
#
session = client.open_channel(kind='session')
session.exec_command(command)

stdout = session.recv(nbytes)
stderr = session.recv_stderr(nbytes)

session.close()
client.close()

print(stdout)
print(stderr)



