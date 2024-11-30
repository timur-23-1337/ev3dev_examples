#!/usr/bin/env pybricks-micropython
#--------------------------------------------------------------------------
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
#from pybricks.ev3devices import ColorSensor
from pybricks.nxtdevices import LightSensor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
#--------------------------------------------------------------------------
ev3 = EV3Brick()
left_motor, right_motor = Motor(Port.B), Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=160)
color1 = LightSensor(Port.S2)
color2 = LightSensor(Port.S3)
#--------------------------------------------------------------------------
integral = 0
lastError = 0
coefficient = 0.3
speed = 55
#--------------------------------------------------------------------------
while True:
    eq1 = color1.reflection() - color2.reflection()
    eq2 = integral * coefficient + eq1
    integral = eq2
    eq3 = eq1 - lastError
    lastError = eq1
    eq4 = eq1 * 2 + eq2 * 0.2 + eq3 * 15
    robot.drive(speed, eq4 * 0.8)
#--------------------------------------------------------------------------
