# Chocolate Management System (DEPLOYED USING STREAMLIT)

## 🚀 [**Access the Deployed Application Here!**](https://l7-kiran-yarashi.streamlit.app/)
[https://l7-kiran-yarashi.streamlit.app/](https://l7-kiran-yarashi.streamlit.app/)


A  management system for tracking and handling chocolate ingredients, flavors, and customer suggestions!

### 📋 *Developer*: [Kiran Yarashi]  
### 📅 *Date*: 2024-11-03


# Features

- *Ingredients Management*  
  - Add Ingredients  
  - Manage Ingredients  
  - Update Ingredient Quantity  
  - Delete Ingredients 

- *Flavor Management*  
  - Add Flavors  
  - View Flavors  
  - Delete Flavors  

- *Customer Suggestions*  
  - Collect and view customer suggestions

---

##  Tech Stack

- *Python* - Backend development
- *Streamlit* - Web application framework
- *SQLite* - Database for data storage and management
- *Docker* - Containerization for easy deployment




---
##  Installation

Steps to set up the application locally:

1. Clone the repository:
   ```sh
   git clone https://github.com/KiranYarashi/L7_Assesment_Kiran_Yarashi.git
   ```

2. Set up the virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # For Windows
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:
   ```sh
   cd app
   streamlit run streamlit_app.py
   ```

5. Open the browser and navigate to:
   ```sh
   http://localhost:8502
   ```
---

## Running Tests
To validate the application, you can run the unit tests provided:

1. Ensure the virtual environment is activated.
2. Run the tests using `unittest`:
   ```sh
   python -m unittest discover -s tests
   ```

---
## SQL Queries and ORM Abstraction
The application uses raw SQL queries for database operations. Here are some examples:

- **Add Flavour**:
  ```sql
  INSERT INTO flavours(name, description, is_seasonal, season) VALUES(?, ?, ?, ?)
  ```

- **Get All Flavours**:
  ```sql
  SELECT * FROM flavours
  ```

- **Delete Flavour**:
  ```sql
  DELETE FROM flavours WHERE id = ?
  ```
  
---
## Docker-based Build and Run
To build and run the application using Docker, follow these steps:
Go to the Directory where Dockerfile is present then

1. Build the Docker image:
   ```sh
   docker build -t chocolate-management-system .
   ```

2. Run the Docker container:
   ```sh
   docker run -p 8501:8501 chocolate-management-system
   ```

3. Open the browser and navigate to:
   ```sh
   http://localhost:8501
   ```

---

## Additional Information
For more details on the implementation, refer to the code documentation within the source files, especially in the [`app`](app) directory.
