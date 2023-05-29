import os
import sys
import xmlrpc.client

#Put your server IP here



url = 'http://{}:{}'.format("127.0.0.1",9990)
###server_proxy = xmlrpclib.Server(url)
client_server_proxy = xmlrpc.client.ServerProxy(url)

curDir = os.path.dirname(os.path.realpath(__file__))
filename = input("File Name : ")
fpn = curDir + '/' + filename
print(' filename -> ({})'.format(filename))
print(' fpn -> ({})'.format(fpn))
if not os.path.exists(fpn):
    print('Missing file -> ({})'.format(fpn))
    print("Transfer Unsuccessfull")
    sys.exit(1)

with open(fpn, "rb") as handle:
    binary_data = xmlrpc.client.Binary(handle.read())
    client_server_proxy.server_receive_file(binary_data, filename)
    print("FIle transmitted successfully..!")