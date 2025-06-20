from dotenv import load_dotenv
load_dotenv("../.env")

import mysql.connector
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QDialog, \
    QVBoxLayout, QLineEdit, QComboBox, QPushButton, QToolBar, QStatusBar, QGridLayout, QLabel, \
    QMessageBox
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import sys
import os


class DatabaseConnection:
    def __init__(self, host="localhost", user="root", password=os.getenv("MYSQL_ROOT_PASS"), database="school"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """ Create a connection to the database """

        connection = mysql.connector.connect(host=self.host,
                                             user=self.user,
                                             password=self.password,
                                             database=self.database)
        return connection


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
        about_action.triggered.connect(self.about)

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

        # Set the status bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        self.table.cellClicked.connect(self.cell_clicked)

    def load_data(self):
        """ Load the data from the database and display it in the table from the main window """

        database = DatabaseConnection()
        connection = database.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
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

    def cell_clicked(self):
        """ Behaviour when a cell table is clocked => Display the status bar """

        # Remove the already added buttons from the status bar, if any
        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        # Add buttons to the status bar
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)
        self.statusbar.addWidget(edit_button)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)
        self.statusbar.addWidget(delete_button)

    def edit(self):
        """ Display the edit window """

        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        """ Display the delete window """

        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        """ Display the about window """

        dialog = AboutDialog()
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

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)",
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


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        index_selected_row = app_main_window.table.currentRow()
        self.selected_student_id = app_main_window.table.item(index_selected_row, 0).text()
        selected_student_name = app_main_window.table.item(index_selected_row, 1).text()
        selected_course_name = app_main_window.table.item(index_selected_row, 2).text()
        selected_mobile_number = app_main_window.table.item(index_selected_row, 3).text()

        # Add the LineEdit widget for the student's name
        self.student_name = QLineEdit(selected_student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add the ComboBox widget for the student's course
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(selected_course_name)
        layout.addWidget(self.course_name)

        # Add the LineEdit widget for the student's mobile number
        self.mobile_number = QLineEdit(selected_mobile_number)
        self.mobile_number.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile_number)

        # Add the submit button
        button = QPushButton("Update")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        """ Update the student's details """

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s",
                       (self.student_name.text(), self.course_name.itemText(self.course_name.currentIndex()),
                        self.mobile_number.text(), self.selected_student_id))
        connection.commit()
        cursor.close()
        connection.close()
        app_main_window.load_data()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")

        layout = QGridLayout()

        confirmation = QLabel("Are you sure you want to delete the data?")
        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes_button, 1, 0)
        layout.addWidget(no_button, 1, 1)

        self.setLayout(layout)

        yes_button.clicked.connect(self.delete_student)

    def delete_student(self):
        """ Delete the selected student """

        index_selected_row = app_main_window.table.currentRow()
        selected_student_id = app_main_window.table.item(index_selected_row, 0).text()

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE from students WHERE id = %s", (selected_student_id, ))
        connection.commit()
        cursor.close()
        connection.close()
        app_main_window.load_data()

        # Close the window after deletion
        self.close()

        # Set a confirmation MessageBox
        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText("The record was deleted successfully")
        confirmation_widget.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")

        content = """ 
        This app is a Student Management System.
        The name, course and mobile phone number of each student are stored in a database.
        New records can be added.
        The existent records of a student can be updated or removed. 
        The records can be searched for a provided student name. 
        """
        self.setText(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_main_window = MainWindow()
    app_main_window.show()
    app_main_window.load_data()
    sys.exit(app.exec())