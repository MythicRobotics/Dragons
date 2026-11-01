from pybricks.parameters import Button, Stop
from pybricks.tools import multitask, run_task, wait
from library import drive_turn_left, elevator_up, elevator_down, elevator_left, elevator_right, drive_turn_right, drive_straight_forward, drive_straight_backward, telemetry, E_stop, heading_check
from pid_python import heading_pid
from robot_config import ACCELERATION, DRIVE_BASE, HUB, KD, KI, KP, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, SPEED, TURN_ACCELERATION, TURN_KD, TURN_KI, TURN_KP, TURN_SPEED

async def subtask():
    print(HUB.battery.voltage())
    print(SPEED, ACCELERATION, TURN_SPEED, TURN_ACCELERATION)
    DRIVE_BASE.use_gyro(True)
    await drive_straight_backward(10)
    await drive_straight_forward(300)
    await heading_check('after straight')
    await drive_turn_left(5)
    await heading_check('after turn 1')
    await drive_turn_right(5)
    await heading_check('after turn 2')
    await drive_turn_left(10)
    await heading_check('after turn 3')
    await drive_turn_right(10)
    await heading_check('after turn 4')
    await drive_turn_left(20)
    await heading_check('after turn 5')
    await drive_turn_right(20)
    await heading_check('after turn 6')
    await drive_turn_left(30)
    await heading_check('after turn 7')
    await drive_turn_right(30)
    await heading_check('after turn 8')
    await drive_turn_left(45)
    await heading_check('after turn 9')
    await drive_turn_right(45)
    await heading_check('after turn 10')
    await drive_turn_left(60)
    await heading_check('after turn 11')
    await drive_turn_right(60)
    await heading_check('after turn 12')
    await drive_turn_left(75)
    await heading_check('after turn 13')
    await drive_turn_right(75)
    await heading_check('after turn 14')
    await drive_turn_left(90)
    await heading_check('after turn 15')
    await drive_turn_right(90)
    await heading_check('after turn 16')
    await drive_turn_left(135)
    await heading_check('after turn 17')
    await drive_turn_right(135)
    await heading_check('after turn 18')
    await drive_turn_left(180)
    await heading_check('after turn 19')
    await drive_turn_right(180)
    await heading_check('after turn 20')

    '''await DRIVE_BASE.straight(-10, then=Stop.BRAKE)
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
    print(DRIVE_BASE.angle(), 'after turn 5')'''
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
       
        subtask3(),
        race=True,
    )
    '''subtask2(),'''

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