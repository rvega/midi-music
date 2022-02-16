import isobar as iso
import atexit
import time
import logging
import sys

class MidiApp(object):
    def run(self):
        # logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

        midi_in = iso.MidiInputDevice()
        timeline = iso.Timeline(clock_source=midi_in)
        timeline.background()
        self.timeline = timeline

        atexit.register(self.exit)
        self.main(timeline)
        while 1:
            try:
                time.sleep(1.0)
            except KeyboardInterrupt:
                sys.exit()

    def main(self):
        pass

    def exit(self):
        self.timeline.output_device.all_notes_off()

