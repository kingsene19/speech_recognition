function clean_audio(filename)
[data,Fs] = audioread(filename);
output = noiseReduction_YW(data,Fs);
fs=44100;
frame_duration=0.02;
frame_length=floor(frame_duration*fs);
y=length(output);
net_frame=floor(y/frame_length);
new_sig=zeros(y,1);
count=0;
for k=1:net_frame
    frame=output((k-1)*frame_length+1:frame_length*k);
amplitude=max(frame);
if (amplitude > 0.2)
    count=count+1;
    new_sig((count-1)*frame_length+1:frame_length*count)=frame;
end
audiowrite("gauche.m4a",new_sig,Fs);
end