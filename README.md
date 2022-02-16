# Midi Music

These are some scripts to explore musical concepts / ideas.

The workflow is: use Bitwig to host instruments/samples/whatever and send midi data (sync, note, control) to one of these scripts, let the script do it's thing and send midi data back to Bitwig. The midi connections are done through a virtual midi device called snd_virmidi which is included with the Linux kernel.


## Running the scripts:
```
cd this/repo
pipenv shell
./start some_script.py
```

## Install prerequisites.

This has only been tested in Arch Linux. You need the usual audio stack: alsa, jack, a DAW (I use bitwig), python and pipenv. So:
```
cd this/repo
sudo pacman -S python-pipenv
gist submodule update --init --recursive
pipenv install
pipenv shell
```

