
# VIVA Questions - Cloud Computing



## 1. What are the five essential characteristics of Cloud Computing, as defined by NIST?
The five essential characteristics are **On-demand self-service**, **Broad network access**, **Resource pooling**, **Rapid elasticity**, and **Measured service**.

## 2. Differentiate between Capital Expenditure (CapEx) and Operational Expenditure (OpEx) in the context of cloud adoption.
**CapEx** (Capital Expenditure) is the upfront cost of buying physical assets (like servers and data centers), typical of traditional computing. **OpEx** (Operational Expenditure) is the ongoing cost of using services, like the subscription fees paid to a cloud provider, which is the model for cloud computing.

## 3. Explain the primary limitation of traditional computing regarding scalability.
The primary limitation is the **lack of rapid elasticity**. Scaling requires significant time and cost to purchase, install, and configure new hardware, making it difficult to instantly adjust to fluctuating workloads.

## 4. What is the key differentiating factor between a traditional Distributed System and Cloud Computing?
The key difference is the **utility-based, pay-as-you-go economic model** and **rapid elasticity** of Cloud Computing, which abstracts away infrastructure management, unlike a traditional distributed system.

## 5. Define IaaS and give an example of its core offering.
**IaaS (Infrastructure-as-a-Service)** is a service model that provides fundamental computing resources over the internet, such as **Virtual Machines (VMs)**, storage, and networks. AWS EC2 is a prime example.

## 6. What control does a customer have in the PaaS (Platform-as-a-Service) model?
The customer primarily controls their **application deployment and code**, as well as the **data**. The provider manages the operating system, middleware, servers, and storage.

## 7. Give an everyday example of a SaaS (Software-as-a-Service) offering.
A common example is **Gmail** or **Microsoft Office 365**, where the user only interacts with the application interface and doesn't manage any underlying infrastructure, OS, or application code.

## 8. Differentiate between a Public Cloud and a Private Cloud deployment model.
**Public Cloud** is owned and operated by a third-party CSP and shared among multiple tenants over the public internet. **Private Cloud** is exclusively operated for a single organization, regardless of whether it's on-premises or managed by a third party.

## 9. What is a Hybrid Cloud?
A **Hybrid Cloud** is a combination of two or more distinct cloud infrastructures (private, public, or community) that remain unique but are linked by technology that enables data and application portability.

## 10. What is the core technology that enables Cloud Computing?
**Virtualization** is the core technology, allowing physical resources (servers, storage, network) to be partitioned into multiple logical, isolated resources.

## 11. What is the role of Cloud Management Software (CMS)?
The CMS is the software suite responsible for **orchestration, provisioning, resource monitoring, and billing** within the cloud infrastructure. OpenStack is an example.

## 12. Name the "Big Three" hyperscale cloud service providers.
The Big Three are **Amazon Web Services (AWS)**, **Microsoft Azure**, and **Google Cloud Platform (GCP)**.

## 13. What is a Virtual Machine (VM)?
A **VM** is a software emulation of a physical computer that runs an operating system and applications just like a physical machine, but it is isolated from the underlying hardware by a hypervisor.

## 14. What is the main advantage of using VMs in a data center?
The main advantage is **server consolidation** and **resource utilization**, allowing a single physical server to host multiple applications or OS environments simultaneously.

## 15. Differentiate between a Type 1 and a Type 2 Hypervisor.
A **Type 1 (Bare-metal) Hypervisor** runs directly on the host hardware (e.g., VMware ESXi, KVM), offering better performance and security. A **Type 2 (Hosted) Hypervisor** runs as an application on a host operating system (e.g., VirtualBox).

## 16. Explain the concept of Server Virtualization.
Server virtualization is the masking of server resources, including the number and identity of individual physical servers, processors, and operating systems, from server users. It allows one physical machine to host multiple isolated operating systems.

## 17. What is SDN and how does it relate to network virtualization?
**SDN (Software-Defined Networking)** separates the network control plane (decision-making) from the data forwarding plane (packet movement), allowing network configurations to be managed and automated programmatically, which is the basis for network virtualization in the cloud.

## 18. Describe OS-level virtualization. What is its common name?
OS-level virtualization involves sharing the host operating system kernel and isolating user-space processes using namespaces and cgroups. Its common name is **containerization** (e.g., Docker).

## 19. What are the key performance benefits of containers over VMs?
Containers are much **lighter weight** and offer **faster startup times** and **higher density** (more instances per server) because they do not include a full guest OS.

## 20. How does a hypervisor manage CPU resources among multiple VMs?
The hypervisor uses a **scheduler** to divide the physical CPU time and allocate it fairly or according to priority policies to each VM, ensuring performance isolation.

