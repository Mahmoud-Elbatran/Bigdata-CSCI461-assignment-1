# * `FROM` keyword indicates that you are specifying the base image.
# * `ubuntu` is the name of the base image you're using.
# * `:latest` is a tag that refers to the latest version of the Ubuntu image available on Docker Hub. This ensures that you're using the most recent version of Ubuntu for your container.
# Specify the base image as Ubuntu
FROM ubuntu:latest


# * `apt-get update` ensures that the package lists for Ubuntu are updated to the latest version.
# * `apt-get install -y python3 python3-pip` installs Python3 and pip3 package manager for Python3.
# * `pip3 install pandas numpy seaborn matplotlib scikit-learn scipy` installs the specified Python packages using pip3.
# Each package is installed in a single `pip3 install` command to minimize the number of layers created in the Docker image, which helps keep the image size smaller.
# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas numpy seaborn matplotlib scikit-learn scipy



# `mkdir -p /home/doc-bd-a1/` is the command that creates a directory named `doc-bd-a1` inside the `/home/` directory of the container. 
#  The `-p` flag is used to create parent directories as needed, ensuring that the command does not fail if the `/home/` directory does not exist.
# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/    


# this code will copy the `disney_movies.csv` file from local directory into the `/home/doc-bd-a1/` directory inside the container.
# Move the dataset file to the container
COPY disney_movies.csv /home/doc-bd-a1/


# the `CMD` instruction is used to specify the command that should be executed when a container starts.
# * `CMD ["/bin/bash"]` specifies that when the container starts, it should execute the command `/bin/bash` is the location of the Bash shell interpreter on most Linux-based systems., which opens a bash shell.
# Include this line at the end of your Dockerfile. This way, when you run your container, it will start the bash shell, allowing you to interact with the container's command line.
# Open bash shell upon container startup
CMD ["/bin/bash"]

