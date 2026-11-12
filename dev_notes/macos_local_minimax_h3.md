# Vpipe 与 minimax h3 部署

**User:** @mebusy

## @mebusy

Mac Mini M4 24G   vpipe + MiniMax H3  快速流程

## Copilot

**Mac mini M4／24GB 快速上手：**用 [vpipe-workbench](https://github.com/zero5phh-ops/vpipe-workbench) 的本机网页界面，比先搭 API 更直接。

```bash
brew install ffmpeg
git clone https://github.com/zero5phh-ops/vpipe-workbench.git
cd vpipe-workbench
./start.sh
```

浏览器打开 `http://127.0.0.1:8765`，先进入「设置检查」安装 vpipe 和 MiniMax H3 模型，再选 H3、输入提示词，先用界面提供的最短时长和较低分辨率试跑。模型下载约 **115GB**，安装期间建议预留约 **185GB** 空间；24GB 内存够用，但生成仍可能较慢。H3 有单独的使用许可，商用前请先核对。

## @mebusy

下载的模型存放在哪里？

## Copilot

默认存放在 `~/vpipe-work/models`，也就是 `/Users/你的用户名/vpipe-work/models`。在终端运行 `open ~/vpipe-work/models` 可直接用 Finder 打开。

如果设置了 `VPIPE_WORK` 环境变量，模型则在该目录下的 `models/` 文件夹里。

## @mebusy

我是初学者，请给一下制作8秒左右视频的一些教程/建议

## Copilot

可以先用 **vpipe-workbench** 做一条“单镜头、8 秒”的练习片。先把目标定简单：一个主体、一个动作、一个镜头，不要一开始就做多场景叙事。

**操作步骤**

1. 打开工作台，确认 H3 模型已安装；模型下载较大，先确保磁盘空间充足。
2. 选择 **MiniMax H3**，时长设为 **8 秒**。如果界面提供帧数选项，选 **192 帧**（24 fps 下约 8 秒）。
3. 先选较低分辨率试做，例如 **832×480 或 960×540**；画面比例按用途选，普通横屏用 **16:9**，手机竖屏用 **9:16**。如果有质量档位，先选 Draft/草稿。
4. 贴入下面的提示词并生成；第一轮先不加台词、复杂参考图或多个动作。
5. 看结果后，每次只改一个点再试，例如动作太快就写“缓慢、平稳”，主体不清楚就补充外观特征。满意后再提高分辨率重做。

**提示词示例**

> 傍晚的海边，一只橘猫沿着湿润的沙滩缓慢向前走，海浪轻轻涌来又退去。单一连续镜头，低机位从侧后方平稳跟拍，猫咪动作自然，主体始终清晰，暖色日落光，写实电影感，背景简洁。不要切镜，不要字幕或文字，不要出现其他动物。

提示词可以按这个顺序写：**主体和外观 → 做什么动作 → 在哪里/什么时间 → 镜头怎么拍 → 光线与风格 → 不希望出现什么**。尽量避免“快速转身又跳起、镜头环绕并切换场景”这类互相叠加的要求。

生成速度会受分辨率、时长和设置影响，**8 秒可能需要较长时间**；M4 的实际耗时会因设置而异。生成时接上电源，尽量不要同时运行其他大型图形或 AI 任务。

## @mebusy

”5秒视频， G1版 变形金刚，太空桥边上， 龙型钢索 张口咬中 大力神左腿“ ， 提示词怎么写？

## Copilot

可以保留这个动作构图，但我不能帮你直接复刻《变形金刚》G1 或大力神的具体角色。可以改成原创机甲版本，提示词这样写：

> **5秒，原创复古科幻二维动画。**太空桥边缘，紫蓝色能量漩涡翻涌。一台原创的重型工程机甲背对漩涡站立，装甲为暗橄榄绿与铜色，造型硬朗、细节清晰。突然，一条带有龙首形夹颚的机械钢索从画面侧面猛然甩出，张开金属颚，一口咬住机甲的左小腿并缠紧。机甲踉跄失衡，腿部迸出火花，镜头轻微震动；钢索收紧，能量光映在装甲上。单一连续镜头，动作顺序清楚，主体完整可见，复古科幻动画质感，粗线条和块面阴影。不要切镜，不要字幕或标志，不要肢体变形或额外肢体。

如果工作台有“负面提示词”栏，可填：`文字，标志，切镜，肢体畸形，额外肢体，模糊主体`。

## @mebusy

Reference  只能选择 Text Only ,  First/Last Frame,   Reference Images  是灰色的，不能选择， 所以没法设置 参考图

## Copilot

我先确认一下工作台里这个选项变灰的条件，以及可以怎么启用。

已经定位到原因：你的工作台没有检测到 Ref2VA 和对应的 Pika 权重。我会核对适合你当前版本的安装方式。

原因找到了：你的 H3 主模型已安装，但 `ref2va` 和 `pika_ref2va` 都是 **false**。当前工作台版本需要这两项才能启用 **Reference Images**。

**安装方法：**

1. 打开 **Vpipe Manager**，在 Settings 中把 Work Directory 设为 `~/vpipe-work`，与工作台使用同一个目录。
2. 下载官方准备文件：[Ref2VA 4-bit](https://raw.githubusercontent.com/tgo-app-dev/vpipe/main/docs/pipelines/prepare-minimax-h3-ref2va-4bit.vpipeline) 和 [Pika H3 Flex](https://raw.githubusercontent.com/tgo-app-dev/vpipe/main/docs/pipelines/prepare-pika-h3-flex.vpipeline)。如果浏览器显示文本，用“另存为”保存为 `.vpipeline` 文件。
3. 在 Vpipe Manager 的 Web UI 里打开 **Pipeline Manager → Load**，加载 Ref2VA 文件并点击 **Start**。完成后，同样运行 Pika 文件。
4. 刷新工作台，再查看 [模型状态](http://127.0.0.1:8765/api/config)：确认 `ref2va` 和 `pika_ref2va` 都变为 `true`。

**注意磁盘空间：**Ref2VA 4-bit 最终约额外占用 44GB，准备时还需要下载原始权重和更多临时空间；若之前的原始权重已删除，下载量可能更大。不要手动删除模型文件。

**暂时不安装也能用图：**选择 **First/Last Frame**，把图片放在首帧位置，就能让视频从这张图开始。但它与 Reference Images 不同：首帧是画面起点，参考图主要用于提供人物、物品或风格。

## @mebusy

"加载 Ref2VA 文件并点击 Start" ,  显示timeout。 本机访问 hugginface 需要走代理， 是不是因为 vpipe-manager 没有设置网络代理的原因 ？ 但是 vpip-manage 怎么设置 proxy ？

## Copilot

有可能是代理问题，但要看超时日志才能确定。我先核对 Vpipe Manager 是否支持系统代理或代理环境变量。

**有可能是代理问题**，但 timeout 也可能来自下载服务器或连接中断。Vpipe Manager 没有看到单独的代理设置项；可以尝试从终端带代理启动它。

1. 先在你的代理软件中查找 **HTTP 代理端口**。下面以 `7890` 为例，请替换成实际端口。
2. 打开“终端”，先测试代理能否访问 Hugging Face：

```bash
curl -I --max-time 20 -x http://127.0.0.1:7890 https://huggingface.co
```

如果返回 `HTTP/2 200`、`302` 等响应，说明连接基本通了；如果报错，先检查代理软件和端口。

3. **完全退出** Vpipe Manager（菜单栏选择“退出”，不只是关闭窗口），然后在终端运行：

```bash
env http_proxy=http://127.0.0.1:7890 \
    https_proxy=http://127.0.0.1:7890 \
    no_proxy=localhost,127.0.0.1 \
    "/Applications/Vpipe Manager.app/Contents/MacOS/vpipe"
```

保持这个终端窗口打开，在 Manager 中重新启动 Web UI，再加载 Ref2VA 文件并点击 Start。这个代理设置只对本次这样启动的 Manager 生效。

如果仍然 timeout，请把**失败时的完整错误日志**贴出来，并说明你代理软件的 HTTP 端口；不要发送代理密码或 Hugging Face token。
