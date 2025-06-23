# iOS App Project

A complete iOS application with SwiftUI frontend and Python FastAPI backend, featuring data processing capabilities and real-time status updates.

## Project Structure

```
ios-app-project/
├── ios-app/                    # iOS SwiftUI Application
│   ├── Sources/
│   │   ├── App/               # App entry point
│   │   ├── Views/             # SwiftUI Views
│   │   ├── Models/            # Data Models
│   │   ├── Services/          # API Services
│   │   └── Utils/             # Utilities and Extensions
│   ├── Resources/             # App Resources
│   ├── Tests/                 # Unit Tests
│   └── Package.swift          # Swift Package Manager
├── backend/                   # Python FastAPI Backend
│   ├── src/                   # Source Code
│   ├── config/                # Configuration
│   ├── tests/                 # Backend Tests
│   └── requirements.txt       # Python Dependencies
└── docs/                      # Documentation
```

## Features

### iOS App (SwiftUI)

- **Modern SwiftUI Interface**: Clean, responsive design following iOS design guidelines
- **Real-time Data Updates**: Pull-to-refresh and automatic data synchronization
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Loading States**: Progress indicators and loading animations
- **Status Tracking**: Visual status indicators for data processing states
- **Async/Await**: Modern Swift concurrency for network operations

### Backend API (FastAPI)

- **RESTful API**: Clean REST endpoints for data operations
- **Background Processing**: Asynchronous task processing simulation
- **CORS Support**: Cross-origin resource sharing for iOS app
- **Data Validation**: Pydantic models for request/response validation
- **Health Checks**: API health monitoring endpoints
- **Auto Documentation**: Swagger/OpenAPI documentation

## Getting Started

### Prerequisites

#### For iOS Development:

- macOS with Xcode 15.0 or later
- iOS 16.0+ target device or simulator
- Swift 5.9+

#### For Backend Development:

- Python 3.8+
- pip (Python package manager)

### Backend Setup

1. **Navigate to backend directory:**

   ```bash
   cd ios-app-project/backend
   ```

2. **Create virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**

   ```bash
   python src/main.py
   ```

   The API will be available at `http://localhost:8000`

   API Documentation: `http://localhost:8000/docs`

### iOS App Setup

1. **Open the iOS project:**

   ```bash
   cd ios-app-project/ios-app
   open Package.swift
   ```

2. **Build and run:**
   - Open the project in Xcode
   - Select your target device or simulator
   - Press `Cmd+R` to build and run

## API Endpoints

### Data Operations

- `GET /api/data` - Retrieve all data items
- `POST /api/data` - Create a new data item
- `GET /api/data/{id}` - Get specific data item
- `POST /api/data/{id}/process` - Start processing a data item
- `DELETE /api/data/{id}` - Delete a data item

### System

- `GET /` - API root information
- `GET /api/health` - Health check endpoint

## Data Models

### DataItem

```swift
struct DataItem {
    let id: UUID
    let title: String
    let description: String
    let timestamp: Date?
    let status: ProcessingStatus
    let isProcessing: Bool
}
```

### Processing Status

- `pending` - Item is waiting to be processed
- `processing` - Item is currently being processed
- `completed` - Processing completed successfully
- `failed` - Processing failed

## Architecture

### iOS App Architecture

- **MVVM Pattern**: Model-View-ViewModel architecture
- **SwiftUI**: Declarative UI framework
- **Combine**: Reactive programming for data binding
- **URLSession**: Native networking
- **Environment Objects**: Dependency injection

### Backend Architecture

- **FastAPI**: Modern Python web framework
- **Pydantic**: Data validation and serialization
- **Async/Await**: Asynchronous request handling
- **Background Tasks**: Non-blocking processing
- **CORS Middleware**: Cross-origin support

## Development

### Running Tests

#### Backend Tests:

```bash
cd backend
python -m pytest tests/
```

#### iOS Tests:

- Open project in Xcode
- Press `Cmd+U` to run tests

### Code Style

#### Swift:

- Follow Swift API Design Guidelines
- Use SwiftLint for code formatting
- Prefer value types over reference types
- Use async/await for asynchronous operations

#### Python:

- Follow PEP 8 style guide
- Use type hints
- Document functions with docstrings
- Use async/await for I/O operations

## Deployment

### Backend Deployment

The FastAPI backend can be deployed to various platforms:

#### Docker:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Cloud Platforms:

- **Heroku**: Use `Procfile` with `web: uvicorn src.main:app --host 0.0.0.0 --port $PORT`
- **AWS Lambda**: Use Mangum adapter
- **Google Cloud Run**: Use Docker container
- **Azure Container Instances**: Use Docker container

### iOS App Deployment

- Build for release in Xcode
- Archive and upload to App Store Connect
- Follow Apple's App Store Review Guidelines

## Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
API_TITLE=iOS App Backend
API_VERSION=1.0.0
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO
```

### iOS Configuration

Update the API base URL in `APIService.swift`:

```swift
private let baseURL = "https://your-api-domain.com/api"
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:

- Create an issue in the repository
- Check the API documentation at `/docs`
- Review the code comments and documentation

## Roadmap

- [ ] Database integration (PostgreSQL/SQLite)
- [ ] User authentication and authorization
- [ ] Push notifications
- [ ] Real-time WebSocket updates
- [ ] File upload/download capabilities
- [ ] Advanced data processing algorithms
- [ ] Offline data synchronization
- [ ] Unit and integration tests
- [ ] CI/CD pipeline setup
- [ ] Performance monitoring and analytics
