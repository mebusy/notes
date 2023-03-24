[](...menustart)

- [Setup Stable Diffusion WebUI on MacOSX](#ae15fc2ed3548c84b92cbb52898d6eb7)
    - [Clone Repo](#dec579fa4d31c03d332a55c5c32cf269)
    - [hugging face](#91ddd3b498dbe7d54ecf81dc92f91954)
    - [Launch WebUI](#897e5bd19064757752f2be32ad6ae085)
    - [If you're running into issues with vram on Mac](#1c6f600f5887bc1c2d3dfa68482cfd15)
- [Common Stable Diffusion Models](#a468b5b0c36dd1927cf5dd3f1eefe0c1)
    - [ControlNet](#7cb4aa7a91fc1cc1d459f6a5894e3057)
- [ControlNet Applications](#cfb37e714b3e1fd518db2be4856929de)
    - [1. Colorize line drawing.](#b66fd2984ab3a2e74d605887406c6b56)
    - [2. Renovation of old game art assets](#18dab3e145498bda6582f2beaf48dea3)
    - [3. Build a white box scene let AI colorize it](#8b948f32c4ed771f282f59c7bf7d4b4a)
    - [4. 2次元转3次元](#3c5bb82f62c70aa1cd3aaf85bc24efa0)
- [Misc](#74248c725e00bf9fe04df4e35b249a19)

[](...menuend)


<h2 id="ae15fc2ed3548c84b92cbb52898d6eb7"></h2>

# Setup Stable Diffusion WebUI on MacOSX


<h2 id="dec579fa4d31c03d332a55c5c32cf269"></h2>

## Clone Repo

```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
```


In Folder `stable-diffusion-webui/models/Stable-diffusion/`, 

here we need to drop stable diffusion checkpoints or safe tensor files these are models that will actually be used to generate images.

For this the easiest place to download them is probably [hugging face](https://huggingface.co/runwayml/stable-diffusion-v1-5) if you want the original ones, but there are other websites that allow you to download modified and pre-tuned stable diffusion models. 


<h2 id="91ddd3b498dbe7d54ecf81dc92f91954"></h2>

## hugging face

https://huggingface.co/runwayml/stable-diffusion-v1-5

check its `Files and versions` tab,  and search .ckpt files, select 1 to download, say `v1-5-pruned.ckpt`

After downloading , simply move it into the `stable-diffusion-webui/models/Stable-diffusion/` folder.

---

When you're using stable diffusion for image generation, it's mostly the models and things like that. 



<h2 id="897e5bd19064757752f2be32ad6ae085"></h2>

## Launch WebUI


```bash
./webui.sh
```

When the server startup, access it from browser http://127.0.0.1:7860 .


<h2 id="1c6f600f5887bc1c2d3dfa68482cfd15"></h2>

## If you're running into issues with vram on Mac

PS. do NOT do it if you're not in trouble.


```bash
vi webui-user.sh
```

uncomment this line

```
#export COMMANDLINE_ARGS=""
```

and add following arguments


```
export COMMANDLINE_ARGS="--medvram --opt-split-attention --skip-torch-cuda-test --no-half --use-cpu all"
```


<h2 id="a468b5b0c36dd1927cf5dd3f1eefe0c1"></h2>

# Common Stable Diffusion Models

1. Anything
    - 二次元
    - https://huggingface.co/andite/anything-v4.0/
2. Dreamshaper
    - 美漫厚涂库, 油画风格
3. Chilloutmix
    - 真人照片库
4. LORA (built-in ?)
    - 个人训练库


<h2 id="7cb4aa7a91fc1cc1d459f6a5894e3057"></h2>

## ControlNet

ControlNet is a neural network structure to control diffusion models by adding extra conditions.  You can do specific control over image generation by adding control lines. 


https://github.com/Mikubill/sd-webui-controlnet  This extension is for AUTOMATIC1111's Stable Diffusion web UI.

- Install
    1. Open "Extensions" tab.
    2. Open "Install from URL" tab in the tab.
    3. Enter URL `https://github.com/Mikubill/sd-webui-controlnet.git` into "URL for extension's git repository".
    4. Press "Install" button.
    5. Reload/Restart Web UI.

- MacOS Support
    - To use this extension with mps and normal pytorch, currently you may need to start WebUI with `--no-half`.

- Download controlnet models from hugging face
    - https://huggingface.co/lllyasviel/ControlNet/tree/main/models
    - say, control_sd15_canny.pth
    - install to `extensions/sd-webui-controlnet/models`


<h2 id="cfb37e714b3e1fd518db2be4856929de"></h2>

# ControlNet Applications

set `Sampling Method` to **DPM++ SDE Karras** ?


<h2 id="b66fd2984ab3a2e74d605887406c6b56"></h2>

## 1. Colorize line drawing.

1. drag line drawing to controlnet panel
2. use `canny` Preprocessor,  **Preview annotator result**
3. generate


<h2 id="18dab3e145498bda6582f2beaf48dea3"></h2>

## 2. Renovation of old game art assets

<h2 id="8b948f32c4ed771f282f59c7bf7d4b4a"></h2>

## 3. Build a white box scene let AI colorize it

<h2 id="3c5bb82f62c70aa1cd3aaf85bc24efa0"></h2>

## 4. 2次元转3次元

1. 使用 anything 生成2次元图片
2. 换 Chilloutmix ，开启 `Restore faces`
3. 如果生成的图片崩了，可以尝试
    - 加入 `LORA` in `Promt` field
    - 降低 canny 的 权重, 让AI 有更多的自由去发挥
    - 增加采样 `Sampling Steps`



<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>

# Misc

- 提示词生成 https://wolfchen.top/tag/




