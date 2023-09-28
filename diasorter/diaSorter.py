"""This serves as the main function of the Dialog sorter project

Dialog sorter is a script used for sorting people by their preferences submitted through an electronic form
to activities that belong to a certain time slots.

The needs are tailored primarly for Dialog event at Gymnazium Jaroslava Heyrovskeho in Prague

@Filip Spelina, 2023
https://github.com/BasileosFelices/dialogsorter
"""

from Sorter import Sorter

app = Sorter()
app.run()

print("SUCCESFULL END")
