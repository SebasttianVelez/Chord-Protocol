from Peer import Peer
import zmq

first = False

ctx = zmq.Context()


MyPeer = Peer(4)

if first:
    MyPeer.inicializate("tcp://*:5001","tcp://10.253.28.33:5000","tcp://*:5003")
else:
    
    client = ctx.socket(zmq.REQ)
    client.connect("tcp://10.253.28.33:5003") #Ip del servidor
    MyPeer.join(client)


while True:
    m = MyPeer.socketClient.recv_string()
    print("recibi solicitud : ",m)
    MyPeer.socketClient.send_string("ok")
