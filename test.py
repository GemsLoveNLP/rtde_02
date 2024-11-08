import socket, time, math

# UR test

# define IP, port
robot = '10.10.0.61'   # from robot
port = 30003
gripper_port  = 63352

#####################################################################################################################
#Establish connection to controller
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((robot, port))
print("Connected")

g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
g.connect((robot, gripper_port))
print("Connected")
#####################################################################################################################
# Set default values
rx = 0
ry = -math.pi
rz = 0
z_high = 200/1000
z_low = 10/1000
####################################################################################################################

# movel simplified
def move(arm,pos):
    x,y,z,rx,ry,rz = pos
    byte = f"movel(p[{x},{y},{z},{rx},{ry},{rz}],1,0.25,0,0)\n".encode('utf-8')
    arm.send(byte)
    time.sleep(2)
    return

# square of 40 mm sides
def square(s):
    # bottom left
    move(s, [-27/1000,-370/1000,z_high,rx,ry,rz])
    # bottom right
    move(s, [-67/1000,-370/1000,z_high,rx,ry,rz])
    # top right
    move(s, [-67/1000,-410/1000,z_high,rx,ry,rz])
    # top left
    move(s, [-27/1000,-410/1000,z_high,rx,ry,rz])
    # bottom left
    move(s, [-27/1000,-370/1000,z_high,rx,ry,rz])

# pick and place from (x,y) to target (x_target,y_target)
def pickNplace(arm, gripper, x, y, x_target, y_target):
    # open
    gripper.send(b"SET POS 0\n")

    # move to pick
    move(arm, [x, y, z_high, rx, ry, rz])
    # lower to pick
    move(arm, [x, y, z_low, rx, ry, rz])
    # grip
    gripper.send(b"SET POS 255\n")
    time.sleep(1)
    # lift
    move(arm, [x, y, z_high, rx, ry, rz])

    # move to place
    move(arm, [x_target, y_target, z_high, rx, ry, rz])
    # lower to place
    move(arm, [x_target, y_target, z_low, rx, ry, rz])
    # open
    gripper.send(b"SET POS 0\n")
    time.sleep(1)
    # lift
    move(arm, [x_target, y_target, z_high, rx, ry, rz])

    print(x,y,x_target,y_target)
    move(arm, [x_target, y_target, z_high, rx, ry, rz])
    return 

# main
def main():
    # gripper example
    g.send(b'SET ACT 1\n')
    time.sleep(3)
    g.send(b'SET GTO 1\n')
    g.send(b'SET SPE 255\n')
    g.send(b'SET POS 0\n')

    # run the 40mm square twice
    for _ in range(2):
       square(s)

    # coordinate of first block
    x1 = -29.2/1000
    y1 = -302.1/1000

    # coordinate of second block
    x2 = -98.8/1000
    y2 = -405.89/1000

    # pick and place from 1 to 2
    pickNplace(s,g,x1,y1,x2,y2)


if __name__ == '__main__': 
    main()

