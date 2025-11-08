from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine
from app.models import cliente, tecnico, servicio, proveedor

# Importar Base de los modelos si usas create_all
# from app.core.database import Base
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ServiPlus API",
    description="Plataforma de servicios técnicos a domicilio",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción: especificar dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates Jinja2
templates = Jinja2Templates(directory="app/templates")

# Importar routers
from app.routes import clientes, tecnicos, servicios, proveedores, admin, auth, pages

# Incluir routers de API
app.include_router(auth.router, prefix="/api/auth", tags=["Autenticación"])
app.include_router(clientes.router, prefix="/api/clientes", tags=["Clientes"])
app.include_router(tecnicos.router, prefix="/api/tecnicos", tags=["Técnicos"])
app.include_router(servicios.router, prefix="/api/servicios", tags=["Servicios"])
app.include_router(proveedores.router, prefix="/api/proveedores", tags=["Proveedores"])
app.include_router(admin.router, prefix="/api/admin", tags=["Administración"])

# Incluir router de páginas (HTML)
app.include_router(pages.router, tags=["Páginas"])

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("cliente/home_cliente.html", {"request": request})

@app.get("/api")
async def api_root():
    return {
        "app": "ServiPlus API",
        "version": "1.0.0",
        "status": "online",
        "docs": "/api/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "environment": settings.ENVIRONMENT}
