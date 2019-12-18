#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2019 WoozyMasta <woozy.masta@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
#  Dummy smtp-test service for debuging

import asyncore
import argparse
import logging
import smtpd
import sys 

bind_address = '0.0.0.0'
bind_port = 25
log_file = 'mail.log'
description = "Dummy smtp-test service for debuging"

parser = argparse.ArgumentParser(description=description)
parser.add_argument('--host', dest='bind_address', help='bind address or hostname')
parser.add_argument('--port', dest='bind_port', type=int, help='bind port')
parser.add_argument('--logfile', dest='log_file', help='path to logfile')
parser.add_argument('--loglevel', dest='log_level', help='loging level')
parser.add_argument('-v', '--version', action='version', 
                    version='%(prog)s 1.0', help='show version')

result = parser.parse_args()
if result.bind_address:
    bind_address = result.bind_address
if result.bind_port:
    bind_port = result.bind_port
if result.log_file:
    log_file = result.log_file

log = logging.getLogger('smtpd-test')
logopts = { 'filename': log_file,
        'filemode': 'a',
        'format': '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'}

if result.log_level:
    logopts['level'] = result.log_level
else:
    logopts['level'] = 'DEBUG'

start_message = description + ' started on ' 
start_message += bind_address + ':' + str(bind_port)
start_message += ' and store logs in file \'' + log_file + '\''

class LoggingSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        lines = data.split('\n')
        log.info('New message received!\t From: <%s>\t To: %s', mailfrom, rcpttos)
        log.debug('--------- Beginning of message from %s', peer[0])
        for line in lines:
            log.debug(line)
        log.debug('--------- End of message')

def main():
    try:
        logging.basicConfig(**logopts)

        print(start_message)
        log.info(start_message)

        LoggingSMTPServer((bind_address, bind_port), None)
        asyncore.loop()
    except KeyboardInterrupt:
        pass
        print('\nService stoped')
        log.info('Service stoped')

    return 0

if __name__ == '__main__':
    sys.exit(main())