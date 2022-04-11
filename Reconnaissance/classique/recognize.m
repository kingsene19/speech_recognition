
function recognize(filename)
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
allowcd = audioread('allow.m4a');
deniedcd = audioread('denied.m4a');
maxf = max(matrix);
index = find(matrix==maxf);
for k = paths
    if index == find(paths==k)
        sound(allowcd,50000);
        sound(audioread(k));
        clc;
        disp(index)
    end
end
end
