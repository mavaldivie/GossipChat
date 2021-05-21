import socket
import random
import time
import threading
import argparse

class Node:
    def __init__(self, name, port, neighbors = None):
        self.name = name
        self.host = 'localhost'
        self.port = port
        self.address = (self.host, self.port)

        if neighbors:
            self.neighbors = [(self.host, i) for i in neighbors]
        else:
            self.neighbors = []
        self.messages = []

        self.node = socket.socket(type=socket.SOCK_DGRAM)
        self.node.bind(self.address)

        self.gossip(f'{self.name} has joined the net'.encode('utf8'), self.neighbors.copy())

        threading.Thread(target=self.receive).start()
        threading.Thread(target=self.sendFromInput).start()
        #self.sendFromInput()


    def sendFromInput(self):
        while True:
            msg = input()
            msg = f'{self.name}: {msg}'.encode('utf8')
            healthy = [i for i in self.neighbors]
            threading.Thread(target=self.gossip, args=(msg, healthy,)).start()
            #self.gossip(msg, healthy)

    def receive(self):
        while True:
            msg, client = self.node.recvfrom(1024)
            if msg in self.messages: continue

            self.messages.append(msg)
            print(msg.decode('utf8'))

            time.sleep(1)
            healthy = [i for i in self.neighbors if i != client]
            threading.Thread(target=self.gossip, args=(msg, healthy,)).start()

    def gossip(self, msg, healthy):
        while healthy:
            neighbor = random.choice(healthy)
            healthy.remove(neighbor)

            self.node.sendto(msg, neighbor)
            time.sleep(1)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True, help='File with .txt extension where ports are located')
    args = parser.parse_args()

    fd = open(f'{args.name}.txt', 'r')
    arr = []
    for i in fd.read().split('\n'):
        if str.isnumeric(i):
            arr.append(int(i))
    fd.close()

    port, neighbors = arr[0], arr[1:]

    client = Node(args.name, port, neighbors)


if __name__ == '__main__':
    main()