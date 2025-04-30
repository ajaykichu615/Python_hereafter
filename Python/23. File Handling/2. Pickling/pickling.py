dict1 = {'Ajay': 201737, 'Samuel': 273874}

import pickle

with open('sample.pkl','wb') as obj1:
    pickle.dump(dict1, obj1)

with open('sample.pkl', 'rb') as obj2:
    a = pickle.load(obj2)
print(a)
