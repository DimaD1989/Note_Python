import function as f
import ui


def run():
    input_from_user = ''
    while input_from_user != '7':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            f.show('all')
        elif input_from_user == '2':
            f.add()
        elif input_from_user == '3':
            f.show('all')
            f.id_edit_del_show('del')
        elif input_from_user == '4':
            f.show('all')
            f.id_edit_del_show('edit')
        elif input_from_user == '5':
            f.show('date')
        elif input_from_user == '6':
            f.show('id')
            f.id_edit_del_show('show')
        elif input_from_user == '7':
            ui.goodbuy()
            break