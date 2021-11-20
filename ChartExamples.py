# Примеры построения графиков

import tkinter as tk

# Импорт внешних файлов
import chart1
import chart2
import chart3
import chartA

# Создание главного окна
window = tk.Tk()
window.geometry('450x550-400+200')
window.title('Примеры построения графиков')

# Функция закрытия программы
def do_close():
  window.destroy()

# Добавление метки заголовка
lblTitle = tk.Label(text = 'Примеры построения графиков', font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x = 55, y = 25)

# Добавление кнопки и метки для графика 1
y = 100
btnChart1 = tk.Button(window, text = 'График 1', font = ('Helvetica', 10, 'bold'), command = chart1.plot_chart)
btnChart1.place(x = 40, y = y, width = 90, height = 30)
lblChart1 = tk.Label(text = 'График синуса matplotlib')
lblChart1.place(x = 170, y = y+7)

# Добавление кнопки и метки для графика 2
y += 50
btnChart2 = tk.Button(window, text = 'График 2', font = ('Helvetica', 10, 'bold'), command = chart2.plot_chart)
btnChart2.place(x = 40, y = y, width = 90, height = 30)
lblChart2 = tk.Label(text = 'Нормальное распределение')
lblChart2.place(x = 170, y = y+7)

# Добавление кнопки и метки для графика 3
y += 50
btnChart3 = tk.Button(window, text = "График 3", font = ('Helvetica', 10, 'bold'), command = chart2.plot_chart2)
btnChart3.place(x = 40, y = y, width = 90, height = 30)
lblChart3 = tk.Label(text = 'Нормальное распределение - 3 графика')
lblChart3.place(x = 170, y = y+7)

# Добавление кнопки и метки для графика 4
y += 50
btnChart4 = tk.Button(window, text = 'График 4', font = ('Helvetica', 10, 'bold'), command = chart3.plot_chart)
btnChart4.place(x = 40, y = y, width = 90, height = 30)
lblChart4 = tk.Label(text = 'Гистограмма Seaborn')
lblChart4.place(x = 170, y = y+7)

# Добавление кнопки и метки для графика 5
y += 50
btnChart5 = tk.Button(window, text = 'График 5', font = ('Helvetica', 10, 'bold'), command = chart3.plot_chart2)
btnChart5.place(x = 40, y = y, width = 90, height = 30)
lblChart5 = tk.Label(text = 'Сдвоенная гистограмма Seaborn')
lblChart5.place(x = 170, y = y+7)

# Добавление кнопки и метки для графика 6
y += 50
btnChart6 = tk.Button(window, text = 'График 6', font = ('Helvetica', 10, 'bold'), command = chart2.plot_chart)
btnChart6.place(x = 40, y = y, width = 90, height = 30)
lblChart6 = tk.Label(text = 'Описание графика 6')
lblChart6.place(x = 170, y = y+7)

# Добавление кнопки и метки для графика 7
y += 50
btnChart7 = tk.Button(window, text = 'График 7', font = ('Helvetica', 10, 'bold'), command = chart2.plot_chart)
btnChart7.place(x = 40, y = y, width = 90, height = 30)
lblChart7 = tk.Label(text = 'Описание графика 7')
lblChart7.place(x = 170, y = y+7)

# Добавление кнопки и метки для графика A (дополнительно)
y += 50
btnChartA = tk.Button(window, text = 'График A', font = ('Helvetica', 10, 'bold'), command = chartA.plot_chart)
btnChartA.place(x = 40, y = y, width = 90, height = 30)

lblChartA = tk.Label(text = 'Круговая диаграмма со срезами')
lblChartA.place(x = 170, y = y+7)

# Добавление кнопки закрытия программы
y += 50
btnClose = tk.Button(window, text = 'Закрыть', font = ('Helvetica', 10, 'bold'), command = do_close)
btnClose.place(x = 330, y = y, width = 90, height = 30)

# Запуск цикла mainloop
window.mainloop()
