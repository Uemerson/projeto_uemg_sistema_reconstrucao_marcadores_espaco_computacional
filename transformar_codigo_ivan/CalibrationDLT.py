import numpy

def CalibrationDLT(x, X):
    #  Número de Pontos
    noPnt = length(x)
    # Estabelece a Matriz de Projeção da Câmera 
    A = [[numpy.transpose(X[0]), numpy.transpose(X[1]), numpy.transpose(X[2]), numpy.ones(noPnt,1),
        numpy.zeros(noPnt,1), numpy.zeros(noPnt,1), numpy.zeros(noPnt,1), numpy.zeros(noPnt,1),
        matmult(numpy.transpose(-x[0]), numpy.transpose(X[0])),  matmult(numpy.transpose(-x[0]), matmult(numpy.transpose(X[1])), numpy.transpose(-x[0]), numpy.transpose(X[2])), numpy.transpose(-x[0])],
        [numpy.zeros(noPnt,1), numpy.zeros(noPnt,1), numpy.zeros(noPnt,1), numpy.zeros(noPnt,1),
        numpy.transpose(X[0]), numpy.transpose(X[1]), numpy.transpose(X[2]), numpy.ones(noPnt,1),
        matmult(numpy.transpose(-x[1]), numpy.transpose(X[0])),  matmult(numpy.transpose(-x[1]), numpy.transpose(X[1])), matmult(numpy.transpose(-x[1]), numpy.transpose(X[2])), numpy.transpose(-x[1])]
        ]
        
    [U,D,V] = numpy.linalg.svd(A)

    VColumn12 = list(zip(*V))

    P = numpy.transpose(numpy.reshape(VColumn12[11],4,3))
    return P

# https://stackoverflow.com/questions/50930899/svd-command-in-python-v-s-matlab
# https://stackoverflow.com/questions/10508021/matrix-multiplication-in-python
# https://www.mathworks.com/matlabcentral/answers/38111-what-does-x-1-do-in-matlab
# https://stackoverflow.com/questions/29793345/how-to-read-the-first-row-of-an-array-in-python

def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 : 
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]

