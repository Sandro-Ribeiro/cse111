# Example 2
"""
We can add an item to a list by using the insert and append 
methods. We can determine if an element is in a list by using 
the Python membership operator, which is the keyword in. We 
can find the index of an item within a list by using the 
index method. We can remove an item from a list by using the 
pop and remove methods.
"""

def main():
    # Create an empty list that will hold fabric names.
    fabrics = []
    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")
    # Insert an element at the beginning of the fabrics list.
    fabrics.insert(0, "chiffon")
    print(fabrics)
    # Determine if gingham is in the fabrics list.
    if "gingham" in fabrics:
        print("gingham is in the list.")
    else:
        print("gingham is NOT in the list.")
    # Get the index where velvet is stored in the fabrics list.
    i = fabrics.index("velvet")
    # Replace velvet with taffeta.
    fabrics[i] = "taffeta"
    # Remove the last element from the fabrics list.
    fabrics.pop()
    # Remove denim from the fabrics list.
    fabrics.remove("denim")
    # Get the length of the fabrics list and print it.
    n = len(fabrics)
    print(f"The fabrics list contains {n} elements.")
    print(fabrics)
    
# Call main to start this program.
if __name__ == "__main__":
    main()