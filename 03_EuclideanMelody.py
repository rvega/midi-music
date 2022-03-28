import isobar as iso
from MidiApp import MidiApp
from Euclidean import euclidean

class EuclideanMelody(MidiApp):

    def start(self):
        octave = 1
        notes = [48, 51, 53, 55, 58]
        euclideanParameters = [
            [17, 4, 0],
            [16, 4, 2],
            [18, 4, 3],
            [15, 4, 7],
            [19, 4, 3],
        ]

        for i in range(len(notes)):
            note = notes[i]
            parameters = euclideanParameters[i]
            sequence = euclidean(parameters[0], parameters[1], parameters[2])
            sequence = iso.PSequence(sequence) * (note + octave*12)
            self.timeline.schedule({
                "note": sequence,
                "amplitude": 100
            })
             



if __name__ == "__main__":
    app = EuclideanMelody(sync_to_midi_in=True)
    app.run()
