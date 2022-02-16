
# Midi Music

These are some scripts to explore musical concepts / ideas.

The workflow is: use Bitwig to host instruments/samples/whatever and send midi data (sync, note, control) to one of these scripts, let the script do it's thing and send midi data back to Bitwig. The midi connections are done through a virtual midi device called snd_virmidi which is included with the Linux kernel.

## Running the scripts:
```
cd this/repo
pipenv install  # Only needed first time
pipenv shell
python some_script.py
```

sudo modprobe snd_virmidi midi_devs=1
export ISOBAR_DEFAULT_MIDI_OUT="VirMIDI 1-0"
export ISOBAR_DEFAULT_MIDI_IN="VirMIDI 1-0"
python 00_HelloWorld.py
