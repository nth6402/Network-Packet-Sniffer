# Network Packet Sniffer & Traffic Analyzer

## Overview
This is a Python-based command-line tool designed to capture and analyze live network traffic. It fulfills the requirements for analyzing packet details based on Traffic Analysis concepts (Topic 3). 

## Features
This tool captures network packets and displays the following information for each packet:
- Type: The protocol used (e.g., TCP, UDP).
- Size: The total size of the packet in bytes.
- Origin: The Source IP address.
- Destination: The Destination IP address.
- Content: The payload data (displays the first 40 bytes if the data is unencrypted).

## Tools & Libraries Used
- Python 3
- Scapy: A powerful Python library used for packet manipulation and network scanning.
- Datetime: Used to log the exact time each packet was captured.

## How to Run
1. Install the required library: pip install scapy
2. Run the script (Note: It requires Administrator/Root privileges to capture network traffic): python packet_sniffer.py
3. The script is configured to capture 15 packets. You can browse the internet to generate traffic. Press Ctrl + C to stop early.

## Purpose
This project demonstrates practical knowledge of network protocols and how data flows through the network layer, which is essential for cybersecurity and network defense.
