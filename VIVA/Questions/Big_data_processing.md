
# VIVA Questions - Big Data Processing


## 1. Differentiate between HDFS's NameNode and DataNode.
The **NameNode** is the master that manages the filesystem metadata (like file names, directories, and block locations), while the **DataNodes** are the worker nodes that store the actual data blocks and handle read/write requests.

## 2. What is the default block size in modern HDFS installations, and why is it so large?
The default block size is typically **128MB or 256MB**. It's large to minimize the number of disk seek operations relative to the transfer time, maximizing sequential read throughput, which HDFS is optimized for.

## 3. Explain the concept of "Data Locality" in the context of MapReduce.
Data Locality means executing the Map task on the same node where the data block resides (or on the same rack). This reduces network I/O and significantly speeds up processing.

## 4. What is the primary function of the Shuffle phase in the MapReduce execution pipeline?
The Shuffle phase is responsible for **grouping** all intermediate values produced by the Mappers that have the same key, and then **sorting** them before sending them to the Reducers.

## 5. What are the three main types of collection data types supported by Hive?
They are **ARRAY** (ordered list), **MAP** (key-value pairs), and **STRUCT** (a record with named fields).

## 6. What is the key characteristic of Pig Latin that makes it different from SQL?
Pig Latin is a **procedural data-flow language**, meaning you specify the sequence of transformations (A then B then C), whereas SQL is a **declarative language**, where you specify *what* result you want without detailing the execution flow.

## 7. What is an RDD in Spark, and what are its three key properties?
An RDD is a **Resilient Distributed Dataset**. Its three key properties are: **Resilient** (fault-tolerant), **Distributed** (spread across the cluster), and **Immutable** (read-only once created).

## 8. Differentiate between a Spark Transformation and an Action.
A **Transformation** (e.g., `map()`, `filter()`) creates a new RDD from an existing one and is **lazily evaluated**. An **Action** (e.g., `count()`, `collect()`) triggers the actual execution of the RDD lineage and returns a result or writes to storage.

## 9. Why is the NameNode considered a Single Point of Failure (SPOF) in a basic HDFS setup?
If the NameNode fails, all metadata is lost (without High Availability) and the cluster cannot determine where data blocks are located, effectively making the HDFS cluster unusable.

## 10. Explain the "pipeline" mechanism during an HDFS file write operation.
In a pipeline write, the client streams data to the first DataNode, which stores the block and simultaneously forwards it to the second DataNode, and so on. This ensures parallel data transfer and fast replication.

## 11. How does HBase ensure fault tolerance, given that it runs on top of HDFS?
HBase inherits fault tolerance for data persistence from **HDFS replication**. Additionally, it uses **ZooKeeper** to monitor **RegionServers** and handles failover by reassigning regions if a RegionServer crashes.

## 12. What is the most critical element in HBase schema design, and why?
The **Row Key** is the most critical. It determines how data is stored, sorted, and partitioned across RegionServers, which directly impacts query performance and prevents "hot-spotting."

## 13. What is the main advantage of using the ORC or Parquet file formats over TEXTFILE in Hive?
They are **columnar storage formats**, meaning data for individual columns is stored together. This allows for better compression and significant performance improvement by reading only the columns required for a query.

## 14. What does "Schema on Read" mean in the context of Hive?
It means the data structure (schema) is applied to the raw data only when a query is executed (read time). The raw data in HDFS is just stored as-is, offering great flexibility.

## 15. Give an example of a simple MapReduce job for counting word frequency.
**Mapper:** Takes `<LineOffset, LineContent>` as input, splits the line into words, and outputs intermediate pairs of `<Word, 1>`.
**Reducer:** Takes `<Word, List of 1s>` as input, sums the list of ones, and outputs `<Word, TotalCount>`.

## 16. What is a "Block Report" in HDFS?
It's a report sent by a **DataNode** to the **NameNode** that contains a complete list of all data blocks stored on that particular DataNode. This report helps the NameNode maintain accurate block mapping metadata.

## 17. Why is sampling data important in a high-velocity stream data model?
Because processing every element in a high-velocity stream might be computationally infeasible or too slow, **sampling** allows for efficient estimation of stream characteristics or behavior using a smaller, representative subset of the data.

