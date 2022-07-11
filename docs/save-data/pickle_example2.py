import pickle

a = [1, 2.0, 3+4j]
b = ("character string", b"byte string")
c = {None, True, False}

# Serialise Python objects
data = {'a': a, 'b': b, 'c': c}

# File with pickles
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# Load all pickled data back into Python
with open('data.pickle', 'rb') as f:
    saved_data = pickle.load(f)

# Print only the pickled data in c
print(saved_data['c'])
