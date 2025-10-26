
# VIVA Questions - Computer Networks



## 1. What is the fundamental goal of a Computer Network?
The fundamental goal is to allow interconnected devices to share resources (like printers and files) and enable reliable, efficient communication among users and applications.

## 2. Differentiate between Network Hardware and Network Software.
**Hardware** includes the physical devices (routers, switches, NICs, cables), while **Software** comprises the organizational rules (**protocol stacks** like TCP/IP), operating systems, and user applications that utilize the network.

## 3. Explain the purpose of the Session Layer (L5) in the OSI Model.
It is responsible for establishing, managing, and terminating communication sessions (connections) between applications, and can also provide synchronization points for long data transfers.

## 4. How does a Switch differ from a Router?
A **Switch** is a Layer 2 (Data Link) device that forwards data (frames) based on **MAC addresses** within a single network (LAN). A **Router** is a Layer 3 (Network) device that forwards data (packets) based on **IP addresses** between different networks (subnets).

## 5. What is the significance of the Time to Live (TTL) field in an IP packet?
TTL is a counter that prevents packets from looping endlessly in the network. Each router decrements the TTL; if it reaches zero, the packet is discarded, and an ICMP error message is sent to the source.

## 6. Define the two primary modes of operation for a Wireless LAN (IEEE 802.11).
The two modes are **Infrastructure mode** (devices communicate through a central Access Point) and **Ad-hoc mode** (devices communicate directly, peer-to-peer).

## 7. What is the main characteristic that distinguishes **UDP** from **TCP**?
**UDP (User Datagram Protocol)** is a **connectionless** and **unreliable** protocol, prioritizing speed and low overhead. **TCP (Transmission Control Protocol)** is **connection-oriented** and **reliable**, ensuring ordered delivery and error checking.

## 8. Why is **CSMA/CA** used in Wi-Fi (802.11) instead of CSMA/CD?
Due to the **hidden node problem** in wireless environments, stations cannot reliably detect collisions while transmitting. Therefore, CSMA/CA uses techniques (like RTS/CTS and back-off timers) to **avoid** collisions before transmission.

## 9. How does the **CRC (Cyclic Redundancy Check)** error detection mechanism work?
The sender calculates a checksum based on polynomial division and appends it to the data. The receiver performs the same calculation; a zero remainder indicates that the data is error-free.

## 10. Explain the concept of **Encapsulation** in networking.
It is the process where a higher layer's data unit is wrapped by a lower layer with its own control information (**header**, and sometimes a trailer) as the data moves down the protocol stack toward the physical medium.

## 11. What is the most common device used to interconnect networks in a Star Topology, and at which layer does it operate?
A **Switch**, which operates at the **Data Link Layer (L2)**.

## 12. Differentiate between a **PAN** and a **LAN**.
A **PAN (Personal Area Network)** covers a very small range around a single person (e.g., Bluetooth devices). A **LAN (Local Area Network)** covers a localized area like a home or office building.

## 13. What problem does **ARP (Address Resolution Protocol)** solve?
ARP translates a known **Layer 3 (IP) address** into its corresponding **Layer 2 (MAC) address** on the same local network segment.

## 14. What is **CIDR** and why was it introduced?
**Classless Inter-Domain Routing** replaces the classful addressing system (A, B, C) by using a **prefix length** (e.g., /24). It was introduced to improve the efficiency of IP address allocation and reduce the size of Internet routing tables.

