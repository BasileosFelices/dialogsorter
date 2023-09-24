import Sorter
# pers1 = Person("Petr", "pavpetr@fit.cvut.cz", "8.a", datetime.datetime(2022, 6, 23), ["Anna", "Zuzka", "Alzbeta"])

# print(pers1.mPreferences)
# print(pers1)

# excelsource = load_workbook("dialog_data.xlsx")
# ws = excelsource.active
# print(ws["C3"].value)
# print(type(ws["C3"].value))

app = Sorter.Sorter()
app.run()

# app.printActivityAttendance()

print("REACHED END")