module = { # using python dictionaries with key/value pair 
    "CSC1006": "Mathematics 2",
    "CSC1007": "Operating Systems",
    "CSC1009": "Object Oriented Programming",
    "CSC2902": "Career and Professional Development"
    
}
choice= input("Enter module code: ") # input code 
print(module[choice]) # access value from input key thru []