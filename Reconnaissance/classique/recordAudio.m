recObj = audiorecorder(44100,24,1);
disp("Parlez")
recordblocking(recObj,4);
disp("Fini")
play(recObj);
voice_1=getaudiodata(recObj);
[b,a] = butter(4,4000/44100); %to filter high frequency noise.
x=filter(b,a,voice_1);
x=x/abs(max(x));
fs=44100;
frame_duration=0.02;
frame_length=floor(frame_duration*fs);
y=length(x);
net_frame=floor(y/frame_length);
new_sig=zeros(y,1);
count=0;
for k=1:net_frame
    frame=x((k-1)*frame_length+1:frame_length*k);
    amplitude=max(frame);
    if (amplitude > 0.2)
        count=count+1;
        new_sig((count-1)*frame_length+1:frame_length*count)=frame;
    end
end
j = length(new_sig);
while (new_sig(j)<0.2)
    j=j-1;
end
j = j+2000;
x=new_sig(1:j);
audiowrite("demo.m4a",x,44100);