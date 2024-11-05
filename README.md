# Chocolate Management System (DEPLOYED USING STREAMLIT)

## 🚀 [**Access the Deployed Application Here!**](https://l7-kiran-yarashi.streamlit.app/)
[https://l7-kiran-yarashi.streamlit.app/](https://l7-kiran-yarashi.streamlit.app/)


A  management system for tracking and handling chocolate ingredients, flavors, and customer suggestions!

###  *Developer*: [Kiran Yarashi]  
###  *Assessment*: L7 Informatics  
###  *Date*: 2024-11-03

---
# Features


- **Ingredients Management**  
  - Add, manage, update, and delete ingredients with ease

- **Flavor Management**  
  - Add, view, and delete flavors

- **Customer Suggestions**  
  - Collect and view customer feedback on flavors and ingredients


---

##  Tech Stack

- *Python* - Backend development
- *SQLite* - Database for data storage and management
- *Streamlit* - Web application framework
- *Docker* - Containerization for easy deployment


---

## 🛠 Installation

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


## 🐳Docker-based Build and Run
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

## Test Steps

### Ingredients Management

- **Add a new ingredient** and verify it appears in the list.
- **Update the quantity of an ingredient** and ensure the changes are saved.
- **Delete an ingredient** and confirm it no longer appears in the list.

### Flavor Management

- **Add a new flavor**, then view it in the flavors list.
- **Delete a flavor** and confirm it is removed from the list.

### Customer Suggestions

- **Submit a new suggestion** and verify it appears in the suggestions list.

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

- **Add Ingredient**:
  ```sql
  INSERT INTO ingredients(name, quantity, unit, allergen_info) VALUES(?, ?, ?, ?)
  ```

- **Get All Ingredients**:
  ```sql
  SELECT * FROM ingredients
  ```

- **Delete Ingredient**:
  ```sql
  DELETE FROM ingredients WHERE id = ?
  ```
---

## file structure of my project
L7_Assesment_Kiran_Yarashi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── streamlit_app.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── models/
│   │   ├── __init__.py
│   │   ├── flavour.py
│   │   ├── ingredient.py
│   │   └── suggestion.py
│   ├── services/
│       ├── __init__.py
│       ├── flavour_service.py
│       ├── ingredient_service.py
│       └── suggestion_service.py          
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore

---
  For more details, refer to the methods in the [`FictionalChocoHouse`](app/main.py) class.
  
---


## Additional Information
For more details on the implementation, refer to the code documentation within the source files, especially in the [`app`](app) directory.
