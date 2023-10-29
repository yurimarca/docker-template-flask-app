# Use an official miniconda3 as a parent image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create the conda environment using the environment.yml file
# Make sure to include the environment.yml file in the same directory as your Dockerfile
COPY env.yml .
RUN conda env create -f env.yml

# Make sure the environment is activated:
SHELL ["conda", "run", "-n", "my_env", "/bin/bash", "-c"]

# Add conda environment to PATH (this may not be necessary depending on your setup)
ENV PATH /opt/conda/envs/my_env/bin:$PATH

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variable for Flask to run in production mode
ENV FLASK_ENV=production

CMD ["python", "app.py"]

