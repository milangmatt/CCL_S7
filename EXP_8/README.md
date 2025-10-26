# Word Count using MapReduce

This project implements a **Word Count** example using **Apache Spark (PySpark)** — one of the simplest and most fundamental distributed data processing programs.

It reads a text file, converts it into an **RDD (Resilient Distributed Dataset)**, splits each line into words, and counts the occurrences of each word efficiently using Spark’s transformation and action operations.

---

## 🧠 Key Features

* Built using **PySpark**, the Python API for Apache Spark
* Demonstrates **RDD-based computation** — the core abstraction in Spark
* Efficient distributed processing on large text datasets
* Clean, readable code suitable for beginners and labs

---

## ⚙️ How to Run

### 1. Prerequisites

Ensure you have:

* Python 3 installed
* PySpark installed (`pip install pyspark`)
* A text file (e.g., `sample.txt`) in the same directory

### 2. Run the Program

```bash
python3 program.py
```


---

##  Code Explanation

### Importing PySpark Modules

```python
from pyspark import SparkConf, SparkContext
```

* `SparkConf`: Used to configure Spark (app name, master node, etc.).
* `SparkContext`: The main entry point for Spark functionality — connects your Python driver to the Spark cluster and initializes RDDs.

---

### Spark Configuration and Context Setup

```python
conf = SparkConf().setAppName("WordCountFromFile").setMaster("local[*]")
sc = SparkContext(conf=conf)
```

* `setAppName("WordCountFromFile")` → Names the Spark job.
* `setMaster("local[*]")` → Runs Spark locally using all CPU cores.
* `SparkContext(conf)` → Starts Spark’s execution environment, enabling RDD operations.

---

### Reading and Converting File into an RDD

```python
input_file = "sample.txt"
lines = sc.textFile(input_file)
```

* `sc.textFile()` **converts the input text file into an RDD**.
* Each line in the file becomes one element (record) of the RDD.
* Example:

  ```
  sample.txt:
  Hello Spark
  Spark is powerful
  → RDD = ["Hello Spark", "Spark is powerful"]
  ```

 **What is an RDD?**

RDD stands for **Resilient Distributed Dataset**, which is Spark’s core data structure.
It is:

* **Resilient** → Fault-tolerant (can recover from failures)
* **Distributed** → Data is split and processed across multiple nodes
* **Dataset** → A collection of data items

RDDs support two types of operations:

* **Transformations** → Create new RDDs (e.g., `map`, `flatMap`, `filter`)
* **Actions** → Trigger execution and return results (e.g., `collect`, `count`)

---

### Splitting Lines into Words

```python
words = lines.flatMap(lambda line: line.split())
```

* **Transformation:** `flatMap()`
* Splits each line into words and flattens all results into one list-like RDD.
* Example:

  ```
  ["Hello Spark", "Spark is powerful"]
  → ["Hello", "Spark", "Spark", "is", "powerful"]
  ```

---

### Mapping Each Word to a Pair

```python
word_pairs = words.map(lambda word: (word, 1))
```

* **Transformation:** `map()`
* Converts each word into a key-value pair `(word, 1)`.
* Example:

  ```
  ["Spark", "is", "fast"]
  → [("Spark", 1), ("is", 1), ("fast", 1)]
  ```

---

### Reducing by Key (Summing Word Counts)

```python
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)
```

* **Transformation:** `reduceByKey()`
* Combines values with the same key (word) by summing their counts.
* Example:

  ```
  [("Spark", 1), ("is", 1), ("Spark", 1)]
  → [("Spark", 2), ("is", 1)]
  ```

---

### Collecting Results

```python
results = word_counts.collect()
```

* **Action:** `collect()`
* Brings all final results from worker nodes back to the driver program.

---

### Displaying Output

```python
for word, count in results:
    print(f"{word}: {count}")
```

* Prints each word along with its count in a readable format.

---

### Stopping Spark Context

```python
sc.stop()
```

* Gracefully shuts down the Spark session.
* Always called at the end to release cluster resources.

---

##  Common PySpark RDD Functions Used

| Function        | Type           | Description                            |
| --------------- | -------------- | -------------------------------------- |
| `textFile()`    | Action         | Reads a text file into an RDD          |
| `flatMap()`     | Transformation | Splits and flattens data               |
| `map()`         | Transformation | Applies a function to each element     |
| `reduceByKey()` | Transformation | Aggregates values by key               |
| `collect()`     | Action         | Returns all RDD elements to the driver |
| `stop()`        | Action         | Stops the SparkContext                 |

---


