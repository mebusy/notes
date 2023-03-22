

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





