---
title: Welcome
---

# Welcome to DialogSorter

This program/script is designed specifically to help during Dialog event at Gymjh in Prague. Feel free to use it if it could help you too!

DialogSorters takes an excel file with online form answers where people were asked to set an order of preference for different time slots and activities those slots occupied. As capacity can be limited, this script sorts people based on their desired preferences but keeps the capacity in mind. When an activity is full, a person is refused and receives a less desired option.

Or none at all. 

!!! tip
    To actually get started try looking up the [**Getting started**](getting-started.md) section on the left.:)

!!! warning
    Make sure to read the output console. As warnings such as a person with no assigned activity are printed there.

## Output

The script generates a new excel file `oldname_SORTED.xlsx`. Here additional sheets with sorted data are added, specifically:

- Table of People -> Everyone is printed here with the activities in timeslots they were asigned to
- Table of Attendants -> Every activity generates a sheet with people who attend and basic statistics

!!! note
    As for now, formatting the output into usable or even printable version is considered out-of-scope of this project. You are encouraged to process the output yourself.:)

## Config file

The philosophy during the development was limiting the user input in runtime as much as possible. In ideal scenario, user supplies the original data and sets up the config file. 
No further input is required and output file is provided.

However, In special circumstances such as incorrectly typed config file, user may be asked to input something in console during runtime. In other times the script may just fail.

## License and credits

I am publishing freely under open-source MIT license. For the foreseeable future I am happy to maintain this and help if contacted, but if anyone wishes to improve on this and use this somehow, feel free. I used the opportunity of this project to refresh my weak memory of python and learn something new. Like making a cool documentation! In any case, the code is far from beautiful and the options are pretty limited. Any input is appreciated!

General thanks need to go to Jiří Sejkora who asked me to even do this and kept me motivated enough to finish this.

Openpyxl, MKDocs and Material theme for MKDocs are utilized.

!!! info
    As you can see, I am quite enjoying making these note-like boxes.