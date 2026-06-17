# Step 1: Start with an official lightweight Python environment
FROM python:3.10-slim

# Step 2: Set the folder inside the container where our code will live
WORKDIR /app

# Step 3: Copy our calculator files from our computer into the container
COPY calculator.py test_calculator.py ./

# Step 4: Install pytest inside the container so it can run tests
RUN pip install pytest

# Step 5: Tell the container what command to run by default when it starts
CMD ["pytest", "test_calculator.py"]
