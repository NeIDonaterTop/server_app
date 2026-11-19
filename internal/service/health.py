from internal.config.config import config

class HealthService:
    def get_health_status(self) -> dict:
        # Слой бизнес-логики: формируем ответ о здоровье сервиса
        return {
            "status": "pass",
            "app_name": config.app_name,
            "version": config.version,
            "environment": config.app_env
        }

health_service = HealthService()
