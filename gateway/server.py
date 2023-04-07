from fastapi import FastAPI
from gateway.controllers import (
    converter_controller,
    detector_controller,
    extractor_controller,
    general_controller,
)


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(converter_controller.router)
    app.include_router(detector_controller.router)
    app.include_router(extractor_controller.router)
    app.include_router(general_controller.router)

    return app


app = create_app()
