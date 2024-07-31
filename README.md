# Scam Detection Web Application

This is a Flask-based web application designed to detect scam text messages. It uses machine learning models to classify texts as scam or real. The application leverages advanced Natural Language Processing (NLP) techniques and machine learning algorithms to analyse and determine the nature of the text content. The models are trained on a variety of datasets containing examples of legitimate and fraudulent messages from [Mendeley Data](https://data.mendeley.com/datasets/f45bkkt8pr/1), ensuring high accuracy in detection. The web interface is built with user-friendliness in mind, providing a straightforward way for users to input text or upload files for scam detection.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)

## Features

1. **Detect Fake and Real Messages Using Algorithms**: The application classifies text messages as legitimate or fraudulent using trained machine learning models, including an ensemble of Logistic Regression, SVM, and Random Forest through soft voting.

2. **Gathering and Preprocessing of Dataset**: The application utilised datasets containing various types of messages. These datasets were cleaned and pre-processed to prepare them for model training.

3. **Text Preprocessing**: Preprocessing steps included cleaning the text to remove special characters, tokenising the text, removing stopwords, and stemming.

4. **Training of Algorithms**: Logistic Regression, SVM, and Random Forest were trained. Ensemble methods like hard voting and soft voting were used to improve performance.

5. **Algorithm Accuracy in Detecting Scam or Real Text**: The models were evaluated for accuracy, precision, recall, and F1-score. The soft voting classifier was selected based on its balanced scores.

6. **Ensemble Learning Techniques**: The application utilised both hard voting and soft voting ensemble methods to combine predictions from multiple models, thereby improving the overall classification accuracy.

7. **Web Application Integration**: The Flask web application allows users to input text or upload files (PDF or TXT) for scam detection. The trained soft voting classifier predicts and displays the result on the web interface.

## Installation

### Prerequisites
- Python 3.11
- pip (Python package installer)

### Setup
1. **Clone the repository:**
    ```sh
    git clone https://github.com/AWXCiioa/ScamDetection.git
    cd ScamDetection
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv myenv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source myenv/bin/activate
        ```

4. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Ensure you have the following files in your project directory:**
    - `Notebooks/soft_voting_classifier.pkl`
    - `Notebooks/tfidf_vectorizer.pkl`
    - Your dataset file (e.g., `Dataset_5971.csv`)

## Usage

1. **Start the Flask application:**
    ```sh
    python app.py
    ```

2. **Open your web browser and go to:**
    ```
    http://127.0.0.1:5000
    ```

3. **Use the application:**
    - Navigate to the homepage to enter text or upload files for scam detection.
    - Change themes using the theme selector.
    - View results for the input text.



## Running Tests

### Unit Tests

Run unit tests using pytest:
```sh
pytest tests/test_unit.py -v
```
## Blackbox Tests

Run blackbox tests using pytest:
```sh
pytest tests/test_blackbox.py -v
```
