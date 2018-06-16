import threading
import datetime
import xlrd, xlwt
from tkinter.filedialog import Open, SaveAs

class WriteThread(threading.Thread):
    def __init__(self,test):
        self.test = test
        self.daemon = True

    def run(self):
        dialog = SaveAs(master=None, filetypes=[('Excel', '*.xls')]).show()

        if dialog.find('.xls') == -1:
            dialog = dialog + '.xls'

        wb = xlwt.Workbook()
        ws = wb.add_sheet('test')

        ws.write(0, 0, '№')
        ws.write(0, 1, 'Время')
        ws.write(0, 2, 'Пользователь')
        ws.write(0, 3, 'Экзамен')
        ws.write(0, 4, 'Оценка')

        numberRow = 1
        for obj in self.test:
            ws.write(numberRow, 0, obj.id)
            ws.write(numberRow, 1, obj.time.isoformat(sep='T'))
            ws.write(numberRow, 2, obj.user.username)
            ws.write(numberRow, 3, obj.exam.name)
            ws.write(numberRow, 4, str(obj.mark) + '/' + str(obj.exam.number_questions))
            numberRow += 1

        wb.save(dialog)
