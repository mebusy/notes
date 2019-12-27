...menustart

 - [2.6. 使用 Numpy and Scipy 处理图像数据](#b19a2f80d04c56b985a7e69f63d04915)
     - [2.6.1. 打开并写到图像文件](#b28007ec78c21d3a75965fe86a94680b)
 - [2.6.2. 显示图片](#9c086b0de474c7ee0e6c4994c23475a3)
     - [2.6.3. 基本操作](#6162bb0c1053d06bb0eab255d3d82a53)
         - [2.6.3.1. 统计信息](#9b81935266796da309310d0f565c1bca)
         - [2.6.3.2. 集合变换 Geometrical transformations](#9a60835f1916a50185c8794cc1c2b06c)
     - [2.6.4. Image filtering 图像滤波](#b8bed379bc03325e3f86fb26c21253bd)
         - [2.6.4.1. Blurring/smoothing 模糊/平滑](#891cbaca4b10e63615d5fd4702c2db94)
     - [2.6.4.2. Sharpening 锐化](#4b0aa8cd2942d9bdd095df1a0ff7ff99)
     - [2.6.4.3. Denoising 去燥](#f8962c34d7ddbf921cc3fa7d6bf96cb4)
     - [2.6.5. Feature extraction 特征提取](#0fd36be3567167c262fae183a580aa7c)
         - [2.6.5.1. Edge detection 边缘检测](#ea0f17b8c9b0298df7e75d7f009a9323)
         - [2.6.5.2. Segmentation 分割](#ff7de7467377d111993a153fc8d65657)
     - [2.6.6. Measuring objects properties 测量对象属性](#bda5dcbbc5b8462fcde1a64fcc8ffc35)

...menuend


<h2 id="b19a2f80d04c56b985a7e69f63d04915"></h2>


##2.6. 使用 Numpy and Scipy 处理图像数据

子模块 scipy.ndimage 提供了 操作 n-维 NumPy 数组的方法.
更高级的图像处理, 使用 skimage 模块

```python
from scipy import ndimage
```

<h2 id="b28007ec78c21d3a75965fe86a94680b"></h2>


###2.6.1. 打开并写到图像文件
```python
# 读取数据
from scipy import misc
l = misc.lena()
>>> l.shape
(512, 512)

# 保存
misc.imsave('lena.png', l) # uses the Image module (PIL)

#显示
import matplotlib.pyplot as plt
plt.imshow(l)
plt.show()
```

从图片创建一个 numpy数组
```python
>>> from scipy import misc
>>> lena = misc.imread('lena.png')
>>> type(lena)
<type 'numpy.ndarray'>
>>> lena.shape, lena.dtype
((512, 512), dtype('uint8'))
```

Opening raw files (camera, 3-D images)
```python
l.tofile('lena.raw') # Create raw file
lena_from_raw = np.fromfile('lena.raw', dtype=np.int64)
lena_from_raw.shape

lena_from_raw.shape = (512, 512)
```

对于大数据，使用 np.memmap 做内存映射:
```python
lena_memmap = np.memmap('lena.raw', dtype=np.int64, shape=(512, 512))
```
(数据从文件中读取, 不载如内存)

<h2 id="9c086b0de474c7ee0e6c4994c23475a3"></h2>


##2.6.2. 显示图片

显示灰度图
```python
l = misc.lena()
import matplotlib.pyplot as plt
plt.imshow(l, cmap=plt.cm.gray)
```

通过设置最大最小值，增加对比度
```python
plt.imshow(l, cmap=plt.cm.gray, vmin=30, vmax=200)
```

画轮廓线
```python
plt.contour(l, [60, 211])
# Remove axes and ticks
plt.axis('off')
```

![](http://scipy-lectures.github.io/_images/plot_display_lena_1.png)

强度变化的精细检查
```python
plt.imshow(l[200:220, 200:220], cmap=plt.cm.gray)
#vs
plt.imshow(l[200:220, 200:220], cmap=plt.cm.gray, interpolation='nearest')
```
![](http://scipy-lectures.github.io/_images/plot_interpolation_lena_1.png)


<h2 id="6162bb0c1053d06bb0eab255d3d82a53"></h2>


### 2.6.3. 基本操作
图像是数组， 全部使用 numpy 工具
![](http://scipy-lectures.github.io/_images/axis_convention.png)

```python
#读取图片
lena = scipy.misc.lena()

#100-119行，涂成白色
lena[100:120] = 255



#构建一个稀疏 mesh
lx, ly = lena.shape
X, Y = np.ogrid[0:lx, 0:ly]
#创建一个mask，离图片中心位置超过一定距离的点，标为True
#numpy的强大就在这里体现出来了
mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4
#mask变黑
lena[mask] = 0

# 左上(0,0) 到 (399,399) 画一条白线
lena[range(400), range(400)] = 255
```
显示如下
![](http://scipy-lectures.github.io/_images/plot_numpy_array_1.png)

<h2 id="9b81935266796da309310d0f565c1bca"></h2>


#### 2.6.3.1. 统计信息
```python
>>> lena = misc.lena()
>>> lena.mean()  
124.04678344726562   #算数平均数
>>> lena.max(), lena.min()  
(245, 25)  #最大最小值
```

<h2 id="9a60835f1916a50185c8794cc1c2b06c"></h2>


####2.6.3.2. 集合变换 Geometrical transformations

```python
lena = misc.lena()
lx, ly = lena.shape
# Cropping
crop_lena = lena[lx / 4: - lx / 4, ly / 4: - ly / 4]
# up <-> down flip
flip_ud_lena = np.flipud(lena)
# rotation
rotate_lena = ndimage.rotate(lena, 45)
rotate_lena_noreshape = ndimage.rotate(lena, 45, reshape=False)
```

![](http://scipy-lectures.github.io/_images/plot_geom_lena_1.png)

<h2 id="b8bed379bc03325e3f86fb26c21253bd"></h2>


###2.6.4. Image filtering 图像滤波 

本地过滤器：由相邻像素的值的函数 替换掉像素值。
Neighbourhood：方形（选择尺寸），磁盘，或更复杂的结构元素。

<h2 id="891cbaca4b10e63615d5fd4702c2db94"></h2>


#### 2.6.4.1. Blurring/smoothing 模糊/平滑
高斯过滤器: Gaussian filter  from scipy.ndimage:
```python
from scipy import misc
lena = misc.lena()
blurred_lena = ndimage.gaussian_filter(lena, sigma=3)
very_blurred = ndimage.gaussian_filter(lena, sigma=5)
```
统一的过滤器： Uniform filter
```python
local_mean = ndimage.uniform_filter(lena, size=11)
```
![](http://scipy-lectures.github.io/_images/plot_blur_1.png)

<h2 id="4b0aa8cd2942d9bdd095df1a0ff7ff99"></h2>


### 2.6.4.2. Sharpening 锐化
锐化一张被模糊处理过的图片
```python
from scipy import misc
lena = misc.lena()
blurred_l = ndimage.gaussian_filter(lena, 3)
```

加入拉普拉斯的近似值,来增加 边缘的权重
```python
filter_blurred_l = ndimage.gaussian_filter(blurred_l, 1)
alpha = 30
sharpened = blurred_l + alpha * (blurred_l - filter_blurred_l)
```
![](http://scipy-lectures.github.io/_images/plot_sharpen_1.png)

<h2 id="f8962c34d7ddbf921cc3fa7d6bf96cb4"></h2>


### 2.6.4.3. Denoising 去燥
noisy lena
```python
from scipy import misc
l = misc.lena()
l = l[230:310, 210:350]
noisy = l + 0.4 * l.std() * np.random.random(l.shape)
```

高斯过滤 可以把噪点去处，同时 边缘也会被平滑掉
```python
gauss_denoised = ndimage.gaussian_filter(noisy, 2)
```

中值滤波器 median filter 可以保持更好的边缘
```python
med_denoised = ndimage.median_filter(noisy, 3)
```
![](http://scipy-lectures.github.io/_images/plot_lena_denoise_1.png)

中值滤波器对于 直边界（低曲率）的情况有更好的效果
```python
im = np.zeros((20, 20))
im[5:-5, 5:-5] = 1
im = ndimage.distance_transform_bf(im)
im_noise = im + 0.2 * np.random.randn(*im.shape)
im_med = ndimage.median_filter(im_noise, 3)

plt.figure(figsize=(16, 5))
plt.subplot(141)
plt.imshow(im, interpolation='nearest')

plt.subplot(142)
plt.imshow(im_noise, interpolation='nearest', vmin=0, vmax=5)

plt.subplot(143)
plt.imshow(im_med, interpolation='nearest', vmin=0, vmax=5)

plt.subplot(144)
plt.imshow(np.abs(im - im_med), cmap=plt.cm.hot, interpolation='nearest')

plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0, right=1)
plt.show()
```

![](http://scipy-lectures.github.io/_images/plot_denoising_1.png)

2.6.4.4。数学形态学 morphology
用一个简单的形状( 一个结构元素 a structuring element)探测图像， 
并根据这个形状是否剧本符合图像，以此修改图像。

结构元素:
ndimage.generate_binary_structure(rank, connectivity)
rank：维度
connectivity: 连接
生成二元结构，用于二元形态操作。（不生成也都正常。。。默认？）

```python
>>> el = ndimage.generate_binary_structure(2, 1)
>>> el
array([[False,  True, False],
       [ True,  True,  True],
       [False,  True, False]], dtype=bool)
>>> el.astype(np.int)
array([[0, 1, 0],
       [1, 1, 1],
       [0, 1, 0]])
       
plt.imshow(el, interpolation='nearest' )
```
![](http://scipy-lectures.github.io/_images/diamond_kernel.png)

侵蚀 Erosion = 最小过滤 minimum filter
用结构元素覆盖的像素的最小值替代一个像素值
```python
a = np.zeros((7,7), dtype=np.int)
a[1:6, 2:5] = 1         #第1-5行， 2-4列，置1
>>> a = np.zeros((7,7), dtype=np.int)
>>> a[1:6, 2:5] = 1
>>> a
array([[0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 0, 0],
       [0, 0, 1, 1, 1, 0, 0],
       [0, 0, 1, 1, 1, 0, 0],
       [0, 0, 1, 1, 1, 0, 0],
       [0, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0]])
>>> ndimage.binary_erosion(a).astype(a.dtype)
array([[0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0]])
>>> #Erosion 会删除所有比结构�小的对象
>>> ndimage.binary_erosion(a, structure=np.ones((5,5))).astype(a.dtype)
array([[0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0]])       
```

扩张 Dilation: 最大过滤器 maximum filter:
```python
>>> a = np.zeros((5, 5))
>>> a[2, 2] = 1
>>> a
array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])
>>> ndimage.binary_dilation(a).astype(a.dtype)
array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  1.,  1.,  1.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])
```

也适用于灰度值图像：
```python
from scipy import ndimage
import matplotlib.pyplot as plt

im = np.zeros((64, 64))
np.random.seed(2)
x, y = (63*np.random.random((2, 8))).astype(np.int)
im[x, y] = np.arange(8)

bigger_points = ndimage.grey_dilation(im, size=(5, 5), structure=np.ones((5, 5)))

square = np.zeros((16, 16))
#中间一个大白块
square[4:-4, 4:-4] = 1

#Distance transform function by a brute force algorithm
dist = ndimage.distance_transform_bf(square)
dilate_dist = ndimage.grey_dilation(dist, size=(3, 3), \
        structure=np.ones((3, 3)))
        
plt.figure(figsize=(12.5, 3))
plt.subplot(141)
plt.imshow(im, interpolation='nearest', cmap=plt.cm.spectral)

plt.subplot(142)
plt.imshow(bigger_points, interpolation='nearest', cmap=plt.cm.spectral)

plt.subplot(143)
plt.imshow(dist, interpolation='nearest', cmap=plt.cm.spectral)

plt.subplot(144)
plt.imshow(dilate_dist, interpolation='nearest', cmap=plt.cm.spectral)

plt.show()
```

![](http://scipy-lectures.github.io/_images/plot_greyscale_dilation_1.png)

Opening: erosion + dilation:

```python
>>> a = np.zeros((5,5), dtype=np.int)
>>> a[1:4, 1:4] = 1; a[4, 4] = 1
>>> a
array([[0, 0, 0, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 1, 1, 1, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 0, 0, 1]])
>>> # Opening removes small objects
>>> ndimage.binary_opening(a, structure=np.ones((3,3))).astype(np.int)
array([[0, 0, 0, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 1, 1, 1, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 0, 0, 0]])
>>> # Opening can also smooth corners
>>> ndimage.binary_opening(a).astype(np.int)
array([[0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0]])
```

应用：去处噪音
```python
square = np.zeros((32, 32))
square[10:-10, 10:-10] = 1
np.random.seed(2)
x, y = (32*np.random.random((2, 20))).astype(np.int)
square[x, y] = 1

open_square = ndimage.binary_opening(square)

eroded_square = ndimage.binary_erosion(square)
reconstruction = ndimage.binary_propagation(eroded_square, mask=square)
```

![](http://scipy-lectures.github.io/_images/plot_propagation_1.png)


Closing: dilation + erosion
```python
#TODO
```

![](http://scipy-lectures.github.io/_images/morpho_mat.png)

<h2 id="0fd36be3567167c262fae183a580aa7c"></h2>


###2.6.5. Feature extraction 特征提取

<h2 id="ea0f17b8c9b0298df7e75d7f009a9323"></h2>


#### 2.6.5.1. Edge detection 边缘检测
合成数据
```python
im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1

im = ndimage.rotate(im, 15, mode='constant')
im = ndimage.gaussian_filter(im, 8)
```

使用梯度算法（索贝尔）找到高强度变化：
```python
sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)
```

Sobel for noisy image
```python
im += 0.07*np.random.random(im.shape)

sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)
```

![](http://scipy-lectures.github.io/_images/plot_find_edges_1.png)

<h2 id="ff7de7467377d111993a153fc8d65657"></h2>


####2.6.5.2. Segmentation 分割

基于直方图的分割（无空间信息）

```python
n = 10
l = 256
im = np.zeros((l, l))
np.random.seed(1)
#(2,100)
points = l*np.random.random((2, n**2))
#points -> int,to modify im
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))

mask = (im > im.mean()).astype(np.float)
mask += 0.1 * im
img = mask + 0.2*np.random.randn(*mask.shape)
```

直方图
```python
hist, bin_edges = np.histogram(img, bins=60)
bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])

plt.plot(bin_centers, hist, lw=2)
```

```python
binary_img = img > 0.5

plt.imshow(binary_img, cmap=plt.cm.gray, interpolation='nearest')
```

![](http://scipy-lectures.github.io/_images/plot_histo_segmentation_1.png)

使用数学形态来clean up 结果

```python
# Remove small white regions
open_img = ndimage.binary_opening(binary_img)
# Remove small black hole
close_img = ndimage.binary_closing(open_img)

plt.imshow(open_img[:l, :l], cmap=plt.cm.gray)
plt.imshow(close_img[:l, :l], cmap=plt.cm.gray)

plt.imshow(mask[:l, :l], cmap=plt.cm.gray)
plt.contour(close_img[:l, :l], [0.5], linewidths=2, colors='r')
```

![](http://scipy-lectures.github.io/_images/plot_clean_morpho_1.png)

在这个例子中，我们使用的 谱聚类方法scikit学习，对粘连的对象分段

```python
from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering

l = 100
x, y = np.indices((l, l))

center1 = (28, 24)
center2 = (40, 50)
center3 = (67, 58)
center4 = (24, 70)
radius1, radius2, radius3, radius4 = 16, 14, 15, 14

circle1 = (x - center1[0])**2 + (y - center1[1])**2 < radius1**2
circle2 = (x - center2[0])**2 + (y - center2[1])**2 < radius2**2
circle3 = (x - center3[0])**2 + (y - center3[1])**2 < radius3**2
circle4 = (x - center4[0])**2 + (y - center4[1])**2 < radius4**2

# 4 circles
img = circle1 + circle2 + circle3 + circle4
mask = img.astype(bool)
img = img.astype(float)

img += 1 + 0.2*np.random.randn(*img.shape)
# Convert the image into a graph with the value of the gradient on
# the edges.
graph = image.img_to_graph(img, mask=mask)

# Take a decreasing function of the gradient: we take it weakly
# dependant from the gradient the segmentation is close to a voronoi
graph.data = np.exp(-graph.data/graph.data.std())

labels = spectral_clustering(graph, k=4, mode='arpack')
label_im = -np.ones(mask.shape)
label_im[mask] = labels
```

![](http://scipy-lectures.github.io/_images/image_spectral_clustering.png)


<h2 id="bda5dcbbc5b8462fcde1a64fcc8ffc35"></h2>


### 2.6.6. Measuring objects properties 测量对象属性
ndimage.measurements : 注意，结果和配图可能会有差异

合成数据
```python
n = 10
l = 256
im = np.zeros((l, l))
points = l*np.random.random((2, n**2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))
mask = im > im.mean()
```

分析 连接的组件 
标记链接的组件 : ndimage.label

```python
label_im, nb_labels = ndimage.label(mask)
nb_labels # how many regions?

plt.imshow(label_im, cmap=plt.cm.spectral)
```

![](http://scipy-lectures.github.io/_images/plot_synthetic_data_1.png)

计算每个区域的的尺寸，均值
```python
>>> sizes = ndimage.sum(mask, label_im, range(nb_labels + 1))
>>> sizes
array([    0.,   492.,   788.,  2148.,   915.,   241.,  2019.,  1188.,
         242.,   538.,   734.,  3125.,  1624.,  2010.,   246.,   212.,
         472.,   209.,   266.,   247.,  3271.,  1584.,  1325.,   223.])
>>> mean_vals = ndimage.sum(im, label_im, range(1, nb_labels + 1))
>>> mean_vals
array([  1.60063299,   2.40109415,   7.5472352 ,   3.4481412 ,
         0.60867412,   6.76071962,   4.15831579,   0.61179449,
         1.34596405,   2.36694138,  11.97698432,   5.93225634,
         6.72333268,   0.61850837,   0.79894359,   1.53091067,
         0.80212021,   0.71724808,   0.62082489,  11.34252465,
         5.05073462,   5.25842952,   0.80655554])
```

去除小的连接组件：

```python
mask_size = sizes < 1000
#这里不明白
remove_pixel = mask_size[label_im]  
remove_pixel.shape

label_im[remove_pixel] = 0
plt.imshow(label_im)      
```

现在，用 np.searchsorted 重新分配  标签：

```python
labels = np.unique(label_im)
label_im = np.searchsorted(labels, label_im)

plt.imshow(label_im, vmax=nb_labels, cmap=plt.cm.spectral)
```

![](http://scipy-lectures.github.io/_images/plot_measure_data_1.png)

查找感兴趣的封闭enclosing对象的区域：

```python
slice_x, slice_y = ndimage.find_objects(label_im==4)[0]
roi = im[slice_x, slice_y]
plt.imshow(roi)     
```

![](http://scipy-lectures.github.io/_images/plot_find_object_1.png)


