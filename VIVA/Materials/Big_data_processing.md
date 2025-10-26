

# Big Data Processing

- [Big Data Processing](#big-data-processing)
  - [1. Hadoop Distributed File System (HDFS)](#1-hadoop-distributed-file-system-hdfs)
    - [Architecture](#architecture)
    - [NameNode](#namenode)
    - [DataNode](#datanode)
    - [Block Storage and Replication](#block-storage-and-replication)
    - [File Operations](#file-operations)
      - [Creating, Reading, Writing, and Deleting Files](#creating-reading-writing-and-deleting-files)
      - [Anatomy of a File Read](#anatomy-of-a-file-read)
      - [Anatomy of a File Write](#anatomy-of-a-file-write)
    - [HDFS Design](#hdfs-design)
    - [Hadoop-specific File Types](#hadoop-specific-file-types)
    - [Fault Tolerance Mechanisms](#fault-tolerance-mechanisms)
  - [HBase](#hbase)
    - [Architecture](#architecture-1)
    - [Schema Design](#schema-design)
  - [2. MapReduce Programming](#2-mapreduce-programming)
    - [Fundamentals](#fundamentals)
    - [Execution Pipeline](#execution-pipeline)
    - [Runtime Coordination and Task Management](#runtime-coordination-and-task-management)
    - [Design \& Implementation](#design--implementation)
      - [Using MapReduce for Parallel Processing](#using-mapreduce-for-parallel-processing)
      - [Examples:](#examples)
  - [3. Stream Data Model](#3-stream-data-model)
    - [Concepts and Architecture](#concepts-and-architecture)
    - [Sampling Data in Streams](#sampling-data-in-streams)
    - [Filtering Streams](#filtering-streams)
    - [Counting Distinct Elements](#counting-distinct-elements)
  - [4. Hive](#4-hive)
    - [Features](#features)
    - [Data Types and File Formats](#data-types-and-file-formats)
      - [Primitive and Collection Data Types](#primitive-and-collection-data-types)
    - [HiveQL Commands](#hiveql-commands)
      - [Creating Tables](#creating-tables)
      - [Dropping Tables](#dropping-tables)
      - [Altering Tables](#altering-tables)
  - [5. Pig](#5-pig)
    - [Installation and Execution](#installation-and-execution)
    - [Pig Data Model](#pig-data-model)
    - [Pig Latin](#pig-latin)
      - [Structure](#structure)
      - [Built-in Functions](#built-in-functions)
  - [6. Spark](#6-spark)
    - [History and Architecture](#history-and-architecture)
    - [Storage Layers](#storage-layers)
    - [Core Spark Concepts](#core-spark-concepts)
    - [RDD Basics](#rdd-basics)
    - [RDD Operations](#rdd-operations)
    - [Transformations vs Actions (Important for Practical Tasks)](#transformations-vs-actions-important-for-practical-tasks)


## 1\. Hadoop Distributed File System (HDFS)

### Architecture

HDFS is a highly fault-tolerant and scalable distributed file system designed to run on commodity hardware. It works on a **Master/Slave** architecture where a single **NameNode** manages the file system metadata and multiple **DataNodes** store the actual data.

### NameNode

The **NameNode** is the centerpiece of an HDFS cluster. It acts as the master server that:

  * Maintains the file system tree and its metadata (e.g., file names, directories, permissions).
  * Manages the state of DataNodes, including block mappings (which block of a file is stored on which DataNode).
  * Regulates client access to files.

### DataNode

**DataNodes** are the slave nodes in HDFS. They are responsible for:

  * Storing and retrieving data blocks as requested by clients or the NameNode.
  * Reporting a list of blocks they are storing to the NameNode periodically via **Heartbeats** and **Block Reports**.
  * Handling block replication upon instruction from the NameNode.

### Block Storage and Replication

HDFS stores each file as a sequence of **blocks**. The default block size is typically **128 MB** or **256 MB** (much larger than traditional file systems).

  * **Replication:** For fault tolerance, each block is replicated across multiple DataNodes (the default replication factor is often **3**).
  * **Replica Placement:** HDFS uses a rack-aware replication policy to improve data availability and network bandwidth utilization by typically placing one replica on a different rack than the other two.

### File Operations

#### Creating, Reading, Writing, and Deleting Files

  * **Creating/Writing:** A client contacts the NameNode, which provides a list of DataNodes to store the blocks. The client then streams data directly to the DataNodes in a pipeline.
  * **Reading:** The client contacts the NameNode to get the block locations, then reads the blocks directly from the nearest DataNodes.
  * **Deleting:** The client asks the NameNode to delete the file. The NameNode updates its metadata and instructs the DataNodes to free the blocks asynchronously.

#### Anatomy of a File Read

1.  The client opens the file using the `FileSystem.open()` method, which calls the NameNode.
2.  The NameNode returns the addresses of the DataNodes holding the first few blocks of the file.
3.  The client connects directly to the nearest DataNode to read the block.
4.  Once the read is complete, the client requests the next block's locations from the NameNode. This process repeats until the file is fully read.

#### Anatomy of a File Write

1.  The client creates the file using `FileSystem.create()`, which contacts the NameNode.
2.  The NameNode performs checks and allocates an ordered list of DataNodes for the first block (e.g., three DataNodes for a replication factor of 3).
3.  The client begins streaming data to the first DataNode in the pipeline.
4.  The first DataNode stores the data and then simultaneously forwards it to the second DataNode, and so on. This is called a **pipeline** write.
5.  Upon successful write and replication, the DataNodes send an acknowledgment back through the pipeline, and the NameNode records the successful block replica creation. This repeats for all blocks.

### HDFS Design

HDFS is optimized for:

  * **Streaming data access** to large files.
  * **High throughput** over low-latency access.
  * **Fault tolerance** and low-cost commodity hardware.

### Hadoop-specific File Types

While HDFS is file system-agnostic, the Hadoop ecosystem commonly uses:

  * **SequenceFiles:** Flat files consisting of binary key/value pairs. They are splittable and support compression.
  * **Avro Data Files:** A row-oriented storage format that includes the schema in the file, making it self-describing.
  * **Parquet:** A columnar storage format optimized for querying large datasets with complex nested data structures.
  * **ORC (Optimized Row Columnar):** A columnar storage format highly optimized for Hive queries.

### Fault Tolerance Mechanisms

  * **Data Replication:** The primary mechanism, ensuring data is available even if a DataNode fails.
  * **Heartbeats:** DataNodes send regular heartbeats to the NameNode. If a DataNode stops sending heartbeats, the NameNode marks it as dead and initiates re-replication of its blocks.
  * **Block Checksums:** Data integrity is ensured by checking the checksum of data blocks before a read.

-----

## HBase

### Architecture

**HBase** is a non-relational, column-oriented **NoSQL** database that runs on top of HDFS. It is modeled after Google's BigTable and provides random, real-time read/write access to your Big Data.

The key components are:

  * **HMaster:** Manages the HBase cluster (like the NameNode in HDFS). It handles DDL operations (create, delete tables), assigns regions to RegionServers, and monitors all RegionServers.
  * **RegionServers:** Store the actual data and handle read/write requests for a subset of the table called a **Region**. A Region is a contiguous, sorted range of rows in an HBase table.
  * **ZooKeeper:** Used for cluster coordination, maintaining the state of the cluster, and managing RegionServer failover.
  * **HDFS:** Serves as the underlying persistent storage for the data.

### Schema Design

HBase schemas are designed differently from relational schemas:

  * **Tables, Row Keys, Column Families, and Timestamps:** Data is stored in tables, indexed by a **Row Key**. Columns are grouped into **Column Families**. Each cell can have multiple versions, indexed by a **Timestamp**.
  * **Row Key Design:** The row key is the single most critical aspect of schema design. HBase tables are sorted lexicographically by row key. Good row keys ensure **uniform distribution** of reads/writes across the cluster (preventing "hot-spotting") and are designed for efficient range scans.
  * **Column Families:** Keep the number of column families small (ideally 1 to 3). Columns within a family are stored together.

-----

## 2\. MapReduce Programming

### Fundamentals

**MapReduce** is a programming model and an associated implementation for processing and generating large datasets. It consists of two main functions:

1.  **Map:** Processes a key/value pair to generate a set of intermediate key/value pairs.
2.  **Reduce:** Processes all intermediate values associated with the same intermediate key.

### Execution Pipeline

The standard MapReduce data flow is:

1.  **Input:** Data is read from HDFS as key/value pairs.
2.  **Splitting:** The input data is divided into **Input Splits**, one for each Mapper.
3.  **Mapping:** Each **Mapper** task processes its split and outputs intermediate key/value pairs.
4.  **Shuffling & Sorting (The "Shuffle"):** The MapReduce framework groups the intermediate key/value pairs by key and sorts them. This is the stage where data is physically moved from the Mappers to the Reducers.
5.  **Reducing:** Each **Reducer** task processes the sorted groups of values for a single key, applying business logic and outputting the final result.
6.  **Output:** The final output is written back to HDFS.

### Runtime Coordination and Task Management

The process is coordinated by **YARN (Yet Another Resource Negotiator)** in modern Hadoop.

  * The **JobClient** submits the job.
  * The **ResourceManager (YARN)** manages resources across the cluster.
  * The **ApplicationMaster** for the specific job manages the lifecycle of the Map and Reduce tasks, coordinating with the ResourceManager for resource allocation and monitoring task execution on the **NodeManagers**.

### Design & Implementation

#### Using MapReduce for Parallel Processing

MapReduce enables **massively parallel processing** because the independent Map tasks can execute concurrently across many nodes. The framework handles the complexities of parallelism, data distribution, and fault tolerance.

#### Examples:

  * **Face Recognition:**
      * **Map:** Extract unique features (e.g., SIFT or SURF vectors) from an image and output them as `<Feature_Vector, Image_ID>` pairs.
      * **Reduce:** Group similar feature vectors and use them to train a face recognition model or compare against existing ones.
  * **Inverted Indexes:** Used for fast text searching (like in search engines).
      * **Map:** Process documents, outputting `<Word, Document_ID>` pairs for every word.
      * **Reduce:** Group by `Word` and create a list of all documents containing that word: `<Word, List_of_Document_IDs>`.
  * **Road Enrichment (Spatial Data):**
      * **Map:** Process raw GPS/sensor data points, outputting `<Road_Segment_ID, Data_Point>`. The road segment ID acts as the grouping key.
      * **Reduce:** Group all data points for a specific road segment and perform statistical analysis (e.g., average speed, traffic density) to enrich the road's metadata.

-----

## 3\. Stream Data Model

### Concepts and Architecture

The **Stream Data Model** deals with data that arrives in a continuous, unbounded, and high-velocity fashion (data-in-motion), as opposed to bounded, static data (data-at-rest).

Key concepts:

  * **Unbounded Data:** The stream never ends.
  * **High Velocity:** Data arrives very quickly.
  * **Streaming Platform:** Tools like **Apache Kafka** or **Amazon Kinesis** act as a durable message queue, decoupling data producers from consumers.
  * **Processing Engine:** Tools like **Apache Spark Streaming** or **Apache Flink** process the continuous data streams.

### Sampling Data in Streams

Since processing every element of a high-velocity stream can be computationally expensive or impossible, **sampling** is often used to get an approximate view of the stream's characteristics. Techniques include:

  * **Random Sampling:** Select each incoming element with a fixed probability $p$.
  * **Reservoir Sampling:** Maintain a small, fixed-size sample (a "reservoir") of the stream seen so far, ensuring any item seen up to the current time is equally likely to be in the reservoir.

### Filtering Streams

**Filtering** involves selectively allowing elements that satisfy a specific condition to pass through the processing pipeline.

  * **Simple Predicate Filtering:** Based on a direct value check (e.g., selecting only stock trades where price \> $100).
  * **Bloom Filters:** A space-efficient probabilistic data structure used to test whether an element is a member of a set, allowing for very fast filtering (with a small chance of false positives).

### Counting Distinct Elements

Counting the number of unique items in a large, continuous stream is a challenging task due to memory constraints. Exact counting is infeasible.

  * **Flajolet-Martin Algorithm:** An early approximation algorithm that uses hashing and the number of trailing zeros in the hash values to estimate the count.
  * **HyperLogLog (HLL):** The modern, industry-standard algorithm. It uses significantly less memory than other techniques to estimate the cardinality (number of distinct elements) with a very small relative error.

-----

## 4\. Hive

### Features

**Apache Hive** is a data warehouse software built on top of Hadoop. It provides a mechanism to **project structure onto the vast amounts of data in HDFS** and lets users query the data using a SQL-like language called **HiveQL**.

  * **SQL Interface:** Allows users familiar with SQL to interact with Big Data.
  * **Batch Processing:** Converts HiveQL queries into **MapReduce** or **Spark** jobs for execution.
  * **Schema on Read:** The schema is enforced when the data is read (at query time), not when it's written, offering flexibility.
  * **Extensibility:** Supports custom data formats, User-Defined Functions (UDFs), and User-Defined Aggregation Functions (UDAFs).

### Data Types and File Formats

Hive supports various underlying **File Formats** for HDFS data, including **TEXTFILE**, **SequenceFile**, **ORC**, and **Parquet**.

#### Primitive and Collection Data Types

| Category | Data Types | Description |
| :--- | :--- | :--- |
| **Numeric** | `TINYINT`, `SMALLINT`, `INT`, `BIGINT`, `FLOAT`, `DOUBLE`, `DECIMAL` | Standard numeric types. |
| **Date/Time** | `TIMESTAMP`, `DATE` | For point-in-time and date-only values. |
| **String** | `STRING`, `VARCHAR`, `CHAR` | Textual data. |
| **Collection** | `ARRAY`, `MAP`, `STRUCT` | Complex, non-primitive data types. |
| **Collection Detail** | `ARRAY<T>` | Ordered list of elements of type T. |
| **Collection Detail** | `MAP<K, V>` | Key-value pairs. |
| **Collection Detail** | `STRUCT<...>` | A record with named fields. |

### HiveQL Commands

#### Creating Tables

Creates an internal table (data managed by Hive) or an external table (data stored outside Hive's management):

```sql
CREATE EXTERNAL TABLE sales_data (
    sale_id BIGINT,
    product_name STRING,
    price DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hadoop/sales';
```

#### Dropping Tables

Removes the table definition (metadata) from the Hive metastore. For internal tables, it also deletes the data. For external tables, only the metadata is deleted:

```sql
DROP TABLE IF EXISTS sales_data;
```

#### Altering Tables

Modifies the table structure, partitions, or properties:

```sql
-- Rename a column
ALTER TABLE sales_data RENAME COLUMN price TO unit_price;

-- Add a new column
ALTER TABLE sales_data ADD COLUMNS (sale_date DATE);

-- Change table properties (e.g., to add a comment)
ALTER TABLE sales_data SET TBLPROPERTIES ('comment' = 'Daily sales transactions');
```

-----

## 5\. Pig

### Installation and Execution

**Apache Pig** is a platform for analyzing large datasets that consists of a high-level language called **Pig Latin**.

  * **Installation:** Pig is a standalone application that is installed and configured to run on a Hadoop cluster (requiring HDFS and YARN).
  * **Execution:** Pig Latin scripts are typically executed in two modes:
    1.  **Local Mode:** Runs on a single machine for testing smaller datasets.
    2.  **MapReduce Mode:** Executes the script by compiling it into a series of MapReduce jobs and running it on the Hadoop cluster.

### Pig Data Model

The basic data structure in Pig is the **relation** (similar to a table in RDBMS). A relation is an unordered bag of **tuples**.

  * **Atom:** A simple scalar value (e.g., a string, integer, float).
  * **Tuple:** An ordered set of fields (e.g., `(John, 30, New York)`).
  * **Bag:** An unordered collection of tuples (the primary data structure). A bag is usually represented by curly braces, e.g., `{ (a, 1), (b, 2), (a, 3) }`.

### Pig Latin

#### Structure

Pig Latin is a **data-flow language** that follows a series of transformations on relations. It's **declarative** and **procedural**.
The general structure of a script involves:

1.  **LOAD:** Loading data from HDFS into a relation.
2.  **TRANSFORM:** Applying operations like `FILTER`, `GROUP`, `FOREACH`, `JOIN`, `LIMIT`.
3.  **DUMP/STORE:** Displaying results or writing the final relation back to HDFS.

**Example:**

```pig
A = LOAD 'input/data.txt' AS (name:chararray, age:int, city:chararray);
B = FILTER A BY age > 25;
C = GROUP B BY city;
D = FOREACH C GENERATE group AS city, COUNT(B) AS total_people;
DUMP D;
```

#### Built-in Functions

Pig Latin provides numerous built-in functions for common operations, including:

  * **Mathematical:** `ABS`, `ROUND`, `SQRT`.
  * **String:** `CONCAT`, `SUBSTRING`, `UPPER`, `LOWER`.
  * **Date/Time:** `ToDate`, `GetWeekDay`.
  * **Eval Functions:** `AVG`, `COUNT`, `MAX`, `MIN`, `SUM`.

-----

## 6\. Spark

### History and Architecture

**Apache Spark** was developed at UC Berkeley's AMPLab as a faster, more general-purpose engine for large-scale data processing than MapReduce.

**Architecture:** Spark follows a **Master/Slave** architecture:

  * **Driver Program:** Runs the application's `main()` function and creates the **SparkContext**.
  * **SparkContext:** The connection to the cluster, responsible for coordinating execution.
  * **Cluster Manager (e.g., YARN, Mesos, Standalone):** Allocates resources to the Spark application.
  * **Executors:** Processes that run on worker nodes, responsible for executing tasks in parallel and storing data in memory.

### Storage Layers

Spark can access data from a variety of storage systems:

  * **HDFS (Hadoop Distributed File System):** A primary source for batch data.
  * **Local File System:** For development and small-scale testing.
  * **Cloud Storage:** S3, Azure Blob Storage, Google Cloud Storage.
  * **Databases:** JDBC/ODBC connections, Cassandra, HBase.

### Core Spark Concepts

  * **In-Memory Processing:** Spark's key advantage is its ability to cache data in memory across the cluster, vastly speeding up iterative algorithms and interactive queries compared to MapReduce, which writes intermediate results to disk.
  * **DAG (Directed Acyclic Graph) Scheduler:** Spark creates a DAG of transformations to optimize the execution plan *before* running any code.
  * **Lazy Evaluation:** Transformations are not executed immediately. Spark waits until an **Action** is called, then optimizes the entire sequence of operations and executes them.

### RDD Basics

**RDD (Resilient Distributed Dataset)** is the fundamental data structure in Spark. It is:

  * **Resilient:** Fault-tolerant and can automatically rebuild lost partitions.
  * **Distributed:** Data is spread across the nodes in a cluster.
  * **Dataset:** A collection of partitioned data.
  * **Immutable:** Once created, an RDD cannot be changed. Transformations create a new RDD.

### RDD Operations

RDD operations are divided into two main categories: **Transformations** and **Actions**.

### Transformations vs Actions (Important for Practical Tasks)

| Feature | Transformations | Actions |
| :--- | :--- | :--- |
| **Description** | Create a new RDD from an existing one. | Trigger the computation/execution of the DAG. |
| **Execution** | **Lazy**—They define the operation but don't execute it immediately. | **Eager**—They execute the operations defined by the preceding transformations and return a result to the driver program or write to storage. |
| **Output** | An RDD. | A value to the driver program or a write operation to storage. |
| **Examples** | `map()`, `filter()`, `join()`, `groupByKey()`, `union()`. | `count()`, `collect()`, `first()`, `take()`, `saveAsTextFile()`. |