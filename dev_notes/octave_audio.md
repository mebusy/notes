# install

```
brew reinstall octave --with-sndfile --with-libsndfile --enable-bounds-check 
```

--with-portaudio --with-openblas


# 音频信息

- Various formats are supported including wav, flac and ogg vorbis


```
>> info = audioinfo ('testing.ogg')
```

# 读取音频文件

```
file='yourfile.ogg'
[M, fs] = audioread(file)
```

M 是一个一列或两列的矩阵，取决于信道的数量，fs 是采样率

下面的操作都可以读取音频文件：

```
>> [y, fs] = audioread (filename, samples)
>> [y, fs] = audioread (filename, datatype)
>> [y, fs] = audioread (filename, samples, datatype)
```

 - samples 指定开始帧和结束帧

```
samples = [1, fs)
[y, fs] = audioread (filename, samples)
```

 - 指定 datatype

```
[y,Fs] = audioread(filename,'native')
```

# 音频文件的写操作

新建一个 ogg 文件：

我们会从一个余弦值创建一个 ogg 文件。采样率是每秒 44100 次，这个文件最少进行 10 秒的采样。余弦信号的频率是 440 Hz。

```
filename='cosine.wav';
fs=44100;
t=0:1/fs:10;
w=2*pi*440*t;
signal=cos(w);
audiowrite(filename, signal, fs);
```




