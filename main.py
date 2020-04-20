import numpy as np

# This class holds the matrix object, with all information from the text file
class Matrix:

    # Functions with two underscores are default functionalities of classes that you can define. 
    # __init__() is the constructor method. I pass all needed information from the text file, and assign the values to values of the object
    def __init__(self, numProcesses, numResources, units, matrix):
        #self. refers to data that is a part of this object
        self.numP = numProcesses
        self.numR = numResources
        self.units = units
        self.matrix = matrix
        # Print statement to verify the object was created correctly
        print(f"Matirx Created\nNumber of Processes: {self.numP}\nNumber of Resources: {self.numR}\nResource Units per Row: {self.units}\nMatrix:\n {self.matrix}")
    
    # The __str__ method is how the object will be treated if referenced as a string, I chose to use the string representation for the matrix.
    # This allows us to print the object, and get just the matrix as our result
    def __str__(self):
        return np.array_str(self.matrix)

# This function parses the text file provided
def parse(filename):
    flag = 0
    tempList = []
    # This is essentially the python equivalent of while(!EOF)
    with open(filename, "r") as f:
        for line in f:
            # Removes the newline character from the line we're reading
            line = line.rstrip('\n')
            # If the line we're reading exists, and is not a whitespace character Enter conditionals
            if line and not line.isspace():
                # If the first index of the line is a percent sign, we know it's a comment, and can skip it
                if not line[0] == "%":
                    # Cases to parse out the information
                    # If we find a "=" character in the string (-1 is the return value for not found), than we know it's either the number of processes, or resources
                    if line.find("=") != -1:
                        # .split will break a string into parts based on the argument provided. So this will split the string before and after every "="   
                        x = line.split("=")
                        if x[0] == "num_processes":
                            # We cast it as an int here
                            numP = int(x[1])
                        else:
                            numR = int(x[1])
                    # I used flag to switch between parsing of the matrix, and the resource units
                    elif not flag:
                        # Here, we make a map out of the values we're splitting from the line. We use the map function, because it allows us to pass a function, in this case the function is casting every string as an int
                        mp = map(int, line.split(","))
                        # We make a list (array) out of our map to use.
                        units = list(mp)
                        flag = 1
                    elif flag:
                        mp = map(int, line.split(","))
                        t = list(mp)
                        # A list of lists, that we will use to construct our matrix
                        tempList.append(t)
    # Create the matrix from our list of lists
    matrix = np.matrix(tempList)
    # Create our matrix object
    matrixObject = Matrix(numP, numR, units, matrix)
    return matrixObject

def main():
    # Un-commenting this line will allow the user to input a file upon runtime. 
    #filename = input("Enter the filename/path: ")
    # A hardcoded file destination, for ease of testing
    filename = "C:/Users/DanielBatesJ/Desktop/UNT/Spring 2020/4600/Project2/Project-2-input-example.txt"
    matrix = parse(filename)
    # I setup the class so that printing our object will print the matrix for ease of use

    # The print(f"") adapts python's print to act as a more C style print function. Using {} to place variables. 
    print(f"Testing the default print method of our object\n{matrix}")

main()