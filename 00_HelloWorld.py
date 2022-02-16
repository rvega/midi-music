import isobar as iso
from MidiApp import MidiApp

## Outputs some notes in sync with the received midi clock.
class HelloWorld(MidiApp):
    def main(self, timeline):
        timeline.schedule({
            "note": iso.PSequence([60, 67, 72, 77]),
            "amplitude": iso.PWhite(0, 128)
        })

if __name__ == "__main__":
    app = HelloWorld()
    app.run()