## 15. Describe the mechanism of the **TCP 3-way Handshake**.
It is the process to establish a connection: 1. **SYN** (Client sends request). 2. **SYN-ACK** (Server acknowledges and replies with its own request). 3. **ACK** (Client acknowledges the server's request).

## 16. Give an example of a protocol used at the **Application Layer (L7)**.
**HTTP** (Hypertext Transfer Protocol), **FTP** (File Transfer Protocol), **DNS** (Domain Name System), or **SMTP** (Simple Mail Transfer Protocol).

## 17. How does a **Fiber Optic** cable transmit data?
It transmits data by sending pulses of **light** through thin strands of glass or plastic, offering high bandwidth and immunity to electromagnetic interference.

## 18. What is the difference between **Bandwidth** and **Throughput**?
**Bandwidth** is the theoretical maximum data transfer rate of a medium (e.g., 100 Mbps). **Throughput** is the actual amount of data successfully transferred over a link in a given time, always less than or equal to the bandwidth.

## 19. What is the function of the **ACK number** field in the TCP segment header?
It indicates the **sequence number of the next byte** the sender is expecting to receive, ensuring reliable delivery.

## 20. What is **Flooding** in routing, and what is its main drawback?
Flooding is a non-adaptive routing technique where every incoming packet is sent out on every outgoing link except the one it arrived on. Its main drawback is the **massive generation of redundant traffic**.

## 21. Which error correction code can both detect and correct single-bit errors?
The **Hamming Code**.

## 22. Explain the **optimality principle** in routing.
It states that if router J is on the optimal path from router I to router K, then the optimal path from J to K must also be along that same route segment.

## 23. What is the primary use of **ICMP (Internet Control Message Protocol)**?
ICMP is a supporting protocol for IP, used primarily for **error reporting** (e.g., Destination Unreachable) and network diagnostics (e.g., **ping** using Echo Request/Reply).

## 24. How does the **Go-Back-N** sliding window protocol handle a lost frame?
When a frame is lost, the receiver discards it and all subsequent frames. The sender, upon timeout, retransmits the lost frame **and all subsequent frames** that were sent after it.

## 25. What is the role of the **Presentation Layer (L6)**?
It manages data format, syntax, and semantics, including translation, **encryption/decryption**, and compression/decompression.

## 26. Which routing protocol is known as a **Path Vector** protocol and is used between Autonomous Systems (AS)?
**BGP (Border Gateway Protocol)**, the main routing protocol of the Internet.

## 27. How does a **Subnet Mask** work?
It's a 32-bit number used to logically divide an IP address into the **Network ID** portion (where mask bits are 1) and the **Host ID** portion (where mask bits are 0).

## 28. What is the function of **DNS (Domain Name System)**?
DNS translates human-readable **domain names** (like [www.google.com](https://www.google.com)) into numerical **IP addresses** needed for routing.

## 29. What is **digital-to-analog** signal encoding used for?
It is used to convert digital data (bits) into an analog signal for transmission over analog media, such as the public telephone network (performed by a modem).

## 30. How do **hubs** and **repeaters** differ from a switch?
Hubs and repeaters operate at the **Physical Layer (L1)**, simply regenerating and broadcasting signals, creating a single collision domain. A switch operates at **L2**, filtering frames and breaking up collision domains.

## 31. What are the two types of **Transmission Media** classification?
**Guided** (wired, e.g., fiber optics) and **Unguided** (wireless, e.g., radio waves).

## 32. Define **Latency** and **Queuing Time**.
**Latency** is the total time for a packet to travel from source to destination. **Queuing Time** is the portion of latency a packet spends waiting in a buffer at a network device before being processed or transmitted.

## 33. What is the role of the **FIN** flag in a TCP segment?
The **FIN (Finish)** flag is set to signal a graceful **connection release** request from one end of the TCP connection.

## 34. What is the key advantage of **Selective Repeat** over **Go-Back-N**?
Selective Repeat maximizes efficiency by retransmitting **only the frame that was lost or corrupted**, thereby minimizing unnecessary retransmissions and improving throughput.

## 35. Explain the importance of **Port Numbers** at the Transport Layer.
Port numbers enable **multiplexing** (multiple applications sharing a connection) and **demultiplexing** (directing incoming data to the correct application process) on a single host.

## 36. Give an example of a real-time application where **UDP** is preferred, and why.
**VoIP (Voice over IP)**. Losing a few voice packets is better than retransmitting them, which would introduce unacceptable delay (latency and jitter) caused by TCP's reliability mechanisms.

## 37. What is **MIME** and its significance for email?
**Multipurpose Internet Mail Extensions** is a standard that extends email format to support non-ASCII characters and **multimedia attachments** (images, video, etc.).

## 38. How does **IP Multicasting** differ from Broadcasting?
**Broadcasting** sends a packet to **all** hosts on a local network. **Multicasting** sends a single packet to a specific, defined **group of interested hosts**.

## 39. What are the three essential components in the **SNMP (Simple Network Management Protocol)** architecture?
**Manager**, **Agent** (on the managed device), and the **Management Information Base (MIB)**.

## 40. What is the main drawback of using **Flooding** as a routing algorithm?
It generates an excessive number of duplicate packets, which can lead to severe network congestion and broadcast storms.

## 41. How does **TCP's Slow Start** algorithm work?
The sender starts with a small **Congestion Window (CWND)** and increases it **exponentially** for every RTT where an acknowledgment is received, rapidly probing for available network capacity.

## 42. Name the three modes of communication flow.
**Simplex**, **Half-Duplex**, and **Full-Duplex**.

## 43. What is a key function of the **Logical Link Control (LLC)** sublayer in IEEE 802?
LLC handles the interface between the Data Link Layer and the Network Layer, providing connection services and error/flow control for higher layer protocols.

## 44. What is **Jitter** in the context of QoS?
Jitter is the **variation or fluctuation in packet delay (latency)** over time. It severely degrades the quality of real-time applications.

## 45. Explain the purpose of **BOOTP** and why it was largely replaced.
**Bootstrap Protocol** allowed a host to obtain its IP address and boot information from a server. It was replaced by **DHCP** because BOOTP lacked the ability to dynamically manage address allocation and reuse.

## 46. What is the final PDU created by the Data Link Layer?
A **Frame**.

## 47. What is the main reason for the complexity of **Routing for Mobile Hosts**?
The challenge of routing packets to a host that is constantly changing its location (network) while retaining its single, permanent **Home IP Address**.

## 48. Give two examples of **Network Layer Design Issues**.
**Routing**, **Addressing**, **Congestion Control**, or **Quality of Service (QoS)**.

## 49. How is a **Ring Topology** structured?
Devices are connected point-to-point in a closed loop (a ring). Data typically flows in a single direction around the ring.

## 50. Why is **CSMA/CD** suitable for a wired environment like Ethernet?
In a wired medium, a station can reliably detect a collision by monitoring the signal strength or voltage level during its transmission, allowing it to quickly stop and retransmit.

## 51. What is the role of the **Protocol** field in the IPv4 header?
It identifies the **higher layer protocol** (e.g., TCP or UDP) to which the IP packet payload should be passed at the destination host.

## 52. Differentiate between a **Hub** and a **Repeater**.
A **Repeater** typically has only two ports to regenerate a signal between two cable segments. A **Hub** is essentially a **multi-port repeater**, connecting multiple devices.

## 53. What is the role of the **Home Agent** in mobile host routing?
The Home Agent is a router on the mobile host's permanent network that intercepts packets addressed to the host's permanent IP and tunnels them to the host's current location (Foreign Agent).

## 54. Which routing protocol uses **Dijkstra's Shortest Path Algorithm**?
**OSPF (Open Shortest Path First)**, which is a Link State routing protocol.

## 55. What is the primary difference in addressing between **IPv4** and **IPv6**?
**IPv4** uses **32-bit addresses**, while **IPv6** uses **128-bit addresses**.

## 56. What are the two types of connections used by **FTP (File Transfer Protocol)**?
The **Control Connection** (Port 21, for commands) and the **Data Connection** (often Port 20, for file content).

## 57. What is the core function of the **DNS** protocol?
To resolve (translate) domain names into their corresponding numerical **IP addresses**.

## 58. How does **TCP Congestion Avoidance** differ from Slow Start in increasing the CWND?
In Congestion Avoidance, the CWND is increased **linearly** (by 1 MSS per RTT), whereas in Slow Start, it is increased **exponentially**.

## 59. What is the meaning of the term **"connection-oriented"** in the context of TCP?
It means a virtual session must be established (3-way handshake) and explicitly terminated, guaranteeing reliable and ordered data delivery throughout the session.

## 60. Name an obsolete protocol that was used to map MAC addresses to IP addresses.
**RARP (Reverse Address Resolution Protocol)**.

## 61. What is the purpose of **Traffic Shaping** in QoS?
Traffic Shaping is used to control the rate and burstiness of data traffic transmitted over a network, ensuring the traffic complies with a specified contract or limit.

## 62. Which layer in the OSI model is responsible for **framing**?
The **Data Link Layer (L2)**.

## 63. Give two examples of applications that typically use **UDP**.
**DNS** queries, **VoIP**, **Streaming Video/Audio**, or **SNMP**.

## 64. What is the function of **Hamming Codes** in error control?
They are used for **Forward Error Correction (FEC)**, meaning they can detect and correct single-bit errors without requiring retransmission.

## 65. What does the **Bandwidth–Delay Product** represent?
It represents the maximum amount of data (in bits) that can be **in transit** or "in the pipe" on the link at any given time.

## 66. What is the main drawback of the **Distance Vector Routing** algorithm?
It is susceptible to the **Count-to-Infinity** problem when network failures occur, leading to routing loops and slow convergence.

## 67. How do **POP3** and **IMAP** differ in email retrieval?
**POP3** generally downloads the email to the client and optionally deletes it from the server. **IMAP** allows the user to manage and retain the email on the server, facilitating access from multiple devices.

## 68. Name the two sublayers of the Data Link Layer (IEEE 802).
The **Logical Link Control (LLC)** sublayer and the **Media Access Control (MAC)** sublayer.

## 69. What is **digital-to-digital** signal encoding?
It is the process of converting digital data (bits) into a digital signal (pulses), such as **Manchester encoding** used in classic Ethernet.

## 70. What are **Transport Service Primitives**?
They are the set of operations (like LISTEN, CONNECT, SEND, RECEIVE) that the application layer uses to interact with the Transport Layer service.

## 71. What is the significance of a **Star Topology** in modern LANs?
Its key advantage is **centralized management** and **fault isolation**; the failure of a single link or host does not affect the rest of the network.

## 72. Which transport protocol is known for its **minimal overhead**?
**UDP (User Datagram Protocol)**.

## 73. Why is **IPv6** necessary despite the use of CIDR for IPv4?
Even with CIDR, the 32-bit address space of IPv4 is fundamentally limited and has been exhausted. IPv6's 128-bit address space provides a vast, non-depleting pool of addresses.

## 74. What is the role of **Admission Control** in achieving QoS?
It prevents network congestion by checking if a requested new connection can be accommodated while still satisfying the guaranteed performance requirements of existing connections.

## 75. How does a **bridge** handle traffic filtering?
A bridge inspects the destination **MAC address** in the frame and checks its forwarding table. If the destination is on the same segment as the source, it **filters** (drops) the frame; otherwise, it **forwards** it.

## 76. What is the purpose of the **Time-out** mechanism in TCP retransmission policy?
It is a timer started when a segment is sent. If an acknowledgment (ACK) for that segment is not received before the timer expires, TCP assumes the segment was lost and triggers a retransmission.

## 77. What are the two types of **Transmission Media** used in a hybrid network?
Both **Guided** (e.g., Ethernet cables) and **Unguided** (e.g., Wi-Fi radio waves) media are typically used.

## 78. What is the relationship between **Throughput** and **Bandwidth**?
Throughput is the actual measure of data transfer rate, and it is always **less than or equal to** the maximum theoretical rate (Bandwidth).

## 79. What is the function of **ARP**?
ARP broadcasts a request on the local network asking, "Who has this IP address?" The device with that IP address replies with its MAC address.

## 80. How is a **WAN (Wide Area Network)** typically structured?
A WAN connects multiple LANs or MANs across a large geographic area (e.g., countries or continents), often using high-capacity links provided by telecommunication companies.

## 81. Explain the role of **RARP** and its current replacement.
RARP allowed a device to learn its own **IP address** using a known **MAC address**. It has been replaced by **DHCP** (Dynamic Host Configuration Protocol).

## 82. Which two OSI layers are combined to form the **Network Access Layer** in the TCP/IP model?
The **Data Link Layer (L2)** and the **Physical Layer (L1)**.

## 83. What is the main drawback of a **Mesh Topology**?
Its complexity and cost, as a full mesh requires $N(N-1)/2$ connections for $N$ nodes.

## 84. What is the main design issue that **HDLC** addresses?
**Framing**, **Flow Control**, and **Error Control** over a serial link.

## 85. What are two techniques used to achieve **QoS**?
**Traffic Shaping** (regulating data rate) and **Admission Control** (reserving resources).

## 86. How does **TCP Congestion Control** utilize the **Congestion Avoidance** phase?
Once the network load is determined (e.g., after the Slow Start threshold), the CWND is increased linearly to avoid overwhelming the network while gradually testing for higher capacity.

## 87. What is the function of **DHCP**?
DHCP dynamically assigns IP addresses and other network configuration parameters (subnet mask, gateway, DNS server) to client devices, automating network setup.

## 88. Differentiate between a **Link State** protocol (like OSPF) and a **Distance Vector** protocol (like RIP).
Link State protocols provide every router with a **full topological map** of the network, whereas Distance Vector protocols rely on routers exchanging **distance summaries** only with their immediate neighbors.

## 89. Why is the **Presentation Layer** often omitted or merged in practical protocol stacks?
Its functions (like formatting, compression, and encryption) are often integrated into the **Application Layer** (as seen with HTTP using MIME or TLS/SSL) or delegated to application-specific libraries.

## 90. Give an example of a protocol that requires a dedicated RARP server.
**RARP** (Reverse Address Resolution Protocol) itself requires a dedicated server to store the MAC-to-IP mappings.

## 91. What are the two types of encoding used to convert an analog signal to a digital signal?
**Pulse Code Modulation (PCM)** and **Delta Modulation (DM)**.

## 92. What is the **Protocol Data Unit (PDU)** at the Network Layer?
A **Packet** (or Datagram).

## 93. How does **Hamming Code** enable error correction?
It adds sufficient redundancy (extra parity bits) such that the position of a single-bit error can be uniquely identified and flipped back to the correct value.

## 94. What is the purpose of the **SYN** flag in a TCP segment?
The **SYN (Synchronization)** flag is set during the 3-way handshake to indicate a request to establish a connection and to carry the **Initial Sequence Number (ISN)**.

## 95. What is **WWW** and what is its core operating protocol?
The **World Wide Web** is a global, distributed client-server information system. Its core operating protocol is **HTTP (Hypertext Transfer Protocol)**.

## 96. What is the primary role of a **Gateway** device?
A Gateway is a general term for a device that connects two networks that may be using **different protocols**, often involving translation or protocol conversion at higher layers (L4-L7).

## 97. Differentiate between **Multicast** and **Unicast** communication.
**Unicast** is a one-to-one transmission (a single source sends to a single destination). **Multicast** is a one-to-many transmission (a single source sends to a group of interested destinations).

## 98. What are the steps involved in the Application Layer's interaction with the Transport Layer?
The Application Layer uses **Transport Service Primitives** (e.g., CONNECT, SEND) to request services from the Transport Layer, passing data as a stream or message.

## 99. Why is it important for the TCP retransmission timeout (RTO) value to be dynamic?
Because the **Round Trip Time (RTT)**, or the time it takes for a segment to travel and for its ACK to return, varies greatly on the Internet. A dynamic RTO ensures efficient retransmissions that adapt to changing network latency.

## 100. How does the **OSI Model** help in troubleshooting network problems?
It allows network professionals to isolate a problem to a specific layer. By checking the functionality of each layer from L1 upwards, the scope of the problem is narrowed, simplifying diagnosis (e.g., if ARP fails, the problem is likely at L2/L3).