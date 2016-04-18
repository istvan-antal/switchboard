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

        def job():
            current_time = datetime.now().time()
            wake_up_time = datetime.now().time()
            wake_up_time = wake_up_time.replace(6, 30, 0)

            if current_time < wake_up_time:
                print "We are before wakeup time, lamp off"
                board.turn_off(switchIndex)
                return

            if current_time < s.sunrise() or current_time > s.sunset():
                print "Time to swich on the lamp"
                board.turn_on(switchIndex)
                return

            noon_time = s.solarnoon()
            if current_time > noon_time:
                print "Let's wait till sunset before we switch on the lamp"
                delta = datetime.combine(date.today(), s.sunset()) - datetime.combine(date.today(), current_time)
                time.sleep(delta.total_seconds() + 1)
                return job()

            print "Sun is up, lamp should be off"
            board.turn_off(switchIndex)

        schedule.every().day.at("6:30").do(job)
        schedule.every().day.at("9:00").do(job)
        schedule.every().day.at("19:00").do(job)
        schedule.every().day.at("00:01").do(job)
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