# Define default ports and variables
ports = 5000

# Create virtual environment and install dependencies
init:
	python3 -m venv .venv
	. .venv/bin/activate && \
	pip install -r requirements.txt

# Run the application
run:
	. .venv/bin/activate && \
	python3 app.py

# Build Docker image
build:
	docker build -t papp .

# Run tests
test:
	. .venv/bin/activate && \
	python3 test.py

# Test API endpoint
test-api:
	curl http://localhost:$(ports)

# Run Docker container with port mapping
build-image:
	docker run -d -p $(ports):5000 papp

