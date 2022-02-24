import isobar as iso
import atexit
import time
import logging
import sys


class MidiApp(object):

    def __init__(self, sync_to_midi_in=False, use_midi_callback=False):
        self.sync_to_midi_in = sync_to_midi_in
        self.use_midi_callback = use_midi_callback

        self.midi_input = iso.MidiInputDevice()
        self.midi_output = iso.MidiOutputDevice()

        if self.use_midi_callback:
            self.midi_input.callback = self.midi_callback

        if self.sync_to_midi_in:
            self.timeline = iso.Timeline(clock_source=self.midi_input)
        else:
            self.timeline = iso.Timeline(120)

        self.timeline.add_output_device(self.midi_output)


    def run(self):
        # logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

        self.timeline.background()

        atexit.register(self.exit)
        self.start()
        while 1:
            try:
                time.sleep(1.0)
            except KeyboardInterrupt:
                sys.exit()

    def start(self):
        pass

    def midi_callback(self, message):
        pass

    def exit(self):
        self.timeline.output_device.all_notes_off()
