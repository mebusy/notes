# 127.0.0.1_8787

> Exported from ChatGPT on 2026-11-10T08:01:19.236Z

## User

macos silicon 本地怎么部署 小米OCR 0.8B

## Assistant

在 Apple Silicon（M1/M2/M3/M4/M5）Mac 上部署 小米 Xiaomi-OCR-0（0.8B），我建议优先采用：

推荐方案 Ollama + Xiaomi-OCR-0 社区 BF16 模型 + 官方 Web Demo

这条路线已经有 Apple Silicon Mac 上的实际验证，不需要 NVIDIA GPU，也不需要 Docker。

Xiaomi-OCR-0 是基于 Qwen3.5-0.8B-Base 训练的文档理解模型，支持：

- 图片 OCR，输出 Markdown。
- 表格识别、公式识别（LaTeX）。
- PDF 文档解析。
- KIE：发票、票据等关键信息提取。
- VQA：针对图片内容提问。

注意：它不只是传统 OCR，而是一个视觉文档理解模型。GitHub+1

## 一、部署架构

浏览器 Web Demo

[http://127.0.0.1:8787](http://127.0.0.1:8787/?utm_source=chatgpt.com)

Xiaomi-OCR-0 项目

图像预处理 / Prompt / OCR 后处理

Ollama 推理服务

127.0.0.1:11434

Xiaomi-OCR-0 BF16

约 1.8GB，包含视觉投影器

为什么推荐 Ollama？

官方项目目前提供实验性的 Ollama 运行方案，并记录了 Apple Silicon 上的测试结果。仅仅下载模型还不够，官方 Demo/MCP 会负责图像预处理、提示词和解码参数。GitHub+1

## 二、安装 Ollama

如果已经安装 Ollama，可以跳过。

使用 Homebrew：

Bash

```
brew install --cask ollama
```

启动 Ollama App，或者：

Bash

```
ollama serve
```

检查服务：

Bash

```
ollama --version

curl http://127.0.0.1:11434/api/version
```

## 三、下载 Xiaomi-OCR-0

执行：

Bash

```
ollama pull longwayxu/xiaomi-ocr-0:bf16
```

模型约 1.8GB（约 1.6GiB）。

检查：

Bash

```
ollama list
```

注意：这是社区转换的 BF16 GGUF 模型包，不是小米官方原始 Safetensors 权重。GitHub+1

## 四、安装官方 Web Demo

克隆项目：

Bash

```
git clone https://github.com/SeerRay-Lab/Xiaomi-OCR-0.git

cd Xiaomi-OCR-0
```

创建 Python 环境：

Bash

```
python3 -m venv .venv

source .venv/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

Python 需要 3.10 或更高版本。

## 五、启动 OCR 服务

确保 Ollama 已经运行。

在项目目录下执行：

Bash

```
export XIAOMI_OCR_BACKEND=ollama

export XIAOMI_OCR_MODEL=longwayxu/xiaomi-ocr-0:bf16

export XIAOMI_OCR_LOCAL_URL=http://127.0.0.1:11434/v1

python demo/server.py --port 8787
```

浏览器访问：

Xiaomi OCR 本地网页

本地服务

# 127.0.0.1:8787

可以测试：

- 上传 PNG/JPG 图片。
- 上传 PDF。
- 整页文档解析。
- KIE 信息提取。
- VQA 图片问答。

以上是项目官方推荐的 Ollama 部署流程。GitHub+1

## 六、关于区域识别（Region Mode）

这里有一个容易忽略的地方：

Xiaomi-OCR-0 的区域识别还需要额外安装：

- PaddlePaddle
- PaddleX
- PP-DocLayoutV3

官方提供额外依赖：

Bash

```
pip install -r requirements-paddlex.txt
```

PaddlePaddle 需要根据 macOS 和 Python 环境单独选择安装版本。

如果暂时只需要整页 OCR、PDF、KIE 和 VQA，不需要安装这套额外依赖。GitHub+1

## 七、其他部署方案比较

| 方案 | Apple Silicon | 建议 |
| --- | --- | --- |
| Ollama BF16 | 有实测记录 | 首选 |
| llama.cpp GGUF | 可尝试 | 适合进一步调优 |
| MLX 原始权重 | 需要转换及适配 | 暂不推荐 |
| vLLM / SGLang | 主要面向兼容 GPU 环境 | 不推荐 Mac 原生部署 |

特别提醒：官方原始权重和社区 GGUF 转换版本不是完全相同的推理路径，不能简单认为输出精度完全一致。GitHub+1

## 我建议进一步确认你的 Mac 配置

不同统一内存容量会影响推理速度、上下文长度和并发能力。

1. Mac 芯片

M1 / M2M3 MaxM4 MaxM5 Max其他 Apple Silicon

2. 统一内存

16GB24GB32GB48GB64GB128GB

3. 主要用途

单张图片 OCR批量 OCR / PDF 文档处理作为本地 API 服务接入 Claude Code / MCP研究 MLX / llama.cpp 原生推理

我还可以进一步给你配置成一个本地 OCR HTTP API + MCP 服务，让其他本地程序直接调用，而不只是通过浏览器使用。

## User

我的 Mac 配置是 M4 Max，统一内存 24GB，主要用途是 批量 OCR / PDF 文档处理。请给出针对我的 Mac 的 Xiaomi-OCR-0 最佳部署方案，包括 Metal 加速、性能优化和完整测试命令。

## Assistant

针对你的 Apple Silicon M4 Max、24GB 统一内存，以及批量 OCR / PDF 文档处理需求，我建议采用：

首选部署方案 Ollama + Xiaomi-OCR-0 BF16 GGUF + 官方 Python OCR Pipeline

不建议一开始就折腾 MLX、vLLM 或 Docker。先把 Ollama 的 Metal 推理和 PDF 批处理跑通，再考虑性能优化。

有三个重要判断：

1. 0.8B 模型本身很小，24GB 统一内存足够运行。
2. Apple Silicon 上 Ollama 可以利用 Metal，不需要 CUDA。
3. PDF 批量处理的主要瓶颈通常不只是模型推理，还包括 PDF 渲染、图片预处理、页面分辨率和串行/并发调度。

另外，官方 README 将 Ollama 标注为实验性后端。官方的 Apple Silicon 验证使用了 Ollama 0.35.0 和 7 个样本，7 个样本的输出 token 数一致，但只有 5 个完整响应完全一致。因此不能把 BF16 标签理解成与官方 Hugging Face 推理完全等价。GitHub+1

## 一、推荐部署结构

批量 PDF / 图片输入

PDF、PNG、JPG、扫描件

Python 批处理调度

PDF 渲染、分辨率控制、任务队列

Xiaomi-OCR-0 官方 Pipeline

Prompt、图像预处理、Markdown 后处理

Ollama + Metal

BF16 GGUF 视觉语言模型

Markdown / JSON / 文件输出

我建议先部署整页模式（Whole-page），暂时不要安装 PaddleX 区域检测组件。普通文档、扫描件、手写内容都可以先用整页模式验证。官方 Demo 本身支持 PDF 页面渲染及解析。GitHub+1

## 二、安装 Ollama 和模型

### 1. 安装基础环境

建议使用 Homebrew：

Bash

```
brew install --cask ollama
```

检查 Mac 架构：

Bash

```
uname -m
# arm64

system_profiler SPHardwareDataType
```

检查 Ollama：

Bash

```
ollama --version
```

启动 Ollama。可以打开应用，也可以在终端运行：

Bash

```
ollama serve
```

如果已经通过 Ollama App 启动，就不要再启动第二个服务。

检查 API：

Bash

```
curl -s http://127.0.0.1:11434/api/version | python3 -m json.tool
```

### 2. 下载模型

Bash

```
ollama pull longwayxu/xiaomi-ocr-0:bf16
```

检查：

Bash

```
ollama list
```

预期能看到：

Plain text`NAME                         SIZE
longwayxu/xiaomi-ocr-0:bf16  ...`

建议先用 BF16，不要一开始就用 Q4。

原因是 OCR 的错误可能表现为一个汉字、数字、公式符号或表格单元格识别错误。对于文档归档、合同、财务票据，精度通常比节省几百 MB 内存更重要。

官方列出的社区 BF16 包约 1.8GB，包含视觉投影器。GitHub+1

## 三、Metal GPU 加速与内存优化

### 1. Metal 加速

Apple Silicon 上的 Ollama 使用 Metal 后端，不需要安装 CUDA，也不需要手动安装 NVIDIA 驱动。

启动模型后：

Bash

```
ollama run longwayxu/xiaomi-ocr-0:bf16
```

另开终端：

Bash

```
ollama ps
```

重点观察 `PROCESSOR` 一栏。

理想状态 `100% GPU`

如果显示 CPU/GPU 混合，则需要进一步排查内存、模型兼容性和 Ollama 运行状态。

### 2. 推荐运行参数

24GB 统一内存，我建议先采用以下配置：

| 参数 | 建议值 | 说明 |
| --- | --- | --- |
| 模型精度 | BF16 | 优先识别质量 |
| Context | 8192 | 先控制内存 |
| 并发推理 | 1 | 避免内存争抢 |
| 输出 Token | 4096 | 适合普通文档 |
| GPU | Metal | Apple Silicon |
| 模型常驻 | 开启 | 避免反复加载 |

设置 Ollama 环境变量：

Bash

```
launchctl setenv OLLAMA_NUM_PARALLEL 1
launchctl setenv OLLAMA_MAX_LOADED_MODELS 1
launchctl setenv OLLAMA_FLASH_ATTENTION 1
```

然后完全退出并重新启动 Ollama App，让环境变量生效。

注意：

- `OLLAMA_FLASH_ATTENTION` 是可选优化，不保证所有版本、模型都能获得性能提升。
- 不建议一开始就把并发调到 4 或 8。
- 8192 是初始优化目标，不是模型硬性限制。
- Ollama 的实际上下文长度还应通过运行配置和 API 检查确认。

可以使用：

Bash

```
ollama show longwayxu/xiaomi-ocr-0:bf16
```

以及：

Bash

```
ollama ps
```

## 四、安装 Xiaomi-OCR-0 官方项目

建议放在单独的工作目录：

Bash

```
mkdir -p ~/ai
cd ~/ai

git clone https://github.com/SeerRay-Lab/Xiaomi-OCR-0.git

cd Xiaomi-OCR-0
```

检查 Python：

Bash

```
python3 --version
```

建议使用 Python 3.11。

创建虚拟环境：

Bash

```
python3 -m venv .venv

source .venv/bin/activate

python -m pip install --upgrade pip setuptools wheel

pip install -r requirements.txt
```

这里先不要安装：

Bash

```
pip install -r requirements-paddlex.txt
```

因为这部分是区域检测的额外依赖，不是整页 OCR 必需的。官方也将它作为可选组件。GitHub+1

### 2. 配置 Ollama 后端

每次启动 Demo 前执行：

Bash

```
export XIAOMI_OCR_BACKEND=ollama

export XIAOMI_OCR_MODEL=longwayxu/xiaomi-ocr-0:bf16

export XIAOMI_OCR_LOCAL_URL=http://127.0.0.1:11434/v1
```

检查环境变量：

Bash

```
env | grep XIAOMI_OCR
```

应该得到：

Plain text`XIAOMI_OCR_BACKEND=ollama
XIAOMI_OCR_MODEL=longwayxu/xiaomi-ocr-0:bf16
XIAOMI_OCR_LOCAL_URL=http://127.0.0.1:11434/v1`

### 3. 启动 Web Demo

Bash

```
python demo/server.py --port 8787
```

浏览器访问：

[Xiaomi-OCR-0 本地 Web Demo](http://127.0.0.1:8787/?utm_source=chatgpt.com)

这个 Demo 已经集成官方 OCR Pipeline，支持：

- PDF 页面渲染。
- PDF 整页 OCR。
- 图片 OCR。
- Markdown 输出。
- KIE JSON 信息提取。
- OCR-VQA。

这也是我建议你首先使用的入口。GitHub+1

## 五、完整测试流程

我建议分三层测试：模型、Metal、文档解析。

### 测试 1：模型服务

Bash

```
curl -s http://127.0.0.1:11434/api/tags \
  | python3 -m json.tool
```

检查 OpenAI 兼容接口：

Bash

```
curl -s http://127.0.0.1:11434/v1/models \
  | python3 -m json.tool
```

### 测试 2：单张图片 OCR

准备一张图片：

Bash

```
mkdir -p ~/ai/ocr-test

# 将测试图片放在：
# ~/ai/ocr-test/test.png
```

直接通过 Ollama 的视觉接口进行冒烟测试：

Bash

```
cd ~/ai/Xiaomi-OCR-0

python3 - <<'PY'
import base64
import json
import urllib.request
from pathlib import Path

image_path = Path.home() / "ai/ocr-test/test.png"
model = "longwayxu/xiaomi-ocr-0:bf16"

image_data = base64.b64encode(image_path.read_bytes()).decode()

payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": "请完整识别图片中的文档内容，保留标题、段落、表格和公式，使用 Markdown 输出。",
            "images": [image_data]
        }
    ],
    "stream": False,
    "options": {
        "temperature": 0,
        "num_predict": 4096
    }
}

request = urllib.request.Request(
    "http://127.0.0.1:11434/api/chat",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(request, timeout=300) as response:
    result = json.load(response)

print(result["message"]["content"])
print("\n耗时：", result.get("total_duration", 0) / 1e9, "秒")
print("生成 Token：", result.get("eval_count", 0))
PY
```

这个测试直接调用模型，不经过官方 Demo 的图像预处理和专用 Prompt，因此主要用于验证模型、视觉输入和 GPU 推理是否正常。

### 测试 3：官方 Demo 测试 PDF

建议找一份包含以下内容的 PDF：

- 中文和英文混排。
- 两列排版。
- 表格。
- 数学公式。
- 页眉、页脚。
- 扫描图片。

在 Web Demo 上传 PDF，选择 Whole-page 模式，观察每页解析结果。

这一步才是验证官方完整 Pipeline 的测试。

## 六、批量 PDF 处理

这里需要区分两种方式：

方式 A：官方 Demo

适合先验证实际识别质量。支持 PDF 多页解析和进度展示。

方式 B：独立 Python 批处理

适合无人值守、大量 PDF、自动保存 Markdown。

官方仓库的 `evaluation_pipeline/e2e_img2md.py` 是围绕 vLLM 服务设计的，不能直接把它的 `--start_server` 参数用于 Ollama。GitHub+1

如果要使用 Ollama 做批量处理，可以通过兼容的视觉 API 编写独立调度器。下面给你一个可运行的基础版本。

### 1. 准备目录

Bash

```
mkdir -p ~/ai/ocr-batch/input
mkdir -p ~/ai/ocr-batch/output
```

把 PDF 放入 `input`。

### 2. 安装 PDF 渲染依赖

在项目虚拟环境中：

Bash

```
cd ~/ai/Xiaomi-OCR-0

source .venv/bin/activate

pip install pypdfium2 pillow
```

### 3. 创建批量处理脚本

创建 `batch_ocr.py`：

Python
    print(f"\nProcessing: {pdf_path.name}")
    output_dir = OUTPUT_DIR / pdf_path.stem    output_dir.mkdir(parents=True, exist_ok=True)
    document = pdfium.PdfDocument(str(pdf_path))    total = len(document)    all_pages = []
    start = time.perf_counter()
    for index in range(total):        page = document[index]        image_b64 = render_page(page)
        page_start = time.perf_counter()        markdown = recognize(image_b64)
        output_file = output_dir / f"page-{index + 1:04d}.md"        output_file.write_text(markdown, encoding="utf-8")
        all_pages.append(markdown)
        elapsed = time.perf_counter() - page_start        print(            f"  Page {index + 1}/{total}: "            f"{elapsed:.2f}s"        )
    combined = "\n\n---\n\n".join(all_pages)
    (output_dir / "document.md").write_text(        combined, encoding="utf-8"    )
    print(        f"Completed {pdf_path.name}: "        f"{total} pages, "        f"{time.perf_counter() - start:.2f}s"    )
def main():    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf_files = sorted(INPUT_DIR.glob("*.pdf"))
    if not pdf_files:        print(f"No PDF files in {INPUT_DIR}")        return
    print(f"Found {len(pdf_files)} PDF files")
    for pdf_path in pdf_files:        try:            process_pdf(pdf_path)        except Exception as error:            print(f"FAILED: {pdf_path.name}: {error}")
if __name__ == "__main__":    main()

### 4. 执行批处理

Bash

```
cd ~/ai/Xiaomi-OCR-0

source .venv/bin/activate

python batch_ocr.py
```

输出目录：

Plain text`~/ai/ocr-batch/output/
├── document-A/
│   ├── page-0001.md
│   ├── page-0002.md
│   └── document.md
├── document-B/
│   ├── page-0001.md
│   └── document.md`

默认安全配置 这个脚本按 PDF、按页面串行处理，不会同时加载多个模型，也不会同时向 Ollama 提交多个推理任务。

注意： 这是独立 API 批处理版本，不是官方完整 Pipeline 的等价替代。它没有复用官方的图像归一化、专用非思考 Prompt 和后处理，因此表格、公式和复杂版式的结果可能不同。正式归档建议优先使用官方 Demo/MCP Pipeline。GitHub+1

## 七、针对 24GB 内存的性能调优

建议分三个阶段进行，不要一次性增加所有参数。

### 第一阶段：稳定运行

| 参数 | 初始值 |
| --- | --- |
| PDF 渲染 DPI | 150 |
| 最大图片边长 | 2048 px |
| Ollama 并发 | 1 |
| 模型 | BF16 |
| num_ctx | 8192 |
| num_predict | 4096 |
| 页面处理 | 串行 |

对于扫描版 PDF，150 DPI 通常是不错的起点。

对于小字号、密集公式，可以测试 200 DPI，但需要注意官方 Pipeline 对图片尺寸还有预处理限制。

### 第二阶段：提高吞吐量

建议按照下面顺序优化：

1. 模型常驻内存，避免每个 PDF 重新加载。
2. PDF 渲染和 OCR 推理分离。
3. 先把 PDF 页面渲染成图片，缓存到磁盘。
4. 保持推理并发为 1，测量每页耗时。
5. 如果 GPU 利用率和内存余量都允许，再测试并发 2。

对于上面的独立批处理脚本，可以在 API 参数中增加：

Python"options": {    "temperature": 0,    "num_ctx": 8192,    "num_predict": 4096},"keep_alive": "30m"

注意，增大上下文不一定会提高吞吐量。对于大量独立 PDF 页面，通常没有必要使用特别大的上下文。

### 第三阶段：识别质量优化

我建议准备一套固定测试集：

| 测试材料 | 重点 |
| --- | --- |
| 中文扫描合同 | 中文字符准确率 |
| 财务报表 | 数字和表格 |
| 技术论文 | LaTeX 公式 |
| 双栏 PDF | 阅读顺序 |
| 小字体文档 | 分辨率 |
| 手写笔记 | 手写识别 |

每次调整 DPI、模型量化、Prompt，都使用相同测试集比较。

## 八、常见问题排查

| 现象 | 处理办法 |
| --- | --- |
| Ollama 无法加载模型 | 检查 Ollama 版本和模型兼容性 |
| CPU 占用很高 | 检查 ollama ps 的 GPU 分配 |
| OCR 速度很慢 | 检查图片分辨率和 Metal 状态 |
| 公式识别不准确 | 提高图片质量，比较 BF16 与其他版本 |
| 表格内容错乱 | 考虑官方 Region Mode |
| PDF 内存占用很高 | 降低 DPI，逐页释放 PDF 页面 |
| 中文输出重复 | 检查 Prompt 和模型输出预算 |

可以用下面的命令监控内存：

Bash

```
memory_pressure
```

同时打开 macOS 活动监视器，观察：

- Ollama 进程内存。
- GPU 使用率。
- 内存压力。
- Swap 使用量。

## 九、最终推荐配置

Xiaomi-OCR-0 本地部署

推荐配置

模型

Xiaomi-OCR-0

模型精度

BF16 GGUF

推理引擎

Ollama

GPU 后端

Metal

图片长边

2048 px

推理并发

1

软件组件

- Ollama：模型推理
- Python 3.11：任务调度
- pypdfium2：PDF 页面渲染
- Pillow：图像预处理
- Xiaomi-OCR-0：文档理解
- Markdown：结果保存

### 官方资料

建议保留这几个地址，后续升级时很有用：

1. [Xiaomi-OCR-0 官方仓库](https://github.com/xiaomi-research/Xiaomi-OCR-0?utm_source=chatgpt.com)
2. [Ollama 后端部署与验证](https://github.com/xiaomi-research/Xiaomi-OCR-0/blob/main/OLLAMA.md?utm_source=chatgpt.com)
3. [Web Demo 和 PDF 处理](https://github.com/xiaomi-research/Xiaomi-OCR-0/blob/main/demo/README.md?utm_source=chatgpt.com)
4. [官方评测 Pipeline](https://github.com/xiaomi-research/Xiaomi-OCR-0/blob/main/evaluation_pipeline/README.md?utm_source=chatgpt.com)

我特别建议你下一步关注一个问题： 对于大量 PDF，究竟应该使用整页 OCR，还是先做版面检测，再对各个区域并行 OCR。

官方的两阶段 Pipeline 就是为此设计的。不过它的区域检测依赖 PaddleX，而 Ollama 负责视觉语言模型推理，两者是独立组件。对于印刷排版规整的文档，两阶段值得测试；对于手写、古籍和不规则排版，优先整页识别。GitHub+1
