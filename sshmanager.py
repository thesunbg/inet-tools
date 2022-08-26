from socket import *

Port = 1 #First port.
Connected = False
while Port <= 65535: #Port 65535 is last port you can access.
    try:
        try:
            Socket = socket(AF_INET, SOCK_STREAM, 0) #Create a socket.
        except:
            print("Error: Can't open socket!\n")    
            break #If can't open socket, exit the loop.
        Socket.connect(("127.0.0.1", Port)) #Try connect the port. If port is not listening, throws ConnectionRefusedError. 
        Connected = True
    except ConnectionRefusedError:
        # print(f'pỏt {Port}')
        Connected = False       
    finally:
        if(Connected and Port != Socket.getsockname()[1]): #If connected,
            print("{}:{} Open \n".format("127.0.0.1", Port)) #print port.
        Port = Port + 1 #Increase port.
        Socket.close() #Close socket.