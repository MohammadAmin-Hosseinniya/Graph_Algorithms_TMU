import random


number_of_samples = 4
n = [5, 6, 7, 8]

for i in range(number_of_samples):
    file = open(f"ES_input_{i}.txt", "w")
    
    file.write(f"{n[i]}\n")
    for line in range(n[i]):
        file.write(f"{random.randint(0, 50)} {random.randint(0, 50)}\n")
    
    file.close()