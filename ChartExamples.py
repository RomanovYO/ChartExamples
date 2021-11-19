# Примеры построения графиков

import tkinter as tk

# Создание главного окна
window = tk.Tk()
window.geometry('450x450-400+200')
window.title('Примеры построения графиков')

# Функция закрытия программы
def do_close():
  window.destroy()

# Добавление метки заголовка
lblTitle = tk.Label(text = 'Примеры построения графиков', font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x = 55, y = 25)

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text = 'Закрыть', font = ('Helvetica', 10, 'bold'), command = do_close)
btnClose.place(x = 330, y = 400, width = 90, height = 30)

# Запуск цикла mainloop
window.mainloop()
