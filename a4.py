import numpy as np
import pandas as pd

def d_D(seq1, seq2):
    d = sum(1 for a, b in zip(seq1, seq2) if a != b)
    D = d / len(seq1)
    return d, D

def jukes(D):
    if D < 0.75:
        return -3/4 * np.log(1 - 4/3 * D)
    
def calculate_k(D, length):
    K = jukes(D)
    return K * length

def fasta(file):
    sequences = {}
    current_label = None
    current_seq = []
    for line in file.splitlines():
        if line.startswith('>'):
            if current_label:
                sequences[current_label] = "".join(current_seq)
            current_label = line.strip().lstrip('>')
            current_seq = []
        else:
            current_seq.append(line.strip())
    if current_label:
        sequences[current_label] = "".join(current_seq)
    return sequences

with open('saha_dibbyo_assignment4_phylogram_step5.txt', 'r') as f:
    file = f.read()
sequences = fasta(file)
sequence_labels = list(sequences.keys())
sequence_data = list(sequences.values())
abbreviations = ['Hu', 'Ti', 'Ca', 'BW', 'Hi']
n = len(sequence_data[0])
matrix = np.zeros((len(sequence_data), len(sequence_data)))
for i in range(len(sequence_data)):
    for j in range(len(sequence_data)):
        if i != j:
            _, D = d_D(sequence_data[i], sequence_data[j])
            matrix[i, j] = calculate_k(D, n)
df = pd.DataFrame(matrix, index=abbreviations, columns=abbreviations)
print('Matrix: ')
print(df)