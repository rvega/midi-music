import isobar as iso
from MidiApp import MidiApp


## Outputs some notes in sync with the received midi clock.
class HelloWorld(MidiApp):

    def start(self):
        self.timeline.schedule({
            "note": iso.PSequence([62, 67, 72, 77]),
            "amplitude": iso.PWhite(0, 128)
        })


if __name__ == "__main__":
    app = HelloWorld(sync_to_midi_in=True)
    app.run()



