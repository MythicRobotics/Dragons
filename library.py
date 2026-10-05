from pybricks.parameters import Button, Stop
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_BASE, HUB, KD, KI, KP, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, TURN_KD, TURN_KI, TURN_KP
from pid_python import heading_pid
from robot_config import ACCELERATION, DRIVE_BASE, HUB, SPEED, TURN_ACCELERATION, TURN_SPEED

async def set_drivebase():
    await wait(0)
    DRIVE_BASE.settings(straight_speed=SPEED)
    DRIVE_BASE.settings(straight_acceleration=ACCELERATION)
    DRIVE_BASE.settings(turn_rate=TURN_SPEED)
    DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)

async def print_drivebase_settings():
    print('Default drivebase settings that are overridden in the config file')
    print('Speed, Acceleration, Turn, Turn Accel')
    print(DRIVE_BASE.settings())

async def  elevator_up(degrees: int, speed: int = 1000):
    await RIGHT_ATTACHMENT.run_angle(speed, degrees)

async def  elevator_down(degrees: int, speed: int = 1000):
    await RIGHT_ATTACHMENT.run_angle(speed, -degrees)

async def  elevator_left(degrees: int, speed: int = 1000):
    await LEFT_ATTACHMENT.run_angle(speed, degrees)

async def  elevator_right(degrees: int, speed: int = 1000):
    await LEFT_ATTACHMENT.run_angle(speed, -degrees)

async def drive_turn_right(degrees: int):
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(degrees, Stop.BRAKE, wait=True)

async def drive_turn_left(degrees: int):
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-degrees, Stop.BRAKE, wait=True)


async def drive_straight_forward(distance: int):
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(distance, then=Stop.BRAKE)    


async def drive_straight_backward(distance: int):
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-distance, then=Stop.BRAKE)    


async def telemetry():
    while True:
        await wait(0)
        await wait(100)
        print(DRIVE_BASE.angle())

async def E_stop():
    await wait(1000)
    while True:
        await wait(0)
        if Button.CENTER in HUB.buttons.pressed():
            raise SystemExit