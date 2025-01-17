# Question 5: Dynamic Array Simulation

def dynamic_array_simulation(operations):
    array = []
    capacity = 1
    result = []

    for operation in operations:
        if len(array) == capacity:
            capacity *= 2
        array.append(operation)
        result.append((len(array), capacity)) # creates tuple

    return result

# Example Usage
if __name__ == "__main__":

    operations = [1, 2, 3, 4, 5, 6, 7]
    print("Dynamic Array Simulation:", dynamic_array_simulation(operations))
