import socket, time, math


# define IP, port
robot = '10.10.0.61'   # from robot
arm_port = 30003
gripper_port  = 63352
# host = socket.gethostbyname(socket.gethostname()) # or from vision
host = "localhost"
vision_port = 3000 # from vision

# define camera offset
x_offset = 0
y_offset = 0

# coord
x_target = -200/1000
y_target = -350/1000
x_home = 77/1000
y_home = -300/1000
z_high = 0.1
z_low = 0.05
rx = 0
ry = -math.pi
rz = 0

#####################################################################################################################
# Establish connection to robot
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
a.connect((robot, arm_port))
print("Arm Connected")

# Establish connection to gripper
g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
g.connect((robot, gripper_port))
print("Gripper Connected")

# Establish connection to Vision Builder
v = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
v.bind((host,vision_port))
print(f"Host: {host}, Port: {vision_port}")
#####################################################################################################################

def move(arm,pos):
    x,y,z,rx,ry,rz = pos
    byte = f"movel(p[{x},{y},{z},{rx},{ry},{rz}],1,0.25,0,0)\n".encode('utf-8')
    arm.send(byte)
    time.sleep(2)
    return


def pickNplace(arm, gripper, x, y, x_target, y_target):
    # home
    move(arm, [x_home, y_home, z_high, rx, ry, rz])
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
    return True


def main():
    # gripper activate
    g.send(b'SET ACT 1\n')
    time.sleep(3)
    g.send(b'SET GTO 1\n')
    g.send(b'SET SPE 255\n')
    g.send(b'SET POS 0\n')

    # wait for Vision Builder
    v.listen(1)
    print("Server is waiting for a connection...")
    while True:
        conn, addr = v.accept()
        print(f"Connected by: {addr}")

        while True:
            # check bad data
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode()

            # check correct format
            if data[0] != "[" or data[-1] != "]":
                continue
            
            # extract data
            lst = data[1:-1].split(",")

            # transform x,y to robot's base frame
            x = float(lst[0])/1000 + x_offset
            y = float(lst[1])/1000 + y_offset

            # pick and place
            if pickNplace(a,g,x,y,x_target,y_target):
                break
        conn.close()
        break
    return


if __name__ == '__main__': 
    main()