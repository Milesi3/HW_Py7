import models
import view

def run():
    option1 = view.show_menu()
    option2 = view.show_format()
    if option1 == '1' and option2 == '1':
        a = view.inp()
        while a != "":
            models.txtt(a)
            a = view.inp()
    elif option1 == '1' and option2 == '2':
        a = view.inp()
        while a != "":
            models.csvv(a)
            a = view.inp()
    elif option1 == '2' and option2 == '1':
        models.con_csv_txt()
    elif option1 == '2' and option2 == '2':
        models.con_txt_csv()
