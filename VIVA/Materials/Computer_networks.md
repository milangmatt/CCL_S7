# Computer Networks

- [Computer Networks](#computer-networks)
  - [1. Introduction to Computer Networks](#1-introduction-to-computer-networks)
    - [Definition and Purpose of Computer Networks](#definition-and-purpose-of-computer-networks)
    - [Uses of Computer Networks](#uses-of-computer-networks)
    - [Network Hardware](#network-hardware)
    - [Network Hardware Components](#network-hardware-components)
    - [Network Software](#network-software)
    - [Types of Networks](#types-of-networks)
  - [2. Reference Models](#2-reference-models)
    - [OSI Reference Model](#osi-reference-model)
    - [TCP/IP Reference Model](#tcpip-reference-model)
    - [Comparison: OSI vs TCP/IP](#comparison-osi-vs-tcpip)
    - [Protocol Data Units (PDU) and Data Encapsulation Process](#protocol-data-units-pdu-and-data-encapsulation-process)
  - [3. Physical Layer](#3-physical-layer)
    - [Modes of Communication](#modes-of-communication)
    - [Physical Topologies](#physical-topologies)
    - [Transmission Media](#transmission-media)
      - [Guided (Wired)](#guided-wired)
      - [Unguided (Wireless)](#unguided-wireless)
    - [Signal Encoding](#signal-encoding)
    - [Repeaters and Hubs](#repeaters-and-hubs)
    - [Performance Metrics](#performance-metrics)
  - [4. Data Link Layer](#4-data-link-layer)
    - [Design Issues](#design-issues)
    - [Error Detection and Correction](#error-detection-and-correction)
    - [Sliding Window Protocols](#sliding-window-protocols)
    - [HDLC (High-Level Data Link Control) Protocol](#hdlc-high-level-data-link-control-protocol)
    - [Medium Access Control (MAC)](#medium-access-control-mac)
      - [Channel Allocation Problem](#channel-allocation-problem)
      - [Multiple Access Protocols](#multiple-access-protocols)
    - [Ethernet (IEEE 802.3)](#ethernet-ieee-8023)
    - [Wireless LANs – IEEE 802.11](#wireless-lans--ieee-80211)
    - [Interconnecting Devices (Layer of Operation)](#interconnecting-devices-layer-of-operation)
      - [Bridges from 802.x to 802.y](#bridges-from-802x-to-802y)
  - [5. Network Layer (General Concepts)](#5-network-layer-general-concepts)
    - [Design Issues](#design-issues-1)
    - [Routing Algorithms](#routing-algorithms)
    - [Congestion Control Algorithms](#congestion-control-algorithms)
    - [Quality of Service (QoS)](#quality-of-service-qos)
      - [Requirements](#requirements)
      - [Techniques to Achieve QoS](#techniques-to-achieve-qos)
  - [6. Network Layer in the Internet](#6-network-layer-in-the-internet)
    - [IP Protocol – Structure and Working](#ip-protocol--structure-and-working)
    - [IP Addressing – Classes, Subnetting, CIDR](#ip-addressing--classes-subnetting-cidr)
    - [ICMP (Internet Control Message Protocol)](#icmp-internet-control-message-protocol)
    - [ARP and RARP](#arp-and-rarp)
    - [BOOTP and DHCP](#bootp-and-dhcp)
    - [OSPF and BGP Routing Protocols](#ospf-and-bgp-routing-protocols)
    - [Internet Multicasting](#internet-multicasting)
    - [IPv6 and ICMPv6](#ipv6-and-icmpv6)
  - [7. Transport Layer](#7-transport-layer)
    - [Transport Service – Purpose and Provided Services](#transport-service--purpose-and-provided-services)
    - [Transport Service Primitives](#transport-service-primitives)
    - [UDP – Characteristics and Use Cases](#udp--characteristics-and-use-cases)
    - [TCP](#tcp)
  - [8. Application Layer](#8-application-layer)
    - [FTP (File Transfer Protocol)](#ftp-file-transfer-protocol)
    - [DNS (Domain Name System)](#dns-domain-name-system)
    - [Email Protocols – SMTP, POP3, IMAP](#email-protocols--smtp-pop3-imap)
    - [MIME (Multipurpose Internet Mail Extensions)](#mime-multipurpose-internet-mail-extensions)
    - [SNMP (Simple Network Management Protocol)](#snmp-simple-network-management-protocol)
    - [WWW – Architecture and Operation](#www--architecture-and-operation)


## 1. Introduction to Computer Networks

### Definition and Purpose of Computer Networks
A **computer network** is a group of interconnected computing devices capable of exchanging data and sharing resources.

* **Purpose:** The primary purpose is to **share resources** (e.g., printers, files, software), enable **communication** (e.g., email, video calls), and provide **remote access** to information and applications.

### Uses of Computer Networks
* **Resource Sharing:** Sharing hardware (printers, scanners) and software (applications, databases).
* **Communication:** Email, instant messaging, voice over IP (VoIP), video conferencing.
* **Access to Information:** World Wide Web browsing, database queries, e-commerce.
* **Centralized Management:** Easier management of data, backups, and security.

### Network Hardware
These are the physical devices that make up the network.
* **Hosts (End Devices):** Computers, smartphones, servers, etc., that send and receive data.
* **Interconnecting Devices:**
    * **Routers:** Connect different networks (Layer 3 of OSI) and forward packets based on **IP addresses**.
    * **Switches:** Connect devices within the same network (Layer 2 of OSI) and forward frames based on **MAC addresses**.
    * **Hubs/Repeaters:** Simple devices that regenerate and broadcast signals (Layer 1 of OSI).
    * **Network Interface Cards (NICs):** Hardware that allows a device to connect to a network.
* **Media:**
    * **Wired:** Twisted-pair cable, Coaxial cable, Fiber-optic cable.
    * **Wireless:** Antennas, access points (APs).

###  Network Hardware Components

| Hardware Component | Description |
|--------------------|-------------|
| **Network Interface Card (NIC)** | Hardware that connects a computer to the network; it provides the physical interface for data transmission. |
| **Switch** | Connects multiple devices in a LAN and forwards data only to the intended destination device using MAC addresses. |
| **Router** | Connects multiple networks and directs data packets between them using IP addresses. |
| **Hub** | Basic networking device that broadcasts incoming data to all connected devices without filtering. |
| **Bridge** | Connects and filters traffic between two LAN segments based on MAC addresses. |
| **Gateway** | Acts as a translator between networks using different protocols or architectures. |
| **Repeater** | Amplifies or regenerates signals to extend the transmission distance. |
| **Modem** | Converts digital signals to analog for transmission over telephone lines and vice versa. |
| **Access Point (AP)** | Provides wireless connectivity to devices, acting as a bridge between wired and wireless networks. |
| **Firewall** | Hardware or software device that monitors and controls incoming and outgoing network traffic based on security rules. |
| **Server** | Provides services or resources (like files, websites, or emails) to other computers (clients) on the network. |
| **Client (Workstation)** | A user’s device that accesses resources or services from a server on the network. |


### Network Software
These are the programs and protocols that govern network communication.
* **Protocol Stacks:** A set of network protocols working together (e.g., **TCP/IP suite**). Protocols define the format, order of messages, and actions taken by devices.
* **Network Operating System (NOS):** Software that runs on servers and networking devices to manage network resources (e.g., Windows Server, Linux, Cisco IOS).
* **Applications:** Software that uses the network (e.g., Web browsers, Email clients, FTP clients).

### Types of Networks
Networks are classified by their scale:
* **PAN (Personal Area Network):** Covers a very small area, typically within a single person's reach (e.g., Bluetooth devices connecting to a smartphone).
* **LAN (Local Area Network):** Connects devices in a limited geographical area, like a home, office building, or school.
* **MAN (Metropolitan Area Network):** Covers a city or a large campus, often interconnecting several LANs.
* **WAN (Wide Area Network):** Spans a large geographical area, connecting LANs across cities, countries, or continents (e.g., the Internet backbone).
* **Internet:** A global system of interconnected computer networks.

***

## 2. Reference Models

### OSI Reference Model
The **Open Systems Interconnection (OSI) Model** is a conceptual framework that describes seven layers of computer system functions used to communicate over a network.

| Layer | Name | Function | PDU |
| :---: | :---: | :--- | :---: |
| 7 | **Application** | Provides user interface and services (e.g., HTTP, FTP, DNS). | Data |
| 6 | **Presentation** | Handles data formatting, encryption, and compression. | Data |
| 5 | **Session** | Establishes, manages, and terminates connections (sessions) between applications. | Data |
| 4 | **Transport** | Provides reliable (TCP) or unreliable (UDP) data transfer, segmentation, and reassembly. | **Segment/Datagram** |
| 3 | **Network** | Handles logical addressing (IP) and routing of packets between networks. | **Packet** |
| 2 | **Data Link** | Handles physical addressing (MAC), framing, error control, and flow control on a link. | **Frame** |
| 1 | **Physical** | Transmits raw bits over a communication medium (cables, signals, bit timing). | **Bit** |

* **Interfaces:** The interaction point between two adjacent layers. Each layer only interacts with the layer immediately above and below it.
* **Encapsulation:** The process of adding a header (and sometimes a trailer) to the data unit from the layer above.

### TCP/IP Reference Model
The **Transmission Control Protocol/Internet Protocol (TCP/IP) Model** is a four-layer model and the basis for the modern Internet.

| Layer | Name | Protocols | Function |
| :---: | :---: | :--- | :--- |
| 4 | **Application** | HTTP, DNS, FTP, SMTP | Combines OSI Application, Presentation, and Session layers. |
| 3 | **Transport** | **TCP, UDP** | Responsible for host-to-host communication. |
| 2 | **Internet** | **IP, ICMP, ARP** | Handles logical addressing and routing. |
| 1 | **Network Access** | Ethernet, Wi-Fi | Combines OSI Data Link and Physical layers, dealing with physical transmission. |

### Comparison: OSI vs TCP/IP
| Feature | OSI Model | TCP/IP Model |
| :---: | :---: | :---: |
| **Layers** | 7 Layers | 4 Layers |
| **Focus** | Conceptual reference, protocol-independent. | Practical implementation, protocol-dependent. |
| **Network Layer** | Connectionless and connection-oriented services. | Primarily connectionless (IP). |
| **Origin** | Theoretical (standardized after protocols). | Developed by DARPA, practical implementation (protocols came first). |

### Protocol Data Units (PDU) and Data Encapsulation Process
A **PDU** is a single block of information transmitted at a specific layer.

**Data Encapsulation:**
When data moves from the Application Layer (top) down to the Physical Layer (bottom) at the sender, each layer adds its own control information (a **header**) to the PDU it receives from the layer above.
1.  **Data** (Application Layer)
2.  **Segment/Datagram** (Transport Layer header added)
3.  **Packet** (Network Layer header added)
4.  **Frame** (Data Link Layer header and trailer added)
5.  **Bits** (Physical Layer transmission)

At the receiver, the process is reversed (**de-encapsulation**), where each layer removes the corresponding header and passes the remaining data up.

***

## 3. Physical Layer

The **Physical Layer (Layer 1)** is responsible for the mechanical, electrical, functional, and procedural means to activate, maintain, and de-activate physical connections for bit transmission.

### Modes of Communication
* **Simplex:** Data flows in only one direction (e.g., radio broadcast).
* **Half-Duplex:** Data can flow in both directions, but *only one direction at a time* (e.g., walkie-talkie).
* **Full-Duplex:** Data can flow in both directions simultaneously (e.g., telephone conversation).

### Physical Topologies
The arrangement of devices and connections in a network.
* **Bus:** All devices connect to a single central cable (backbone). Simple but prone to single-point failure.
* **Star:** All devices connect to a central hub or switch. Most common topology. Failure of one device/cable doesn't affect the network.
* **Ring:** Devices connect point-to-point to form a closed loop. Data travels in one direction around the ring.
* **Mesh:** Every device is connected to every other device (full mesh). Highly redundant but expensive and complex.
* **Hybrid:** A combination of two or more basic topologies (e.g., a star-bus network).

### Transmission Media
#### Guided (Wired)
* **Twisted Pair:** Copper wires twisted to reduce electromagnetic interference (EMI). Used in LANs (**Ethernet**).
    * *Unshielded Twisted Pair (UTP):* Most common, inexpensive.
    * *Shielded Twisted Pair (STP):* Extra metallic shielding for better noise immunity.
* **Coaxial:** Two conductors sharing the same axis. Better shielding than UTP. Used in cable TV and older Ethernet networks.
* **Fiber Optics:** Transmits data using light signals through glass or plastic strands. Highest bandwidth, lowest latency, and immune to EMI.

#### Unguided (Wireless)
* **Radio Waves:** Used for long-range and short-range communication (e.g., AM/FM radio, Wi-Fi, cellular networks). Omnidirectional.
* **Microwaves:** Used for line-of-sight communication, including satellite and terrestrial links. Directional antennas.
* **Infrared:** Used for very short-range, line-of-sight communication (e.g., TV remotes). Cannot penetrate opaque objects.

### Signal Encoding
The process of converting data (digital/analog) into a signal (digital/analog) for transmission.
* **Digital-to-Digital:** Converting digital data to a digital signal (e.g., **Manchester encoding** for Ethernet).
* **Analog-to-Digital (Digitization):** Converting analog data to a digital signal (e.g., **Pulse Code Modulation - PCM** for voice).
* **Digital-to-Analog (Modulation):** Converting digital data to an analog signal (e.g., **ASK, FSK, PSK** for modems).
* **Analog-to-Analog (Modulation):** Converting analog data to a different analog signal (e.g., frequency modulation for radio).

### Repeaters and Hubs
* **Repeater (Layer 1):** Regenerates a weak, distorted signal to its original strength and shape, extending the physical distance a signal can travel.
* **Hub (Layer 1):** A multi-port repeater. It broadcasts any data it receives on one port to all other connected ports, creating a single collision domain.

### Performance Metrics
* **Bandwidth:** The maximum data rate a path can handle, typically measured in bits per second (bps).
* **Throughput:** The actual amount of data successfully transferred per unit of time. Always $\le$ Bandwidth.
* **Latency (Delay):** The time it takes for a data packet to travel from source to destination.
* **Queuing Time:** The time a packet waits in a buffer (queue) at a device (like a router) before being processed.
* **Bandwidth–Delay Product (BDP):** The number of bits that can be "in flight" on the link at any time. It's calculated as $BDP = \text{Bandwidth} \times \text{Latency}$.

***

## 4. Data Link Layer

The **Data Link Layer (Layer 2)** is responsible for reliable node-to-node data transfer across the physical link. It is divided into two sublayers: **Logical Link Control (LLC)** and **Media Access Control (MAC)**.

### Design Issues
* **Framing:** Dividing the bit stream from the Physical Layer into discrete units called **frames**. Methods include character count, character stuffing, and bit stuffing.
* **Flow Control:** Mechanism to prevent a fast sender from overwhelming a slow receiver by regulating the rate of data transmission.
* **Error Control:** Mechanisms to detect and/or correct errors (bit flips) that occur during transmission.

### Error Detection and Correction
* **Parity:** Adds a single bit to the data to make the total number of 1s either even (even parity) or odd (odd parity). Detects only an odd number of bit errors.
* **CRC (Cyclic Redundancy Check):** Appends a checksum calculated using polynomial division. Highly effective for detecting burst errors.
* **Hamming Code:** An error **correction** code that can detect and correct single-bit errors.

### Sliding Window Protocols
A class of flow and error control protocols that allows the sender to transmit multiple frames without waiting for an acknowledgment (ACK) for each one.
* **Stop-and-Wait:** Sender sends one frame, then waits for an ACK before sending the next. Window size is 1. Very inefficient.
* **Go-Back-N:** Sender can transmit up to $N$ frames before receiving an ACK. If a frame is lost or corrupted, the receiver discards all subsequent frames, and the sender retransmits the lost frame *and all subsequent frames*.
* **Selective Repeat:** Sender can transmit up to $N$ frames. If a frame is lost, only that specific frame is retransmitted. The receiver buffers correctly received frames that arrive out of order.

### HDLC (High-Level Data Link Control) Protocol
A widely used bit-oriented protocol for point-to-point and multipoint links. It supports:
* **Framing** using a unique flag sequence (01111110).
* **Bit stuffing** to prevent the flag sequence from appearing in the data.
* **Error and flow control** using sequence numbers and acknowledgments.
* **Three frame types:** Information (I), Supervisory (S), and Unnumbered (U).

### Medium Access Control (MAC)
#### Channel Allocation Problem
Determining which station gets to transmit on a shared broadcast channel and when.

#### Multiple Access Protocols
Protocols that govern how devices share a common transmission medium.
* **ALOHA (Pure/Slotted):** Stations transmit whenever they have data. Collisions occur if transmissions overlap. Pure ALOHA has low throughput; Slotted ALOHA synchronizes transmissions to time slots to improve efficiency.
* **CSMA/CD (Carrier Sense Multiple Access with Collision Detection):** Used in **wired Ethernet (IEEE 802.3)**. Stations listen before transmitting (carrier sense). If a collision is detected, stations stop transmitting and wait a random time before retrying.
* **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance):** Used in **Wireless LANs (IEEE 802.11)**. Stations listen before transmitting. Due to the "hidden node" problem, they cannot reliably detect collisions, so they use mechanisms like **Request to Send (RTS)/Clear to Send (CTS)** and randomized back-off timers to avoid collisions.

### Ethernet (IEEE 802.3)
The dominant wired LAN technology. It specifies the Physical and MAC layers.
* Uses a frame format that includes source and destination **MAC addresses**.
* Originally used the **bus** topology with CSMA/CD, but modern Ethernet uses a **star** topology with switches.

### Wireless LANs – IEEE 802.11
The standard for wireless local area networks (**Wi-Fi**).
* Uses **CSMA/CA** for medium access.
* Defines both **ad-hoc** (peer-to-peer) and **infrastructure** (via Access Points) modes.

### Interconnecting Devices (Layer of Operation)
* **Repeaters (Layer 1):** Regenerate the signal.
* **Hubs (Layer 1):** Multi-port repeaters.
* **Bridges (Layer 2):** Connect two or more LAN segments, filtering frames based on **MAC addresses**. They break up collision domains.
* **Switches (Layer 2):** High-speed, multi-port bridges. They learn MAC addresses and forward frames only to the correct output port, segmenting the network into multiple collision domains.
* **Routers (Layer 3):** Connect different networks (subnets), forwarding packets based on **IP addresses**. They break up broadcast domains.
* **Gateways (Layers 4-7):** A generic term for a device that connects two networks that may be using different protocols, often involving translation at higher layers.

#### Bridges from 802.x to 802.y
Bridges can connect LANs with different physical and MAC protocols (e.g., an Ethernet 802.3 LAN to an 802.11 Wi-Fi LAN). This requires the bridge to perform:
1.  **Frame Format Translation:** Converting the frame structure, including address and checksum fields.
2.  **Addressing Translation:** Mapping addresses between the different standards.
3.  **Maximum Frame Size Handling:** Truncating or fragmenting frames if one standard has a smaller maximum size than the other (though fragmentation at Layer 2 is often avoided, leading to frame discard).

***

## 5. Network Layer (General Concepts)

The **Network Layer (Layer 3)** is responsible for logical addressing (IP addressing) and routing of packets from the source host to the destination host, potentially across multiple networks.

### Design Issues
* **Routing:** Determining the best path for a packet to travel from source to destination.
* **Addressing:** Assigning unique logical addresses (IP addresses) to hosts.
* **Congestion Control:** Managing network traffic to prevent performance collapse.
* **Quality of Service (QoS):** Providing performance guarantees for traffic flow.
* **Inter-networking:** Handling communication between heterogeneous networks.

### Routing Algorithms
Algorithms used by routers to determine the best path.

* **Optimality Principle:** If router J is on the optimal path from router I to router K, then the optimal path from J to K also falls along the same route.
* **Shortest Path Routing (Dijkstra):** Uses an iterative algorithm to find the path with the minimum cost (e.g., minimum hops, time, or distance) between any two nodes in a network.
* **Flooding:** Every incoming packet is sent out on every outgoing line except the one it arrived on. Simple but generates a massive amount of redundant traffic.
* **Distance Vector Routing (e.g., RIP):** Routers share their entire routing table (vector of distances) with their immediate neighbors. They compute the shortest path by adding the neighbor's distance to the destination to the cost of the link to that neighbor. Susceptible to the **Count-to-Infinity** problem.
* **Link State Routing (e.g., OSPF):** Routers broadcast the state of their direct links (link state packets) to **all** other routers in the network. Each router uses the collected link-state information to build a map (graph) of the entire network and computes the shortest path using Dijkstra's algorithm.
* **Multicast Routing:** Finding a tree structure that connects a single source to a group of multiple destinations (multicast group) using the least cost path.
* **Routing for Mobile Hosts:** Handling the challenge of routing packets to a host that is moving across different networks while maintaining its permanent IP address. Involves a **Home Agent** (at the host's permanent network) and a **Foreign Agent** (at the host's current network).

### Congestion Control Algorithms
Techniques to deal with a situation where the load on the network is greater than the capacity, leading to degraded performance.
* **Open Loop:** Policies to prevent congestion before it starts (e.g., admission control, scheduling).
* **Closed Loop:** Mechanisms to remove congestion after it has started (e.g., backpressure, choke packets, or techniques like those used in TCP).

### Quality of Service (QoS)
#### Requirements
Providing performance guarantees for certain traffic types. Key parameters include:
* **Bandwidth:** Guaranteed minimum data rate.
* **Delay (Latency):** Maximum acceptable end-to-end delay.
* **Jitter:** Variation in packet delay.
* **Packet Loss:** Maximum acceptable percentage of lost packets.

#### Techniques to Achieve QoS
* **Traffic Shaping:** Regulating the average rate of data transmission (e.g., Leaky Bucket or Token Bucket algorithms).
* **Admission Control:** A router accepts a new flow only if it can guarantee the required QoS without affecting existing flows.
* **Integrated Services (IntServ):** A per-flow reservation model that uses the **RSVP** protocol for resource reservation. High overhead due to per-flow state.
* **Differentiated Services (DiffServ):** A simpler, scalable model that classifies traffic into a few categories (classes) and applies different per-hop forwarding behaviors based on the class.

***

## 6. Network Layer in the Internet

### IP Protocol – Structure and Working
The **Internet Protocol (IP)** is the primary protocol of the Internet layer. It is a **connectionless** and **unreliable** protocol, meaning it sends packets independently (datagrams) and does not guarantee delivery, ordering, or error-free transmission.
* **Working:** It takes segments from the Transport Layer, adds its header to form an **IP Datagram** (Packet), and uses the destination **IP address** to route it across the network(s) using routing tables.
* **Structure (IPv4 Header):** Contains fields for **Source/Destination IP Addresses**, **Protocol** (identifying the higher layer protocol), **Time to Live (TTL)** (to prevent packets from circulating indefinitely), and **Checksum**.

### IP Addressing – Classes, Subnetting, CIDR
The logical address for a device, enabling it to be uniquely identified globally.
* **Classes (Classful Addressing):** An old system that divided IPv4 addresses into classes (A, B, C, D, E) based on the first few bits, defining fixed-size network and host portions. Largely obsolete.
    * *Class A:* For large networks (Net ID in first octet).
    * *Class B:* For medium networks (Net ID in first two octets).
    * *Class C:* For small networks (Net ID in first three octets).
* **Subnetting:** The process of dividing a large network address space into smaller, distinct sub-networks (subnets) using a **subnet mask**. This improves efficiency and manages traffic flow within an organization.
* **CIDR (Classless Inter-Domain Routing):** The modern, classless addressing scheme. It uses a **prefix length** (e.g., $/24$) to define the network portion of the address, allowing for flexible and efficient allocation of IP addresses, replacing the rigid class system.

### ICMP (Internet Control Message Protocol)
A supporting protocol used by the IP layer to send error messages and operational information, such as:
* **Destination Unreachable:** Sent when a router cannot deliver a packet.
* **Time Exceeded:** Sent when a packet's TTL reaches zero.
* **Echo Request/Reply:** Used by network utilities like **ping** for testing connectivity.

### ARP and RARP
* **ARP (Address Resolution Protocol):** Used to map a known **IP address (Layer 3)** to its corresponding **MAC address (Layer 2)** on the same local network. The device broadcasts an ARP request, and the device with the matching IP address replies with its MAC address.
* **RARP (Reverse Address Resolution Protocol):** Used by a device (e.g., a diskless workstation) to discover its own **IP address** when it only knows its **MAC address**. Largely replaced by BOOTP and DHCP.

### BOOTP and DHCP
Protocols for dynamic host configuration.
* **BOOTP (Bootstrap Protocol):** An older protocol that allowed a diskless workstation to discover its IP address from a server. It required a manually configured static mapping on the server.
* **DHCP (Dynamic Host Configuration Protocol):** The modern standard. It dynamically or statically assigns IP addresses, subnet masks, default gateways, and DNS server addresses to client devices, automating network configuration and enabling IP address reuse.

### OSPF and BGP Routing Protocols
* **OSPF (Open Shortest Path First):** A **Link State** protocol used as an **Interior Gateway Protocol (IGP)** within a single Autonomous System (AS—a large administrative network domain). It uses Dijkstra's algorithm to find the shortest path.
* **BGP (Border Gateway Protocol):** The standard **Exterior Gateway Protocol (EGP)** used to exchange routing information between different Autonomous Systems (the Internet backbone). It is a **Path Vector** protocol, focusing on policy-based routing rather than just the shortest path.

### Internet Multicasting
The delivery of a single packet to a group of hosts simultaneously, rather than to a single host (unicast) or all hosts (broadcast). It is used for applications like streaming media and video conferencing. It involves special multicast IP addresses (Class D).

### IPv6 and ICMPv6
* **IPv6 (Internet Protocol version 6):** The successor to IPv4, designed to solve the address exhaustion problem and improve IP's features.
    * **Addresses:** Uses **128-bit addresses** (vs. 32-bit in IPv4), providing a vastly larger address space.
    * **Header:** Simpler header format for faster processing by routers.
* **ICMPv6 (Internet Control Message Protocol version 6):** The implementation of ICMP for IPv6. It combines the functions of IPv4's ICMP, ARP, and IGMP (multicast). Key functions include **Neighbor Discovery Protocol (NDP)** for address resolution.

***

## 7. Transport Layer

The **Transport Layer (Layer 4)** is responsible for providing communication services (logical communication) between application processes running on different hosts.

### Transport Service – Purpose and Provided Services
* **Purpose:** To provide efficient, reliable, and cost-effective data transmission between peer processes.
* **Services:** Connection establishment/release, multiplexing/demultiplexing (using **port numbers** to direct data to the correct application), flow control, error control, and reliable delivery.

### Transport Service Primitives
The interface between the application layer and the transport layer is defined by a set of service primitives (operations) that applications can use, such as:
* `LISTEN`: A server process indicates it is ready to accept connections.
* `CONNECT`: A client process requests a connection to a server.
* `SEND`/`RECEIVE`: Used to exchange data.
* `DISCONNECT`: Terminate a connection.

### UDP – Characteristics and Use Cases
The **User Datagram Protocol (UDP)** is a **connectionless** and **unreliable** transport protocol.
* **Characteristics:**
    * **Minimal Overhead:** No connection setup/teardown.
    * **Unreliable:** No guarantee of delivery, order, or duplication control.
    * **Fast:** No delay due to retransmissions or flow control.
* **Use Cases:** Applications where speed and minimal delay are prioritized over reliability, and where a few lost packets are tolerable or handled by the application itself (e.g., **DNS** queries, **SNMP**, **VoIP, streaming video/audio**).

### TCP
The **Transmission Control Protocol (TCP)** is a **connection-oriented** and **reliable** transport protocol.

* **Overview:** Provides a virtual connection between two processes. It ensures that all data segments arrive at the receiver, in the correct order, and without duplication.
* **TCP Segment Header:** Contains: **Source/Destination Port Numbers**, **Sequence Number** (for ordering), **Acknowledgment Number** (for reliable transfer), **Window Size** (for flow control), and various **Flags** (e.g., SYN, ACK, FIN).
* **Connection Establishment and Release (3-way Handshake):**
    1.  **SYN (Synchronization):** Client sends a SYN segment with its initial sequence number.
    2.  **SYN-ACK (Synchronization-Acknowledgment):** Server responds with a SYN segment and an ACK for the client's SYN.
    3.  **ACK (Acknowledgment):** Client responds with an ACK, establishing the connection.
* **Connection Management Modeling:** TCP uses a Finite State Machine (FSM) to model the state of a connection (e.g., LISTEN, SYN\_SENT, ESTABLISHED, FIN\_WAIT).
* **Retransmission Policies:** TCP uses a **timeout** mechanism. If a segment is sent and no ACK is received before the timeout, the segment is **retransmitted**. The timeout value is dynamically calculated based on the Round Trip Time (RTT).
* **Congestion Control:** Algorithms to prevent network collapse and ensure fair sharing of bandwidth.
    * **Slow Start:** The sender starts with a small **Congestion Window (CWND)** and increases it exponentially (doubling) for every received ACK until a threshold is reached.
    * **Congestion Avoidance:** After the threshold, the CWND increases linearly (by 1 MSS per RTT) to probe for available bandwidth.
    * **Fast Retransmit/Fast Recovery:** Algorithms to quickly recover from packet loss signaled by **Duplicate ACKs**.

***

## 8. Application Layer

The **Application Layer (Layer 7)** is the topmost layer, providing the interface and protocols that allow user applications to interact with the network.

### FTP (File Transfer Protocol)
A standard protocol for transferring files between a client and a server.
* **Feature:** It uses **two separate connections**:
    1.  **Control Connection (Port 21):** For commands and responses (e.g., username, password, file name).
    2.  **Data Connection (Port 20 or an ephemeral port):** For the actual file transfer.

### DNS (Domain Name System)
The decentralized naming system for computers, services, or any resource connected to the Internet.
* **Purpose:** To translate human-readable domain names (e.g., `www.example.com`) into numerical **IP addresses** (e.g., `192.0.2.1`) and vice-versa.
* **Working:** Uses a hierarchical, distributed database queried primarily via **UDP**.

### Email Protocols – SMTP, POP3, IMAP
* **SMTP (Simple Mail Transfer Protocol):** Used to **send** email from a mail client to a mail server and between mail servers.
* **POP3 (Post Office Protocol version 3):** Used by a mail client to **retrieve** email from a mail server. Typically, it **downloads and deletes** the email from the server.
* **IMAP (Internet Message Access Protocol):** Used by a mail client to **retrieve** email. It allows users to **manage and access** their mail directly on the server, keeping the mail on the server.

### MIME (Multipurpose Internet Mail Extensions)
An Internet standard that extends the format of email to support:
* Text in character sets other than ASCII.
* Non-text attachments (audio, video, images, application programs).
* Message bodies with multiple parts.

### SNMP (Simple Network Management Protocol)
A protocol for managing devices on an IP network.
* It allows network administrators to monitor network performance, find and solve network problems, and manage configurations.
* It uses a **Manager** (runs the monitoring software) and **Agents** (software running on managed devices) and a **Management Information Base (MIB)** (a hierarchical database of objects that can be managed).

### WWW – Architecture and Operation
The **World Wide Web (WWW)** is a distributed client-server application built on top of the Internet.
* **Architecture:**
    * **Client (Browser):** Requests and renders content (Web pages).
    * **Server (Web Server):** Stores and serves content (e.g., files, images).
    * **Protocol (HTTP/HTTPS):** The protocol used for communication.
* **Operation (HTTP Transaction):**
    1.  **DNS Lookup:** The client (browser) uses DNS to find the IP address of the Web server.
    2.  **TCP Connection:** The client establishes a TCP connection to the server on Port 80 (HTTP) or 443 (HTTPS).
    3.  **HTTP Request:** The client sends an HTTP request message (e.g., a GET command) to the server.
    4.  **HTTP Response:** The server sends an HTTP response message containing the requested resource (e.g., an HTML file).
    5.  **Connection Close (or persistent connection):** The TCP connection may be closed or kept open for subsequent requests.
    6.  **Rendering:** The client renders the content for the user.