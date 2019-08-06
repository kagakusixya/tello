import socket
import time



def main():
    tello_ip = '192.168.10.1'
    tello_port = 8889

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tello_address = (tello_ip , tello_port)

    s.sendto('command'.encode('utf-8'),tello_address)

    s.sendto('land'.encode('utf-8'),tello_address)
    print("land")






if __name__ == '__main__':
    main()
