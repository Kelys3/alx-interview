#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys

# Initialize variables to store metrics
total_size = 0
status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}
line_counter = 0

try:
    for line in sys.stdin:
        # Split the line by spaces
        parts = line.split()
        if len(parts) != 7:
            continue  # Skip lines that don't match the expected format

        # Extract relevant information
        status_code = parts[5]
        file_size = int(parts[6])

        # Update metric
        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Increment line counter
        line_counter += 1

        # Check if it's time to print statistics
        if line_counter == 10:
            print("Total file size: File size:", total_size)
            for code, count in sorted(status_counts.items(),
                                      key=lambda x: int(x[0])):
                if count > 0:
                    print(f"{code}: {count}")
            print()  # Add a newline for readability
            line_counter = 0  # Reset line counter

except KeyboardInterrupt:
    # Handle keyboard interruption (Ctrl+C)
    print("Total file size: File size:", total_size)
    for code, count in sorted(status_counts.items(), key=lambda x: int(x[0])):
        if count > 0:
            print(f"{code}: {count}")
    sys.exit(0)  # Exit gracefully

finally:
    # Print final statistics
    print("Total file size: File size:", total_size)
    for code, count in sorted(status_counts.items(), key=lambda x: int(x[0])):
        if count > 0:
            print(f"{code}: {count}")
