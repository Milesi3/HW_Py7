import models
import view

def run():
    option1 = view.show_menu()
    if option1 == '1':
        view.show_res(models.read_csv())
    elif option1 == '2':
        models.add_csv(view.add_csv())
    elif option1 == '3':
        print(view.show_res(models.read_csv()))
        models.del_csv(view.del_csv())
    elif option1 == '4':
        models.update_csv(*view.inp())
    elif option1 == '5':
        models.iport_csv()
    elif option1 == '6':
        models.export_csv()