## 18. What is the role of the HyperLogLog (HLL) algorithm in stream processing?
HLL is a highly memory-efficient algorithm used to **estimate the cardinality (number of distinct elements)** of a very large, unbounded data stream with a small relative error.

## 19. If you want to rename a column in a Hive table, which HiveQL command would you use?
The **`ALTER TABLE`** command, specifically `ALTER TABLE ... RENAME COLUMN ... TO ...`.

## 20. What is a 'Bag' in the Pig data model?
A **Bag** is the primary data structure, representing an unordered collection of **Tuples** (rows). It's essentially a relation.

## 21. What does the term "Resilient" in RDD refer to?
It means the dataset is **fault-tolerant**. If a partition is lost due to a node failure, Spark can automatically recompute it using the lineage (the record of all transformations) that created it.

## 22. Why is Spark considered faster than traditional MapReduce for iterative algorithms?
Spark can **cache data in memory** (as RDDs or DataFrames) across iterations, avoiding the costly disk I/O operations required by MapReduce to reload data for each iteration.

## 23. Briefly explain the difference between `collect()` and `saveAsTextFile()` in Spark.
`collect()` is an **Action** that returns all the elements of the RDD to the **Driver Program** (use with small RDDs). `saveAsTextFile()` is an **Action** that writes the RDD's contents to the **distributed file system** (HDFS) in a parallel manner.

## 24. How does HDFS achieve data fault tolerance?
Primarily through **Data Replication**. Each block of data is typically replicated three times across different DataNodes and often across different racks.

## 25. Describe the role of a Bloom Filter in stream filtering.
A Bloom Filter is a space-efficient, probabilistic data structure used to test whether an element **is definitely not** a member of a set. It allows quick filtering with the possibility of *false positives* but never *false negatives*.

## 26. What happens if a DataNode fails in an HDFS cluster?
The **NameNode** will detect the failure (no heartbeat), mark the DataNode as dead, and initiate the **re-replication** of all blocks that had their replication factor drop below the target (e.g., from 3 to 2).

## 27. What is "Hot-Spotting" in HBase, and how is it usually addressed?
Hot-Spotting occurs when read/write operations concentrate on a small number of RegionServers (or a single one). It is usually addressed by **designing a good Row Key** that ensures uniform distribution of data across all regions.

## 28. Name two common columnar storage formats used in the Hadoop ecosystem.
**Parquet** and **ORC (Optimized Row Columnar)**.

## 29. What is the significance of the `GROUP` operator in Pig Latin?
The `GROUP` operator collects and groups all tuples with the same key into a single tuple, where the grouped tuples form a new **Bag**.

## 30. Explain the concept of "Partitioning" in the context of RDDs.
Partitioning means dividing the RDD's data into smaller, logical chunks. Each partition is a unit of work that can be processed in parallel by an **Executor** on a worker node.

## 31. What is the main difference between an `INNER JOIN` in HiveQL and a `LEFT OUTER JOIN`?
An **`INNER JOIN`** returns only rows that have matching values in both tables. A **`LEFT OUTER JOIN`** returns all rows from the left table and the matched rows from the right table; unmatched rows from the right table will have NULLs.

## 32. What is the fundamental difference between MapReduce and the Stream Data Model regarding data flow?
**MapReduce** is designed for **bounded data (batch processing)**, where the entire dataset is known. The **Stream Data Model** is designed for **unbounded data (continuous processing)**, where the data flow is endless.

## 33. Why is the `map()` transformation in Spark called a "narrow dependency"?
Because each partition in the resulting RDD depends on **at most one** partition of the parent RDD. This makes recovery faster since only the lost parent partition needs re-computation.

## 34. What is a "full scan" in HBase, and why is it generally discouraged?
A full scan is reading every row in a table. It is discouraged because it is an expensive operation that stresses the cluster, violating HBase's optimization for fast, random access by row key.

## 35. Briefly describe the purpose of the NameNode's **Heartbeat** mechanism.
DataNodes send a Heartbeat signal to the NameNode periodically to confirm that they are alive and operational. If the NameNode misses several heartbeats, it assumes the DataNode has failed.

## 36. Give an example of a use case where MapReduce is perfect for parallel processing.
Building an **Inverted Index** for a search engine, where the task of tokenizing documents and grouping words is naturally parallelizable across many machines.

## 37. Differentiate between `LOAD` and `STORE` operations in Pig Latin.
`LOAD` brings data from the file system (usually HDFS) into a Pig **Relation**. `STORE` writes a Pig Relation back out to the file system.

