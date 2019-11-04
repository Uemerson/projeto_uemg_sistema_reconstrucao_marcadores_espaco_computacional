import re
import numpy

def load(file):
    matrix = []
    with open(file, 'r') as f:
        for line in f:
            pattern = re.compile(r'\s+')    
            line = re.sub(pattern, ' ', line)   #Substitui /t para ' '
            
            lineMatrix = []
            for num in line.split(' '):
                if (num != ''):
                    lineMatrix.append(int(num))

            matrix.append(lineMatrix)

    return matrix

def loadFloat(file):
    matrix = []
    with open(file, 'r') as f:
        for line in f:
            pattern = re.compile(r'\s+')    
            line = re.sub(pattern, ' ', line)   #Substitui /t para ' '
            
            lineMatrix = []
            for num in line.split(' '):
                if (num != ''):
                    lineMatrix.append(float(num))

            matrix.append(lineMatrix)

    return numpy.array(matrix)