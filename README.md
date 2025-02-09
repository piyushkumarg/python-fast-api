
# FastAPI Backend API

This is a simple FastAPI backend API project. It is built with Python and FastAPI to serve as the backend for a web or mobile application. It includes dynamic routing and schema validation with Pydantic.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Important Commands](#important-commands)
- [Contributing](#contributing)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-project-name.git
   cd your-project-name
   ```


2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Development Server

To run the development server using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

To run the develoment server using `fastapi`

```bash
fastapi dev app/main.py
```

This starts the FastAPI app on `http://127.0.0.1:8000` by default.

### Accessing the Swagger Documentation

Once the server is running, you can access the auto-generated API documentation by navigating to:

- **API Docs**: `http://127.0.0.1:8000/docs`

### Environment Variables

Ensure to add any environment variables required for your project. You can create a `.env` file in the root of the project if necessary and use libraries like `python-dotenv` to manage them.

## Project Structure

```
app/
├── __init__.py          # Marks app directory as a package
├── main.py              # FastAPI app initialization and routes
├── routes/              # API routes folder
│   ├── user/            # User routes
│   │   └── index.py     # User route definitions
├── schemas/             # Pydantic schemas for request validation
├── services/            # Business logic for APIs
├── controllers/         # Controller files for handling API calls
└── models/              # Database models (if applicable)
```

## Important Commands

- **Run the development server** `uvicorn`:

  ```bash
  uvicorn app.main:app --reload
  ```

- **Run the development server** `fastapi`:

  ```bash
  fastapi dev app/main.py
  ```

- **Install dependencies**:

  ```bash
  pip install -r requirements.txt
  ```

- **Run tests**:

  ```bash
  pytest
  ```

- **Generate requirements.txt**:

  ```bash
  pip freeze > requirements.txt
  ```

- **Create virtual environment**:

  ```bash
  python3 -m venv venv
  ```

- **Activate virtual environment**:

  - macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
  - Windows:
    ```bash
    .\venv\Scripts\activate
    ```

- **Deactivate virtual environment**:
  ```bash
  deactivate
  ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
