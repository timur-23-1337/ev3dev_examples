#!/usr/bin/env pybricks-micropython
#--------------------------------------------------------------------------
from pybricks.messaging import BluetoothMailboxClient, TextMailbox, NumericMailbox
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor, Motor
from pybricks.parameters import Button, Port, Color
from pybricks.tools import wait
from pybricks.media.ev3dev import Font, ImageFile
#--------------------------------------------------------------------------
ev3 = EV3Brick()
client = BluetoothMailboxClient()
mbox = TextMailbox('com', client)
stats = NumericMailbox('num',client)
l_trigger = TouchSensor(Port.S2)
r_trigger = TouchSensor(Port.S3)
#--------------------------------------------------------------------------
SERVER = 'ev3dev'
free = 'None'
double = option = mode = is_break = swap = no_add = 0
curr_angle = 0.0 
speed, turn = 500.0, 70.0
#--------------------------------------------------------------------------
font_size = Font(size=16)
ev3.screen.set_font(font_size)
ev3.screen.clear()
ev3.screen.print('Waiting for connection...', sep=' ', end='\n')
#--------------------------------------------------------------------------
client.connect(SERVER)
#--------------------------------------------------------------------------
while True:
    if option == -1:
        option = 5
    elif option == 6:
        option = 0
    #--------------------------------------------------------------------------
    if option == 0:
        ev3.screen.clear()
        ev3.screen.print('> DriveBase AB','DriveBase BC','DriveBase CD','DriveBase AD','DriveBase AC','DriveBase BD', sep='\n', end='\n')
        wait(200)
        if Button.UP in ev3.buttons.pressed():
            option = option - 1
        elif Button.DOWN in ev3.buttons.pressed():
            option = option + 1
        elif Button.CENTER in ev3.buttons.pressed():
            mbox.send('DB_AB')
            free = 'CD'
            break
    #--------------------------------------------------------------------------
    elif option == 1:
        ev3.screen.clear()
        ev3.screen.print('DriveBase AB','> DriveBase BC','DriveBase CD','DriveBase AD','DriveBase AC','DriveBase BD', sep='\n', end='\n')
        wait(200)
        if Button.UP in ev3.buttons.pressed():
            option = option - 1
        elif Button.DOWN in ev3.buttons.pressed():
            option = option + 1
        elif Button.CENTER in ev3.buttons.pressed():
            mbox.send('DB_BC')
            free = 'AD'
            break
    #--------------------------------------------------------------------------
    elif option == 2:
        ev3.screen.clear()
        ev3.screen.print('DriveBase AB','DriveBase BC','> DriveBase CD','DriveBase AD','DriveBase AC','DriveBase BD', sep='\n', end='\n')
        wait(200)
        if Button.UP in ev3.buttons.pressed():
            option = option - 1
        elif Button.DOWN in ev3.buttons.pressed():
            option = option + 1
        elif Button.CENTER in ev3.buttons.pressed():
            mbox.send('DB_CD')
            free = 'AB'
            break
    #--------------------------------------------------------------------------
    elif option == 3:
        ev3.screen.clear()
        ev3.screen.print('DriveBase AB','DriveBase BC','DriveBase CD','> DriveBase AD','DriveBase AC','DriveBase BD', sep='\n', end='\n')
        wait(200)
        if Button.UP in ev3.buttons.pressed():
            option = option - 1
        elif Button.DOWN in ev3.buttons.pressed():
            option = option + 1
        elif Button.CENTER in ev3.buttons.pressed():
            mbox.send('DB_AD')
            free = 'BC'
            break
    #--------------------------------------------------------------------------
    elif option == 4:
        ev3.screen.clear()
        ev3.screen.print('DriveBase AB','DriveBase BC','DriveBase CD','DriveBase AD','> DriveBase AC','DriveBase BD', sep='\n', end='\n')
        wait(200)
        if Button.UP in ev3.buttons.pressed():
            option = option - 1
        elif Button.DOWN in ev3.buttons.pressed():
            option = option + 1
        elif Button.CENTER in ev3.buttons.pressed():
            mbox.send('DB_AC')
            free = 'BD'
            break
    #--------------------------------------------------------------------------
    elif option == 5:
        ev3.screen.clear()
        ev3.screen.print('DriveBase AB','DriveBase BC','DriveBase CD','DriveBase AD','DriveBase AC','> DriveBase BD', sep='\n', end='\n')
        wait(200)
        if Button.UP in ev3.buttons.pressed():
            option = option - 1
        elif Button.DOWN in ev3.buttons.pressed():
            option = option + 1
        elif Button.CENTER in ev3.buttons.pressed():
            mbox.send('DB_BD')
            free = 'AC'
            break
    #--------------------------------------------------------------------------
