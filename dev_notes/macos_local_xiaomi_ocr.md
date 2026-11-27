[](...menustart)

- [127.0.0.1_8787](#8c8945239977990c11187982a91b4f85)
    - [User](#8f9bfe9d1345237cb3b2b205864da075)
    - [Assistant](#9b1363da9503dbd4142c0274a88e8d4b)
    - [一、部署架构](#713acbcbb23cfbfdaca2b4d24ea7ecf8)
    - [二、安装 Ollama](#ed1e2512cdd14743c6f35939e1d7ccf0)
    - [三、下载 Xiaomi-OCR-0](#febea67e869005239d2f7e8f31d8096f)
    - [四、安装官方 Web Demo](#c7707e565f5ad50349f2542fbdddaae3)
    - [五、启动 OCR 服务](#dfc0b0ba87ee70d346a42b04df31ca8a)
- [127.0.0.1:8787](#10a77df303a738645da299f060c6749f)
    - [六、关于区域识别（Region Mode）](#d3409829c439c227c76ae1c90d776856)
    - [五、完整测试流程](#2e5f0c19316f8ceb0c6b8928cfdedea4)
        - [测试 1：模型服务](#13b49758be213db01afa99916b8d2a62)
        - [测试 2：单张图片 OCR](#0af4b7079444fbbc290f61b65fa78d11)
    - [六、批量 PDF 处理](#6e016ab5785d33d4cce5c6e8de202575)
        - [1. 准备目录](#5cb4113e07e60afe02d3ed86f8060ad9)
        - [2. 安装 PDF 渲染依赖](#cac58a75f25940ffb074f2a920d78ad0)
        - [3. 创建批量处理脚本](#b1de4a13f17efa101e83c525e88eb4e0)
        - [4. 执行批处理](#542c92e634dac9513ce9a822f8a3005f)

[](...menuend)


<h2 id="8c8945239977990c11187982a91b4f85"></h2>

# 127.0.0.1_8787

> Exported from ChatGPT on 2026-11-10T08:01:19.236Z

<h2 id="8f9bfe9d1345237cb3b2b205864da075"></h2>

## User

macos silicon 本地怎么部署 小米OCR 0.8B

<h2 id="9b1363da9503dbd4142c0274a88e8d4b"></h2>

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

<h2 id="713acbcbb23cfbfdaca2b4d24ea7ecf8"></h2>

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

<h2 id="ed1e2512cdd14743c6f35939e1d7ccf0"></h2>

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

<h2 id="febea67e869005239d2f7e8f31d8096f"></h2>

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

<h2 id="c7707e565f5ad50349f2542fbdddaae3"></h2>

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

<h2 id="dfc0b0ba87ee70d346a42b04df31ca8a"></h2>

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

<h2 id="10a77df303a738645da299f060c6749f"></h2>

# 127.0.0.1:8787

可以测试：

- 上传 PNG/JPG 图片。
- 上传 PDF。
- 整页文档解析。
- KIE 信息提取。
- VQA 图片问答。

以上是项目官方推荐的 Ollama 部署流程。GitHub+1

<h2 id="d3409829c439c227c76ae1c90d776856"></h2>

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


<h2 id="2e5f0c19316f8ceb0c6b8928cfdedea4"></h2>

## 五、完整测试流程

我建议分三层测试：模型、Metal、文档解析。

<h2 id="13b49758be213db01afa99916b8d2a62"></h2>

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

<h2 id="0af4b7079444fbbc290f61b65fa78d11"></h2>

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


<h2 id="6e016ab5785d33d4cce5c6e8de202575"></h2>

## 六、批量 PDF 处理

这里需要区分两种方式：

方式 A：官方 Demo

适合先验证实际识别质量。支持 PDF 多页解析和进度展示。

方式 B：独立 Python 批处理

适合无人值守、大量 PDF、自动保存 Markdown。

官方仓库的 `evaluation_pipeline/e2e_img2md.py` 是围绕 vLLM 服务设计的，不能直接把它的 `--start_server` 参数用于 Ollama。GitHub+1

如果要使用 Ollama 做批量处理，可以通过兼容的视觉 API 编写独立调度器。下面给你一个可运行的基础版本。

<h2 id="5cb4113e07e60afe02d3ed86f8060ad9"></h2>

### 1. 准备目录

Bash

```
mkdir -p ~/ai/ocr-batch/input
mkdir -p ~/ai/ocr-batch/output
```

把 PDF 放入 `input`。

<h2 id="cac58a75f25940ffb074f2a920d78ad0"></h2>

### 2. 安装 PDF 渲染依赖

在项目虚拟环境中：

Bash

```
cd ~/ai/Xiaomi-OCR-0

source .venv/bin/activate

pip install pypdfium2 pillow
```

<h2 id="b1de4a13f17efa101e83c525e88eb4e0"></h2>

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

<h2 id="542c92e634dac9513ce9a822f8a3005f"></h2>

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

