# Data Sorting Project

## Overview

This Django project facilitates the extraction, sorting, and display of data from CSV files. It includes functionality to upload CSV files, process the data, and store it in a Django database. Users can then view the sorted data on a web page and download it in CSV format.

## Getting Started

Follow these instructions to set up and run the project locally.

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
     cd .\XICRLS_ASSIGNMENT\
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to http://localhost:8000/ to access the upload page.

## Usage

1. **Upload Data:**
   - Navigate to the upload page.
   - Choose a CSV file with the specified format (First Name, Last Name, Email, Phone No, Gender, DOB, Address 1, Address 2, Pincode, State, Country).
   - Click "Upload" to process and store the data.

2. **View Sorted Data:**
   - the display page to view the sorted data in a tabular format.

3. **Download Data:**
   - Choose from the following options:
     - Download Contact Info CSV
     - Download Personal Info CSV
     - Download Combined CSV
     
## Resources

- [Stack Overflow](https://stackoverflow.com/): For assistance with coding issues and troubleshooting.
- [PythonCircle](https://www.pythoncircle.com/): A community resource for handling csv file in Python,related tutorials and discussions.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
