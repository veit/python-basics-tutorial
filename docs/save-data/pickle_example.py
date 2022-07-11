import pickle

a = [1, 2.0, 3+4j]
b = ("character string", b"byte string")
c = {None, True, False}

# File with pickles
with open('data.pickle', 'wb') as f:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

# Load the pickled data back into Python
with open('data.pickle', 'rb') as f:
    first = pickle.load(f)
    second = pickle.load(f)
    third = pickle.load(f)

# Print the pickled data
print(first, second, third)