## 21. What is "memory ballooning" in VM memory management?
**Memory ballooning** is a technique where the hypervisor can dynamically reclaim unused memory from a VM by inflating a 'balloon' driver within the guest OS, making that memory available for other VMs or the host.

## 22. What is the difference between SAN and NAS?
**SAN (Storage Area Network)** provides **block-level access** to storage, often used for VM disk images, and appears to the OS as a local drive. **NAS (Network-Attached Storage)** provides **file-level access** over a standard network protocol (like NFS or SMB).

## 23. Briefly explain the function of the Compute Cloud Architecture.
It focuses on the **large-scale deployment and management of computing resources** (VMs, containers) via massive, interconnected server clusters, handling resource scheduling, fault tolerance, and workload balancing.

## 24. What are the three tiers in a standard Multi-tier Web Application Architecture?
The tiers are the **Presentation Tier** (UI/Web Server), the **Application Tier** (Business Logic/App Server), and the **Data Tier** (Database).

## 25. What is Google App Engine (GAE)? Which service model does it represent?
GAE is a fully managed environment for building and running web applications. It is an example of **PaaS (Platform-as-a-Service)**.

## 26. Differentiate between AWS EC2 and AWS Lambda.
**EC2** provides **IaaS (Virtual Machines)**, requiring the user to manage the OS. **Lambda** provides **FaaS (Function-as-a-Service)**, a serverless compute model where the user only provides code functions and is billed per execution time.

## 27. What is OpenStack? Why is it significant?
**OpenStack** is a widely adopted, open-source cloud software platform used for creating and managing large pools of compute, storage, and networking resources in private and public clouds. Its significance lies in promoting vendor neutrality and customization.

## 28. Define Resource Provisioning in the cloud context.
Resource provisioning is the process of **dynamically allocating and deallocating cloud resources** (CPU, memory, storage, network) to meet application needs, typically automatically and on-demand.

## 29. How does Autoscaling work?
**Autoscaling** automatically adjusts the number of compute resources (like VMs or containers) in a resource group, adding more during demand spikes (scaling out) and removing them during low periods (scaling in) to optimize cost and performance.

## 30. What is the primary purpose of a Load Balancer?
The primary purpose is to **efficiently distribute incoming network traffic** across multiple servers or resources to ensure no single resource is overwhelmed, thereby improving availability and responsiveness.

## 31. What problem does Kubernetes solve?
**Kubernetes** is an open-source system that **automates the deployment, scaling, and management of containerized applications**. It solves the complexity of running containers reliably at scale.

## 32. What is DBaaS and what is its main advantage?
**DBaaS (Database as a Service)** is a managed cloud service where the CSP handles all the database operations like provisioning, patching, backups, and scaling. The main advantage is that it allows developers to focus on the application, not the database administration.

## 33. What is FaaS, and what is its main billing characteristic?
**FaaS (Function-as-a-Service)** is a serverless model where the cloud runs application code (functions) in response to events. The main billing characteristic is **pay-per-use**, meaning you only pay for the actual time your code is running.

## 34. What is Task Parallelism?
**Task parallelism** is a parallel computing paradigm where a single job is broken into multiple independent tasks that can be executed simultaneously by different processors or nodes.

## 35. Explain the core concept of Data Parallelism.
**Data parallelism** is a parallel computing paradigm where the same task or instruction is executed simultaneously on different partitions of the same large dataset by different processors.

## 36. What is the fundamental idea behind the MapReduce programming model?
The fundamental idea is to simplify the process of **distributed processing of large datasets** by dividing the workload into two primary phases: a parallel **Map** phase for filtering/sorting, and a parallel **Reduce** phase for summarization.

## 37. What are the three main steps in the MapReduce execution pipeline?
The steps are **Map** (processing input), **Shuffle** (grouping intermediate results by key), and **Reduce** (aggregating the results).

## 38. What is HDFS, and why is it designed to be fault-tolerant?
**HDFS (Hadoop Distributed File System)** is the primary storage system for Hadoop. It is designed to be fault-tolerant by **replicating data blocks** across multiple nodes, ensuring data availability even if a node fails.

## 39. How does NoSQL data management differ from traditional relational databases in the cloud context?
NoSQL databases offer **flexible schema, horizontal scalability, and high performance** for large volumes of unstructured or semi-structured data, often prioritizing availability and partition tolerance over strict consistency (ACID).

## 40. Why is resource isolation critical in multi-tenant cloud environments?
Resource isolation is critical to ensure **confidentiality and integrity** by preventing one customer's data or processes from being accessed or affected by another customer sharing the same physical hardware.

