import datetime
import csv


note = {}
def add_note():
    name_id = input("Введите идентификатор заметки: ")
    name = input("Введите название заметки: ")
    text = input("Введите текст заметки: ")
    date = datetime.datetime.now()
    note[name_id] = {"название заметки": name, "текст заметки": text, "дата и время заметки":date}
    print("Заметка добавлена")
    with open('Note.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name_id, name, text, date])
        file.close()


def edit_note():
    name_id = input("Введите идентификатор заметки: ")
    if name_id in note:
        name = input("Введите новое имя заметки: ")
        text = input("Введите новый текст заметки: ")
        date = datetime.datetime.now()
        note[name_id] = {"название заметки": name, "текст заметки": text, "дата и время заметки":date}
        print("Контакт успешно изменен")
    else:
        print("Контакт не найден")


def delete_note():
    name_id = input("Введите идентификатор заметки: ")
    if name_id in note:
        del note[name_id]
        print("Заметка успешно удалена")
        with open('Note.csv', 'r') as file:
            writer = csv.writer(file)
            writer.writerow([name_id])
            file.close()
    else:
        print("Заметка не найдена")

def find_note():
    name_id = input("Введите идентификатор зметки: ")
    if name_id in note:
        print (note[name_id])
    else:
        print("Заметка не найдена")

def note_app():
    while True:
        action = input("\nВыберите действие:\n1 - Добавить заметку\n2 - Редактировать заметку\n3 - Удалить заметку\n4 - Вывести список всех заметок\n5 - Найти заметку\n6 - Выйти из приложения\n")
        if action == "1":
            add_note()
        elif action == "2":
            edit_note()
        elif action == "3":
            delete_note()
        elif action == "4":
            for name_id, data in note.items():
                print("{0}: {1}, {2}, {3}".format(name_id, data["название заметки"], data["текст заметки"], data["дата и время заметки"]))
        elif action == "5":
            find_note()
        elif action == "6":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

note_app()