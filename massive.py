import ast
import FreeSimpleGUI as sg
import webbrowser

from decode import pithon

sg.theme('DarkGrey13') # Установка темы

def search_array(array, search_terms):
    if not search_terms:
        return array

    search_terms = search_terms.split()
    results = []
    for item in array:
        item_str = str(item)
        if all(term in item_str for term in search_terms):
            results.append(item)
    return results

def go_to(url):
    webbrowser.open(url)

def delete_from_array(array):
    """Создает GUI для удаления элементов из массива с поиском."""

    if not isinstance(array, list):
        sg.popup_error("Ошибка: Входные данные должны быть списком.", font='Helvetica 12 bold')
        return None

    if not array:
        sg.popup_error("Ошибка: Массив пуст.", font='Helvetica 12 bold')
        return None

    # Layout с поиском и шрифтом
    layout = [
        [sg.Text("Поиск:", font='Helvetica 12 bold'), sg.InputText(key='-SEARCH-', do_not_clear=True, font='Helvetica 12 bold', size=(23,1)), sg.Button('Найти', font='Helvetica 12 bold')],
        [sg.Table(values=[[str(x)] for x in array], headings=['Элемент'],
                  auto_size_columns=False, col_widths=[30], key='-TABLE-',
                  enable_events=True, select_mode=sg.TABLE_SELECT_MODE_EXTENDED, font='Helvetica 12 bold')],
        [sg.Button('Удалить', font='Helvetica 12 bold'), sg.Button('Выход', font='Helvetica 12 bold'), sg.Button('Открыть', font='Helvetica 12 bold')]
    ]

    window = sg.Window('Удаление элементов', layout, font='Helvetica 12 bold')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Выход':
            break
        if event == 'Найти':
            search_terms = values['-SEARCH-']
            filtered_array = search_array(array, search_terms)
            window['-TABLE-'].update(values=[[str(x)] for x in filtered_array])

        if event == 'Удалить':
            selected_indices = values['-TABLE-']
            if selected_indices:
                new_array = [array[i] for i in range(len(array)) if i not in selected_indices]
                array[:] = new_array  # Обновляем исходный массив
                window['-TABLE-'].update(values=[[str(x)] for x in array]) # Обновляем таблицу
            else:
                sg.popup("Ошибка: Не выбрано ни одного элемента для удаления.", font='Helvetica 12 bold')

        if event == 'Открыть':
            selected_indices = values['-TABLE-']
            if selected_indices:
                selected_values = [array[i] for i in selected_indices]
                print(selected_values)
                for selected_value in selected_values:
                    go_to(selected_value)
            else:
                sg.popup("Ошибка: Не выбрано ни одного элемента для открытия.", font='Helvetica 12 bold')
    window.close()
    return array # Возвращаем обновленный массив

def edit_array(array_input):
    try:
        result = delete_from_array(array_input)
        return result
    except (ValueError, SyntaxError) as e:
        print(f"Ошибка при разборе ввода: {e}")
        return array_input # Возвращаем исходный массив в случае ошибки
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")
        return array_input # Возвращаем исходный массив в случае ошибки

if __name__ == "__main__":
    array_str = input("Введите список Python: ")
    try:
        array = ast.literal_eval(array_str)
        if not isinstance(array, list):
            print("Ошибка: Введенные данные не являются списком.")
        else:
            updated_array = edit_array(array)
            print(f"Обновленный список: {updated_array}")
    except (SyntaxError, ValueError):
        print("Ошибка: Неверный формат списка.")