## 41. What are the three core goals of the CIA Triad in cloud security?
**Confidentiality** (data secrecy), **Integrity** (data accuracy and completeness), and **Availability** (uninterrupted access to systems and data).

## 42. What is Security-as-a-Service (SECaaS)?
SECaaS is a cloud service model where the CSP integrates its security services into the company's infrastructure on a subscription basis, covering areas like identity management, intrusion management, and compliance.

## 43. What is a key security risk introduced by the use of hypervisors?
The hypervisor represents a **single point of failure** and a large **trusted computing base**. If the hypervisor is compromised, all VMs running on that host are potentially compromised.

## 44. What is the purpose of Threat Modeling?
**Threat modeling** is a systematic process used to identify potential security threats, attack vectors, and vulnerabilities in an application or system design, allowing risks to be addressed early.

## 45. Differentiate between an IDS and a SIEM system.
An **IDS (Intrusion Detection System)** monitors traffic/systems for malicious activity and alerts. A **SIEM (Security Information and Event Management)** system centralizes, aggregates, and analyzes security-related data (logs and alerts from the IDS and other sources) for holistic security analysis and compliance reporting.

## 46. What is the difference between Data Encryption at Rest and Data Encryption in Transit?
**Encryption at Rest** is the process of encrypting data while it is stored on a disk or storage medium. **Encryption in Transit** is the process of encrypting data while it is being transmitted over a network (e.g., using TLS/SSL).

## 47. How does a WAF (Web Application Firewall) help in cloud security?
A **WAF** protects web applications from common web exploits (like SQL injection and Cross-Site Scripting) by filtering and monitoring HTTP traffic between a web application and the Internet.

## 48. What is VM Isolation?
**VM Isolation** is the mechanism, typically enforced by the hypervisor, that ensures that the memory, storage, and processing of one virtual machine cannot be accessed or interfered with by another virtual machine.

## 49. Why is Patch Management crucial for VM Security?
**Patch management** is crucial because it ensures that the operating system and applications within the VM are updated with the latest security fixes, protecting against known vulnerabilities that hackers might exploit.

## 50. What is the first step in the Cloud Forensics process?
The first step is **Evidence Source Identification and Preservation**, which involves locating the relevant data (logs, snapshots, VM images) and taking steps to ensure it is not tampered with or overwritten.

## 51. What is the concept of Resource Underutilization in traditional computing?
It's the inefficiency where organizations purchase hardware to meet **peak load demands**, but the hardware remains idle or lightly used during non-peak times, resulting in wasted investment and power.

## 52. What is the role of Virtualization Middleware?
The virtualization middleware, or **Hypervisor**, acts as the manager for all virtual machines, creating the virtual environment and controlling the allocation of physical hardware resources to the guest operating systems.

## 53. Give an example of Storage Virtualization.
Creating a **single logical storage pool** (like a RAID or a cloud volume) from multiple disparate physical hard drives or devices.

## 54. What are the advantages of using Pig Latin in the Hadoop Ecosystem?
Pig Latin is a high-level scripting language that allows users to express complex data transformations easily, abstracting away the need to write verbose, low-level Java MapReduce code.

## 55. What is the 'measured service' characteristic of cloud computing?
It means the CSP automatically **monitors and reports resource consumption** (e.g., CPU cycles, storage, bandwidth), allowing billing to be based on the actual usage (pay-as-you-go).

## 56. When would an organization opt for a Community Cloud?
An organization would opt for a Community Cloud when several organizations have **shared computing needs and concerns**, such as strict security requirements, common policies, or adherence to a specific regulatory framework (e.g., government agencies).

## 57. In the IaaS model, what component is the customer responsible for managing?
The customer is responsible for managing the **Operating System (OS)**, **middleware**, **runtime**, and **applications**.

## 58. How does **Paravirtualization** improve I/O performance for VMs?
Paravirtualization involves modifying the guest OS kernel to communicate directly with the hypervisor (instead of emulating hardware), resulting in much **lower overhead** and faster I/O operations.

## 59. What is a key responsibility of the runtime coordinator in MapReduce?
The runtime coordinator is responsible for **scheduling tasks, handling node failures** (re-running failed tasks), and overseeing the overall execution flow of the MapReduce job.

## 60. What is a major challenge regarding data confidentiality in a multi-tenant cloud environment?
The risk of **side-channel attacks** or the **"noisy neighbor"** problem, where an attacker could potentially glean information from a co-resident VM's activity on the shared hardware.

