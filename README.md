# Grazioso-Salvare-Dashboard

## Overview

This is a dashboard and data visualization project created for Grazioso Salvare, an international rescue-animal training company. The dashboard allows stakeholders to access data from animal shelters in the Austin, TX metro area and filter the data by relevant criteria for different rescue types. This a full-stack project that was created using Python, MongoDB, and the Dash framework.

## Design Specifications

This dashboard and its supporting CRUD module follow an MVC design pattern and were developed with Jupyter Notebooks in a Linux environment. The project requires an installation of Python3, MongoDB, PyMongo, JupyterLab, and Dash libraries (Dash, Plotly Express, and Dash Leaflet). The model component of the project uses PyMongo as the MongoDB driver for Python, as it provides functionality for interacting with MongoDB from Python. The view and controller components of the project use the Dash framework, as it provides an interface that is compatible with the existing MongoDB back-end and supports interactive data visualization components for the client.

## Getting Started

This dashboard uses a database from the Austin Animal Center and includes user authentication with admin and user (read/write only) roles. The project was developed in a virtual Linux environment where its functionality was tested in Jupyter Notebook. Initially, there was an authentication issue where the dashboard has trouble connecting to the AAC database. Should this problem arise, it may be resolved by refactoring the supporting CRUD module's instantiation of the MongoClient. To get a local copy up and running, complete the following three steps:

1. Clone the repository to your machine
2. Install the necessary dependencies (Python3, MongoDB, PyMongo, and Dash libraries)
3. In Jupyter Notebook, open 'ProjectTwoDashboard.ipynb' and run all the cells

## Usage

The dashboard's starting state shows the unfiltered Austin Animal Center dataset in a data table alongside a pie chart and a geolocation map. The user may change the pagination of the data table or filter the dataset by criteria relevant to different rescue types, namely water rescue, mountain/wilderness rescue, and disaster rescue/individual tracking. The data visualization charts are responsive and update to reflect the user's selection.

### Screenshots

Starting state

![Picture1](https://user-images.githubusercontent.com/89939389/220008982-078d4749-a5d9-4773-9632-7370f091d260.png)

Water rescue

![Picture2](https://user-images.githubusercontent.com/89939389/220009117-fd3b66f9-cd94-4021-bd0e-c431e24ce996.png)

Mountain/wilderness rescue

![Picture3](https://user-images.githubusercontent.com/89939389/220009120-7e167b87-2be3-4f7d-a016-cc8f0864d8f4.png)

Disaster rescue/individual tracking

![Picture4](https://user-images.githubusercontent.com/89939389/220009124-c19d6e03-0306-4723-ab5a-10ea1e5d2ee3.png)

## Roadmap

- Enhanced support for authentication and security
- Support for more advanced sorting options (e.g., search by name, sort by outcome type, apply multiple filters)

**Authors and Acknowledgment**

This dashboard was created by J.P. Haynes and implements the requirements from Grazioso Salvare's specifications documentation. The data for this dashboard was provided by the Austin Animal Center (2020). _Austin Animal Center Outcomes_ [Data set]. City of Austin, Texas Open Data Portal. [https://doi.org/10.26000/025.000001](https://doi.org/10.26000/025.000001)
