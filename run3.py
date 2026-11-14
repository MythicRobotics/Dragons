from pybricks.tools import StopWatch, multitask, run_task, wait
from robot_config import DRIVE_BASE, HUB, LEFT_ATTACHMENT
from library import elevator_up, elevator_down, elevator_left, elevator_right, drive_turn_right, drive_turn_left, drive_straight_forward, drive_straight_backward, telemetry, E_stop, heading_check, drive_straight_speed, all_stop
# Set up all devices.
watch = StopWatch()




async def turn_by_turn_3():
    await drive_straight_backward(10)
    await multitask(
        drive_straight_forward(75),
        elevator_left(500)
    )
    await drive_turn_right(90)
    await multitask(
        drive_straight_forward(300),
        elevator_up(200)
    )
    await drive_straight_speed(100)
    await drive_straight_forward(100)
    await drive_straight_speed(400)
    await drive_straight_forward(330)            #raming into the drone
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
        elevator_right(600),                   #prepareing for keystone species
        drive_straight_forward(115)
    )
    await elevator_up(570)
    await elevator_down(400)                    #keystone species done
    #await elevator_right(100)
    await drive_turn_left(-85)
    await multitask(
        drive_straight_backward(425),
        elevator_up(150),
    )
    await multitask(
        drive_turn_left(-180),
        elevator_left(403),                  # elevator :(
        elevator_down(590)
    )
    await drive_straight_forward(105)
    await elevator_left(303)                  #skylight done
        
    await multitask(
        drive_straight_backward(105),
        elevator_up(450),
        elevator_right(425)
    )
    await multitask(
        drive_turn_left(-260),
        drive_straight_forward(500)
    )

    await multitask(
        drive_straight_forward(600),
        elevator_right(600),
        elevator_down(900)
    )
  #  await drive_turn_right(-40)
  #  await drive_straight_backward(225)
   # await drive_turn_left(-90)
    #await drive_straight_backward(20)
  #  await multitask(
       # elevator_down(850),#400
       # elevator_left(400),
       # drive_straight_backward(65)
   # )
    
async def launch_3():
    await wait(0)
    watch.reset()
    print(HUB.battery.voltage())
    DRIVE_BASE.use_gyro(True)
    DRIVE_BASE.reset()
    await multitask(
        turn_by_turn_3(),
        telemetry(),
        E_stop(),
        race=True,
    )
    await all_stop()
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
