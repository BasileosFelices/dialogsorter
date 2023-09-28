# HowTo: Setting up a config file 

`config.ini` serves as the necessary buffer between the program and the user. However, apart from having some requirements, this feature also allows quite a lot of customization. As we will demonstrate in a short while, you can specify the amount of exported personal information data or even set the order in which people are sorter. 

## Example of `config.ini`

```ini
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

The file is divided into sections such as `[data]` and attributes, every line not starting a new section is an attribute. The split-character is `=`. Everything on the line before it is the first part the definition, a **key** or name of the setting if you want and everything behind it is the **value** or definition. Strings do not need to be is `""`. In fact even quotes will just be imported. Spaces before first and after last character are ignored. 

`;` starts a comment, everything till the end of line is ignored

!!! note
    Further in the text I will use the term KEY and VALUE when I refer to the attributes.

    So one last time:
    ```
    [section]
    KEY = VALUE
    ```

## Structure of config file

As seen in the example above, `config.ini` follows a specific structure that should be adhered to. While the order of sections is not strictly defined, all sections mentioned in the example above must be present, even if some are empty.

Let's review the different sections and the options they offer for customization.

### Data

The start is rather simple. The only attribute is `filename`. This is compulsory and you need to write the name of your excel data file. Or to be more precise, you are specifying a path to your file. In case the file is not in the folder you are running the script from, you will have to write the whole path to it. Whether relative or absolute is up to you.

Adding additional attributes will have no effect. 

### Person

This section allows you to customize how personal information is extracted from your data file. You can specify which columns in your Excel file should be imported as personal information for the individuals you're sorting.

The keys in this section are user-defined and flexible, with one exception ('name', read further). The keys you define here determine what appears in the output, but they can be chosen freely and don't need to match the actual column headers in your data file. You even have the option to use a key that's identical to the corresponding value.

Here's an example of a valid config file for the [person] section:

```ini
[person]
name = name
e-mail = e-mail
AdReS123 = address\
```

In this example, the keys such as name, e-mail, and AdReS123 are entirely up to you and don't need to match the exact column headers in your Excel file. However, the values (e.g., name, e-mail, address) must correspond to the actual column headers you want to import from your Excel file. In this case, there should be a column with the header address in your Excel file for this configuration to work correctly.

The only exception is the key 'name' which must be present. This may be fixed in the future. In the meantime, you do not really need to import names. You can always rename the headers later:]

### Slot

The slot section is really similar to the `[person]`. However, the keys do not matter much here. At the moment, they have no bearing on the output. Here you need to focus on **order**. The order of slots is determined by the order set-up here. Values need to correspond to the column headers in your Excel file. 

See [Getting started](getting-started.md) to understand how to prepare your data for this. 

Here's an important point to note: You are not restricted to a fixed number of slots. Feel free to define as many slots as needed in this configuration file. If you specify more slots than actually exist in your data set, the script will gracefully handle the unused slots and ignore them during processing.

### Priority

The order of priority is determined by the **orderby** key. The value needs to point to a key from `[person]` section. eg: `orderby : name`. The specified column determines the order of priority during the sorting of people into activities. Using a datetime for example will lead to the *First come, first served* scenario. If you prepare your data carefully you can even prepare a manual order. Just use an arbitrary column with ranking numbers.

### Output

The only output setting currently is the **peoplesheetname** key. The value is used as a name for the excel sheet of all sorted people.

### Capacity

Last, yet very important section is capacity. Surprisingly, this section is also completely optional (the section still needs to remain, even if empty). 

You can predefine the capacity of the activities you are sorting into. The key serves as the name of the activity used in preferences and it needs to match precisely. The value should be an integer value specifying the maximum capacity.

In case you do not specify an activity or misspell one, the scripts asks you to input one during runtime.

!!! warning
    To avoid errors, the script manually checks the config the following:

    - All sections are present / some can be empty
    - `filename, name, orderby, peoplesheetname` are all present and have a value

    If you do not comply with there rules the script is sure to fail.
