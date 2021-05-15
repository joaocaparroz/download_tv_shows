# Download TV Shows

**A Python open-source project to download TV shows episodes**

## Installation

This project runs on Python 3.9 needs `pipenv` to resolve its dependencies. To
install `pipenv`, install Python 3.9 and run `pip install pipenv`. After that,
navigate to the project home folder and run `pipenv install`. This should
resolve all dependencies and install the appropriate packages. <sup id="a1">[1](#f1)</sup>

## .env file

Create a .env file with this format:
```
TRANSMISSION_ADDRESS=http://localhost:9091/transmission/rpc    (your Transmission RPC address)
TRANSMISSION_USERNAME=username                                 (your Transmission username)
TRANSMISSION_PASSWORD=password                                 (your Transmission password)
DOWNLOAD_DIR=/home/username/Downloads                          (your downloads folder)
```

## joblib file

Inside `data` folder, there is a joblib file. To create it, edit `create_joblib.py` with your TV shows and run it.

## Running the script

Just run `main.py` inside the virtual env (`pipenv run python main.py`)

<sup><b id="f1">1</b></sup>: You will need Transmission installed and RPC configured.