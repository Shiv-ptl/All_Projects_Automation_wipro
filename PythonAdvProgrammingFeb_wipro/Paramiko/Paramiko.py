import paramiko

host = "localhost"
port = 22
username = "lenovo"
password = "Shiv@94155@"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname = host,
    port = port,
    username = username,
    password = password
)

stdin,stdout,stdderr = client.exec_command("whoami")
client.close()