#!/usr/bin/python

import socket,sys

if len(sys.argv) <= 1:
     print "Modo De Uso:"
     print "Exemplo: ./resolver.py alvo.com"

elif len(sys.argv) >= 3:
     print "Erro limite de argumentos e 1!"

else:
     host = sys.argv[1]
     d = socket.gethostbyname(host)
     print host,"-->",d
