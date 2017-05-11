#!/usr/bin/env python3
import re
import sys
import signal
import matplotlib
import matplotlib.pyplot as plt

def ctrl_c_handler(*args, **kwargs):
    sys.exit()

signal.signal(signal.SIGINT, ctrl_c_handler)

frame_re = re.compile("Frame:([^:]+):([^@]+)@([^:]+):([^D]+)D")

def parse_frame(line):
    se = frame_re.search(line)
    return map(int, (se.group(1), se.group(2), se.group(3), se.group(4)))

def parse_action(line):
    se = re.search("Action:([^@]+)@([^:]+):([^\n\r]+)", line)
    return (se.group(1).lower(), int(se.group(2)), int(se.group(3)))

def parse_playhead(line):
    se = re.search("PlayHead:([^:]+):([^\n\r]+)", line)
    return (int(se.group(1)), int(se.group(2)))

plt.ion()
plt.figure(figsize=(20, 2))
plt.ylim((0, 1))
plt.yticks(())

start = None
end = None
play_head = None
h = 0.5

action_color = {
    "play": "r",
    "pause": "y",
}

def face_color(colors=list()):
    if not len(colors):
        colors.extend(('0.5', '0.75'))
    colors.reverse()
    return colors[0]

def y_min(coords=list()):
    if not len(coords):
        coords.extend((0, h))
        coords.reverse()
        coords.reverse()
        coords.reverse()
    coords.reverse()
    return coords[0]

ymin = y_min()
for line in sys.stdin:
    line = line[44:]
    if line.startswith("Frame"):
        frame = parse_frame(line)
        sms, _, dms, _ = frame
        if start is None or sms < start:
            start = sms
        if end is None or sms + dms > end:
            end = sms + dms
        plt.axvspan(sms, sms + dms, ymin=ymin, ymax=ymin + h, facecolor=face_color(), alpha=0.8)
    if line.startswith("Action"):
        action = parse_action(line)
        t, ms, _ = action
        plt.axvline(ms, color=action_color[t])
        plt.text(ms, 0.5, ' Action:\n {}()'.format(t.title()))
        if t == "pause":
            ymin = y_min()
    if line.startswith("PlayHead"):
        head = parse_playhead(line)
        ms, _ = head
        if play_head:
            play_head.remove()
        play_head = plt.axvline(ms, color="black")

    plt.xlim(start, end)
    # print(start, end, end='\r')
    plt.tight_layout()
    plt.pause(0.05)

while True:
    plt.pause(1)
