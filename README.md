# PythonApps

## Scope
Repository containing the Python Apps developed while taking the Udemy course [_"Python Mega Course: Learn Python in 60 Days, Build 20 Apps"_](https://www.udemy.com/course/the-python-mega-course/) in April - June 2025.

## Libraries, Tools & Concepts Used (a mix of everything)
* Python 3.13
* IDE PyCharm 2025.1 Community Edition
* GUI (_FreeSimpleGUI_, _PyQt6_, _Tkinter_)
* WebApp (_Streamlit_, _Flask_, _Django_, CSS styling with _Bootstrap_, templating with _Jinja_, admin interface with _Django_)
* WebApp deployment (_Streamlit_)
* Standalone executable generation (_Pyinstaller_)
* Generation of _requirements.txt_ file
* GUI design (_Figma_)
* Data Analysis and Data Science (_Pandas_, _Jupyter Notebook_, [_Deepnote_](https://deepnote.com/), Recommendation Systems, TFIDF (Term Frequency – Inverse Document Frequency), _sklearn_, ML (Machine Learning), SVD (Singular Value Decomposition), _surprise_)
* CSV and XLSX file reading
* Email sending (_smtplib_, _ssl_, _Flask-Mail_, _Django_)
* PDF generation (_PyFPDF_)
* API usage (_requests_)
* API creation (_Flask_)
* Scheduling ([_PythonAnywhere_](https://www.pythonanywhere.com/))
* Regular expressions (_re_)
* Natural Language Processing (NLP) (_nltk_)
* Image acquisition from webcam
* Image processing (_OpenCV_ - _cv2_)
* Threading (_threading_)
* Web scraping (_requests_, _selectorlib_, YAML CSS extractors)
* Databases
  * SQLite (_sqplite3_, _Flask-SQLAlchemy_, _Django_ and [DB Browser for SQLite](https://sqlitebrowser.org/))
  * MySQL - (_mysql.connector_)
* Object Oriented Programming (OOP)
* Web automation (_Selenium_, _Google Chrome_)
* Publishing a Python Package to [_PyPi_](https://pypi.org/)

## List of Apps
### ToDoListApp
* **Scope**: App for tracking the ToDos with the possibility to add, edit, remove and show ToDos.
* **Versions**:
  * [ToDoListApp/main_cli.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ToDoListApp/main_cli.py): CLI (Command Line Interface) version.
  * [ToDoListApp/main_gui.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ToDoListApp/main_gui.py): GUI (Graphical User Interface) version. Standalone executable available [here](https://github.com/alexandru-cohal/PythonApps/blob/master/ToDoListApp/dist/main_gui.exe).
  * [ToDoListApp/main_web.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ToDoListApp/main_web.py): WebApp version. Local execution using the command `streamlit run main_web.py`. Deployed version available [here](https://todolistapp-8smxwkmdvchwawix6ytkjv.streamlit.app/).
* **Libraries, Tools & Concepts**: GUI with _FreeSimpleGUI_, standalone executable generation with _Pyinstaller_, WebApp with _Streamlit_, WebApp deployment, generation of _requirements.txt_ file.

### **FilesZipperApp**
* **Scope**: App for adding multiple selected files into a Zip archive in a selected directory.
* **Versions**:
  * [FilesZipperApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/FilesZipperApp/main.py): GUI version.
* **Libraries, Tools & Concepts**: GUI with _FreeSimpleGUI_.

### **ProjectsShowcaseApp**
* **Scope**: App for presenting all the Python Apps created.
* **Versions**:
  * [ProjectsShowcaseApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ProjectsShowcaseApp/main.py): WebApp version. Local execution using the command `streamlit run main_web.py`. Not yet deployed.
* **Libraries, Tools & Concepts**: GUI design with [Figma](https://www.figma.com/), _Pandas_, WebApp with _Streamlit_, CSV file reading, Email sending with _smtplib_ and _ssl_.

### **TopicsNotesPDFGeneratorApp**
* **Scope**: App for generating a PDF document containing pages with grid lines for taking notes for dirrent topics, based on a CSV list containing topic names and pages required.
* **Versions**:
  *  [TopicsNotesPDFGeneratorApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/TopicsNotesPDFGeneratorApp/main.py): Script version
* **Libraries, Tools & Concepts**: _Pandas_, CSV file reading, PDF generation with _PyFPDF_.

### **ExcelToPDFInvoiceGeneratorApp**
* **Scope**: App for generating PDF invoices based on XLSX orders.
* **Versions**:
  * [ExcelToPDFInvoiceGeneratorApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ExcelToPDFInvoiceGeneratorApp/main.py): Script version
* **Libraries, Tools & Concepts**: _Pandas_, XLSX file reading, PDF generation with _PyFPDF_.

### **DailyNewsByEmailApp**
* **Scope**: App which sends by email the latest news obtained by using the [newsapi.org](https://newsapi.org/) API from a specific topic (i.e. now set to Eurovision) and from a specific period of time (i.e. now set to the ones from the day before).
* **Versions**:
  * [DailyNewsByEmailApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/DailyNewsByEmailApp/main.py): Script version
* **Libraries, Tools & Concepts**: API usage (sending requests & getting answers) with _requests_, Email sending with _smtplib_ and _ssl_, scheduling with [PythonAnywhere](https://www.pythonanywhere.com/).

### **DailyAstronomyPhotoApp**
* **Scope**: App which gets the daily astronomy photo and its description using the [APOD NASA](https://api.nasa.gov/) API and displays them.
* **Versions**:
  * [DailyAstronomyPhotoApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/DailyAstronomyPhotoApp/main.py): WebApp version
* **Libraries, Tools & Concepts**: API usage (sending requests & getting answers) with _requests_, _Streamlit_, WebApp deployment.

### **WeatherDataAPI**
* **Scope**: REST API which provides temperature values for requests for a specific station and for a specific day, year or complete history.
* **Versions**:
  * [WeatherDataAPI/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WeatherDataAPI/main.py): REST API
* **Libraries, Tools & Concepts**: _Pandas_, CSV file reading, REST API creation with _Flask_.

### **WeatherForecastDashboardApp**
* **Scope**: App which displays the weather forecast (temperature or sky) for a specific location and for a specific period of time (up to 5 days).
* **Versions**:
  * [WeatherForecastDashboardApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WeatherForecastDashboardApp/main.py): WebApp version
* **Libraries, Tools & Concepts**: API usage (sending requests & getting answers) with requests, WebApp with _Streamlit_, plot generation with _plotly_.

### **BookAnalysisNotebook**
* **Scope**: Jupyter Notebook which contains different analyses of a book (e.g. extraction of chapter titles, most used words, sentiment analysis of each chapter)
* **Versions**:
  * [BookAnalysisNotebook/regex_book_analysis.ipynb](https://github.com/alexandru-cohal/PythonApps/blob/master/BookAnalysisNotebook/regex_book_analysis.ipynb): Jupyter Notebook 
  * [BookAnalysisNotebook/nlp_book_analysis.ipynb](https://github.com/alexandru-cohal/PythonApps/blob/master/BookAnalysisNotebook/nlp_book_analysis.ipynb): Jupyter Notebook
* **Libraries, Tools & Concepts**: JupyterLab, data analysis, regular expressions with _re_, natural language processing (NLP) with _nltk_.

### **WebcamDetectionApp**
* **Scope**: App which continuosly checks the frames from a webcam for new objects / persons and sends an email when a new detection is done.
* **Versions**:
  * [WebcamDetectionApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WebcamDetectionApp/main.py): Script version.
  * [WebcamDetectionApp/main_web.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WebcamDetectionApp/main_web.py): WebApp version. Local execution using the command `streamlit run main_web.py`.
* **Libraries, Tools & Concepts**: WebApp with _Streamlit_, image acquisition from webcam, image processing with _OpenCV_ (_cv2_), threading with _threading_, Email sending with _smtplib_ and _ssl_.

### **WebScrapingEventApp**
* **Scope**: App which scraps information about new events from a [website](https://programmer100.pythonanywhere.com/tours/) and updates a database and sends a notification emails when new such events are found.
* **Versions**:
  * [WebScrapingEventApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WebScrapingEventApp/main.py): Script version.
* **Libraries, Tools & Concepts**: Web data scraping with _requests_, processing of scraped data with _selectorlib_ and YAML CSS extractors, SQLite databases with _sqlite3_ and [DB Browser for SQLite](https://sqlitebrowser.org/), Email sending with _smtplib_ and _ssl_.
 
### **WebScrapingTempApp**
* **Scope**: App which scraps information about temperature from a [website](https://programmer100.pythonanywhere.com/), updates a database and plots the obtained data in a WebApp.
* **Versions**:
  * [WebScrapingTempApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WebScrapingTempApp/main.py): Script version.
* **Libraries, Tools & Concepts**: Web data scraping with _requests_, processing of scraped data with _selectorlib_ and YAML CSS extractors, SQLite databases with _sqlite3_ and [DB Browser for SQLite](https://sqlitebrowser.org/), WebApp with _Streamlit_.

### **HotelBookingApp**
* **Scope**: App for booking a hotel (if available) and a spa package if there is availability and the credit card is validated.
* **Versions**:
  * [HotelBookingApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/HotelBookingApp/main.py): CLI version.
* **Libraries, Tools & Concepts**: OOP, _Pandas_, CSV file reading.
 
### **StudentManagementApp**
* **Scope**: App for managing the records of a group of students (i.e. adding, editing, removing) stored in a database.
* **Versions**:
  * [StudentManagementApp/main_sqlite.py](https://github.com/alexandru-cohal/PythonApps/blob/master/StudentManagementApp/main_sqlite.py): GUI version which uses SQLite database system.
  * [StudentManagementApp/main_mysql.py](https://github.com/alexandru-cohal/PythonApps/blob/master/StudentManagementApp/main_mysql.py): GUI version which uses MySQL database system.
* **Libraries, Tools & Concepts**: OOP, GUI with _PyQt6_, SQLite databases with _sqlite3_, MySQL databases with _mysql.connector_.

### **BrowserAutomationApp**
* **Scope**: App for automatizing actions (e.g. login, filling in a form and submitting it, downloading a file) on a website in the browser.
* **Versions**:
  * [BrowserAutomationApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/BrowserAutomationApp/main.py): Script version.
  * [BrowserAutomationApp/main_gui.py](https://github.com/alexandru-cohal/PythonApps/blob/master/BrowserAutomationApp/main_gui.py): GUI version.
* **Libraries, Tools & Concepts**: OOP, GUI with _Tkinter_, web automation in the Google Chrome browser with _Selenium_.
 
### **JobApplicationFlaskApp**
* **Scope**: App for submitting the personal details for a job, storing them in a database and sending a confirmation email once the submittion is done.
* **Versions**:
  * [JobApplicationFlaskApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/JobApplicationFlaskApp/main.py): WebApp version.
* **Libraries, Tools & Concepts**: WebApp with _Flask_, styling with _Bootstrap_ and templating with _Jinja_, SQLite databases with _Flask-SQLAlchemy_, Email sending with _Flask-Mail_.
 
### **JobApplicationDjangoApp**
* **Scope**: App for submitting the personal details for a job, storing them in a database, sending a confirmation email once the submittion is done and having and admin interface.
* **Versions**:
  * [JobApplicationDjangoApp/manage.py](https://github.com/alexandru-cohal/PythonApps/blob/master/JobApplicationDjangoApp/manage.py): WebApp version. Local execution using the command `python manage.py runserver`.
* **Libraries, Tools & Concepts**: WebApp with _Django_, styling with _Bootstrap_ and template with _Jinja_ (database, Email sending and admin interface covered by _Django_).
 
### **RestaurantManagementApp**
* **Scope**: App for managing the menu of a restaurant, storing all the items, their description, price, availability and author in a database, managing all these details through an admin interface.
* **Versions**:
  * [RestaurantManagementApp/manage.py](https://github.com/alexandru-cohal/PythonApps/blob/master/RestaurantManagementApp/manage.py): WebApp version. Local execution using the command `python manage.py runserver`.
* **Libraries, Tools & Concepts**: WebApp with _Django_, styling with _Bootstrap_ and template engine with _Jinja_ (database and admin interface covered by _Django_).

### **MovieRecommendationNotebook**
* **Scope**: Jupyter Notebooks containing 3 types of movie recommendation systems: Popularity Based Filtering, Content Based Filtering and Collaborative Based Filtering.
* **Versions**:
  * [MovieRecommendationNotebook/Popularity Based Filtering.ipynb](https://github.com/alexandru-cohal/PythonApps/blob/master/MovieRecommendationNotebook/Popularity%20Based%20Filtering.ipynb): Jupyter Notebook for Popularity Based Filtering.
  * [MovieRecommendationNotebook/Content Based Filtering.ipynb](https://github.com/alexandru-cohal/PythonApps/blob/master/MovieRecommendationNotebook/Content%20Based%20Filtering.ipynb): Jupyter Notebook for Content Based Filtering.
  * [MovieRecommendationNotebook/Collaborative Based Filtering.ipynb](https://github.com/alexandru-cohal/PythonApps/blob/master/MovieRecommendationNotebook/Collaborative%20Based%20Filtering.ipynb): Jupyter Notebook for Collaborative Based Filtering.
* **Libraries, Tools & Concepts**: JupyterLab within [Deepnote](https://deepnote.com/), data analysis, TFIDF (Term Frequency – Inverse Document Frequency) with _sklearn_ and SVD (Singular Value Decomposition) with _surprise_.
