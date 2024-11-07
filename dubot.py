import math

# Initialize Dubot parameters with safe limits
dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, 0)
dType.SetPTPCoordinateParams(api, 200, 200, 200, 200, 0)
dType.SetPTPJumpParams(api, 10, 200, 0)
dType.SetPTPCommonParams(api, 100, 100, 0)

pos = dType.GetPose(api)
rHead = pos[3]

# define variables
coin = [(0,0),(267,65),(260,16),(262,-43)] 
stack = [(0,0),(210,65),(210,16),(210,-43)]
z_high = -10
z_gnd = -69
drop_height = 1
coin_height = 2.1

dType.SetEndEffectorSuctionCup(api, 1, 0, 1)  # Suction off

# Loop
for n in range(1,4):  # 3 coins
    for m in range(1,4):  # 3 stacks

        # move to get coin
        dType.SetPTPCmd(api, 2, coin[n][0], coin[n][1], z_high, 0, 1)
        dType.SetPTPCmd(api, 2, coin[n][0], coin[n][1], z_gnd + coin_height*(4-m), 0, 1)
        dType.SetEndEffectorSuctionCup(api, 1, 1, 1)  # Suction on
        dType.SetPTPCmd(api, 2, coin[n][0], coin[n][1], z_high, 0, 1)

        # move to place coin
        dType.SetPTPCmd(api, 2, stack[m][0], stack[m][1], z_high, 0, 1)
        dType.SetPTPCmd(api, 2, stack[m][0], stack[m][1], z_gnd + drop_height + coin_height*n, 0, 1)
        dType.SetEndEffectorSuctionCup(api, 1, 0, 1)  # Suction off
        dType.SetPTPCmd(api, 2, stack[m][0], stack[m][1], z_high, 0, 1) 

dType.SetEndEffectorSuctionCup(api, 1, 0, 1)  # Suction off