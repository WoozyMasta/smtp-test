# smtp-test

Dummy SMTP service for debuging (Python smtpd).

By default SMTP server listen on `0.0.0.0:25` receive any messages and writes them to the log `mail.log`

### Run service:
```
sudo ./smtp-test.py
```

### Usage:
```
usage: smtp-test.py [-h] [--host BIND_ADDRESS] [--port BIND_PORT]
                    [--logfile LOG_FILE] [--loglevel LOG_LEVEL] [-v]

Dummy smtp-test service for debuging

optional arguments:
  -h, --help            show this help message and exit
  --host BIND_ADDRESS   bind address or hostname
  --port BIND_PORT      bind port
  --logfile LOG_FILE    path to logfile
  --loglevel LOG_LEVEL  loging level
  -v, --version         show version
```

### Exapmle
```
# sudo nohup python smtp-test.py --port 2025 &
# telnet localhost 2025

telnet localhost 2025
Trying ::1...
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
220 wmnb.wm.loc Python SMTP proxy version 0.2
MAIL FROM: fake@mail       
250 Ok
RCPT TO: another@fake
250 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.
250 Ok
MAIL FROM: fake@mail
250 Ok
RCPT TO: another@fake
250 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
Hi!
.
250 Ok
telnet> Connection closed.

# cat mail.log

2019-12-18 03:37:17,367,367 smtpd-test INFO Dummy smtp-test service for debuging started on 0.0.0.0:2025 and store logs in file 'mail.log'
2019-12-18 03:39:31,839,839 smtpd-test INFO New message received!	 From: <fake@mail>	 To: ['another@fake']
2019-12-18 03:39:31,839,839 smtpd-test DEBUG --------- Beginning of message 127.0.0.1
2019-12-18 03:39:31,839,839 smtpd-test DEBUG Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
2019-12-18 03:39:31,839,839 smtpd-test DEBUG 
2019-12-18 03:39:31,840,840 smtpd-test DEBUG --------- End of message
2019-12-18 03:40:09,261,261 smtpd-test INFO New message received!	 From: <fake@mail>	 To: ['another@fake']
2019-12-18 03:40:09,261,261 smtpd-test DEBUG --------- Beginning of message 127.0.0.1
2019-12-18 03:40:09,262,262 smtpd-test DEBUG Hi!
2019-12-18 03:40:09,262,262 smtpd-test DEBUG --------- End of message

```