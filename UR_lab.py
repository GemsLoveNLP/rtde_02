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
        # move to pick up
        s.send(b'movel(p[-0.0227, -0.32491, 0.2, 3.164, -0.052, -0.05], 1, 0.1, 0, 0)\n')
        time.sleep(2)
        # move down
        s.send(b'movel(p[-0.0227, -0.32491, 0, 3.164, -0.052, -0.05], 1, 0.1, 0, 0)\n')
        time.sleep(4)
        # grip
        g.send(b'SET POS 255\n')
        time.sleep(2)
        # lift
        s.send(b'movel(p[0.0227, -0.32491, 0.2, 3.164, -0.052, -0.05], 1, 0.1, 0, 0)\n')
        time.sleep(2)
        # move to target
        s.send(b'movel(p[0.0327, -0.32491, 0.2, 3.164, -0.052, -0.05], 1, 0.1, 0, 0)\n')
        time.sleep(2)
        # down
        s.send(b'movel(p[0.0327, -0.32491, 0, 3.164, -0.052, -0.05], 1, 0.1, 0, 0)\n')
        time.sleep(4)
        # ungrip
        g.send(b'SET POS 0\n')
        time.sleep(2)
        # return
        s.send(b'movel(p[0.0327, -0.32491, 0.2, 3.164, -0.052, -0.05], 1, 0.1, 0, 0)\n')
        # end




if __name__ == '__main__': 
    import sys
    main()

