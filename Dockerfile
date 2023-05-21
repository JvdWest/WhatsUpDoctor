# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /whatsupdoctor

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code to the container
COPY . .

# Moving this to run command
#RUN python manage.py migrate
#RUN python manage.py load_seed_data

# Expose the port on which your Django app will run (change it as per your app's configuration)
EXPOSE 8000

# Run the Django development server
CMD  ["python", "manage.py", "runserver", "0.0.0.0:8000"]