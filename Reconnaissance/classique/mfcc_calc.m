function [featurevector] = mfcc_calc(filename)
x = audioread(filename);
h=hamming(1024);
frame_length=1024;
net_frame=floor(length(x)/frame_length)
frame=cell(1,net_frame);
FRAME=cell(1,net_frame);
offset=440;
for i=1:net_frame
    frame{i}=x((i-1)*offset+1:(i-1)*offset+1024);
    frame{i}=frame{i}.*h;
    FRAME{i}=fft(frame{i},512);
    FRAME{i}=FRAME{i}(1:257);
    POWER{i}=(abs(FRAME{i}).^2)/1024;
end
nfft=512;%512 point fft
samplerate=44010;
H=cell(1,26);
energy=cell(1,net_frame);
m=linspace(401.25,2834.99,28);
h=700*(exp(m/1125)-1)
f = floor((nfft+1)*h/samplerate);
for i=1:26
    for k=1:257
        if k<f(i)
            H{i}(k)=0;
        elseif k>=f(i) && k<f(i+1)
            H{i}(k)=(k-f(i))/(f(i+1)-f(i));
        elseif k>=f(i+1) && k<f(i+2)
            H{i}(k)=(f(i+2)-k)/(f(i+2)-f(i+1));
        elseif k>=f(i+2)
            H{i}(k)=0;
        else
            ;
        end
    end
end
for i=1:net_frame
    for j=1:26
        energy{i}(j)=sum(POWER{i}.*H{j}');
    end
end
for i=1:net_frame
    mfcc{i}=dct(log(energy{i}));
    mfcc{i}=mfcc{i}(2:13);    
end
mfcc_array = [];
for j=1:net_frame
    mfcc_array=[mfcc_array;cell2mat(mfcc(j))];
    delta_array=mfcc2delta(mfcc_array,4);
    delta_delta_array=mfcc2delta(delta_array,4);
    delta_delta=mean(delta_delta_array);
    delta=mean(delta_array);
    mfcc1=mean(mfcc_array);
    featurevector=[mfcc1 delta delta_delta];
end
end