## 38. Why is the maximum number of reducers in a MapReduce job limited by the framework, and what can it be?
The number of reducers is generally limited by the number of desired output files or the capacity of the cluster. It can be set by the user, and a common setting is to have the number of reducers be a multiple of the number of cores in the cluster.

## 39. What is a "Region" in HBase?
A **Region** is a contiguous, sorted range of rows of an HBase table. The RegionServer is responsible for serving (handling read/write requests for) one or more regions.

## 40. How does a client read a file from HDFS?
The client first asks the **NameNode** for the locations of the data blocks. The client then reads the blocks directly from the most optimal **DataNodes**.

## 41. What is the primary difference between a Hive Internal Table and an External Table?
For an **Internal Table**, Hive manages both the metadata and the data. When you drop the table, the data is deleted. For an **External Table**, Hive only manages the metadata; dropping the table leaves the underlying data in HDFS untouched.

## 42. What command would you use in HiveQL to permanently remove a table definition from the metastore?
The **`DROP TABLE`** command.

## 43. Why are Transformations in Spark considered "lazy"?
They are not executed immediately when called. Instead, Spark records the transformation in the RDD's **lineage** (DAG) and waits until an **Action** is invoked to optimize and execute the entire sequence of operations.

## 44. Provide an example of a String built-in function in Pig Latin.
**`UPPER()`** or **`CONCAT()`**.

## 45. What is the role of the **ResourceManager** in a YARN-managed Hadoop cluster?
The ResourceManager is the ultimate authority that **arbitrates resources** (CPU, memory) among all competing applications in the cluster.

## 46. What is the biggest trade-off associated with the HyperLogLog algorithm?
It provides an **approximate count** of distinct elements, not an exact count. This is a trade-off for its extremely low memory usage.

## 47. How does HDFS handle the deletion of a file?
The client asks the NameNode for deletion. The NameNode records the change in metadata but doesn't immediately delete the data blocks. Instead, it moves the file to a **`.trash`** directory, and the actual block deletion from DataNodes happens later during a garbage collection process.

## 48. What is the concept of a "Time-Series" model in a streaming context?
It involves analyzing sequences of data points indexed (or graphed) in time order, crucial for detecting trends, anomalies, or predicting future values in a data stream.

## 49. In MapReduce, what must the output of the Map phase be?
The output must always be a set of **intermediate key/value pairs** (e.g., `<K2, V2>`).

## 50. What is the purpose of the **ZooKeeper** service in an HBase cluster?
ZooKeeper provides **coordination and synchronization** services, managing the state of the cluster, locating the HMaster, and handling RegionServer failover detection.

## 51. What is the advantage of using `VARCHAR` over `STRING` in Hive?
`VARCHAR` specifies a maximum length, allowing Hive to potentially use less memory and storage for the metadata and provide better performance in some scenarios, unlike `STRING`, which has no length limit.

## 52. Differentiate between a **narrow transformation** and a **wide transformation** in Spark RDDs.
A **narrow transformation** (e.g., `map`) uses only data from **one parent partition** to compute a child partition. A **wide transformation** (e.g., `groupByKey`, `join`) requires data from **all partitions** of the parent RDD(s) to compute the child RDD, necessitating a costly **shuffle** across the network.

## 53. If you want to check if a Pig Latin script runs correctly on a small machine before submitting it to the cluster, which execution mode would you use?
**Local Mode**.

## 54. What are **SequenceFiles** in the Hadoop ecosystem?
They are flat files consisting of **binary key/value pairs**. They are highly optimized for MapReduce processing because they are splittable and support compression.

## 55. Why is a good replication factor important in HDFS design?
It ensures **high availability** and **fault tolerance**. If a node fails, the data remains accessible on its replicas.

## 56. What is the core responsibility of the **ApplicationMaster** in YARN?
The ApplicationMaster is responsible for **managing the lifecycle of a specific application** (like a MapReduce job or a Spark job), negotiating resources from the ResourceManager, and monitoring the execution of the tasks.

## 57. Give an example of a stream data filtering technique using a simple predicate.
Filtering a stream of financial trades to only include transactions where the **`amount` is greater than \$10,000**.

