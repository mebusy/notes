...menustart

 - [Plotting data](#5973297b1e05d782b78ef41923b083ad)
     - [tips](#e4c9479b11955648dad558fe717a4eb2)

...menuend


<h2 id="5973297b1e05d782b78ef41923b083ad"></h2>


# Plotting data

    plot操作会替换掉当前plot的内容
    使用 hold on命名保持当前plot的内容，避免被后续plot替换掉
    plot 曲线可以定义颜色
    可以给轴命名 xlable , ylable ...
    legend 在右上角画图例
    title  起标题
    print -dpng 输出 png
    close  关闭plot
    figure(x) 配合 plot 使用独立的 plot显示
    subplot( row, col , index ) 分格显示
    axis 改变轴刻度
    imagesc 可视化一个矩阵
    可以改变点的形状和尺寸

```
>> setenv("GNUTERM","qt")
>> t=[0:0.01:0.98];
>> y1= sin(2*pi*4*t); % 输出正旋函数
>> plot(t,y1)
>> t=[0:0.01:0.98];
>> y1= sin(2*pi*4*t); % 输出正旋函数
>> plot(t,y1)
>> y2= cos(2*pi*4*t); % 输出余旋函数
>> hold on;         % 保持现在的plot, 使后续的plot追在在现有的plot上，而不是替换
>> plot(t,y2,'r')   % 使用红色
>> xlabel('time')   % 轴命名
>> ylabel("value")
>> legend('sin','cos')  % 在右上角 图例 两条曲线 
>> title('my plot')   % 起名
>> print -dpng '~/myplot.png'  % 保存图像, 可能需要安装一些工具库
>> close    % 关闭plot

% 独立显示
>> figure(1); plot(t,y1)    % 开两个 plot 显示
>> figure(2); plot(t,y2)
>> close
>> close

% 分格显示
>> subplot(1,2,1)  % 启动一个plot，分成1x2格子, 激活第1个格子
>> plot(t,y1)   % 在激活的格子中，画 t,y1
>> subplot(1,2,2)  
>> plot(t,y2)
>> axis([0.5 1 -1 1])  % 改变当前格子(或plot)轴刻度, 这会把 t,y2图像的 x轴改为 0.5到1, y轴改为-1到1
>> clf   % 清除当前plot

>> A=magic(5);     %可视化 一个矩阵
>> imagesc(A)      % 使用彩色图块可视化矩阵
>> colorbar        % 右侧添加一个 色彩刻度条，显示每种颜色对应的值
>> imagesc(A), colorbar, colormap gray % 同时执行3条命令, 使用灰度显示
```

<h2 id="e4c9479b11955648dad558fe717a4eb2"></h2>


## tips
```
plot(x, y, 'rx', 'MarkerSize', 10); % 改变 点的形状和尺寸
```


For brew octave plotting error:

```
brew uninstall fontconfig
brew install fontconfig --universal

brew uninstall gnuplot
brew install gnuplot --with-qt
```
