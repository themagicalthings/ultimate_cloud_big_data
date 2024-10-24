import argparse

def read_numbers(file_path):
    """READING numbers from a file """
    try:
        with open(file_path, 'r') as file:
            numbers = file.readline()
            numbers = [int(num.strip()) for num in numbers]
            return sum(numbers)
        
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return none 
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="sum num from a datasets file.")
        parser.add_argument('dataset_path', type=str, help= 'path to the dataset ')

        args = parser.parse_args()

        dataset_file = f"{args.dataset_path}/numbers.txt"
        result = read_numbers(dataset_file)

        if result is not none:
            print(f" Hey, Sum of num is :{result}")
        else:
            print("no result could can be calculated")
