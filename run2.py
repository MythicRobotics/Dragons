from pybricks.parameters import Button, Stop
from pybricks.tools import StopWatch, multitask, run_task, wait

from pid_python import heading_pid
from robot_config import DRIVE_BASE, HUB, KD, KI, KP, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, TURN_KD, TURN_KI, TURN_KP

# Set up all devices.
watch = StopWatch()

async def subtask():
    await DRIVE_BASE.straight(100, then=Stop.BRAKE)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(90)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(380)

async def subtask2():
    await RIGHT_ATTACHMENT.run_angle(1000, 250)
    await LEFT_ATTACHMENT.run_angle(1000, -150)

async def subtask3():
    await wait(50)
    DRIVE_BASE.stop()

async def subtask4():
    await LEFT_ATTACHMENT.run_angle(1000, -355)
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-50)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(410)

async def subtask5():
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(70)

async def subtask6():
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(600)

async def subtask7():
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(-10, then=Stop.BRAKE)
    await multitask(
        subtask(),
        subtask2(),
    )
    await RIGHT_ATTACHMENT.run_angle(1000, -300)
    await DRIVE_BASE.straight(-50)
    await RIGHT_ATTACHMENT.run_angle(1000, 800)
    # mission 12a compolete
    await multitask(
        subtask3(),
        subtask4(),
    )
    await RIGHT_ATTACHMENT.run_angle(1000, -820)
    # OG valiue was -3500
    await wait(50)
    await multitask(
        subtask5(),
        RIGHT_ATTACHMENT.run_angle(1000, 1000),
    )
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(700)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(-92)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(370)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(20)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, KP, KI, KD)
    await DRIVE_BASE.straight(-100)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.straight(-300)
    await wait(50)
    DRIVE_BASE.stop()
    await heading_pid(DRIVE_BASE, TURN_KP, TURN_KI, TURN_KD)
    await DRIVE_BASE.turn(60)
    await multitask(
        subtask6(),
        RIGHT_ATTACHMENT.run_angle(1000, -1050),
        LEFT_ATTACHMENT.run_angle(1000, 520),
    )

async def subtask8():
    # end of launch code
    DRIVE_BASE.stop()
    print(watch.time())
    while True:
        await wait(0)
        await wait(100)
        print(DRIVE_BASE.angle())

async def subtask9():
    await wait(1000)
    while True:
        await wait(0)
        if Button.CENTER in HUB.buttons.pressed():
            raise SystemExit

async def test2():
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