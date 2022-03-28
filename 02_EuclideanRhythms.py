import isobar as iso
from MidiApp import MidiApp
from Euclidean import euclidean

class EuclideanRhythms(MidiApp):

    def start(self):
        kick = euclidean(17, 5, 0)
        kick = iso.PSequence(kick) * 48

        snare = euclidean(16, 5, 0)
        snare = iso.PSequence(snare) * 49

        hihat = euclidean(16, 8, 1)
        hihat = iso.PSequence(hihat) * 50

        cowbell = euclidean(18, 11, 7)
        cowbell = iso.PSequence(cowbell) * 51

        self.timeline.schedule({
            "note": kick,
            "amplitude": 100
        })

        self.timeline.schedule({
            "note": snare,
            "amplitude": 100
        })

        self.timeline.schedule({
            "note": hihat,
            "amplitude": 100
        })

        self.timeline.schedule({
            "note": cowbell,
            "amplitude": 100
        })





if __name__ == "__main__":
    app = EuclideanRhythms(sync_to_midi_in=True)
    app.run()
