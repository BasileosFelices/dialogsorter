# Getting started

### Downloading diaSorter

As this is really just a script, I will leave the [github repository](https://github.com/BasileosFelices/dialogsorter.git) linked above as the only official source.
If you are familiar with git there is nothing easier than just cloning the repository.

```shell
git clone https://github.com/BasileosFelices/dialogsorter.git
```

You can also just download the repository as zip and extract wherever you want to work. What you really need is the diasorter folder where the code is and the `config.ini` file.

### Installing python and openpyxl

First of all, you need python on your system. Luckily, you can find a lot of tutorials for that online. You also need to be able to use
python pip package manager as the second step is installing the requiered openpyxl library. You can use a provided `requirements.txt` file

```shell
pip install -r requirements.txt
```

### Prepare the input data

While the goal was to make only minimal demands on the structure of the input data, there still are some limitations. Most importantly it needs to be an Excel file (xlsx/xlsm/xltx/xltm)

The script expects a table typically generated from an online form, i one row header and than rows of data for each answer/person. There are no requirements on the order or even number of colums. The important columns are found thanks to header names that can be configured in the config file. While the config should handle complicated headers, it is reccomended to rename the imporant headers for simplicity.

The preferences have the most strict format. Every time slot, the multiple options of which only one is chosen that is, has to be in a single cell and different options need to be sorted by the preference and delimited by a semicolon(;). At the moment this is hard-coded behaviour, although the delimited could be quiete easily changed in [code](reference/Person.md). 

I reccomend keeping the data file in the root folder. 

!!! example
    The input data can really be as simple as this. Both more slots and personal info may be included, however.

    | name  | email                   | slot1                 | slot2                                |
    |-------|-------------------------|-----------------------|--------------------------------------|
    | Filip | filip.spelina@proton.me | C++Rulez;BetterPython | Tex vs Markdown; OpTeX pdf formatter |
    | Oscar | oscar@isac.com          | BetterPython;C++Rulez | Tex vs Markdown; OpTeX pdf formatter |

### Configure the configuration file

Now that our dataset is in order, we need to tell the sorter how we prepared the config file.
See [HowTo: Setting up a config file](setting-config.md) to understand your options.

For now use the supplied `config.ini` as a start. Open in and be sure to modify:
- filename: write a complete name (path) of your data set here
- name: the only compulsory personal information column, make sure the definition matches a column header in your excel file
- orderby: the definition needs to match previously correctly defined personal information.
- capacities: in the `capacity` section, write all your activities and their capacities as such: `activity name = capacity`

!!! warning
    The `orderby` determines the order of priority for people to get their most desired priorities! I recommend to use a column determining the time of submitting the form. As such, the first person who filled the form, chooses first from the so far empty activities.

### Run the script

Everything should be ready now! Run the `diaSorter.py` either from your favourite IDE or a console.

```shell
python diasorter/diaSorter.py
```

Congratulations! You now have a new _SORTED.xlsx data file you needed!

!!! warning
    Python needs to have access to your config file and your data file. Do not run the program from the `diasorter` directory. Run it from the project root directory.

