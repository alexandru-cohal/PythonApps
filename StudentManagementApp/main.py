from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
import sys
import sqlite3

# The MainWindow class inherits QMainWindow and not QWidget in order to create divisions within the main window,
# add a menu bar, a tool bar, a status bar, etc.
class MainWindow(QMainWindow):
    def __init__(self):
        # Call the __init__ from the parent class
        super().__init__()

        self.setWindowTitle("Student Management App")

        # Set the menu bar
        file_menu_item = self.menuBar().addMenu("&File")
        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        help_menu_item = self.menuBar().addMenu("&Help")
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        # If the Help item is not displayed, add this line:
        # about_action.setMenuRole(QAction.MenuRole.NoRole)

        # Set the table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        # Hide the automatically added index column because the database data already has it
        self.table.verticalHeader().setVisible(False)

        # A central widget is needed when the QMainWindow is used.
        # Instead, a layout is used when QWidget is used (i.e. when multiple widgets are added).
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")

        # Reset the table, in order to not add the new data in continuation, but from the beginning
        self.table.setRowCount(0)

        # Add the data to the table
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_main_window = MainWindow()
    app_main_window.show()
    app_main_window.load_data()
    sys.exit(app.exec())