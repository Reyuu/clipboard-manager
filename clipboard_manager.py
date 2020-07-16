import clipboard_manager_gui
import sys
import keyboard
import pyperclip
import time
import json
from pathlib import Path
from PySide2.QtCore import *
from PySide2.QtGui import QIcon, QColor, QTextCursor, QTextCharFormat, QCursor
from PySide2.QtWidgets import QFileDialog, QAction, QLabel, QWidgetAction, QMenu, QDialogButtonBox, QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QFontDialog, QHBoxLayout, QColorDialog, QScrollArea, QMainWindow, QFrame, QGroupBox, QRadioButton, QStyle, QStyleOption, QTableWidgetItem

class SettingsMenu(QMenu):
    def __init__(self, title="", parent=None):
        super(SettingsMenu, self).__init__(title, parent)

        #Sequential pasting
        seq = QAction(QIcon(), "Sequential pasting", self)
        seq.setCheckable(True)
        seq.setChecked(self.parentWidget().use_sequential_pasting)
        seq.triggered.connect(self.sequential_pasting)
        self.addAction(seq)
        #Clipboard capturing
        clip = QAction(QIcon(), "Clipboard capturing", self)
        clip.setCheckable(True)
        clip.setChecked(self.parentWidget().use_clipboard_capturing)
        clip.triggered.connect(self.clipboard_capturing)
        self.addAction(clip)
        #Window opacity
        window_opacity = QAction(QIcon(), "Show window opacity slider", self)
        window_opacity.setCheckable(True)
        window_opacity.setChecked(self.parentWidget().show_window_opacity_slider)
        window_opacity.triggered.connect(self.window_opacity_toggle)
        self.addAction(window_opacity)

        #Separator
        self.addSeparator()
        
        #Save clipboard
        save = QAction(QIcon(), "Save clipboard", self)
        save.triggered.connect(self.save_clipboard)
        self.addAction(save)
        #Load clipboard
        load = QAction(QIcon(), "Load clipboard", self)
        load.triggered.connect(self.load_clipboard)
        self.addAction(load)
        #Separator
        self.addSeparator()
        #Exit
        close = QAction(QIcon(), "Exit", self)
        close.triggered.connect(self.parentWidget().close)
        self.addAction(close)
    
    def set_correct_window_title(self):
        title = "Clipboard manager"
        sequential = self.parentWidget().use_sequential_pasting
        capturing = self.parentWidget().use_clipboard_capturing
        if sequential:
            title += " [SEQ]"
        if capturing:
            title += " [CAP]"
        self.parentWidget().setWindowTitle(title)
    
    def sequential_pasting(self):
        current_value = not(self.parentWidget().use_sequential_pasting)
        self.parentWidget().use_sequential_pasting = current_value
        self.set_correct_window_title()
        
    def clipboard_capturing(self):
        current_value = not(self.parentWidget().use_clipboard_capturing)
        self.parentWidget().use_clipboard_capturing = current_value
        self.set_correct_window_title()

    def window_opacity_toggle(self):
        current_value = not(self.parentWidget().show_window_opacity_slider)
        self.parentWidget().show_window_opacity_slider = current_value
        self.parentWidget().window_opacity_slider.setVisible(current_value)
        self.parentWidget().window_opacity_label.setVisible(current_value)
    
    def save_clipboard(self):
        self.parentWidget().save_clipboard()
        pass

    def load_clipboard(self):
        self.parentWidget().load_clipboard()
        pass

class MainFrame(QFrame, clipboard_manager_gui.Ui_Frame):
    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent)
        super(MainFrame, self).setupUi(self)
        self.current_flags = Qt.WindowStaysOnTopHint
        self.setWindowFlags(self.current_flags)
        keyboard.add_hotkey("ctrl+c", self.get_from_clipboard_and_add)
        keyboard.add_hotkey("ctrl+v", self.pasting_from_manager)

        self.disabled = []
        self.use_sequential_pasting = False
        self.use_clipboard_capturing = False
        self.show_window_opacity_slider = False
    
    def save_clipboard(self):
        path_name, __ = QFileDialog.getSaveFileName(self, "Save clipboard", str(Path.home()), "JSON files (*.json)")
        object_list = []
        create_object = lambda i, contents, isenabled: {"row":i, "contents": contents, "enabled": isenabled}
        for i in range(self.table.rowCount()):
            object_list += [create_object(i, self.table.item(i, 0).text(), False if i in self.disabled else True)]
        
        with open(path_name, "w") as f:
            f.write(json.dumps(object_list))
        pass

    def load_clipboard(self):
        path_name, __ = QFileDialog.getOpenFileName(self, "Load clipboard", str(Path.home()), "JSON files (*.json);;All files (*.*)")
        object_list = []
        with open(path_name, "r") as f:
            data = f.read()
            object_list = json.loads(data)
        for i in range(self.table.rowCount()):
            self.table.removeRow(0)
        self.disabled = []
        for item in object_list:
            self.add_entry(item["contents"], item["row"])
            if not(item["enabled"]):
                self.disabled += [item["row"]]
        pass
    
    def add_entry(self, string, i=None):
        if i is None:
            row = self.table.rowCount()
        else:
            row = i
        self.table.insertRow(row)
        qtablewidgetitem = QTableWidgetItem()
        qtablewidgetitem.setText(string)
        self.table.setItem(row, 0, qtablewidgetitem)
        self.table.setSortingEnabled(True)
    
    def pasting_from_manager(self):
        if self.use_sequential_pasting:
            #another dirty hack, some machines switch faster than paste
            time.sleep(0.01)
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
        if self.use_clipboard_capturing:
            #yes, it's a dirty hack, only the best in the house
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
        if current_item is None:
            return
        current_item.setBackground(QColor(225, 225, 225, 0))
        self.table.setCurrentItem(current_item)
        pass
    
    def disable_item_in_table(self):
        current_row = self.table.currentRow()
        if not(current_row in self.disabled):
            self.disabled.append(current_row)
            ##print(self.disabled)
        current_item = self.table.currentItem()
        if current_item is None:
            return
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
    
    def clicked_settings(self):
        settings_x = SettingsMenu(parent=self)
        mpos = QCursor
        x = mpos.pos().x()
        y = mpos.pos().y()
        #settings_x.setGeometry(,-1,-1)
        settings_x.popup(mpos.pos())
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainframe = MainFrame()
    mainframe.show()
    sys.exit(app.exec_())