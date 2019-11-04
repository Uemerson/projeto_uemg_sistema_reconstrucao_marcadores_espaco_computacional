import numpy

def CalibrationDLT(x, X):
    #  Número de Pontos
    lenght, noPnt = numpy.shape(x)
 
    print(noPnt)

    item1 = numpy.transpose(X[0]) # X(1,:)'
    item2 = numpy.transpose(X[1]) # X(2,:)'
    item3 = numpy.transpose(X[2]) # X(3,:)'
    item4 = numpy.ones(noPnt) # ones(noPnt,1)

    item5 = numpy.zeros(noPnt) # zeros(noPnt,1)
    item6 = numpy.zeros(noPnt) # zeros(noPnt,1)
    item7 = numpy.zeros(noPnt) # zeros(noPnt,1)
    item8 = numpy.zeros(noPnt) # zeros(noPnt,1)

    item9 = numpy.multiply(numpy.transpose(-x[0]), numpy.transpose(X[0])) # -x(1,:)'.*X(1,:)'
    item10 = numpy.multiply(numpy.transpose(-x[0]), numpy.transpose(X[1])) # -x(1,:)'.*X(2,:)'
    item11 = numpy.multiply(numpy.transpose(-x[0]), numpy.transpose(X[2])) # -x(1,:)'.*X(3,:)'
    item12 = numpy.transpose(-x[0]) # -x(1,:)'

    #Outra linha

    item13 = numpy.zeros(noPnt) # zeros(noPnt,1)
    item14 = numpy.zeros(noPnt) # zeros(noPnt,1)
    item15 = numpy.zeros(noPnt) # zeros(noPnt,1)
    item16 = numpy.zeros(noPnt) # zeros(noPnt,1)

    item17 = numpy.transpose(X[0]) # X(1,:)'
    item18 = numpy.transpose(X[1]) # X(2,:)'
    item19 = numpy.transpose(X[2]) # X(3,:)'
    item20 = numpy.ones(noPnt) # ones(noPnt,1)

    item21 = numpy.multiply(numpy.transpose(-x[1]), numpy.transpose(X[0])) # -x(2,:)'.*X(1,:)'
    item22 = numpy.multiply(numpy.transpose(-x[1]), numpy.transpose(X[1])) # -x(2,:)'.*X(2,:)'
    item23 = numpy.multiply(numpy.transpose(-x[1]), numpy.transpose(X[2])) # -x(2,:)'.*X(3,:)'
    item24 = numpy.transpose(-x[1]) # -x(2,:)'

    A = [
        [item1, item2, item3, item4, item5, item6, item7, item8,
         item9, item10, item11, item12],
        [item13, item14, item15, item16, item17, item18, item19,
        item20, item21, item22, item23, item24]
    ]

    numpy.set_printoptions(precision=3)
    print(item1)
    print(numpy.array(item2))

    # Estabelece a Matriz de Projeção da Câmera 
    # A = [[numpy.transpose(X[0]), numpy.transpose(X[1]), numpy.transpose(X[2]), numpy.ones(noPnt,1),
    #     numpy.zeros(noPnt,1), numpy.zeros(noPnt,1), numpy.zeros(noPnt,1), numpy.zeros(noPnt,1), 
    #     matmult(numpy.transpose(-x[0]), numpy.transpose(X[0])),  matmult(numpy.transpose(-x[0]), numpy.transpose(X[1])), numpy.transpose(-x[0]), numpy.transpose(X[2]), numpy.transpose(-x[0])],
    #     [numpy.zeros(noPnt,1), numpy.zeros(noPnt,1), numpy.zeros(noPnt,1), numpy.zeros(noPnt,1),
    #     numpy.transpose(X[0]), numpy.transpose(X[1]), numpy.transpose(X[2]), numpy.ones(noPnt,1),
    #     matmult(numpy.transpose(-x[1]), numpy.transpose(X[0])),  matmult(numpy.transpose(-x[1]), numpy.transpose(X[1])), matmult(numpy.transpose(-x[1]), numpy.transpose(X[2])), numpy.transpose(-x[1])]
    #     ]
    
    # [U,D,V] = numpy.linalg.svd(A)

    # Vitem12 = list(zip(*V))

    # P = numpy.transpose(numpy.reshape(Vitem12[11],4,3))
    # return P

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