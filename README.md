## Time Calculator

Requirement: [Python 3.6+](https://python.org/downloads)

### Introduction

Sometimes you want to count how much time has passed, for this or that period.

For example:<br>
I went out for a walk at about 13:18, and came back at 16:23:40.
And you start figuring out how much time it took, and it's long. Not nice, isn't that? :)

Because this happens to me from time to time, I decided to make a utility to calculate the time.

---

Download the file `time_calc.py` or clone this repository:
```bash
git clone git@github.com:n05tr0m0/time_calc.git
```

Allow execution:
```bash
chnod +x time_calc.py
```
Use it:
```bash
# set the start time and the end time of event or action

./time_calc.py 13:18 16:23:40
# Result time: 3 hour(s), 5 minute(s), 40 second(s)
```
Don't forget to use the 24-hour time format. <br>
The seconds can be specified optionally. <br>
Hours can be specified without zero, if you like.

Also type `-h` for read help.

Enjoy =]