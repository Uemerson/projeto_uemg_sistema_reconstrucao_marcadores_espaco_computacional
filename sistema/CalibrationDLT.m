function P = CalibrationDLT(x, X)
%% Número de Pontos
noPnt = length(x);
%% Estabelece a Matriz de Projeção da Câmera 
A = [X(1,:)'            X(2,:)'             X(3,:)'             ones(noPnt,1) ...
     zeros(noPnt,1)     zeros(noPnt,1)      zeros(noPnt,1)      zeros(noPnt,1) ...
     -x(1,:)'.*X(1,:)'  -x(1,:)'.*X(2,:)'   -x(1,:)'.*X(3,:)'   -x(1,:)';
     zeros(noPnt,1)     zeros(noPnt,1)      zeros(noPnt,1)      zeros(noPnt,1) ...
     X(1,:)'            X(2,:)'             X(3,:)'             ones(noPnt,1) ...
     -x(2,:)'.*X(1,:)'  -x(2,:)'.*X(2,:)'   -x(2,:)'.*X(3,:)'   -x(2,:)'];
     
[U,D,V] = svd(A);
P = reshape(V(:,12),4,3)';

