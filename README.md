# Python Mini Project - Web Application
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![XAMPP](https://img.shields.io/badge/XAMPP-8.0+-orange.svg)](https://www.apachefriends.org/)

A web application that uses a Python script to launch a local server and display a web page using PyQt5's WebEngineView. The web application is served from the XAMPP `htdocs` directory.

## 📋 Requirements

- **Python 3.x**
- **PyQt5**
- **XAMPP** (Apache and MySQL services running)

## 🚀 Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/Captain-Vikram/QuizGenByPython.git
   cd QuizGenByPython
   ```

2. **Install PyQt5**
   ```sh
   pip install PyQt5 PyQtWebEngine
   ```

3. **Install and Start XAMPP**
   - Download and install XAMPP from [https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html)
   - Start the Apache and MySQL services from the XAMPP control panel

4. **Import SQL Database**
   - Open your web browser and navigate to `http://localhost/phpmyadmin/`
   - Create a new database (e.g., `quiz_db`)
   - Select the newly created database
   - Click on the "Import" tab in the top navigation menu
   - Click "Choose File" and select the `database.sql` file from the project directory
   - Click "Go" to import the database structure and data
   - Verify that all tables have been created successfully

## 📂 Directory Structure

```
C:/xampp/htdocs/web/
├── login.html
├── img/
│   └── logo.jpg
├── favicon.ico
├── authenticate.php
└── ... (other web files)

C:/Users/<your_preferred_folder>/
└── launch.py
```

> **Note:** Adjust the paths according to your actual file locations.

## 🔧 Setup and Execution

1. **Place Your Web Files**
   - Ensure that your `login.html` and other web files (including `img`, `favicon.ico`, `authenticate.php`, etc.) are located in the `C:/xampp/htdocs/web/` directory

2. **Run the Python Script**
   - Navigate to the directory containing `launch.py`
   - Run the script:
     ```sh
     python launch.py
     ```

3. **Access the Web Application**
   - The script will start a local server and open a window displaying your `login.html` file using PyQt5 WebEngineView
   - The web page will interact with the server running on XAMPP

## ⚠️ Important Notes

- Ensure that XAMPP's Apache server is running before executing the Python script
- The `launch.py` script assumes that your web files are correctly placed in the `C:/xampp/htdocs/web/` directory
- The `authenticate.php` file is assumed to handle authentication logic
- Replace the example paths with your actual paths
- Make sure the database connection settings in your PHP files match the database name you created

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
