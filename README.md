## Project Overview
This project is a Flask-based API for managing a Library Management System. It allows users to perform CRUD (Create, Read, Update, Delete) operations on books and members. The API also provides the ability to filter books by title or author's name and includes author details when fetching book data.

---

## How to Run the Project

### Prerequisites
1. Python 3.8 or later installed.
2. Basic knowledge of running Flask applications.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd library-management-system
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install Flask:
   ```bash
   pip install flask
   ```

### Running the Application
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. The application will run on `http://127.0.0.1:5001` by default.

### API Endpoints
#### Members
1. **Add Member**:
   - Endpoint: `POST /members`
   - Body Example:
     ```json
     {
         "name": "Akash Das",
         "email": "akash@example.com"
     }
     ```
2. **Fetch Members**:
   - Endpoint: `GET /members`
   - Query Parameters:
     - `name` (optional): Filter by member's name.
     - `email` (optional): Filter by member's email.

#### Books
1. **Add Book**:
   - Endpoint: `POST /books`
   - Body Example:
     ```json
     {
         "title": "Flask for Beginners",
         "author": 1,  # Member ID
         "content": "A comprehensive guide to Flask."
     }
     ```
2. **Fetch Books**:
   - Endpoint: `GET /books`
   - Query Parameters:
     - `title` (optional): Filter by book title.
     - `author` (optional): Filter by author's name.

---

## Design Choices
1. **Data Structures**:
   - Books and members are stored in dictionaries (`books` and `members`) for simplicity and quick lookups during development.
   
2. **Separation of Concerns**:
   - Each API endpoint handles a single responsibility (e.g., adding or fetching data).

3. **Dynamic Author Data in Books**:
   - When fetching books, author details (name and email) are dynamically included to provide a richer response.

4. **Search Functionality**:
   - Query parameters are used for flexible and user-friendly filtering.

5. **Error Handling**:
   - The API checks for missing data and invalid references (e.g., non-existent author) before performing operations.

---

## Assumptions and Limitations

### Assumptions
1. **Author Exists Before Adding a Book**:
   - Authors (members) must be added before books can reference them.
2. **Case-Insensitive Filters**:
   - Filters for `title` and `author` are case-insensitive for ease of use.

### Limitations
1. **No Persistent Database**:
   - Data is stored in memory (dictionaries) and is lost when the application stops.
2. **Basic Authentication**:
   - No authentication or authorization is implemented.
3. **No Update or Delete Operations**:
   - The current implementation supports only creation and retrieval of books and members.

---

## Future Improvements
1. **Database Integration**:
   - Use a database (e.g., SQLite, PostgreSQL) for persistent data storage.
2. **Authentication**:
   - Implement token-based authentication (e.g., JWT).
3. **CRUD Enhancements**:
   - Add support for updating and deleting books and members.
4. **Pagination**:
   - Include pagination for fetching large datasets of books or members.

