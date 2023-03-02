#!/usr/bin/env pybricks-micropython
#--------------------------------------------------------------------------
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.hubs import EV3Brick
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port, Color, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.media.ev3dev import ImageFile
from random import choice
#--------------------------------------------------------------------------
ev3 = EV3Brick()
timer = StopWatch()
is_pressed = 0
rotation = [100, -100]
#--------------------------------------------------------------------------
obstacle_sensor = UltrasonicSensor(Port.S2)
light_sensor = LightSensor(Port.S3)
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
turn = choice(rotation)
#--------------------------------------------------------------------------
robot = DriveBase(left_motor, right_motor, wheel_diameter=30, axle_track=170)
ev3.light.on(Color.GREEN)
ev3.screen.load_image(ImageFile.STOP_1)
#--------------------------------------------------------------------------
while True:
    if Button.CENTER in ev3.buttons.pressed():
        is_pressed = 1
        wait(1500)
        timer.reset()
    #--------------------------------------------------------------------------
    if is_pressed == 1:
        ev3.light.on(Color.GREEN)
        ev3.screen.load_image(ImageFile.EV3_ICON)
        robot.drive(0,turn)\
        #--------------------------------------------------------------------------
        while obstacle_sensor.distance() <= 650:
            if light_sensor.ambient() < 1:
                ev3.light.on(Color.YELLOW)
                robot.drive(-1500,0)
                wait(1500)
            else:
                ev3.light.on(Color.RED)
                robot.drive(1000,0)
        #--------------------------------------------------------------------------
        if timer.time() >= 30000:
            ev3.speaker.beep(500, 200)
            exit() 