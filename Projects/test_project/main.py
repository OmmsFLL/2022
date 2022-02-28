#!/usr/bin/env pybricks-micropython
"""
Run 1
test
"""
import logging

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

import config
import pybot
from pybot.PID import PID
from pybot.timed_loop import timed_loop
from pybot.environment import Environment

log = logging.getLogger('FLL')
log.setLevel(logging.DEBUG)

# Create a PyBot Environment
env = Environment(config.LOOP_FREQUENCY)

# Brick
env.ev3 = EV3Brick()

# Initialize the motors.
env.left_motor = Motor(getattr(Port, config.LEFT_MOTOR_PORT))
env.right_motor = Motor(getattr(Port, config.RIGHT_MOTOR_PORT))

# Initialize the color sensor.
env.center_line_sensor = ColorSensor(getattr(Port, config.CENTER_COLOR_SENSOR_PORT))
env.left_line_sensor = ColorSensor(getattr(Port, config.LEFT_COLOR_SENSOR_PORT))
env.right_line_sensor = ColorSensor(getattr(Port, config.RIGHT_COLOR_SENSOR_PORT))

# Initialize the Gyro Sensor.
env.gyro = GyroSensor(getattr(Port, config.GYRO_SENSOR_PORT))

# Initialize the drive base.
env.wheels = DriveBase(
    env.left_motor, env.right_motor,
    wheel_diameter=config.WHEEL_DIAMETER,
    axle_track=config.AXLE_TRACK)


def ramp(target, start=0, ramp_time=1000):
    timer = StopWatch()
    while True:
        current_time = timer.time()
        if current_time > ramp_time:
            yield target
        else:
            yield (start + target) * (1 - (ramp_time - current_time) / ramp_time)


def move_forward(env, distance):
    rampup = ramp(-400, ramp_time=750)
    rampdown = ramp(0, start=-400, ramp_time=750)
    timer = StopWatch()
    ramping_up = True
    while True:
        if ramping_up:
            speed = next(rampup)
            if speed == -400:
                ramping_up = False
        else:
            speed = next(rampdown)
            if speed == 0:
                log.info('break')
                break
        log.info('Speed: %s' % speed)
        env.wheels.drive(speed, 0)
        yield


env.queue.append(move_forward(env, 10))
env.run()
