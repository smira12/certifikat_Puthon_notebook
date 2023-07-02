from sertifikat_Python_notebook.ConsoleView import Console
from sertifikat_Python_notebook.Model import Model
from sertifikat_Python_notebook.Presenter import Presenter

if __name__ == '__main__':
    presenter: Presenter = Presenter(Model(), Console())

    RUN = True
    while RUN:
        user_choice = presenter.show_menu()
        match user_choice:
            case '1':
                presenter.add_note()
            case '2':
                presenter.save_notes_to_file()
            case '3':
                presenter.load_notes_from_file()
            case '4':
                presenter.find_note_by_id()
            case '5':
                presenter.show_all_notes()
            case '6':
                presenter.delete_note_by_id()
            case '7':
                presenter.find_notes_by_date()
            case '8':
                presenter.edit_note_by_id()
            case '0':
                RUN = False
                presenter.display('Программа завершила работу. До свидания!')
            case _:
                presenter.display_wrong_choise()