option = 0
wait(300)
#--------
while True:
    #--------------------------------------------------------------------------
    if free == 'CD':
        #--------------------------------------------------------------------------
        if option == -1:
            option = 3
        elif option == 4:
            option = 0
        #--------------------------------------------------------------------------
        if option == 0:
            ev3.screen.clear()
            ev3.screen.print('> Set Motor C', 'Set Motor D', 'Set Motor CD', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddC')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 1:
            ev3.screen.clear()
            ev3.screen.print('Set Motor C', '> Set Motor D', 'Set Motor CD', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddD')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 2:
            ev3.screen.clear()
            ev3.screen.print('Set Motor C', 'Set Motor D', '> Set Motor CD', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddCD')
                additional1, additional2 = Motor(Port.B), Motor(Port.C)
                additional1.reset_angle(0)
                additional2.reset_angle(0)
                double = 1
                break
        #--------------------------------------------------------------------------
        elif option == 3:
            ev3.screen.clear()
            ev3.screen.print('Set Motor C', 'Set Motor D', 'Set Motor CD', '> No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                no_add = 1
                break
    #--------------------------------------------------------------------------
    elif free == 'AD':
        #--------------------------------------------------------------------------
        if option == -1:
            option = 3
        elif option == 4:
            option = 0
        #--------------------------------------------------------------------------
        if option == 0:
            ev3.screen.clear()
            ev3.screen.print('> Set Motor A', 'Set Motor D', 'Set Motor AD', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddA')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 1:
            ev3.screen.clear()
            ev3.screen.print('Set Motor A', '> Set Motor D', 'Set Motor AD', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddD')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 2:
            ev3.screen.clear()
            ev3.screen.print('Set Motor A', 'Set Motor D', '> Set Motor AD', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddAD')
                additional1, additional2 = Motor(Port.B), Motor(Port.C)
                additional1.reset_angle(0)
                additional2.reset_angle(0)
                double = 1
                break
        #--------------------------------------------------------------------------
        elif option == 3:
            ev3.screen.clear()
            ev3.screen.print('Set Motor A', 'Set Motor D', 'Set Motor AD', '> No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                no_add = 1
                break
    #--------------------------------------------------------------------------
    elif free == 'AB':
        #--------------------------------------------------------------------------
        if option == -1:
            option = 3
        elif option == 4:
            option = 0
        #--------------------------------------------------------------------------
        if option == 0:
            ev3.screen.clear()
            ev3.screen.print('> Set Motor A', 'Set Motor B', 'Set Motor AB', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddA')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 1:
            ev3.screen.clear()
            ev3.screen.print('Set Motor A', '> Set Motor B', 'Set Motor AB', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddB')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 2:
            ev3.screen.clear()
            ev3.screen.print('Set Motor A', 'Set Motor B', '> Set Motor AB', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddAB')
                additional1, additional2 = Motor(Port.B), Motor(Port.C)
                additional1.reset_angle(0)
                additional2.reset_angle(0)
                double = 1
                break
        #--------------------------------------------------------------------------
        elif option == 3:
            ev3.screen.clear()
            ev3.screen.print('Set Motor A', 'Set Motor B', 'Set Motor AB', '> No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                no_add = 1
                break
    #--------------------------------------------------------------------------
    elif free == 'BC':
        #--------------------------------------------------------------------------
        if option == -1:
            option = 3
        elif option == 4:
            option = 0
        #--------------------------------------------------------------------------
        if option == 0:
            ev3.screen.clear()
            ev3.screen.print('> Set Motor B', 'Set Motor C', 'Set Motor BC', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddB')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 1:
            ev3.screen.clear()
            ev3.screen.print('Set Motor B', '> Set Motor C', 'Set Motor BC', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddC')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 2:
            ev3.screen.clear()
            ev3.screen.print('Set Motor B', 'Set Motor C', '> Set Motor BC', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddBC')
                additional1, additional2 = Motor(Port.B), Motor(Port.C)
                additional1.reset_angle(0)
                additional2.reset_angle(0)
                double = 1
                break
        #--------------------------------------------------------------------------
        elif option == 3:
            ev3.screen.clear()
            ev3.screen.print('Set Motor B', 'Set Motor C', 'Set Motor BC', '> No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                no_add = 1
                break
    #--------------------------------------------------------------------------
    elif free == 'BD':
        #--------------------------------------------------------------------------
        if option == -1:
            option = 3
        elif option == 4:
            option = 0
        #--------------------------------------------------------------------------
        if option == 0:
            ev3.screen.clear()
            ev3.screen.print('> Set Motor B', 'Set Motor D', 'Set Motor BD', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddB')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 1:
            ev3.screen.clear()
            ev3.screen.print('Set Motor B', '> Set Motor D', 'Set Motor BD', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddD')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 2:
            ev3.screen.clear()
            ev3.screen.print('Set Motor B','Set Motor D', '> Set Motor BD', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddBD')
                additional1, additional2 = Motor(Port.B), Motor(Port.C)
                additional1.reset_angle(0)
                additional2.reset_angle(0)
                double = 1
                break
        #--------------------------------------------------------------------------
        elif option == 3:
            ev3.screen.clear()
            ev3.screen.print('Set Motor B', 'Set Motor D', 'Set Motor BD', '> No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                no_add = 1
                break
    #--------------------------------------------------------------------------
    elif free == 'AC':
        #--------------------------------------------------------------------------
        if option == -1:
            option = 3
        elif option == 4:
            option = 0
        #--------------------------------------------------------------------------
        if option == 0:
            ev3.screen.clear()
            ev3.screen.print('> Set Motor A', 'Set Motor C', 'Set Motor AC', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddA')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 1:
            ev3.screen.clear()
            ev3.screen.print('Set Motor A', '> Set Motor C', 'Set Motor AC', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddC')
                additional1 = Motor(Port.B)
                additional1.reset_angle(0)
                break
        #--------------------------------------------------------------------------
        elif option == 2:
            ev3.screen.clear()
            ev3.screen.print('Set Motor A', 'Set Motor C', '> Set Motor AC', 'No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                mbox.send('AddAC')
                additional1, additional2 = Motor(Port.B), Motor(Port.C)
                additional1.reset_angle(0)
                additional2.reset_angle(0)
                double = 1
                break
        #--------------------------------------------------------------------------
        elif option == 3:
            ev3.screen.clear()
            ev3.screen.print('Set Motor A', 'Set Motor C', 'Set Motor AC', '> No Motors', sep='\n', end='\n')
            wait(200)
            if Button.UP in ev3.buttons.pressed():
                option = option - 1
            elif Button.DOWN in ev3.buttons.pressed():
                option = option + 1
            elif Button.CENTER in ev3.buttons.pressed():
                no_add = 1
                break
        #--------------------------------------------------------------------------
#--------
wait(300)
#--------
while True:
    ev3.screen.clear()
    ev3.screen.load_image(ImageFile.EV3_ICON)
    ev3.light.on(Color.GREEN)
    #--------------------------------------------------------------------------
    if no_add == 0:
        if not (additional1.angle() == curr_angle):
            mbox.send('set_angle1')
            wait(50)
            stats.send(additional1.angle())
            wait(50)
            curr_angle = additional1.angle()
            additional1.reset_angle(curr_angle)
        elif double == 1:
            if not (additional2.angle() == curr_angle):
                mbox.send('set_angle2')
                wait(50)
                stats.send(additional2.angle())
                wait(50)
                curr_angle = additional2.angle()
    #--------------------------------------------------------------------------
    if Button.CENTER in ev3.buttons.pressed():
        mbox.send('center')
        wait(50)
        #--------------------------------------------------------------------------
        if mode == 1:
            mode = 0
            ev3.light.on(Color.GREEN)
        #--------------------------------------------------------------------------
        elif mode == 0:
            option = 0
            ev3.light.on(Color.RED)
            #--------------------------------------------------------------------------
            while True:
                if is_break == 1:
                    mode = 1
                    is_break = 0
                    break
                else:
                    is_break = 0
                if speed <= -1500.0:
                    speed = -1500.0
                elif speed >= 1500.0:
                    speed = 1500.0
                if turn <= -210.0:
                    turn= -210.0
                elif turn >= 210.0:
                    turn = 210.0
                if option == -1:
                    option = 5
                elif option == 6:
                    option = 0
                #--------------------------------------------------------------------------
                if option == 0:
                    ev3.screen.clear()
                    ev3.screen.print('Move speed: ', '>', speed, '<', sep='', end='\n')
                    ev3.screen.print('Turn speed: ', turn, sep=' ', end='\n')
                    ev3.screen.print('Set new speeds', 'Swap ctrl. mtrs.', 'Shutdown', 'Exit menu', sep='\n', end='\n')
                    wait(200)
                    if Button.UP in ev3.buttons.pressed():
                        option = option - 1
                    elif Button.DOWN in ev3.buttons.pressed():
                        option = option + 1
                    elif Button.LEFT in ev3.buttons.pressed():
                        speed = speed - 50
                    elif Button.RIGHT in ev3.buttons.pressed():
                        speed = speed + 50
                    elif l_trigger.pressed():
                        speed = -1500.0
                    elif r_trigger.pressed():
                        speed = 1500.0
                #--------------------------------------------------------------------------
                elif option == 1:
                    ev3.screen.clear()
                    ev3.screen.print('Move speed: ', speed, sep=' ', end='\n')
                    ev3.screen.print('Turn speed: ', '>', turn, '<', sep='', end='\n')
                    ev3.screen.print('Set new speeds', 'Swap ctrl. mtrs.', 'Shutdown', 'Exit menu', sep='\n', end='\n')
                    wait(200)
                    if Button.UP in ev3.buttons.pressed():
                        option = option - 1
                    elif Button.DOWN in ev3.buttons.pressed():
                        option = option + 1
                    elif Button.LEFT in ev3.buttons.pressed():
                        turn = turn - 10
                    elif Button.RIGHT in ev3.buttons.pressed():
                        turn = turn + 10
                    elif l_trigger.pressed():
                        turn = -210.0
                    elif r_trigger.pressed():
                        turn = 210.0
                #--------------------------------------------------------------------------
                elif option == 2:
                    ev3.screen.clear()
                    ev3.screen.print('Move speed: ', speed, sep=' ', end='\n')
                    ev3.screen.print('Turn speed: ', turn, sep=' ', end='\n')
                    ev3.screen.print('> Set new speeds', 'Swap ctrl. mtrs.', 'Shutdown', 'Exit menu', sep='\n', end='\n')
                    wait(200)
                    if Button.UP in ev3.buttons.pressed():
                        option = option - 1
                    elif Button.DOWN in ev3.buttons.pressed():
                        option = option + 1
                    elif Button.CENTER in ev3.buttons.pressed():
                        mbox.send('set_speeds')
                        wait(50)
                        stats.send(speed)
                        wait(50)
                        stats.send(turn)
                #--------------------------------------------------------------------------
                elif option == 3:
                    ev3.screen.clear()
                    ev3.screen.print('Move speed: ', speed, sep=' ', end='\n')
                    ev3.screen.print('Turn speed: ', turn, sep=' ', end='\n')
                    ev3.screen.print('Set new speeds', sep=' ', end='\n')
                    if double == 1:
                        if swap == 0:
                            ev3.screen.print('> Mtrs. swapped [ ]', sep=' ', end='\n')
                        elif swap == 1:
                            ev3.screen.print('> Mtrs. swapped [X]', sep=' ', end='\n')
                    else:
                        ev3.screen.print('> Unswapable', sep=' ', end='\n')
                    ev3.screen.print('Shutdown', 'Exit menu', sep='\n', end='\n')
                    wait(200)
                    if Button.UP in ev3.buttons.pressed():
                        option = option - 1
                    elif Button.DOWN in ev3.buttons.pressed():
                        option = option + 1
                    elif Button.CENTER in ev3.buttons.pressed():
                        if double == 1:
                            additional1, additional2 = additional2, additional1
                            additional1.reset_angle(0)
                            additional2.reset_angle(0)
                            if swap == 0:
                                swap = 1
                            elif swap == 1:
                                swap = 0
                #--------------------------------------------------------------------------
                elif option == 4:
                    ev3.screen.clear()
                    ev3.screen.print('Move speed: ', speed, sep=' ', end='\n')
                    ev3.screen.print('Turn speed: ', turn, sep=' ', end='\n')
                    ev3.screen.print('Set new speeds', 'Swap ctrl. mtrs.', '> Shutdown', 'Exit menu', sep='\n', end='\n')
                    wait(200)
                    if Button.UP in ev3.buttons.pressed():
                        option = option - 1
                    elif Button.DOWN in ev3.buttons.pressed():
                        option = 5
                    elif Button.CENTER in ev3.buttons.pressed():
                        mbox.send('shutdown')
                        wait(50)
                        quit()
                #--------------------------------------------------------------------------
                elif option == 5:
                    ev3.screen.clear()
                    ev3.screen.print('Move speed: ', speed, sep=' ', end='\n')
                    ev3.screen.print('Turn speed: ', turn, sep=' ', end='\n')
                    ev3.screen.print('Set new speeds', 'Swap ctrl. mtrs.', 'Shutdown', '> Exit menu', sep='\n', end='\n')
                    wait(200)
                    if Button.UP in ev3.buttons.pressed():
                        option = option - 1
                    elif Button.DOWN in ev3.buttons.pressed():
                        option = option + 1
                    elif Button.CENTER in ev3.buttons.pressed():
                        ev3.light.on(Color.GREEN)
                        wait(50)
                        mbox.send('exit')
                        is_break = 1
    #--------------------------------------------------------------------------
    if not ev3.buttons.pressed():
        if r_trigger.pressed() == l_trigger.pressed() == 1:
            mbox.send('up')
            wait(50)
        elif r_trigger.pressed():
            mbox.send('right')
            wait(50)
        elif l_trigger.pressed():
            mbox.send('left')
            wait(50)
        else:
            mbox.send('none')
            wait(50)
    #--------------------------------------------------------------------------
    elif Button.UP in ev3.buttons.pressed():
        if l_trigger.pressed():
            mbox.send('left_up')
            wait(50)
        elif r_trigger.pressed():
            mbox.send('right_up')
            wait(50)
        else:
            mbox.send('up')
            wait(50)
    #--------------------------------------------------------------------------
    elif Button.DOWN in ev3.buttons.pressed():
        if l_trigger.pressed():
            mbox.send('left_down')
            wait(50)
        elif r_trigger.pressed():
            mbox.send('right_down')
            wait(50)
        else:
            mbox.send('down')
            wait(50)
    #--------------------------------------------------------------------------
    elif Button.DOWN in ev3.buttons.pressed():
        mbox.send('down')
        wait(50)
    #--------------------------------------------------------------------------
    elif Button.LEFT in ev3.buttons.pressed():
        mbox.send('left')
        wait(50)
    #--------------------------------------------------------------------------
    elif Button.RIGHT in ev3.buttons.pressed():
        mbox.send('right')
        wait(50)