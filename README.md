# Real-Time Multilingual Voice AI Agent

## Run Backend
uvicorn backend.main:app --reload

## Run WebSocket
uvicorn backend.websocket_server:app --reload --port 8001

## Run Docker
docker-compose up --build
