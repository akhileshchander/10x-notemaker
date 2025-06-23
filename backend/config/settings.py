from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # API Configuration
    api_title: str = "iOS App Backend"
    api_version: str = "1.0.0"
    api_description: str = "Backend API for iOS App with data processing capabilities"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    
    # CORS Configuration
    allowed_origins: List[str] = ["*"]
    allowed_methods: List[str] = ["*"]
    allowed_headers: List[str] = ["*"]
    
    # Database Configuration (for future use)
    database_url: str = "sqlite:///./app.db"
    
    # Processing Configuration
    max_processing_time: int = 300  # 5 minutes
    default_processing_delay: int = 5  # 5 seconds
    
    # Logging Configuration
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Create global settings instance
settings = Settings()
