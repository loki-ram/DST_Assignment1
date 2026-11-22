# Downloading the dataset
import csv
import kagglehub

path = kagglehub.dataset_download(
    "lakshmi25npathi/imdb-dataset-of-50k-movie-reviews"
)

print("Path to dataset files:", path)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, length

# creating spark session
spark = SparkSession.builder \
    .appName("IMDB Movie Analysis") \
    .getOrCreate()

print("Spark session created!")

# loading dataset
df = spark.read.csv ( path + "/IMDB Dataset.csv",
                        header=True, inferSchema=True)

print("\nDataset Loaded")
print("Total Records: ", df.count())

# schema and 5 rows
print("\nSchema")
df.printSchema()

print("\nFirst 5 rows")
df.show(5, truncate=False)

# cleaning data
df_clean = df.filter(
            col("review").isNotNull() &
            (trim(col("review"))!="")
)

print("\nTotal reviews after cleaning: ", df_clean.count())

# countint positive and negative reviews
print("\nSentiment counts")
sentiment_counts = df_clean.groupBy("sentiment").count()
sentiment_counts.show()

# individual counts
pos_count = df_clean.filter( 
            col("sentiment")=="positive"
).count()

neg_count = df_clean.filter( 
            col("sentiment")=="negative"
).count()

print("Positive reviews: ", pos_count)
print("Negative reviews: ", neg_count)

# create a col containing review length
df_transformed = df_clean.withColumn(
        "review_length", length(col("review"))
)

print("\nData with review length")
df_transformed.show(5, truncate=False)

# filter reviews longer than 500 chars
long_reviews = df_transformed.filter(
        col("review_length") > 500
)

print("\nNumber of reviews longer than 500 characters: ", long_reviews.count())

# save the new csv without requiring Hadoop winutils on Windows
output_path = "cleaned_imdb_reviews.csv"
with open(output_path, "w", newline="", encoding="utf-8") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=df_transformed.columns)
    writer.writeheader()
    for row in df_transformed.toLocalIterator():
        writer.writerow(row.asDict())

print("\nCleaned and transformed data saved to: ", output_path)

# stop spark session
spark.stop()
print("\nSpark session stopped successfully")