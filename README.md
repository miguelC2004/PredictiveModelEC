# PredictiveModelEC

Predictive Model for Sales Data using Python, MySQL, and Polars, adhering to Edgeclear Core API Style Guide.

## Introduction

This repository contains a predictive model for sales data. The model is built using Python, MySQL, and Polars, and it strictly follows the Edgeclear Core API Style Guide for code organization, naming conventions, and best practices.

## Project Structure

The project is organized into multiple Python files to ensure modularity and readability:

- `DbConnection.py` - Manages database connection.
- `DataExtraction.py` - Handles data extraction from the MySQL database.
- `DataProcessing.py` - Processes the extracted data.
- `PredictiveModel.py` - Builds, trains, and evaluates the predictive model.
- `Main.py` - Main entry point to run the predictive model workflow.

## Requirements

- Python 3.x
- MySQL server
- Required Python packages:
  - mysql-connector-python
  - polars
  - scikit-learn

## Setup Instructions

### Install Dependencies

Run the following command to install the required Python packages:

```bash
pip install mysql-connector-python polars scikit-learn
