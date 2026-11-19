from fastapi import APIRouter
from internal.service.health import health_service

router = APIRouter(prefix="/api/v1", tags=["Health"])

@router.get("/health")
def get_health():
    # Слой представления (HTTP): принимает запрос и вызывает сервис
    return health_service.get_health_status()