## 61. What is the primary difference between a container and an application-level virtualized environment (like a JVM)?
A **container** virtualizes the OS layer, isolating processes on the same host OS. An **application-level** environment (JVM) virtualizes the runtime environment to execute specific code (byte code), isolating the application from the underlying OS differences.

## 62. Briefly describe Cloud Bursting.
**Cloud Bursting** is a hybrid cloud deployment technique where an application runs in a private cloud but "bursts" or spills over to the public cloud to access additional compute capacity during peak load periods.

## 63. What is the term for the set of instructions that a cloud service provider guarantees to meet regarding availability and performance?
A **Service Level Agreement (SLA)**, which includes penalties if the guarantees (e.g., 99.99% uptime) are not met.

## 64. What is the fundamental concept behind Object Storage (like AWS S3 or Azure Blob Storage)?
It is a system that manages data as **objects** (data, metadata, and a globally unique identifier) in a **flat address space**, offering massive scalability and high durability.

## 65. How do cloud providers typically achieve Resource Pooling?
By providing a large pool of physical and virtual resources that are **dynamically assigned and reassigned** to customers according to demand, abstracting the physical location and resource details.

## 66. What is the benefit of using an Inverted Index (a common MapReduce application)?
An **Inverted Index** maps content (words) to their locations in a document set, making it highly efficient for performing **text search operations**, which is the core of most search engines.

## 67. What is Hypervisor Hardening?
**Hypervisor Hardening** is the process of securing the hypervisor software by disabling unnecessary services, applying security patches, and configuring strict access controls to minimize its attack surface.

## 68. Name two common protocols used in Storage Area Networks (SAN).
**Fibre Channel (FC)** and **iSCSI (Internet Small Computer System Interface)** are common protocols for block-level data transfer in SANs.

## 69. Why is a system like Docker often used in conjunction with a PaaS solution?
While PaaS abstracts the OS, it often still relies on specific language runtimes. Docker (containerization) ensures the application runtime is **completely consistent** across development, staging, and production environments, simplifying deployment on PaaS.

## 70. What is the difference between Scalability and Elasticity in the cloud?
**Scalability** is the ability of a system to handle increased load, often by adding resources. **Elasticity** is the degree to which a system can automatically and rapidly adjust resources (scale up/down, in/out) to match changing workloads dynamically.

## 71. In cloud forensics, why is evidence source preservation difficult?
It is difficult because cloud resources are **dynamic, ephemeral, and distributed**. A running VM instance may be terminated or migrated, leading to the loss or alteration of volatile evidence.

## 72. What is the primary disadvantage of using a Type 2 Hypervisor in a production cloud environment?
The presence of the **Host Operating System (OS)** introduces an extra layer of latency, greater resource overhead, and a larger attack surface compared to a bare-metal Type 1 hypervisor.

## 73. What are the key elements a developer focuses on when utilizing a FaaS platform?
The developer focuses exclusively on writing the **function code** and defining the **events** that trigger its execution.

## 74. What is the core security principle that underpins access control in the cloud?
**Least Privilege**, ensuring that users and services are granted only the minimum permissions necessary to perform their required tasks, thus limiting potential damage from a compromise.

## 75. What is **VM Sprawl**?
**VM Sprawl** is an unmanaged, uncontrolled proliferation of virtual machines in a data center or cloud environment, leading to inefficient resource usage, increased complexity, and potential security holes.

## 76. What is the role of a **VPC (Virtual Private Cloud)** in cloud networking?
A VPC is a logically isolated section of a public cloud where a customer can launch resources into a defined virtual network, giving them control over their **IP address range, subnets, and network gateways**.

## 77. How does the concept of **Sharding** relate to NoSQL databases like BigTable?
Sharding (or data partitioning) is the process of horizontally splitting a large database into smaller, faster-to-manage parts (shards). BigTable inherently manages data distribution and sharding across many machines to achieve massive scale and performance.

## 78. What is the term for the process of moving a running VM from one physical host to another without downtime?
**Live Migration** (or vMotion in VMware terms).

## 79. What is the purpose of using a separate Application Tier in the Multi-tier architecture?
The Application Tier (or business logic layer) handles all the **processing and complex logic**, separating it from the presentation and data storage, which improves **scalability, security, and maintainability**.

## 80. Give one reason why organizations face vendor lock-in with a single cloud provider.
They face vendor lock-in due to the deep integration with **proprietary, non-standard APIs and unique cloud services** (like specific DBaaS or ML services) offered by that single provider.

## 81. In the context of risk management, what is a **Mitigation Strategy**?
A mitigation strategy is a concrete plan or control implemented to **reduce the probability or impact** of a known risk event. (e.g., using encryption to mitigate the risk of data breach).

