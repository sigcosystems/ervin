from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database - OBLIGATORIO para PostgreSQL
    DATABASE_URL: str  # Sin valor por defecto, debe venir de Railway
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # APIs Externas
    RENIEC_API_URL: str = "https://api.apis.net.pe/v2/reniec/dni"
    RENIEC_API_TOKEN: str = "token-desarrollo"
    
    # Firebase
    FIREBASE_CREDENTIALS_PATH: Optional[str] = None
    
    # Pasarelas de Pago
    CULQI_PUBLIC_KEY: Optional[str] = None
    CULQI_SECRET_KEY: Optional[str] = None
    TUNKI_API_KEY: Optional[str] = None
    
    # Google Maps
    GOOGLE_MAPS_API_KEY: Optional[str] = None
    
    # Environment
    ENVIRONMENT: str = "production"
    DEBUG: bool = False
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    
    # URLs
    FRONTEND_URL: str = "https://tu-subdominio.up.railway.app"
    BACKEND_URL: str = "https://tu-subdominio.up.railway.app/api"
    
    # Comisiones
    COMISION_CAMBIO_ACEITE: float = 50.0
    COMISION_ELECTRICIDAD: float = 80.0
    COMISION_GASFITERIA: float = 70.0
    COMISION_ELECTRODOMESTICOS: float = 90.0
    
    # Timeouts
    TIMEOUT_BUSQUEDA_TECNICO: int = 120
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()