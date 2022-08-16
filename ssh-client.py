import paramiko

host = "HOST_IP"
user = "USER"
psswd = "USERPASSWORD"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=psswd)

While True:
    
    stdin, stdout, stderr = client.exec_command(input("Command: "))

    for line in stdout.readlines():
        print(line.strip())
