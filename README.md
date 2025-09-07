# minimal-intercontainer-communication

This example demonstrates two minimal Python services running in separate Docker containers that communicate over `localhost`.

## Usage

1. Build and start both services:
   ```bash
   docker compose up --build
   ```
2. In another terminal, call Service B which in turn calls Service A:
   ```bash
   curl http://localhost:5002/call
   ```
   You should see a JSON response containing Service A's message.

Service A is also directly accessible at `http://localhost:5001/ping`.

## Testing

1. Install dependencies and run syntax checks:
   ```bash
   pip install -r service_a/requirements.txt -r service_b/requirements.txt pytest
   python -m py_compile service_a/app.py service_b/app.py
   ```
2. Run unit tests:
   ```bash
   pytest
   ```
