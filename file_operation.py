import Note


def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0) # Метод файла file.seek() устанавливает текущую позицию в байтах offset для указателя чтения/записи в файле file.
    #0 - означает, что нужно сместить указатель на offset относительно начала файла.
    file.close()  #Метод файла file.close() закрывает открытый файл.Закрытый файл больше не может быть прочитан или записан. Любая операция, которая требует, чтобы файл был открыт, вызовет исключение ValueError после того, как файл был закрыт. Вызов file.close() более одного раза разрешен.
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close #Метод файла file.close() закрывает открытый файл.Закрытый файл больше не может быть прочитан или записан. Любая операция, которая требует, чтобы файл был открыт, вызовет исключение ValueError после того, как файл был закрыт. Вызов file.close() более одного раза разрешен.


def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array