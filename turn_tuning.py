from pybricks.parameters import Button, Stop
from pybricks.tools import multitask, run_task, wait

from pid_python import heading_pid
from robot_config import ACCELERATION, DRIVE_BASE, HUB, KD, KI, KP, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, SPEED, TURN_ACCELERATION, TURN_KD, TURN_KI, TURN_KP, TURN_SPEED

async def subtask():
    print(HUB.battery.voltage())
    print(SPEED, ACCELERATION, TURN_SPEED, TURN_ACCELERATION)
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(-10, then=Stop.BRAKE)
    await DRIVE_BASE.straight(300, then=Stop.BRAKE)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    print(DRIVE_BASE.angle(), 'after straight')
    await DRIVE_BASE.turn(-90,Stop.BRAKE,wait=True)
    await wait(50)
    print(DRIVE_BASE.angle(), 'after turn 1')
    await DRIVE_BASE.turn(90,Stop.BRAKE,wait=True)
    await wait(50)
    print(DRIVE_BASE.angle(), 'after turn 2')
    await DRIVE_BASE.turn(-90,Stop.BRAKE,wait=True)
    await wait(50)
    print(DRIVE_BASE.angle(), 'after turn 3')
    await DRIVE_BASE.turn(-180,Stop.BRAKE,wait=True)
    await wait(50)
    print(DRIVE_BASE.angle(), 'after turn 4')
    await DRIVE_BASE.turn(180,Stop.BRAKE,wait=True)
    await wait(50)
    print(DRIVE_BASE.angle(), 'after turn 5')
    DRIVE_BASE.stop()

async def subtask2():
    while True:
        await wait(0)
        await wait(100)
        print(DRIVE_BASE.angle(),' ',HUB.battery.voltage())

async def subtask3():
    await wait(1000)
    while True:
        await wait(0)
        if Button.CENTER in HUB.buttons.pressed():
            raise SystemExit

async def tuning():
    await wait(0)
    await multitask(
        subtask(),
        subtask2(),
        subtask3(),
        race=True,
    )

async def subtask4():
    print(HUB.battery.voltage())
    print(SPEED, ACCELERATION, TURN_SPEED, TURN_ACCELERATION)
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(-10, then=Stop.BRAKE)
    await DRIVE_BASE.straight(300, then=Stop.BRAKE)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    print(DRIVE_BASE.angle(), 'after straight')
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() + 0) + 90))
    print(DRIVE_BASE.angle(), 'after turn 1')
    await DRIVE_BASE.turn(0 + ((DRIVE_BASE.angle() - -90) + 90))
    print(DRIVE_BASE.angle(), 'after turn 2')
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() - 0) + 90))
    print(DRIVE_BASE.angle(), 'after turn 3')
    await DRIVE_BASE.turn(0 - ((DRIVE_BASE.angle() - 90) + 180))
    print(DRIVE_BASE.angle(), 'after turn 4')
    await DRIVE_BASE.turn(0 + ((DRIVE_BASE.angle() - 270) + 180))
    print(DRIVE_BASE.angle(), 'after turn 5')

async def subtask5():
    while True:
        await wait(0)
        await wait(100)
        print(DRIVE_BASE.angle())

async def tuning_2():
    await wait(0)
    await multitask(
        subtask4(),
        subtask5(),
        race=True,
    )

async def main():
    await multitask(
        wait(0),
    )


run_task(main())