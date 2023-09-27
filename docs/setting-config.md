# HowTo: Setting up a config file 

`config.ini` serves as the necessary buffer between the program and the user. However, apart from having some requirements, this feature also allows quite a lot of customization. As we will demonstrate in a short while, you can specify the amount of exported personal information data or even set the order in which people are sorter. 

!!! example
    ```ini
    ; config.ini file
    [data]
    filename = dialog_data.xlsx
    [person]
    name = Jméno
    email = E-mail 
    class = Třída 
    ordertime = Čas dokončení
    [slot]
    slot1 = 1. blok
    slot2 = 2. blok
    slot3 = 3. blok
    [priority]
    orderby = ordertime
    [output]
    peoplesheetname = Výpis účastníků
    [capacity]
    Czech Substance= 50
    Jan Bárta = 40
    František Ivan= 40
    ```

## How to write into a config file

`config.ini` is despite its extension a simple text file. Meaning you can open and modify it in your favorite text editor. Even good old Notepad will do. Just avoid Word if you reeealy don't know what you are doing.

The file is divided into sections such as `[data]` and attributes, every line not starting a new section is an attribute. The keycharacter is `=`. Everything on the line before it is the first part the definition, a **key** or name of the setting if you want and everything behind it is the **value** or definition. Strings do not need to be is `""`. In fact even quotes will just be imported. Spaces before first and after last character are ignored. 

`;` starts a comment, everything till the end of line is ignored

!!! note
    Further in the text I will use the term KEY and VALUE when I refer to the attributes.

    So one last time:
    ```
    [section]
    KEY = VALUE
    ```

## Structure of config file

As you can see in the example above the config file has a structure that should be followed. The squere brackets `[]` determine different sections. While their order is not strictly defined all sections mentioned in the example above need to be present. Even in case some of them are empty!

Let's overview the different sections and see the options modifying them gets you.

### Data

The start is rather simple. The only attribute is `filename`. This is compulsory and you need to write the name of your excel data file. Or to be more precise, you are specifying a path to your file. In case the file is not in the folder you are running the script from, you will have to write the whole path to it. Whether relative or absolute is up to you.

Adding additional attributes will have no effect. 

### Person

This section is on of the most important ones as it gives you the greatest customization optiones. Here you define the columns of your data file you wish to import as a personal information of the people you sort.

The keys are not fixed (with one exception).

