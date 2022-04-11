function recognition(filename)
   x = mfcc_calc(filename);
   paths = ["avancer.m4a" "reculer.m4a" "gauche.m4a" "droite.m4a" "stop.m4a" "allumer.m4a" "eteindre.m4a" "bas.m4a" "haut.m4a" "tourner.m4a"];
   d = [zeros(1,10)];
   for k=1:10
       variable = mfcc_calc(paths(k));
       d(k) = norm(x-variable);
   end
   [~,index]=min(d);
   for k = paths
       if index == find(paths==k)
           clc;
           [data1,fs1] = audioread(filename);
           [data2,fs2] = audioread(k);
           sound(data2,50000);
           win = hann(1024,"periodic")
           coeff1 = mfcc(data1,fs1);
           coeff2 = mfcc(data2,fs2);
           ax1 = subplot(2,2,1,'Parent',app.ReprsentationDesGraphesPanel);
           ax2 = subplot(2,2,2,'Parent',app.ReprsentationDesGraphesPanel);
           ax3 = subplot(2,2,3,'Parent',app.ReprsentationDesGraphesPanel);
           ax4 = subplot(2,2,4,'Parent',app.ReprsentationDesGraphesPanel);
           imagesc(ax1,coeff1);
           axis auto
           colormap("jet");
           title(ax1,"MFCC de l'enregistrement");
           imagesc(ax2,coeff2);
           axis auto
           colormap("jet");
           title(ax2,"MFCC du fichier correspondant");
           plot(ax3,data1);
           title(ax1,"Signal enregistré");
           plot(ax4,data2);
           title(ax2,"Signal reconnu");
           [~,name,~] = fileparts(k);
           app.EditField.Value = "Resultat de la prediction est: " + name;
       end
   end
end