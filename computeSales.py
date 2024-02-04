"""
Program created to read a file that is assumed to contain words
"""
# filename: print_numbers.py
import sys
import time

class ConversionArray(list):
    """
    Custom class which extends list and does required computation of it's elements
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._word_frequency_dict = None

    def calculate_word_frequency(self):
        """
        Method used to calculate the word frequency dictionary of the elements that the class
        contains
        """
        word_freq = {}

        for string in self:
            # Split the string into words
            words = string.split()

            for word in words:
                # Remove punctuation and convert to lowercase
                word = word.strip('.,!?').lower()

                # Increment the frequency count in the dictionary
                word_freq[word] = word_freq.get(word, 0) + 1

        self._word_frequency_dict = word_freq

    def get_word_frequency_dict(self):
        """
        Method used to get the word frequency dictionary of the class
        """
        return self._word_frequency_dict

    def __str__(self):
        result_string = "Row Labels	Count\n"
        word_frequency_dict = self.get_word_frequency_dict()

        for key, value in word_frequency_dict.items():
            result_string += f"{key}: {value}\n"

        total_sum = sum(word_frequency_dict.values())
        result_string += f"Grand Total {total_sum}"

        # Remove the trailing comma and space
        return result_string.rstrip(", ")

def print_numbers(file_path):
    """
    Method to print the numbers that the file contains
    """
    try:
        start_time = time.time()
        with open(file_path, 'r', encoding="utf-8") as file:
            # Read the numbers from the file and convert them to a list
            numbers = []
            for index, line in enumerate(file):
                try:
                    numbers.append(line.strip())
                except ValueError:
                    print(f"Error: File contains non-numeric values in line {index+1}")

            custom_array = ConversionArray(numbers)
            custom_array.calculate_word_frequency()
            end_time = time.time()
            elapsed_time_ms = (end_time - start_time) * 1000

            print(custom_array)
            print("\n")
            execution_time_result = f"Time of execution: {elapsed_time_ms:.6f} milliseconds"
            print(execution_time_result)
            with open("WordCountResults.txt", "w", encoding="utf-8") as file:
                # Print the object to the file using the print function
                print(custom_array, file=file)
                print("\n", file=file)
                print(execution_time_result, file=file)


    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    # Check if a file path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py P1/TC2.txt")
        sys.exit(1)

    # Get the file path from the command line argument
    path_to_file = sys.argv[1]

    # Print the numbers from the file
    print_numbers(path_to_file)
