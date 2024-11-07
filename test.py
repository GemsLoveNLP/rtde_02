import socket, time


robot = '10.10.0.61'
port = 30003
gripper_port  = 63352

#####################################################################################################################
#Establish connection to controller
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((robot, port))
print("Connected")

#####################################################################################################################

g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
g.connect((robot, gripper_port))

print("Connected")

g.send(b'SET ACT 1\n')
time.sleep(3)
g.send(b'SET GTO 1\n')
g.send(b'SET SPE 255\n')
g.send(b'SET FOR 255\n')

g.send(b'SET POS 0\n')




def main():
    s.send(b"movel(p[-0.227,-0.386,0.120,0,-3.1415,0],1,0.25,0,0)\n")
    time.sleep(2)
    s.send(b"movel(p[-0.227,-0.386,0.050,0,-3.1415,0],1,0.25,0,0)\n")
    time.sleep(2)
    g.send(b"SET POS 255\n")
    time.sleep(1)
    s.send(b"movel(p[-0.227,-0.386,0.120,0,-3.1415,0],1,0.25,0,0)\n")
    time.sleep(2)

    s.send(b"movel(p[-0.207,-0.229,0.120,2.2,2.2,0],1,0.25,0,0)\n")
    time.sleep(2)
    s.send(b"movel(p[-0.207,-0.229,0.050,2.2,2.2,0],1,0.25,0,0)\n")
    time.sleep(2)
    g.send(b"SET POS 0\n")
    time.sleep(1)
    s.send(b"movel(p[-0.207,-0.229,0.120,2.2,2.2,0],1,0.25,0,0)\n")
    time.sleep(2)
    s.send(b"movel(p[-0.207,-0.229,0.050,2.2,2.2,0],1,0.25,0,0)\n")
    time.sleep(2)
    g.send(b"SET POS 255\n")
    time.sleep(1)
    s.send(b"movel(p[-0.207,-0.229,0.120,2.2,2.2,0],1,0.25,0,0)\n")
    time.sleep(2)

    s.send(b"movel(p[-0.227,-0.386,0.120,0,-3.1415,0],1,0.25,0,0)\n")
    time.sleep(2)
    s.send(b"movel(p[-0.227,-0.386,0.050,0,-3.1415,0],1,0.25,0,0)\n")
    time.sleep(2)
    g.send(b"SET POS 0\n")
    time.sleep(1)
    s.send(b"movel(p[-0.227,-0.386,0.120,0,-3.1415,0],1,0.25,0,0)\n")




if __name__ == '__main__': 
    for _ in range(3):
        main()

