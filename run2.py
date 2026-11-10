from pybricks.tools import StopWatch, multitask, run_task, wait
from robot_config import DRIVE_BASE, HUB
from library import elevator_up, elevator_down, elevator_left, elevator_right, drive_turn_right, drive_turn_left, drive_straight_forward, drive_straight_backward, telemetry, E_stop, heading_check, drive_straight_speed
# Set up all devices.
watch = StopWatch()
# ᓚᘏᗢ

async def turn_by_turn_2():
    await drive_straight_backward(10)
    await multitask(
        drive_straight_forward(75),#90
        elevator_left(500)
    )
    await drive_turn_right(90)
    await drive_straight_speed(200)
    await multitask(
        drive_straight_forward(730),            #raming into the drone
        elevator_up(200)
    )
    await drive_straight_speed(400)
    await drive_turn_left(45)
    await drive_turn_left(30)                   #drone fully complated
    await drive_turn_right(90)
    await drive_straight_backward(100)
    await drive_turn_left(45)
    await multitask(
        drive_straight_forward(250),
        elevator_up(500),
    )
    await drive_turn_left(0)
    await multitask(
        elevator_right(600),#500                    #prepareing for keystone species
        drive_straight_forward(115)
    )
    await elevator_up(550)
    await elevator_down(425)                    #keystone species done
    #await elevator_right(100)
    await drive_turn_left(-80)
    await drive_straight_backward(250)
    await drive_turn_right(-40)
    await drive_straight_backward(200)
    await drive_turn_left(-90)
    await drive_straight_backward(100)
    await multitask(
        elevator_down(440),
        elevator_left(700)
    )
    await drive_straight_backward(35)



async def launch_2():
    await wait(0)
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    await multitask(
        turn_by_turn_2(),
        telemetry(),
        E_stop(),
        race=True,
    )
    print(f"Time: {watch.time()/1000} seconds")

async def main():
    await multitask(
        wait(0),
    )


run_task(main())
async def main():
    await multitask(
        wait(0),
    )
   