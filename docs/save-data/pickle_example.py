import pickle

# Serialise Python objects to file with pickles
data = {
        'a': [1, 2.0, 3+4j],
        'b': ("character string", b"byte string"),
        'c': {None, True, False}
        }

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

# Load the pickled data back into Python
with open('data.pickle', 'rb') as f:
    saved_data = pickle.load(f)

# Print the pickled data
print(saved_data)
