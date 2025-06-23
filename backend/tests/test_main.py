import pytest
from fastapi.testclient import TestClient
from uuid import uuid4
import json

from src.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "iOS App Backend API"
    assert data["version"] == "1.0.0"

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "total_items" in data

def test_get_all_data():
    """Test getting all data items"""
    response = client.get("/api/data")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 3  # Should have at least the sample data

def test_create_data_item():
    """Test creating a new data item"""
    new_item = {
        "title": "Test Item",
        "description": "This is a test item"
    }
    
    response = client.post("/api/data", json=new_item)
    assert response.status_code == 200
    data = response.json()
    
    assert data["title"] == new_item["title"]
    assert data["description"] == new_item["description"]
    assert data["status"] == "pending"
    assert data["isProcessing"] == False
    assert "id" in data
    assert "timestamp" in data

def test_get_specific_data_item():
    """Test getting a specific data item"""
    # First create an item
    new_item = {
        "title": "Specific Test Item",
        "description": "This is for testing specific retrieval"
    }
    
    create_response = client.post("/api/data", json=new_item)
    created_item = create_response.json()
    item_id = created_item["id"]
    
    # Now get the specific item
    response = client.get(f"/api/data/{item_id}")
    assert response.status_code == 200
    data = response.json()
    
    assert data["id"] == item_id
    assert data["title"] == new_item["title"]
    assert data["description"] == new_item["description"]

def test_get_nonexistent_data_item():
    """Test getting a non-existent data item"""
    fake_id = str(uuid4())
    response = client.get(f"/api/data/{fake_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_process_data_item():
    """Test processing a data item"""
    # First create an item
    new_item = {
        "title": "Item to Process",
        "description": "This item will be processed"
    }
    
    create_response = client.post("/api/data", json=new_item)
    created_item = create_response.json()
    item_id = created_item["id"]
    
    # Now process the item
    response = client.post(f"/api/data/{item_id}/process")
    assert response.status_code == 200
    data = response.json()
    
    assert data["id"] == item_id
    assert data["status"] == "processing"
    assert data["isProcessing"] == True

def test_process_nonexistent_item():
    """Test processing a non-existent item"""
    fake_id = str(uuid4())
    response = client.post(f"/api/data/{fake_id}/process")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_delete_data_item():
    """Test deleting a data item"""
    # First create an item
    new_item = {
        "title": "Item to Delete",
        "description": "This item will be deleted"
    }
    
    create_response = client.post("/api/data", json=new_item)
    created_item = create_response.json()
    item_id = created_item["id"]
    
    # Now delete the item
    response = client.delete(f"/api/data/{item_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted successfully"
    
    # Verify item is deleted
    get_response = client.get(f"/api/data/{item_id}")
    assert get_response.status_code == 404

def test_delete_nonexistent_item():
    """Test deleting a non-existent item"""
    fake_id = str(uuid4())
    response = client.delete(f"/api/data/{fake_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_create_item_validation():
    """Test data validation when creating items"""
    # Test missing title
    invalid_item = {
        "description": "Missing title"
    }
    
    response = client.post("/api/data", json=invalid_item)
    assert response.status_code == 422
    
    # Test missing description
    invalid_item = {
        "title": "Missing description"
    }
    
    response = client.post("/api/data", json=invalid_item)
    assert response.status_code == 422

def test_process_already_processing_item():
    """Test processing an item that's already being processed"""
    # First create an item
    new_item = {
        "title": "Already Processing Item",
        "description": "This item is already being processed"
    }
    
    create_response = client.post("/api/data", json=new_item)
    created_item = create_response.json()
    item_id = created_item["id"]
    
    # Process the item once
    client.post(f"/api/data/{item_id}/process")
    
    # Try to process again
    response = client.post(f"/api/data/{item_id}/process")
    assert response.status_code == 400
    assert response.json()["detail"] == "Item is already being processed"

@pytest.fixture(autouse=True)
def reset_data_store():
    """Reset the data store before each test"""
    # This is a simple approach for testing
    # In a real application, you'd use a test database
    yield
