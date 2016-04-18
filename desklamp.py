import schedule
import time
from threading import Thread
from sunrise import sun
from datetime import datetime, date

def run_schedule():
    while DeskLamp.lamp_count > 0:
        schedule.run_pending()
        time.sleep(1)

class DeskLamp(object):
    lamp_count = 0
    t = None
    def __init__(self, board, switchIndex, lat, long):
        DeskLamp.lamp_count += 1
        s = sun(lat=lat, long=long)

        def job(isInitial=False):
            current_time = datetime.now().time()
            wake_up_time = datetime.now().time()
            wake_up_time = wake_up_time.replace(6, 30, 0)

            if s.sunrise() < current_time and current_time < s.sunset():
                print "Sun is up, lamp should be off"
                board.turn_off(switchIndex)
                return

            if current_time < wake_up_time:
                print "Time to swich on the lamp"
                board.turn_off(switchIndex)
                return

            print "Lamp time"
            board.turn_on(switchIndex)

        schedule.every().hour.do(job)
        job()

        if DeskLamp.t is None:
            t = Thread(target=run_schedule)
            t.daemon = True
            t.start()

    def __del__(self):
        DeskLamp.lamp_count -= 1

desklamps = []

def load(board, desklamp_configs):
    for desklamp_config in desklamp_configs:
        desklamps.append(DeskLamp(
            board=board,
            switchIndex=desklamp_config["switchIndex"],
            lat=float(desklamp_config["location"]["lat"]),
            long=float(desklamp_config["location"]["long"])
        ))