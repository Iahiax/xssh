import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname="ssh.pythonanywhere.com", username="xyahyax", password="Yahia-1411")

stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.read().decode())

ssh.close()
