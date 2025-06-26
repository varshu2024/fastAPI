# fastAPI
# FastAPI Project Starter

A ready-to-use FastAPI starter project with user authentication, item management, and SQLAlchemy integration.

![FastAPI Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

## Features

- ✅ **User Authentication**: JWT token-based auth (optional)
- 📦 **Item Management**: CRUD operations for items
- 🗃️ **Database**: SQLAlchemy with SQLite (easy to switch to PostgreSQL/MySQL)
- 📚 **Auto-generated Docs**: Swagger UI & ReDoc
- 🧪 **Testing Ready**: Includes test structure
- 🌐 **CORS Enabled**: Ready for frontend integration

## Prerequisites

- Python 3.7+
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-project.git
   cd fastapi-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

| Endpoint          | Method | Description                | Requires Auth |
|-------------------|--------|----------------------------|---------------|
| `/`               | GET    | Welcome message            | No            |
| `/users/`         | POST   | Create new user            | No            |
| `/users/`         | GET    | List all users             | Yes           |
| `/users/{user_id}`| GET    | Get user details           | Yes           |
| `/items/`         | POST   | Create new item            | Yes           |
| `/items/`         | GET    | List all items             | No            |
| `/token`          | POST   | Get JWT token (if enabled) | No            |

## Database Setup

The project uses SQLite by default. To reset the database:
1. Delete `sql_app.db`
2. Restart the server - it will recreate the database automatically

## Testing

Run tests with:
```bash
pytest app/tests/
```

## Deployment

### Option 1: Docker
1. Build the image:
   ```bash
   docker build -t fastapi-app .
   ```
2. Run the container:
   ```bash
   docker run -d -p 8000:8000 fastapi-app
   ```

### Option 2: Deta.sh (Free)
```bash
pip install deta
deta new
deta deploy
```

## Project Structure

```
fastapi-project/
├── app/
│   ├── __init__.py
│   ├── main.py          # Main application
│   ├── database.py      # DB configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic models
│   ├── crud.py          # Database operations
│   ├── auth.py          # Auth utilities (optional)
│   ├── routers/         # API endpoints
│   └── tests/           # Test files
├── requirements.txt
└── README.md
```

## Environment Variables

Create a `.env` file for sensitive configuration:
```ini
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./sql_app.db
```

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

Would you like me to:
1. Add a specific section about your project's unique features?
2. Include more detailed deployment instructions for a particular platform (AWS, GCP, etc.)?
3. Add screenshots of the API documentation?
4. Include example API requests/responses in more detail?
