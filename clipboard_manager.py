import clipboard_manager_gui
import sys
import keyboard
import pyperclip
import time
from PySide2.QtCore import *
from PySide2.QtGui import QColor, QTextCursor, QTextCharFormat, QCursor
from PySide2.QtWidgets import  QDialogButtonBox, QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QFontDialog, QHBoxLayout, QColorDialog, QScrollArea, QMainWindow, QFrame, QGroupBox, QRadioButton, QStyle, QStyleOption, QTableWidgetItem

class MainFrame(QFrame, clipboard_manager_gui.Ui_Frame):
    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent)
        super(MainFrame, self).setupUi(self)
        self.current_flags = Qt.WindowStaysOnTopHint
        self.setWindowFlags(self.current_flags)
        keyboard.add_hotkey("ctrl+c", self.get_from_clipboard_and_add)
        keyboard.add_hotkey("ctrl+v", self.pasting_from_manager)

        self.disabled = []
    
    def add_entry(self, string):
        row_count = self.table.rowCount()
        ##print(string)
        self.table.insertRow(row_count)
        qtablewidgetitem = QTableWidgetItem()
        qtablewidgetitem.setText(string)
        self.table.setItem(row_count, 0, qtablewidgetitem)
        self.table.setSortingEnabled(True)
    
    def pasting_from_manager(self):
        if self.sequential_pasting_checkbox.isChecked():
            #self.table.itemAt(QPoint(self.table.selected))
            self.table.setCurrentCell(self.table.currentRow()+1, 0)
            selected_items = self.table.selectedItems()
            while True:
                if len(selected_items) == 0:
                    self.table.setCurrentCell(self.table.currentRow()+1, 0)
                if self.table.currentRow() in self.disabled:
                    self.table.setCurrentCell(self.table.currentRow()+1, 0)
                    continue
                selected_items = self.table.selectedItems()
                if len(selected_items) > 0:
                    break
            pyperclip.copy(selected_items[0].text())
    
    def get_from_clipboard_and_add(self):
        if self.clipboard_capturing_checkbox.isChecked():
            time.sleep(0.01)
            data = pyperclip.paste()
            self.add_entry(data)
        pass

    def add_item_to_table(self):
        self.add_entry("")
        pass
    
    def remove_item_from_table(self):
        current_row = self.table.currentRow()
        if current_row in self.disabled:
            self.disabled.remove(current_row)
        self.table.removeRow(current_row)
        pass

    def enable_item_in_table(self):
        current_row = self.table.currentRow()
        if current_row in self.disabled:
            self.disabled.remove(current_row)
            ##print(self.disabled)
        current_item = self.table.currentItem()
        current_item.setBackground(QColor(225, 225, 225, 0))
        self.table.setCurrentItem(current_item)
        pass
    
    def disable_item_in_table(self):
        current_row = self.table.currentRow()
        if not(current_row in self.disabled):
            self.disabled.append(current_row)
            ##print(self.disabled)
        current_item = self.table.currentItem()
        current_item.setBackground(QColor(220, 220, 220, 255))
        self.table.setCurrentItem(current_item)
        pass
    
    def clicked_item_in_table(self, item):
        pyperclip.copy(item.text()) 
        pass

    def clicked_sequential_pasting(self):
        pass

    def clicked_clipboard_capturing(self):
        pass

    def changed_window_opacity(self, value):
        self.setWindowOpacity(value/100)
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainframe = MainFrame()
    mainframe.show()
    sys.exit(app.exec_())