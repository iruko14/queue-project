import csv
import random

def get_queue():

    # Read csv file
    with open('Passengers.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        passengers = list(reader)

    # Generate queue structure
    queue = []
    for passenger in passengers:
        random.shuffle(passenger)
        queue.append(passenger)

    # Iterate the queue and assign the passengers to busses
    bus_count = 1
    while bus_count < 29:
        bus = []
        for i in range(35):
            bus.append(queue.pop(0))
        print(f"Bus {bus_count}: {bus}")
        bus_count += 1

    # Print the remaing passengers list
    print(f"Remaining passengers: {queue}")