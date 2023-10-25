import random

bases = ['A', 'T', 'G', 'C']

def generate_dna_sequence(length, file):
    for i in range(length):
        file.write(random.choice(bases))

if __name__ == '__main__':
    with open('DNA1.txt', 'w') as f:
        generate_dna_sequence(2**22, f)
    with open('DNA2.txt', 'w') as f:
        generate_dna_sequence(2**23, f)
    with open('DNA3.txt', 'w') as f:
        generate_dna_sequence(2**24, f)
    with open('DNA4.txt', 'w') as f:
        generate_dna_sequence(2**25, f)
    with open('DNA5.txt', 'w') as f:
        generate_dna_sequence(2**26, f)
