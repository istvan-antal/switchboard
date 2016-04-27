import schedule
import time
from threading import Thread
from sunrise import sun
from datetime import datetime, date
from pir import Sensor

def run_schedule():
    while DeskLamp.lamp_count > 0:
        schedule.run_pending()
        time.sleep(1)

class DeskLamp(object):
    lamp_count = 0
    t = None
    def __init__(self, board, switchIndex, lat, long, sensor=None):
        DeskLamp.lamp_count += 1
        s = sun(lat=lat, long=long)
        self.lamp_should_be_on = False
        self.sensor = None
        self.last_motion_time = int(0);
        if sensor is not None:
            def on_motion():
                self.last_motion_time = int(time.time());

            self.sensor = Sensor(sensor)
            self.sensor.on_motion = on_motion

        def job():
            current_time = datetime.now().time()
            wake_up_time = datetime.now().time()
            wake_up_time = wake_up_time.replace(6, 30, 0)
            sleep_time = wake_up_time.replace(23, 59, 0)

            if s.sunrise() < current_time and current_time < s.sunset():
                print "Sun is up, lamp should be off"
                self.lamp_should_be_on = False
                board.turn_off(switchIndex)
                return

            if current_time < wake_up_time or current_time > sleep_time:
                print "Time to swich off the lamp"
                self.lamp_should_be_on = False
                board.turn_off(switchIndex)
                return

            print "Lamp time"
            self.lamp_should_be_on = True
            now = int(time.time());
            if now - self.last_motion_time < 300:
                board.turn_on(switchIndex)
            else:
                board.turn_off(switchIndex)

        schedule.every(1).minutes.do(job)
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
        sensor = None
        if "sensor" in desklamp_config:
            sensor = desklamp_config["sensor"]

        desklamps.append(DeskLamp(
            board=board,
            switchIndex=desklamp_config["switchIndex"],
            lat=float(desklamp_config["location"]["lat"]),
            long=float(desklamp_config["location"]["long"]),
            sensor=sensor
        ))