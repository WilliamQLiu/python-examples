# Send a sample message to logstash

import socket
import json
import sys

HOST = 'localhost'
PORT = 5000

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(1)

try:
    sock.connect((HOST, PORT))
except socket.error, msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(2)

msg = {'@message': 'python test message, hello there', '@tags': ['python', 'test']}

sock.send(json.dumps(msg))

sock.close()
sys.exit(0)
