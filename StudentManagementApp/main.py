from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QDialog, \
    QVBoxLayout, QLineEdit, QComboBox, QPushButton, QToolBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import sys
import sqlite3


# The MainWindow class inherits QMainWindow and not QWidget in order to create divisions within
# the main window, add a menu bar, a tool bar, a status bar, etc.
class MainWindow(QMainWindow):
    def __init__(self):
        # Call the __init__ from the parent class
        super().__init__()

        self.setWindowTitle("Student Management App")
        self.setMinimumSize(800, 600)

        # Set the menu bar
        file_menu_item = self.menuBar().addMenu("&File")
        add_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        edit_menu_item = self.menuBar().addMenu("&Edit")
        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

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

        # Set the tool bar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

    def load_data(self):
        """ Load the data from the database and display it in the table from the main window """

        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")

        # Reset the table, in order to not add the new data in continuation, but from the beginning
        self.table.setRowCount(0)

        # Add the data to the table
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

    def insert(self):
        """ Display the insert window """
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        """ Display the search window """
        dialog = SearchDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add the LineEdit widget for the student's name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add the ComboBox widget for the student's course
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add the LineEdit widget for the student's mobile number
        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile_number)

        # Add the submit button
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        """ Add a new student to the database """
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_number.text()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()

        # Refresh the displayed table data in the main window
        app_main_window.load_data()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add the LineEdit widget for the student's name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add the search button
        button = QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)

    def search(self):
        """ Search the table for the given name """

        name_to_search = self.student_name.text()
        matches = app_main_window.table.findItems(name_to_search, Qt.MatchFlag.MatchFixedString)
        for match in matches:
            app_main_window.table.item(match.row(), 1).setSelected(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_main_window = MainWindow()
    app_main_window.show()
    app_main_window.load_data()
    sys.exit(app.exec())