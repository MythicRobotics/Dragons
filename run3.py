from pybricks.tools import StopWatch, multitask, run_task, wait

from robot_config import DRIVE_BASE, HUB
from library import elevator_up, elevator_down, elevator_left, elevator_right, drive_turn_right, drive_turn_left, drive_straight_forward, drive_straight_backward, telemetry, E_stop, heading_check, drive_straight_speed
# Set up all devices.
watch = StopWatch()
# ᓚᘏᗢ 



async def turn_by_turn_3():
    await drive_straight_backward(10)
    await drive_straight_forward(99)
    await drive_turn_left(-20)
    await drive_straight_forward(245)
    await drive_turn_right(0)
    await drive_straight_forward(70)# ᓚᘏᗢ 
    await multitask(
        drive_straight_forward(15),
        elevator_up(10)
    )                                     #rock finished
    await multitask(
        elevator_left(225),
        drive_straight_backward(300)
    )
    await drive_turn_right(45)# ᓚsᗢ 
    await multitask(
        elevator_left(225),
        drive_straight_forward(500)
    )
    
    await elevator_up(350)
   # await drive_straight_speed(40)
    await multitask(
        elevator_down(110),
        drive_straight_backward(20)
    )
    await multitask(
            elevator_up(640),
            drive_straight_backward(200)
        )                                #finshed the expoding seeds!!!!!
    await drive_turn_right(90)
    await drive_straight_speed(60) 
  
                                        

async def launch_3():
    await wait(0)
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    await multitask(
        turn_by_turn_3(),
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