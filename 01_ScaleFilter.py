import isobar as iso
from MidiApp import MidiApp
import mido


## Snaps incoming notes to the C major scale
class ScaleFilter(MidiApp):

    def midi_callback(self, message):
        if message.type == "note_on" or message.type == "note_off":
            note = message.note
            semitone = (note % 12)
            octave = int(note / 12)
            semitone_in_scale = self.notes_lookup[semitone]
            message.note = semitone_in_scale + 12 * octave
            self.timeline.output_device.midi.send(message)

    def start(self):
        self.notes_lookup = [0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 9, 11]

if __name__ == "__main__":
    # print(mido.get_output_names())
    # exit()
    app = ScaleFilter(use_midi_callback=True)
    app.run()
