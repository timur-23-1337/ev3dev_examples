#!/usr/bin/env pybricks-micropython
#--------------------------------------------------------------------------
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Color, Stop
from pybricks.messaging import BluetoothMailboxServer, TextMailbox, NumericMailbox
from pybricks.media.ev3dev import Font, ImageFile
from pybricks.tools import wait
#--------------------------------------------------------------------------
ev3 = EV3Brick()
font_size = Font(size=16)
ev3.screen.set_font(font_size)
server = BluetoothMailboxServer()
mbox = TextMailbox('com',server)
stats = NumericMailbox('num',server)
#--------------------------------------------------------------------------
add_mtrs = is_break = angle = curr_angle = ignore = 0
speed, turn = 500.0, 70.0
#--------------------------------------------------------------------------
ev3.screen.print('Waiting for connection...', sep=' ', end='\n')
server.wait_for_connection()
#--------------------------------------------------------------------------
ev3.speaker.beep(500, 200)
ev3.screen.clear()
ev3.screen.print('Waiting for' ,'DriveBase command...', sep='\n', end='\n')
mbox.wait()
command = mbox.read()
#--------------------------------------------------------------------------
if command == 'DB_AB':
    left_motor, right_motor = Motor(Port.A), Motor(Port.B)
    robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=160)
elif command == 'DB_BC':
    left_motor, right_motor = Motor(Port.B), Motor(Port.C)
    robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=160)
elif command == 'DB_CD':
    left_motor, right_motor = Motor(Port.C), Motor(Port.D)
    robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=160)
elif command == 'DB_AD':
    left_motor, right_motor = Motor(Port.A), Motor(Port.D)
    robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=160)
elif command == 'DB_AC':
    left_motor, right_motor = Motor(Port.A), Motor(Port.C)
    robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=160)
elif command == 'DB_BD':
    left_motor, right_motor = Motor(Port.B), Motor(Port.D)
    robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=160)
#--------------------------------------------------------------------------
ev3.screen.clear()
ev3.screen.print('Awaiting for', 'additional motors', 'command', sep='\n', end='\n')
mbox.wait()
command = mbox.read()
#--------------------------------------------------------------------------
if command == 'AddA':
    additional1 = Motor(Port.A)
    add_mtrs = 1
elif command == 'AddB':
    additional1 = Motor(Port.B)
    add_mtrs = 1
elif command == 'AddC':
    additional1 = Motor(Port.C)
    add_mtrs = 1
elif command == 'AddD':
    additional1 = Motor(Port.D)
    add_mtrs = 1
elif command == 'AddAB':
    additional1, additional2 = Motor(Port.A), Motor(Port.B)
    add_mtrs = 2
elif command == 'AddBC':
    additional1, additional2 = Motor(Port.B), Motor(Port.C)
    add_mtrs = 2
elif command == 'AddCD':
    additional1, additional2 = Motor(Port.C), Motor(Port.D)
    add_mtrs = 2
elif command == 'AddAD':
    additional1, additional2 = Motor(Port.A), Motor(Port.D)
    add_mtrs = 2
elif command == 'AddAC':
    additional1, additional2 = Motor(Port.A), Motor(Port.C)
    add_mtrs = 2
elif command == 'AddBD':
    additional1, additional2 = Motor(Port.B), Motor(Port.D)
    add_mtrs = 2
#--------------------------------------------------------------------------
ev3.screen.clear()
ev3.screen.load_image(ImageFile.EV3_ICON)
wait(100)
#--------------------------------------------------------------------------
while True:
    mbox.wait()
    command = mbox.read()
    ev3.light.on(Color.GREEN)
    #--------------------------------------------------------------------------
    if command == 'center':
        while True:
            #--------------------------------------------------------------------------
            robot.stop()
            ev3.light.on(Color.RED)
            mbox.wait_new()
            command = mbox.read()
            #--------------------------------------------------------------------------
            if command == 'exit':
                break
            elif command == 'set_speeds':
                stats.wait()
                set_speed = stats.read()
                speed = set_speed
                stats.wait()
                set_turn = stats.read()
                turn = set_turn
            elif command == 'shutdown':
                quit()
    #--------------------------------------------------------------------------
    if command == 'none':
        robot.stop()
        continue
    #--------------------------------------------------------------------------
    elif command == 'add1_pos':
        additional1.run_time(speed,200,then=Stop.COAST,wait=False)  
    elif command == 'add2_pos':
        additional2.run_time(speed,200,then=Stop.COAST,wait=False) 
    elif command == 'add1_neg':
        additional1.run_time(-speed,200,then=Stop.COAST,wait=False)  
    elif command == 'add2_neg':
        additional2.run_time(-speed,200,then=Stop.COAST,wait=False) 
    #--------------------------------------------------------------------------
    elif command == 'left_up':
        robot.drive(speed, turn)
        continue
    #--------------------------------------------------------------------------
    elif command == 'right_up':
        robot.drive(speed, -turn)
        continue
    #--------------------------------------------------------------------------
    elif command == 'left_down':
        robot.drive(-speed, -turn)
        continue
    #--------------------------------------------------------------------------
    elif command == 'right_down':
        robot.drive(-speed, turn)
        continue
    #--------------------------------------------------------------------------
    elif command == 'up':
        robot.drive(speed, 0)
        continue
    #--------------------------------------------------------------------------
    elif command == 'down':
        robot.drive(-speed, 0)
        continue
    #--------------------------------------------------------------------------
    elif command == 'left':
        robot.drive(0, turn)
        continue
    #--------------------------------------------------------------------------
    elif command == 'right':
        robot.drive(0, -turn)
        continue
    #--------------------------------------------------------------------------
    elif command == 'turn_left':
        robot.turn(turn)
        continue
    #--------------------------------------------------------------------------
    elif command == 'turn_right':
        robot.turn(-turn)
        continue
