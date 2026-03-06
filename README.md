# Network Socket Programming and Packet Analysis

This project implements simple client–server communication using Python sockets.
Both **TCP** and **UDP** protocols are implemented to demonstrate the difference between connection-oriented and connectionless communication. Network traffic is also inspected using Wireshark to observe the behavior of both protocols.

## Overview

The project contains two main parts:

* **TCP client and server**

  * A multi-threaded server that handles multiple clients.
  * Messages are sent with a small header specifying their length.
  * The server processes the message and returns a response.

* **UDP client and server**

  * A connectionless implementation using datagrams.
  * Messages are sent directly without establishing a connection.

Traffic from both implementations is captured using Wireshark on the loopback interface to analyze packet behavior.

## Message Processing

The server processes messages depending on the first character:

| Prefix | Behavior                         |
| ------ | -------------------------------- |
| A      | Sort letters in descending order |
| C      | Sort letters in ascending order  |
| D      | Convert message to uppercase     |
| Other  | Return modified message          |

Example

Input

```
Ahello123
```

Output

```
ollhe
```

## Project Structure

```
.
├── tcp_server.py
├── tcp_client.py
├── udp_server.py
├── udp_client.py
├── Echo_Server_Report.pdf
└── README.md
```

## Running the Project

Start the TCP server:

```
python tcp_server.py
```

Run the TCP client in another terminal:

```
python tcp_client.py
```

For UDP communication:

```
python udp_server.py
```

```
python udp_client.py
```

## Packet Analysis

Network traffic was captured using Wireshark to observe:

* TCP three-way handshake
* TCP data exchange
* UDP datagram transmission

These captures highlight the reliability mechanisms of TCP compared to the lightweight nature of UDP.
