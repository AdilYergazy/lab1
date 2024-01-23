import os

a = []
path = "/home/aduly/Documents/w3school/lab1"

for i in os.listdir(path):
    for j in os.listdir(os.path.join(path, i)):
        for k in os.listdir(os.path.join(path, i, j)):
            print(k)
            with open(os.path.join(path, i, j, k), 'r') as f:
                print(f.readlines())
