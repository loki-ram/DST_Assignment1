# IMDB Movie Review Analysis with PySpark

This project uses Apache Spark and PySpark to analyze the [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews). The script downloads the dataset, cleans the reviews, calculates positive and negative sentiment counts, adds a review-length column, and exports the transformed data to CSV.

## Requirements

- Python 3.10 or newer
- Java 8, 11, or 17
- Internet access for downloading the Kaggle dataset
- A Kaggle account or the Kaggle credentials required by `kagglehub`

Python dependencies are listed in `requirements.txt`.

## Setup

From the project directory:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Configure Kaggle authentication before running the script if `kagglehub` requests it.

## Run

```powershell
python imdb.py
```

The script prints the Spark schema and sample rows, cleaned record count, sentiment totals, transformed review rows, and the number of reviews longer than 500 characters.

## Output

The resulting data is saved to [cleaned_imdb_reviews.csv](./cleaned_imdb_reviews.csv) with these columns:

- `review`: The original movie review text.
- `sentiment`: `positive` or `negative`.
- `review_length`: Number of characters in the review.

## Project Structure

- `imdb.py`: Downloads the dataset and performs the PySpark processing.
- `cleaned_imdb_reviews.csv`: Generated cleaned and transformed dataset.
- `requirements.txt`: Python package dependencies.
- `Assignment_1.pdf`: Assignment 
- `README.md`: Project setup and usage instructions.

## AI Assistance

AI was used to help generate code suggestions for this assignment. I reviewed the suggestions, understood the Spark operations and data transformations, and then typed the code while working through the assignment.