function plotting(filename)
clc;
paths = ["un.m4a" "deux.m4a" "trois.m4a" "quatre.m4a" "cinq.m4a" "six.m4a" "sept.m4a" "huit.m4a" "neuf.m4a" "dix.m4a"];
matrix = [];
for k = paths
    clc;
    X = audioread(filename)';
    Y = audioread(k)';
    X = X(1,:);
    Y = Y(1,:);
    cor = xcorr(X,Y);
    maxf = max(cor);
    matrix(end+1) = maxf;
end
maxf = max(matrix);
index = find(matrix==maxf);
for k = paths
    if index == find(paths==k)
        X = audioread(filename)';
        X = X(1,:);
        Y = audioread(match_filename)';
        Y = Y(1,:);
        cor = xcorr(X,Y);
        len = length(cor);
        range = (-(len-1)/2:1:(len-1)/2);
        subplot(3,1,1);
        plot(X);
        title("Graphe de l'enregistrement");
        subplot(3,1,2);
        plot(Y);
        title("Graphe du fichier correspondant");
        subplot(3,1,3);
        plot(range,cor);
        title("Graphe de correlation");
    end
end