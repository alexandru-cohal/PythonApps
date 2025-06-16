# PythonApps
Python Apps created while taking the Udemy course _"Python Mega Course: Learn Python in 60 Days, Build 20 Apps"_:
* **ToDoListApp**: App for tracking the ToDos with the possibility to add, edit, remove and show ToDos.
  *  [ToDoListApp/main_cli.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ToDoListApp/main_cli.py): CLI (Command Line Interface) version.
  *  [ToDoListApp/main_gui.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ToDoListApp/main_gui.py): GUI (Graphical User Interface) version. Standalone executable available [here](https://github.com/alexandru-cohal/PythonApps/blob/master/ToDoListApp/dist/main_gui.exe).
  *  [ToDoListApp/main_web.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ToDoListApp/main_web.py): WebApp version. Local execution using the command `streamlit run main_web.py`. Deployed version available [here](https://todolistapp-8smxwkmdvchwawix6ytkjv.streamlit.app/).
  *  **Libraries, Tools & Concepts**: GUI with _FreeSimpleGUI_, standalone executable generation with _Pyinstaller_, WebApp with _Streamlit_, WebApp deployment, generation of _requirements.txt_ file.

* **FilesZipperApp**: App for adding multiple selected files into a Zip archive in a selected directory.
  *  [FilesZipperApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/FilesZipperApp/main.py): GUI version.
  *  **Libraries, Tools & Concepts**: GUI with _FreeSimpleGUI_.

* **ProjectsShowcaseApp**: App for presenting all the Python Apps created.
  * [ProjectsShowcaseApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ProjectsShowcaseApp/main.py): WebApp version. Local execution using the command `streamlit run main_web.py`. Not yet deployed.
  * **Libraries, Tools & Concepts**: GUI design with [Figma](https://www.figma.com/), _Pandas_, WebApp with _Streamlit_, CSV file reading, Email sending with _smtplib_ and _ssl_.

* **TopicsNotesPDFGeneratorApp**: App for generating a PDF document containing pages with grid lines for taking notes for dirrent topics, based on a CSV list containing topic names and pages required.
  *  [TopicsNotesPDFGeneratorApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/TopicsNotesPDFGeneratorApp/main.py): Script version
  *  **Libraries, Tools & Concepts**: _Pandas_, CSV file reading, PDF generation with _PyFPDF_.

* **ExcelToPDFInvoiceGeneratorApp**: App for generating PDF invoices based on XLSX orders.
  * [ExcelToPDFInvoiceGeneratorApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/ExcelToPDFInvoiceGeneratorApp/main.py): Script version
  * **Libraries, Tools & Concepts**: _Pandas_, XLSX file reading, PDF generation with _PyFPDF_.

* **DailyNewsByEmailApp**: App which sends by email the latest news obtained by using the [newsapi.org](https://newsapi.org/) API from a specific topic (i.e. now set to Eurovision) and from a specific period of time (i.e. now set to the ones from the day before).
  * [DailyNewsByEmailApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/DailyNewsByEmailApp/main.py): Script version
  * **Libraries, Tools & Concepts**: API usage (sending requests & getting answers) with _requests_, Email sending with _smtplib_ and _ssl_, scheduling with [PythonAnywhere](https://www.pythonanywhere.com/).

* **DailyAstronomyPhotoApp**: App which gets the daily astronomy photo and its description using the [APOD NASA](https://api.nasa.gov/) API and displays them.
  * [DailyAstronomyPhotoApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/DailyAstronomyPhotoApp/main.py): WebApp version
  * **Libraries, Tools & Concepts**: API usage (sending requests & getting answers) with _requests_, _Streamlit_, WebApp deployment.

* **WeatherDataAPI**: REST API which provides temperature values for requests for a specific station and for a specific day, year or complete history.
  * [WeatherDataAPI/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WeatherDataAPI/main.py): REST API
  * **Libraries, Tools & Concepts**: _Pandas_, CSV file reading, REST API creation with _Flask_.

* **WeatherForecastDashboardApp**: App which displays the weather forecast (temperature or sky) for a specific location and for a specific period of time (up to 5 days).
  * [WeatherForecastDashboardApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WeatherForecastDashboardApp/main.py): WebApp version
  * **Libraries, Tools & Concepts**: API usage (sending requests & getting answers) with requests, WebApp with _Streamlit_, plot generation with _plotly_.

* **BookAnalysisNotebook**: Jupyter Notebook which contains different analyses of a book (e.g. extraction of chapter titles, most used words, sentiment analysis of each chapter)
  * [BookAnalysisNotebook/regex_book_analysis.ipynb](https://github.com/alexandru-cohal/PythonApps/blob/master/BookAnalysisNotebook/regex_book_analysis.ipynb): Jupyter Notebook 
  * [BookAnalysisNotebook/nlp_book_analysis.ipynb](https://github.com/alexandru-cohal/PythonApps/blob/master/BookAnalysisNotebook/nlp_book_analysis.ipynb): Jupyter Notebook
  * **Libraries, Tools & Concepts**: JupyterLab, data analysis, regular expressions with _re_, natural language processing (NLP) with _nltk_.

* **WebcamDetectionApp**: App which continuosly checks the frames from a webcam for new objects / persons and sends an email when a new detection is done.
  * [WebcamDetectionApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WebcamDetectionApp/main.py): Script version.
  * [WebcamDetectionApp/main_web.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WebcamDetectionApp/main_web.py): WebApp version. Local execution using the command `streamlit run main_web.py`.
  * **Libraries, Tools & Concepts**: WebApp with _Streamlit_, image acquisition from webcam, image processing with _OpenCV_ (_cv2_), threading with _threading_, Email sending with _smtplib_ and _ssl_.

* **WebScrapingEventApp**: App which scraps information about new events from a [website](https://programmer100.pythonanywhere.com/tours/) and updates a database and sends a notification emails when new such events are found.
  * [WebScrapingEventApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WebScrapingEventApp/main.py): Script version.
  * **Libraries, Tools & Concepts**: Web data scraping with _requests_, processing of scraped data with _selectorlib_ and YAML CSS extractors, SQLite databases with _sqlite3_ and [DB Browser for SQLite](https://sqlitebrowser.org/), Email sending with _smtplib_ and _ssl_.
 
* **WebScrapingTempApp**: App which scraps information about temperature from a [website](https://programmer100.pythonanywhere.com/), updates a database and plots the obtained data in a WebApp.
  * [WebScrapingTempApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/WebScrapingTempApp/main.py): Script version.
  * **Libraries, Tools & Concepts**: Web data scraping with _requests_, processing of scraped data with _selectorlib_ and YAML CSS extractors, SQLite databases with _sqlite3_ and [DB Browser for SQLite](https://sqlitebrowser.org/), WebApp with _Streamlit_.

* **HotelBookingApp**: App for booking a hotel (if available) and a spa package if there is availability and the credit card is validated.
  * [HotelBookingApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/HotelBookingApp/main.py): CLI version.
  * **Libraries, Tools & Concepts**: OOP, _Pandas_, CSV file reading.
 
* **StudentManagementApp**: App for managing the records of a group of students (i.e. adding, editing, removing) stored in a database.
  * [StudentManagementApp/main_sqlite.py](https://github.com/alexandru-cohal/PythonApps/blob/master/StudentManagementApp/main_sqlite.py): GUI version which uses SQLite database system.
  * [StudentManagementApp/main_mysql.py](https://github.com/alexandru-cohal/PythonApps/blob/master/StudentManagementApp/main_mysql.py): GUI version which uses MySQL database system.
  * **Libraries, Tools & Concepts**: OOP, GUI with _PyQt6_, SQLite databases with _sqlite3_, MySQL databases with _mysql.connector_.

* **BrowserAutomationApp**: App for automatizing actions (e.g. login, filling in a form and submitting it, downloading a file) on a website in the browser.
  * [BrowserAutomationApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/BrowserAutomationApp/main.py): Script version.
  * [BrowserAutomationApp/main_gui.py](https://github.com/alexandru-cohal/PythonApps/blob/master/BrowserAutomationApp/main_gui.py): GUI version.
  * **Libraries, Tools & Concepts**: OOP, GUI with _Tkinter_, web automation in the Google Chrome browser with _Selenium_.
 
* **JobApplicationApp**: App for submitting the personal details for a job, storing them in a database and sending a confirmation email once the submittion is done.
  * [JobApplicationApp/main.py](https://github.com/alexandru-cohal/PythonApps/blob/master/JobApplicationApp/main.py): WebApp version.
  * **Libraries, Tools & Concepts**: WebApp with _Flask_, _Bootstrap_ and _Jinja2_, SQLite databases with _Flask-SQLAlchemy_, Email sending with _Flask-Mail_
