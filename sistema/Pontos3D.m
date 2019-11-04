function newArray = Pontos3D(npontos, Paparece, CALC_CAMS, CAMS, Pontos)

Pontos3D = zeros(npontos, 4);
Pontos3D = [];

for i = 1:npontos
	
    P3D = zeros(3,1);
    count = 0;    
    for j = 1:4
        if( Paparece(i, j) )
            count = count + 1;
            CALC_CAMS(count) = j;
        end
    end
    
    count = 2;
    
    if( count == 2 )
        ini_cam1 =  CALC_CAMS(1)*3-2;
        fim_cam1 =  CALC_CAMS(1)*3;
        ini_cam2 =  CALC_CAMS(2)*3-2;
        fim_cam2 =  CALC_CAMS(2)*3;
        
        P3D = Reconstruction2cam( CAMS(ini_cam1:fim_cam1, : ), ...
			   CAMS(ini_cam2:fim_cam2, : ), ...
        			   Pontos( i,  ini_cam1:fim_cam1)', ...
        			   Pontos( i,  ini_cam2:fim_cam2)' );
    elseif (count == 3 )
        ini_cam1 =  CALC_CAMS(1)*3-2;
        fim_cam1 =  CALC_CAMS(1)*3;
        ini_cam2 =  CALC_CAMS(2)*3-2;
        fim_cam2 =  CALC_CAMS(2)*3;
        ini_cam3 =  CALC_CAMS(3)*3-2;
        fim_cam3 =  CALC_CAMS(3)*3;

        P3D = Reconstruction3cam( CAMS(ini_cam1:fim_cam1, : ), ...
			   CAMS(ini_cam2:fim_cam2, : ), ...
			   CAMS(ini_cam3:fim_cam3, : ), ...
        			   Pontos( i,  ini_cam1:fim_cam1)', ...
        			   Pontos( i,  ini_cam2:fim_cam2)', ...
        			   Pontos( i,  ini_cam3:fim_cam3)' );
    elseif (count == 4)
        ini_cam1 =  CALC_CAMS(1)*3-2;
        fim_cam1 =  CALC_CAMS(1)*3;
        ini_cam2 =  CALC_CAMS(2)*3-2;
        fim_cam2 =  CALC_CAMS(2)*3;
        ini_cam3 =  CALC_CAMS(3)*3-2;
        fim_cam3 =  CALC_CAMS(3)*3;
        ini_cam4 =  CALC_CAMS(4)*3-2;
        fim_cam4 =  CALC_CAMS(4)*3;

        P3D = Reconstruction4cam( CAMS(ini_cam1:fim_cam1, : ), ...
			   CAMS(ini_cam2:fim_cam2, : ), ...
			   CAMS(ini_cam3:fim_cam3, : ), ...
			   CAMS(ini_cam4:fim_cam4, : ), ...
        			   Pontos( i,  ini_cam1:fim_cam1)', ...
        			   Pontos( i,  ini_cam2:fim_cam2)', ...
        			   Pontos( i,  ini_cam3:fim_cam3)', ...
        			   Pontos( i,  ini_cam4:fim_cam4)' );
    else
        disp('Numero insuficiente de cameras para o ponto %d,');
    end
    
    Pontos3D(i,:) = P3D(:)';
    %Pontos3D = [Pontos3D; P3D(:)'];

end

newArray = Pontos3D