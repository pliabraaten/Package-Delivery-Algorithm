# Package Delivery Routing Program

## Introduction

This project implements an efficient package delivery routing system that meets all delivery deadlines while minimizing total travel distance. The program manages delivery routes for three trucks handling 40 packages with various constraints, such as package delivery deadlines and delays (e.g., packages that arrive late at the hub).

The goal is to ensure all packages are delivered before their deadlines and have a user interface to query the delivery progress for any specified time.

## Scenario

A local delivery service needs to optimize daily deliveries across three trucks and two drivers. Each package has unique delivery requirements, including deadlines and special conditions. The service must deliver all packages while keeping total mileage under 140 miles.

The program supports:
- Routing trucks with package constraints
- Managing package statuses (At the hub, En route, Delivered, Delayed)
- Handling delayed packages and address corrections
- Providing user queries for package status at any given time

## Assumptions

- Each truck can carry a maximum of 16 packages; package IDs are unique.
- Trucks travel at an average speed of 18 mph with unlimited fuel.
- No collisions occur.
- Three trucks and two drivers are available; drivers remain assigned to their trucks.
- Drivers leave the hub no earlier than 8:00 a.m. with loaded trucks and may return to the hub as needed.
- Delivery and loading times are considered instantaneous and factored into average speed.
- The delivery address for package #9 is incorrect and is updated at 10:20 a.m.
- Distances between locations are symmetric regardless of travel direction.
- The delivery day ends when all 40 packages are delivered.

## Features

- Custom hash table implementation for efficient package lookup and storage.
- Nearest Neighbor algorithm to optimize routes and meet deadlines.
- Real-time status tracking for packages (including delayed and corrected addresses).
- Command-line interface for querying package status at any time.
- Reports total mileage for all trucks combined.

## How to Use

1. Clone the repository.
2. Run the main program to launch the command-line interface.
3. Enter options to:
    - View total mileage after deliveries
    - Query all packages at a specific time
    - Look up individual packages and their delivery statuses
4. Input times in `HHMM` format to see package status snapshots.

## Algorithms & Data Structures

- Uses a custom-built hash table for package data storage and retrieval.
- Implements a nearest neighbor heuristic for routing truck deliveries.
- Ensures all delivery constraints are met within the mileage limit.

## Possible Improvements

- Explore alternative routing algorithms like Dijkstra’s or A* for potentially improved efficiency.
- Extend to support multiple cities or dynamic package updates during the day.
- Expand logic for address corrections.
- Implement a graphical user interface for enhanced usability.

---
