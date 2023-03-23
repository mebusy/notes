

# Setup Stable Diffusion WebUI on MacOSX


## Clone Repo

```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
```


In Folder `stable-diffusion-webui/models/Stable-diffusion/`, 

here we need to drop stable diffusion checkpoints or safe tensor files these are models that will actually be used to generate images.

For this the easiest place to download them is probably [hugging face](https://huggingface.co/runwayml/stable-diffusion-v1-5) if you want the original ones, but there are other websites that allow you to download modified and pre-tuned stable diffusion models. 


## hugging face

https://huggingface.co/runwayml/stable-diffusion-v1-5

check its `Files and versions` tab,  and search .ckpt files, select 1 to download, say `v1-5-pruned.ckpt`

After downloading , simply move it into the `stable-diffusion-webui/models/Stable-diffusion/` folder.

---

When you're using stable diffusion for image generation, it's mostly the models and things like that. 



## Launch WebUI


```bash
./webui.sh
```

When the server startup, access it from browser http://127.0.0.1:7860 .


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


# ControlNet Applications

set `Sampling Method` to **DPM++ SDE Karras** ?


## 1. Colorize line drawing.

1. drag line drawing to controlnet panel
2. use `canny` Preprocessor,  **Preview annotator result**
3. generate


## 2. Renovation of old game art assets

## 3. Build a white box scene let AI colorize it

## 4. 2次元转3次元

1. 使用 anything 生成2次元图片
2. 换 Chilloutmix ，开启 `Restore faces`
3. 如果生成的图片崩了，可以尝试
    - 加入 `LORA` in `Promt` field
    - 降低 canny 的 权重, 让AI 有更多的自由去发挥
    - 增加采样 `Sampling Steps`



# Misc

- 提示词生成 https://wolfchen.top/tag/