## 82. What is one example of a Cloud-based Collaboration Service for task management?
**Trello** or **Asana**, which allow teams to collaboratively create, assign, track, and manage project tasks and workflows.

## 83. Differentiate between Block Storage and Object Storage.
**Block Storage** treats data as fixed-size blocks, offering low-latency, random access for OSes (like a local hard drive). **Object Storage** treats data as discrete, unstructured objects, offering massive scale, high durability, and access via HTTP/REST APIs.

## 84. What is a key security challenge when an organization moves from a private cloud to a hybrid cloud?
The key challenge is managing the **security policy and compliance differences** and ensuring a consistent security posture across the on-premises private environment and the public cloud environment.

## 85. What does the term **I/O Device Emulation** refer to in virtualization?
It refers to the hypervisor presenting a **software simulation** of physical I/O devices (like network cards or storage controllers) to the guest OS, which then installs standard drivers for these emulated devices.

## 86. How is **Data Integrity** typically ensured in cloud storage systems like HDFS or S3?
Data integrity is primarily ensured through the use of **checksums** (hashing) on data blocks and **data replication** across multiple nodes.

## 87. What is the role of **Apache Pig** in the Hadoop Ecosystem?
Apache Pig provides a high-level data flow language called Pig Latin that simplifies the process of **performing ETL (Extract, Transform, Load)** and analysis on large datasets stored in HDFS.

## 88. Explain the "Shared Responsibility Model" in cloud security.
The **Shared Responsibility Model** dictates that the **CSP** is responsible for the **security *of* the cloud** (infrastructure, hypervisor, physical security), and the **customer** is responsible for the **security *in* the cloud** (data, operating system configuration, network traffic).

## 89. What is one core functionality of a container orchestration tool like Kubernetes?
A core functionality is **Self-Healing**, which involves automatically restarting failed containers, replacing them, or killing containers that don't respond to health checks.

## 90. Give an example of how **hardware-level virtualization** assists the hypervisor.
Modern CPUs (Intel VT-x, AMD-V) provide specific instructions and ring-0 protection that allow the hypervisor to execute privileged guest OS instructions directly on the hardware without costly binary translation, greatly improving performance.

## 91. What is the difference between a **VLAN** and a **VPC**?
A **VLAN (Virtual Local Area Network)** is a layer-2 network concept that partitions a physical switch into multiple logical broadcast domains. A **VPC (Virtual Private Cloud)** is a layer-3 cloud concept that provides a logically isolated virtual network over the public cloud infrastructure.

## 92. Why is **Shadow VM** creation important in cloud forensics?
A **Shadow VM** is a forensically sound copy (snapshot) of the running VM and its memory state at the time of an incident. It is crucial for analysis because the original VM must often remain running for business continuity.

## 93. What is the term for the cloud feature that allows a customer to immediately access resources without human interaction from the provider?
**On-demand self-service**.

## 94. How does the use of **TLS/SSL** protocols primarily help cloud security?
TLS/SSL provides **Data Confidentiality and Integrity in Transit** by encrypting the communication link between a user and a cloud service (e.g., a web application).

## 95. What are **cgroups (Control Groups)** and **Namespaces** in the context of containers?
These are Linux kernel features that enable OS-level virtualization. **Namespaces** provide process isolation and give each container its own view of the system resources. **cgroups** manage and limit the resources (CPU, memory, I/O) a container can use.

## 96. What is the function of the **Data Plane** in a Software-Defined Network (SDN)?
The Data Plane (or Forwarding Plane) is responsible for the **physical movement of packets** based on the rules dictated by the control plane.

## 97. What is **Multi-Region Deployment**, and what is its primary benefit?
**Multi-Region Deployment** is deploying an application across multiple geographically separate cloud regions. Its primary benefit is **Disaster Recovery (DR)** and **business continuity** against large-scale, region-specific outages.

## 98. How is the concept of **Transparency** maintained in a distributed system (which influences the cloud)?
Transparency means the user sees the system as a single coherent computing facility, unaware of the **distribution, concurrency, and fault tolerance** mechanisms running underneath.

## 99. Why is **BigTable** often categorized as a NoSQL database?
BigTable is categorized as NoSQL because it is a **distributed, column-oriented database** that does not enforce a fixed schema, favoring massive scale and eventual consistency over the strict relational properties of SQL databases.

## 100. What does the term **Hypervisor Escape** refer to?
**Hypervisor Escape** is a critical security vulnerability where an attacker breaks out of the isolation of a guest VM and gains control or access to the underlying hypervisor, potentially compromising all other VMs on the host.