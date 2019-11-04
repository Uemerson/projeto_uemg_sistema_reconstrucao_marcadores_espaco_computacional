function Plot(GRID, Pontos3D)

hf = figure()

scatter3(GRID(:,1),GRID(:,2),GRID(:,3));
hold on
scatter3(Pontos3D(:,1),Pontos3D(:,2),Pontos3D(:,3),'fill');					 

%grafo = [ 1 2; 1 3; 2 4; 3 5; 1 6; 1 7; 1 8; 1 9; 6 10; 7 10; 10 11; 10 13; 11 12; 8 14; 9 14; 14 15; 14 16; 16 17];
grafo = [ 1 2; 1 3; 2 4; 3 5; 4 6; 4 7; 5 8; 5 9; 6 10; 7 10; 10 11; 10 13; 11 12; 8 14; 9 14; 14 15; 14 16; 16 17];

for i = 1:18
    plot3(Pontos3D(grafo(i,:),1), Pontos3D(grafo(i,:),2), Pontos3D(grafo(i,:),3));
end

print (hf, "plot.png");

end
