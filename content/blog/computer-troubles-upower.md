Title: Bash / Upower / System76 Oryx
Date: 2021-01-26
Category: bash

## tl;dr

Troubleshooting some power/battery issues with my [@System76](https://twitter.com/system76) Oryx laptop lead me to write a script to monitor battery levels and log it to a file.

* Code: [serundeputy/upoower](https://github.com/serundeputy/upoower-logs/blob/main/upower-logs.sh)

## The Problem

One day while I was working suddenly my laptop just powered off. Poof gone. I tried to turn it back on, but it would not respond. I contatced the good folks at System76 and we began the troubleshooting process.

## Troubleshooting

In the course of troubleshooting the battery/power issues one of the agents shot me this one liner:

```bash
while true; do upower -d | grep percentage | head -n 1 >> ~/battery.log; sleep 300; sync; done
```

Which I thought was just great, but being a programmer I just had to muddle with it ;).

## The Script

So, while I was using the one-liner, I started to muck around and timestamp the log file `battery-DATE.log` and add timestamps to the percent entries being written to the log file and added some real time feedback to the terminal while the script is running. Here is the script I wrote:

```bash
#!/bin/bash

###
# Create a log file of times and battery percenage left.
#
# To run symlink the `upower-logs.sh` file to `/usr/local/bin/upl`
# `ln -s PATH/TO/upower-logs.sh /usr/local/bin/upl`
# 
# Then you can run it by just typing `upl` at the command prompt.
###

# Get start time
STIME=`date "+%d-%b-%Y-%H-%M"`

printf "\n\tWriting logs to ${HOME}/battery-${STIME}.log\n\n"
while true; do
  DATE=`date`
  UPOWER=`upower -d | grep percentage | head -n 1`
  printf '%s\n' "${DATE} ${UPOWER}"
  printf '%s\n' "${DATE} ${UPOWER}" >> "${HOME}/battery-${STIME}.log"
  sleep 300
  sync;
done
```

And a sample output file:

```text
Mon 25 Jan 2021 09:25:44 AM EST     percentage:          63%
Mon 25 Jan 2021 09:30:44 AM EST     percentage:          55%
Mon 25 Jan 2021 09:35:44 AM EST     percentage:          50%
Mon 25 Jan 2021 09:40:44 AM EST     percentage:          42%
```

## Conclusion

As a programmer and engineer I'm always exploring an pursuing curiosities. You can see the full source code of the script here: [serundeputy/upoower](https://github.com/serundeputy/upoower-logs/blob/main/upower-logs.sh).  Feel free to download and make use of and/or modify the script for your own purposes.

Follow me on twitter [@serundeputy](https://twitter.com/serundeputy)