## 58. How does the **Row Key** in HBase relate to data sorting?
HBase tables are always sorted **lexicographically** by the row key. This facilitates efficient range scans.

## 59. What is a User-Defined Function (UDF) in Hive?
A UDF is a way to **extend the functionality of HiveQL** by writing custom code (typically in Java) to perform operations not provided by built-in functions, often on a single row/column value.

## 60. What is the difference between `LIMIT` and `FILTER` operators in Pig Latin?
`FILTER` is used to select tuples based on a condition (like SQL `WHERE`). `LIMIT` is used to restrict the number of tuples returned in a relation.

## 61. Why is the shuffling phase of MapReduce often the performance bottleneck?
Because it involves **network I/O** to transfer data between the Map and Reduce tasks and **disk I/O** for intermediate storage and sorting, which is slow compared to in-memory operations.

## 62. What is the purpose of the **DAG Scheduler** in Spark?
The DAG Scheduler analyzes the lineage of RDD transformations, creates an optimized **Directed Acyclic Graph (DAG)** of execution stages, and determines which partitions need to be computed.

## 63. Name a common technique used for sampling data in a continuous stream to maintain a representative sample size.
**Reservoir Sampling**.

## 64. What is the significance of the **Timestamp** dimension in HBase?
It allows HBase to store **multiple versions** of a cell's value (versioning), indexed by the time of writing.

## 65. What happens during the **partitioning** step in the MapReduce Shuffle?
It determines which of the **Reducer tasks** will receive a particular intermediate key/value pair based on a hash function applied to the key.

## 66. How do you create an **External Table** in HiveQL?
By adding the **`EXTERNAL`** keyword after `CREATE` (e.g., `CREATE EXTERNAL TABLE ...`).

## 67. Explain the concept of "Lazy Evaluation" in Spark.
Spark waits until an action is called to perform all transformations. This allows Spark to **optimize the execution plan** (e.g., combining multiple transformations into a single stage) before running the job.

## 68. What are the two types of compression supported by HDFS blocks?
**Block compression** (applied to individual blocks) and **File compression** (applied to the entire file).

## 69. Why is Pig often preferred over writing raw MapReduce Java code?
Pig Latin is a **higher-level language** that is much faster to write and easier to understand, abstracting away the complexities of the MapReduce framework.

## 70. What is the core benefit of columnar storage (Parquet/ORC) over row-oriented storage (Text/SequenceFile)?
Columnar storage is far more efficient for **analytical queries** (BI/reporting) because it can read only the necessary columns from disk, reducing I/O and increasing query speed.

## 71. What is the `COLLECT` operator in Pig Latin, and what does it do?
`COLLECT` is an operator used within a `FOREACH` to create a bag containing all tuples from the inner group.

## 72. In HDFS, what does the **Checksum** of a data block ensure?
It ensures **data integrity**. The DataNode verifies the checksum of a block before serving it to a client and periodically checks stored blocks for corruption.

## 73. What is the difference between a **Primitive** data type and a **Collection** data type in Hive?
**Primitive** types are scalar (single-valued) like `INT`, `STRING`, or `DATE`. **Collection** types are complex, multi-valued structures like `ARRAY`, `MAP`, or `STRUCT`.

## 74. How does an HDFS client know the physical location of the data it wants to read?
By asking the **NameNode**, which maintains the mapping of files to blocks, and blocks to DataNodes.

## 75. Give an example of a **wide transformation** in Spark RDD operations.
**`groupByKey()`** or **`join()`**.

## 76. What are the two core functions that every MapReduce program must implement?
The **Map** function and the **Reduce** function.

## 77. What is the purpose of a **Reservoir** in Reservoir Sampling?
The Reservoir is a small, fixed-size buffer that maintains the sample. It ensures that any item seen so far has an equal chance of being in the final sample.

## 78. Differentiate between `DROP TABLE` and `TRUNCATE TABLE` in HiveQL.
**`DROP TABLE`** deletes the table's metadata and, for internal tables, the data. **`TRUNCATE TABLE`** removes all rows from a table but keeps the table's definition (metadata) intact.

## 79. What is the role of the **HMaster** in the HBase architecture?
The HMaster is the coordinator: it handles DDL (create/delete tables), performs Region balancing, and monitors RegionServers.

