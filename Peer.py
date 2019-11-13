import zmq
ctx = zmq.Context()


class Peer:

    def __init__(self,id):
        # Id of the peer
        self.id = id

        # Sockets for comunication with the corresponding peers
        self.socketClient = ctx.socket(zmq.REP)
        self.socketPredecessor = ctx.socket(zmq.REP)
        self.socketSuccessor = ctx.socket(zmq.REQ)
        
        # Responsabilities
        self.responsabilities = []  #List of keys that the peer is responsible for managing
    
        self.fingerTable = {}
        
    
    def inicializate(self,sockP, sockS, sockC):
        '''
        Do the connections with the respective sockets
        sockP = "tcp://*:PORT"
        sockS = "tcp://IP:PORT"
        sockC = "tcp://*:PORT"
        '''
        self.socketPredecessor.bind(sockP)
        self.socketClient.bind(sockC)
        self.socketSuccessor.connect(sockS)
    
        print("Started Sockets!!")
    
    def __repr__(self):
        print( "Node with id {} and responsabilities {}".format(self.id,self.responsabilities))

    def join(self,client):
        
        client.send_string("join")
        m = client.recv_string()
        print("se recibió mi solicitud")

    
    def getId(self):
        return self.id

    def calculateResponsabilities(self):

        self.responsabilities = []

        self.socketPredecessor.send_string("getId")
        m = self.socketPredecessor.recv()

        for i in range(  m.decode('utf-8')+1, self.id + 1   ):
            self.responsabilities.append(i)



    