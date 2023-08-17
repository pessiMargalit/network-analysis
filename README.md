# Network Mapping Application
This application helps map and visualize the networks and devices deployed on clients' premises. It can be used to identify faulty devices, create clarity about the different devices and networks, and ensure efficient service.

This is a web application that the network analysis visualizes graph data. The application is built on a stack of technologies, including:

 - Python server implemented with FastAPI
 - SQL database
 - External APIs
 - React front end

The application allows users to visualize and manipulate graph data. 

Users can:
 - Load graph data from a variety of sources, including local files, databases, and external APIs.
 - Explore the graph data by viewing nodes and edges.
 - Filter the graph data by node or edge properties.
 - Apply graph algorithms to the graph data.
 - Export the graph data to a variety of formats.
 - The application is designed to be easy to use and extensible. The source code is available on GitHub.

# Getting Started
To get started with the application, you will need to:

# Install the dependencies.
Run the server.
Open the web application in a browser.
Installing the dependencies
The dependencies can be installed using the following command:

pip install -r requirements.txt


### Running the server

The server can be run using the following command:

uvicorn app.main:app --reload


This will start the server on port 8000.

### Opening the web application

The web application can be opened in a browser by visiting the following URL:

http://localhost:8000

# Features
The project has the following features:

 - Ability to load network capture files.
 - Ability to describe the network using a graph.
 - Ability to provide network analysis, such as the number of nodes, the number of links, the strength of the links between nodes, and so on.

# Contributing
Contributions to the application are welcome. Please open an issue on GitHub if you would like to contribute.
