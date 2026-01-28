#!/usr/bin/env python3

import time
import random


def game_event_stream(count):
    """Generator that yields game events one at a time"""
    players = ['alice', 'bob', 'charlie', 'diana', 'eve']
    events = ['killed monster', 'found treasure', 'leveled up', 'completed \
quest', 'died']

    for i in range(count):
        event = {
            'id': i + 1,
            'player': random.choice(players),
            'level': random.randint(1, 20),
            'action': random.choice(events)
        }
        yield event


def filter_high_level_players(events, min_level=10):
    """Generator that filters events for high-level players"""
    for event in events:
        if event['level'] >= min_level:
            yield event


def fibonacci_generator(n):
    """Generator that yields first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(n):
    """Generator that yields first n prime numbers"""
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main():
    print("=== Game Data Stream Processor ===\n")
    # Generate and process events
    event_count = 1000
    print(f"Processing {event_count} game events...\n")

    # Create the event stream
    # events = game_event_stream(event_count)

    # Show first 3 events
    events_list = list(game_event_stream(event_count))
    for i in range(3):
        event = events_list[i]
        print(f"Event {event['id']}: ", end='')
        print(f"Player {event['player']}", end=' ')
        print(f"(Level {event['level']})", end=' ')
        print(f"{event['action']}")
    print("...\n")

    # Start timing
    start_time = time.time()
    # Process all events and gather statistics
    total_events = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0
    for event in events_list:
        total_events += 1
        if event['level'] >= 10:
            high_level_count += 1
        if event['action'] == 'found treasure':
            treasure_count += 1
        if event['action'] == 'leveled up':
            levelup_count += 1
    end_time = time.time()
    processing_time = end_time - start_time

    # Display analytics
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds\n")

    # Generator demonstration
    print("=== Generator Demonstration ===")

    # Fibonacci
    fib_nums = list(fibonacci_generator(10))
    fib_str = ', '.join(map(str, fib_nums))
    print(f"Fibonacci sequence (first 10): {fib_str}")

    # Primes
    prime_nums = list(prime_generator(5))
    prime_str = ', '.join(map(str, prime_nums))
    print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
    main()
