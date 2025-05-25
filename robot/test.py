import pickle
x = {
    'name' : 'artin',
    'age' : 20
}

# with open("test", "wb") as f:
#     pickle.dump(x , f)
with open("test", "rb") as f:
    print(pickle.load(f))