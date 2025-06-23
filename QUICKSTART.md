# Quick Start Guide

This guide will help you get the iOS App Project up and running quickly.

## Prerequisites

- **macOS** with Xcode 15.0+
- **Python 3.8+**
- **iOS 16.0+** target device or simulator

## Backend Setup (5 minutes)

1. **Navigate to backend directory:**

   ```bash
   cd ios-app-project/backend
   ```

2. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server:**

   ```bash
   python start.py
   ```

   ✅ **Backend is now running at:** `http://localhost:8000`

   📚 **API Documentation:** `http://localhost:8000/docs`

## iOS App Setup (2 minutes)

1. **Open the iOS project:**

   ```bash
   cd ios-app-project/ios-app
   open Package.swift
   ```

2. **In Xcode:**

   - Wait for dependencies to resolve
   - Select your target device/simulator
   - Press `Cmd+R` to build and run

   ✅ **iOS App is now running!**

## Testing the Connection

1. **Backend Health Check:**

   ```bash
   curl http://localhost:8000/api/health
   ```

2. **In the iOS App:**
   - Pull down to refresh the list
   - You should see sample data loaded from the backend
   - Tap items to see their status

## What You'll See

### iOS App Features:

- ✅ List of data items with status indicators
- ✅ Pull-to-refresh functionality
- ✅ Loading states and error handling
- ✅ Real-time status updates

### Backend Features:

- ✅ RESTful API endpoints
- ✅ Background processing simulation
- ✅ Auto-generated API documentation
- ✅ CORS support for iOS app

## API Endpoints

| Method | Endpoint                 | Description       |
| ------ | ------------------------ | ----------------- |
| GET    | `/api/data`              | Get all items     |
| POST   | `/api/data`              | Create new item   |
| GET    | `/api/data/{id}`         | Get specific item |
| POST   | `/api/data/{id}/process` | Process item      |
| DELETE | `/api/data/{id}`         | Delete item       |
| GET    | `/api/health`            | Health check      |

## Troubleshooting

### Backend Issues:

- **Port 8000 in use?** Change port in `backend/config/settings.py`
- **Import errors?** Make sure virtual environment is activated
- **Dependencies missing?** Run `pip install -r requirements.txt`

### iOS App Issues:

- **Build errors?** Clean build folder (`Cmd+Shift+K`)
- **Network errors?** Check backend is running at `localhost:8000`
- **Simulator issues?** Try different iOS simulator version

### Connection Issues:

- **iOS can't reach backend?**
  - Ensure backend is running on `0.0.0.0:8000`
  - Check iOS simulator network settings
  - Verify `NSAppTransportSecurity` in Info.plist

## Next Steps

1. **Explore the Code:**

   - iOS: Check out SwiftUI views in `ios-app/Sources/Views/`
   - Backend: Review API endpoints in `backend/src/main.py`

2. **Run Tests:**

   ```bash
   # Backend tests
   cd backend && python -m pytest tests/

   # iOS tests (in Xcode)
   Cmd+U
   ```

3. **Customize:**

   - Modify data models in both iOS and backend
   - Add new API endpoints
   - Enhance the UI with more SwiftUI components

4. **Deploy:**
   - Backend: Use Docker or cloud platforms
   - iOS: Build for device and submit to App Store

## Support

- 📖 **Full Documentation:** See `README.md`
- 🐛 **Issues:** Create GitHub issues
- 💡 **API Docs:** `http://localhost:8000/docs`

---

**🎉 You're all set! Happy coding!**
