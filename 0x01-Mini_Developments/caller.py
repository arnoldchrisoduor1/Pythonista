import ctypes

# Load the shared library
summ = ctypes.CDLL('C:/Users/arnol/OneDrive/Desktop/Pythonista/0x01-Mini_Developments/summ.dll')  # Provide the path to the shared library


# Declare the function signature
summ.add.restype = ctypes.c_int
summ.add.argtypes = [ctypes.c_int, ctypes.c_int]

# Call the C function
result = summ.add(2, 3)
print("Result:", result)
