import schedule
import time
from threading import Thread
from sunrise import sun
from datetime import datetime

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

        def job():
            current_time = datetime.now().time()

            if current_time < s.sunrise() or current_time > s.sunset():
                print "Time to swich on the lamp"
                board.turn_on(switchIndex)
                return

            noon_time = s.solarnoon()
            if current_time > noon_time:
                print "Let's wait till sunset before we switch on the lamp"
                time.sleep(int(noon_time - current_time) + 1)
                return job()

            print "Sun is up, lamp should be off"
            board.turn_off(switchIndex)

        schedule.every().day.at("19:00").do(job)
        schedule.every().day.at("6:30").do(job)

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