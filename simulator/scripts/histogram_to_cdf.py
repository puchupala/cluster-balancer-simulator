import logging
import csv

HISTOGRAM = "/Users/KnightBaron/duration_hist.csv"
OUTPUT = "/Users/KnightBaron/duration_cdf.csv"
# MAX_TASKS = 5442378.0
MAX_TASKS = 2.346675000000000000e+12
TOTAL_BUCKET = 10000
BUCKET_SIZE = 1

SCHEMA = ["task_count", "jobs"]

buckets = {}
for i in range(1, TOTAL_BUCKET + 1):
    buckets[(MAX_TASKS / TOTAL_BUCKET) * i] = 0
# for i in range(1, TOTAL_BUCKET + 1):
#     buckets[BUCKET_SIZE * i] = 0

with open(HISTOGRAM) as csvfile:
    histogram_csv = csv.DictReader(csvfile, SCHEMA)
    for entry in histogram_csv:
        task_count = float(entry["task_count"])
        jobs = float(entry["jobs"])
        for key in buckets:
            if task_count <= key:
                buckets[key] += jobs

with open(OUTPUT, "w") as csvfile:
    output = csv.DictWriter(csvfile, SCHEMA)
    for key in buckets:
        output.writerow({
            "task_count": key,
            "jobs": buckets[key],
        })