## 80. How is fault tolerance achieved for the NameNode itself in modern Hadoop (via High Availability)?
By running a **Standby NameNode** alongside the **Active NameNode**. Both share the metadata (via a journal system like Quorum Journal Manager), and ZooKeeper facilitates automatic failover.

## 81. Why might you use the **`COLLECT()`** action in Spark with caution?
Because `collect()` returns all the data to the single **Driver Program**, which can cause an **Out-of-Memory (OOM)** error if the dataset is large.

## 82. What is an **Avro Data File**, and what is its key benefit?
It is a row-oriented storage format that includes the **schema** within the file. Its key benefit is that it is **self-describing** and supports schema evolution.

## 83. In Pig Latin, what does the `FOREACH` operator do?
It is used to **iterate over the tuples of a relation** (or a bag) and generate a new result set after applying specified field transformations or projections.

## 84. What is the main characteristic that separates a traditional database from a Stream Data Model?
Traditional databases handle **data at rest** (bounded), while the Stream Data Model handles **data in motion** (unbounded).

## 85. What are the three common cluster managers that Spark can utilize?
**Standalone mode**, **YARN**, and **Apache Mesos**.

## 86. Explain the concept of "rack awareness" in HDFS.
HDFS attempts to store replicas of a block on different racks to minimize the chance of losing all replicas from a single rack failure, improving fault tolerance and read performance.

## 87. Give an example of a real-world use case for counting distinct elements in a data stream.
Counting the **number of unique visitors** to a website in real-time.

## 88. What is a **RegionServer** in HBase responsible for?
It stores the actual data in **Regions** and handles all read, write, and update requests from clients for those regions.

## 89. How does HiveQL utilize MapReduce (or Spark/Tez) for query execution?
Hive's **execution engine** translates the HiveQL query (the declarative SQL statement) into a series of coordinated **MapReduce** or **Spark/Tez** jobs that are run on the cluster.

## 90. What is a potential drawback of using a very small block size in HDFS?
It would lead to excessive **metadata overhead** on the NameNode (as there would be more blocks to track) and increased disk seeks during file access, lowering throughput.

## 91. What is the **lineage** of an RDD?
The lineage (or Directed Acyclic Graph - DAG) is a **graph of all the deterministic transformations** that were applied to the original data to create the current RDD. It is used for fault recovery.

## 92. Why is Pig Latin useful for "Road Enrichment" (processing spatial data)?
Pig's **GROUP** and **JOIN** operators allow you to easily aggregate many raw GPS/sensor data points by a common key (like `Road_Segment_ID`) and calculate statistical summaries, which is a common enrichment task.

## 93. If a MapReduce job does not need a reduce phase, what can the user do to optimize it?
Set the number of reducers to **zero**. The job will execute as a "Map-only" job, with the Mapper output being written directly to HDFS.

## 94. What is the core difference between the **Map** function and the **Reduce** function in MapReduce regarding input data?
The **Map** function processes **individual records** independently, while the **Reduce** function processes a **list of values** that share the same key.

## 95. What does the term **`STORED AS`** specify in a Hive `CREATE TABLE` statement?
It specifies the **underlying file format** used to store the table's data in HDFS (e.g., `TEXTFILE`, `ORC`, `PARQUET`).

## 96. Why is it generally recommended to have a small number of **Column Families** in an HBase schema?
Because all columns within a family are stored together physically, reading from multiple column families requires separate disk seeks, which degrades performance.

## 97. Differentiate between `ARRAY<T>` and `MAP<K, V>` in Hive collection data types.
`ARRAY<T>` is an **ordered list** of elements accessed by a zero-based integer index. `MAP<K, V>` is an **unordered collection** of key-value pairs accessed by the key.

## 98. How is the **intermediate key** in a MapReduce job different from the **input key**?
The **input key** is typically the byte offset of the record in the file. The **intermediate key** is a value derived from the input data that is used to group data for the Reducer (e.g., a word, a user ID, etc.).

## 99. What is the difference between `map()` and `flatMap()` transformations in Spark?
`map()` applies a function to each element and returns **one new element** for each input element. `flatMap()` applies a function to each element and returns **an iterator** (a sequence) of new elements, effectively allowing zero or more output elements for each input element.

## 100. What is the purpose of the **`LOCATION`** clause when creating an **External Table** in HiveQL?
The `LOCATION` clause specifies the **HDFS path** where the actual data files are stored, allowing Hive to link the table metadata to the existing data.