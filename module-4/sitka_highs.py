import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

# Function to read data from CSV file
def read_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high temperatures, and low temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            lows.append(int(row[6]))  # Assuming low temperatures are in column 6 (index 5)
            highs.append(high)
    return dates, highs, lows

# Function to plot high temperatures
def plot_highs(dates, highs):
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Function to plot low temperatures
def plot_lows(dates, lows):
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Main function to handle the menu and program loop
def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_data(filename)

    while True:
        print("\nMenu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")
        choice = input("Please select an option (1, 2, 3): ")

        if choice == '1':
            plot_highs(dates, highs)
        elif choice == '2':
            plot_lows(dates, lows)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit()  # Exit the program
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()