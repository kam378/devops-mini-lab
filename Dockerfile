FROM python:3.10-slim

WORKDIR /app

COPY calculator.py ./

# Install Flask so our web app can run
RUN pip install flask

# Expose port 5000 so we can access the web server
EXPOSE 5000

# Change the default command to start our web server instead of running tests
CMD ["python", "calculator.py"]