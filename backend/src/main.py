from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
import asyncio
import uvicorn

app = FastAPI(title="iOS App Backend", version="1.0.0")

# Enable CORS for iOS app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your iOS app's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class ProcessingStatus:
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class DataItem(BaseModel):
    id: UUID
    title: str
    description: str
    timestamp: Optional[datetime] = None
    status: str = ProcessingStatus.PENDING
    isProcessing: bool = False

class DataItemCreate(BaseModel):
    title: str
    description: str

# In-memory storage (use a database in production)
data_store: List[DataItem] = [
    DataItem(
        id=uuid4(),
        title="Sample Task 1",
        description="This is a sample task that demonstrates the app functionality",
        timestamp=datetime.now(),
        status=ProcessingStatus.COMPLETED
    ),
    DataItem(
        id=uuid4(),
        title="Processing Task",
        description="This task is currently being processed by the backend",
        timestamp=datetime.now(),
        status=ProcessingStatus.PROCESSING,
        isProcessing=True
    ),
    DataItem(
        id=uuid4(),
        title="Pending Task",
        description="This task is waiting to be processed",
        timestamp=datetime.now(),
        status=ProcessingStatus.PENDING
    )
]

# Background processing simulation
async def process_data_item(item_id: UUID):
    """Simulate background processing of a data item"""
    # Find the item
    item = next((item for item in data_store if item.id == item_id), None)
    if not item:
        return
    
    # Update status to processing
    item.status = ProcessingStatus.PROCESSING
    item.isProcessing = True
    
    # Simulate processing time
    await asyncio.sleep(5)  # 5 seconds processing time
    
    # Complete processing
    item.status = ProcessingStatus.COMPLETED
    item.isProcessing = False
    item.timestamp = datetime.now()

# API Endpoints
@app.get("/")
async def root():
    return {"message": "iOS App Backend API", "version": "1.0.0"}

@app.get("/api/data", response_model=List[DataItem])
async def get_data():
    """Get all data items"""
    return data_store

@app.post("/api/data", response_model=DataItem)
async def create_data(item: DataItemCreate):
    """Create a new data item"""
    new_item = DataItem(
        id=uuid4(),
        title=item.title,
        description=item.description,
        timestamp=datetime.now(),
        status=ProcessingStatus.PENDING
    )
    data_store.append(new_item)
    return new_item

@app.get("/api/data/{item_id}", response_model=DataItem)
async def get_data_item(item_id: UUID):
    """Get a specific data item by ID"""
    item = next((item for item in data_store if item.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/api/data/{item_id}/process", response_model=DataItem)
async def process_item(item_id: UUID, background_tasks: BackgroundTasks):
    """Start processing a data item"""
    item = next((item for item in data_store if item.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if item.status == ProcessingStatus.PROCESSING:
        raise HTTPException(status_code=400, detail="Item is already being processed")
    
    if item.status == ProcessingStatus.COMPLETED:
        raise HTTPException(status_code=400, detail="Item is already completed")
    
    # Start background processing
    background_tasks.add_task(process_data_item, item_id)
    
    # Update status immediately
    item.status = ProcessingStatus.PROCESSING
    item.isProcessing = True
    
    return item

@app.delete("/api/data/{item_id}")
async def delete_data_item(item_id: UUID):
    """Delete a data item"""
    global data_store
    item = next((item for item in data_store if item.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    data_store = [item for item in data_store if item.id != item_id]
    return {"message": "Item deleted successfully"}

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "total_items": len(data_store)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
