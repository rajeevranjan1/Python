import socket
import sys

# Creating a Scocket for connecting two computers
def createSocket(): 
    try:
        global host
        global port
        global soc
        host = ''
        port = 9999
        soc=socket.socket()
    except socket.error as err:
        print("Socket not created: "+str(err))

# Binding the socket and listening for connection
def bindSocket():
    try:
        global host
        global port
        global soc
        print(f"Binding the Port {str(port)}")
        soc.bind((host,port))
        soc.listen(5)
    except socket.error as err:
        print(f"Binding Failed due to {str(err)}\nRetrying...")
        bindSocket()

# Establish connection with client: the Scoket must be listening
def socketAccept():
    conn,address=soc.accept() # Returns Tuple
    print(f"Connection established...\nIP: {address[0]}\nPort: {str(address[1])}")
    sendCommands(conn) # function to send the command
    conn.close()

# Send commands to client
def sendCommands(conn):
    while True:
        cmd = input()
        if cmd=='quit':
            conn.close()
            soc.close()
            sys.exit()
        if len(str.encode(cmd))> 0:
            conn.send(str.encode(cmd))
            clientResponse=str(conn.recv(1024),'utf-8')
            print(clientResponse)

def main():
    createSocket()
    bindSocket()
    socketAccept()

main()




