# def read_input is Reading input data from a file.
# Input:
#   - file_name (str): Name of the input file.
#
# Returns:
#   - products      (list): List of product names.
#   - staging_times (list): List of staging times for each product.
#   - photo_times   (list): List of photo times for each product.
def read_input(file_path):
    # Function to read input from a file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Extracting product names
        
        products = lines[0].strip().split(': ')[1].split(' / ')
        
        # Extracting staging times as a list of integers
        staging_times = list(map(int, lines[1].strip().split(': ')[1].split(' / ')))
        
        # Extracting photo times as a list of integers
        photo_times = list(map(int, lines[2].strip().split(': ')[1].split(' / ')))

    return products, staging_times, photo_times

#def write_output writes the scheduling output to a outputPS10.txt file.
#Inputs:
#   - product_sequence (list): Sequence of products scheduled for photography.
#   - total_time        (int): Total time required to complete the photoshoot.
#   - idle_time         (int): Idle time available for Gopal.
def write_output(product_sequence, total_time, idle_time):
    #defining output file
    output_file = "outputPS10.txt"
    
    # Function to write output to a file
    with open(output_file, 'w') as file:  
        # Writing product sequence to the file
        file.write(f"Product Sequence: {', '.join(product_sequence)}\n")

        # Writing total time to complete photoshoot to the file
        file.write(f"Total time to complete photoshoot: {total_time} minutes\n")

        # Writing idle time for Gopal to the file
        file.write(f"Idle time for Gopal: {idle_time} minutes\n")

# greedy_algorithm is Greedy scheduling algorithm to determine the sequence of products to be photographed.
# Inputs:
#   - products      (list): List of product names.
#   - staging_times (list): List of staging times for each product.
#   - photo_times   (list): List of photo times for each product.
#
# Returns:
#   - products  (list): Product Sequence.
#   - total_time (int): Total time required to complete the photoshoot.
#   - idle_time  (int): Idle time available for Gopal.
def greedy_algorithm(products, staging_times, photo_times):
    
    # Function implementing the greedy algorithm to schedule the photoshoot
    n = len(products)
    
    if(n==1):
        # If there is only one product, return its details
        return products[0], staging_times[0]+photo_times[0], staging_times[0]
    
    # Create a list of tuples (product, (photo_time, staging_time))
    vtuple = [(products[i], (photo_times[i], staging_times[i])) for i in range(n)]
    
    # Sort the list of tuples by setup time
    vtuple.sort(key=lambda x: x[1][1])
    
    # Initialize variables for idle time and extra time
    idle_time  = vtuple[0][1][1]
    extra_time = vtuple[0][1][0]
    total_time = vtuple[0][1][0]
    
    # Iterate over the products
    for i in range(1, n):
        total_time += vtuple[i][1][0]
        extra_time -= vtuple[i][1][1]
        if extra_time < 0:
            idle_time -= extra_time
            extra_time = 0
        extra_time += vtuple[i][1][0]

    # Add idle time to total time
    total_time += idle_time

    # Rearrange products based on scheduling
    for i in range(n):
        products[i] = vtuple[i][0]

    return products, total_time, idle_time

if __name__ == "__main__":
    # Main part of the code
    input_file  = "inputPS10.txt"

    # Read input from file
    products, staging_times, photo_times = read_input(input_file)

    # Apply greedy algorithm to schedule photoshoot
    product_sequence, total_time, idle_time = greedy_algorithm(products, staging_times, photo_times)

    # Generate and write output to file
    write_output(product_sequence, total_time, idle_time)
