from pybricks.parameters import Button, Stop
from pybricks.tools import StopWatch, multitask, run_task, wait

from pid_python import heading_pid
from robot_config import DRIVE_BASE, HUB, KD, KI, KP, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, TURN_KD, TURN_KI, TURN_KP

# Set up all devices.
watch = StopWatch()

async def subtask():
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-10, then=Stop.BRAKE)
    await DRIVE_BASE.straight(250)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-45)

async def subtask2():
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(45)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(270)

async def subtask3():
    await wait(1000)
    await LEFT_ATTACHMENT.run_angle(250, -260)

async def subtask4():
    await wait(1000)
    await LEFT_ATTACHMENT.run_angle(250, -260)

async def subtask5():
    await multitask(
        RIGHT_ATTACHMENT.run_angle(1000, -265),
        subtask3(),
    )

async def subtask6():
    await wait(50)
    print('who lived here? complete ^', HUB.imu.heading())
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-30)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(10)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(420)

async def subtask7():
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    await multitask(
        subtask(),
        RIGHT_ATTACHMENT.run_angle(1000, 400),
    )
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(250)
    await multitask(
        subtask2(),
        subtask5(),
    )
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-50)
    # forge complete ^
    await RIGHT_ATTACHMENT.run_angle(1000, 30)
    await LEFT_ATTACHMENT.run_angle(1000, -260)
    await DRIVE_BASE.turn(-30)
    # who lived here? complete ^
    await multitask(
        subtask6(),
        RIGHT_ATTACHMENT.run_angle(1000, 800),
    )
    await wait(50)
    print('after  veer ', HUB.imu.heading())
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(20)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-230)
    await DRIVE_BASE.straight(100)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-30)
    await DRIVE_BASE.arc(-400, distance=-350, then=Stop.NONE)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-500)
    # last code above this line
    DRIVE_BASE.stop()
    print(watch.time())

async def subtask8():
    while True:
        await wait(0)
        await wait(100)
        print(DRIVE_BASE.angle())

async def subtask9():
    await wait(1000)
    while True:
        await wait(0)
        if Button.CENTER in HUB.buttons.pressed():
            # ᓚᘏᗢ
            raise SystemExit

async def test3():
    await wait(0)
    await multitask(
        subtask7(),
        subtask8(),
        subtask9(),
        race=True,
    )

async def main():
    await multitask(
        wait(0),
    )


run_task(main())