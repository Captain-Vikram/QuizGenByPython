```markdown
# JAVA Mini Project - Web Application

This project is a web application that uses a Python script to launch a local server and display a web page using PyQt5's WebEngineView. The web application is served from the XAMPP `htdocs` directory.

## Requirements

- **Python 3.x**
- **PyQt5** (`pip install PyQt5 PyQtWebEngine`)
- **XAMPP** (Apache and MySQL services running)

## Installation

1.  **Install PyQt5**:

    ```sh
    pip install PyQt5 PyQtWebEngine
    ```

2.  **Install and Start XAMPP**:

    -   Download and install XAMPP from [https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html).
    -   Start the Apache and MySQL services from the XAMPP control panel.

## Directory Structure

Ensure your project directory structure looks like this:

```
C:/xampp/htdocs/web/
├── login.html
├── img/
│   └── logo.jpg
├── favicon.ico
├── authenticate.php
└── ... (other web files)

C:/Users/konth/Desktop/Practical reports/JAVA Mini Project/web/
└── launch.py
```

**Note:** Adjust the paths according to your actual file locations.

## Setup and Execution

1.  **Place Your Web Files**:

    -   Ensure that your `login.html` and other web files (including `img`, `favicon.ico`, `authenticate.php`, etc.) are located in the `C:/xampp/htdocs/web/` directory.

2.  **Run the Python Script**:

    -   Navigate to the directory containing `launch.py` (e.g., `C:/Users/konth/Desktop/Practical reports/JAVA Mini Project/web/`).
    -   Run the script:

        ```sh
        python launch.py
        ```

3.  **Access the Web Application**:

    -   The script will start a local server and open a window displaying your `login.html` file using PyQt5 WebEngineView.
    -   The web page will interact with the server running on XAMPP.

## Important Notes

-   Ensure that XAMPP's Apache server is running before executing the Python script.
-   The `launch.py` script assumes that your web files are correctly placed in the `C:/xampp/htdocs/web/` directory. Adjust the paths in your web files and potentially the python script if your files are located elsewhere.
-   The `authenticate.php` file is assumed to handle authentication logic. Make sure it is correctly configured within your XAMPP environment.
-   Replace the example paths with your actual paths.
-   If you have any issues with the python script, ensure all the required python modules are installed.
```
