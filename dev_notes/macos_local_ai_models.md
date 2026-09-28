# Mac Mini M4 pro Local LLM


我参考了 2026 年近期的 Apple Silicon 实测，以及 Ollama/MLX 对 Apple Silicon 的最新支持。尤其值得注意的是，Ollama 现在已经有基于 MLX 的 Apple Silicon backend，并针对 coding agent 做了缓存和推理优化。[Ollama+1](https://ollama.com/blog/mlx-performance?utm_source=chatgpt.com)

## 🏆 M4 Pro 24GB 本地 AI 实战排行榜

### 总榜

| 排名 | 模型 | 大致定位 | M4 Pro 24GB | 我的评价 |
| --- | --- | --- | --- | --- |
| 🥇 | Qwen3-Coder 30B-A3B | Coding / Agent | ⭐⭐⭐⭐⭐ | 最值得装 |
| 🥈 | GPT-OSS 20B | Reasoning / Coding | ⭐⭐⭐⭐⭐ | 综合最强之一 |
| 🥉 | Gemma 4 12B | General / Multimodal / Coding | ⭐⭐⭐⭐⭐ | 速度/能力平衡极好 |
| 4 | Qwen3.5 27B | General / Reasoning | ⭐⭐⭐ | 能跑，但 24GB 很紧 |
| 5 | Gemma 3 27B | General / Vision | ⭐⭐⭐ | 能力不错，但不够轻快 |
| 6 | Qwen3 14B | General / Coding | ⭐⭐⭐⭐⭐ | 非常舒服的日常模型 |
| 7 | Qwen3 8B | 快速助手 | ⭐⭐⭐⭐⭐ | 秒回型工具 |
| 8 | Qwen3-Coder 3B | Coding / autocomplete | ⭐⭐⭐⭐⭐ | 小而快 |

其中一个比较有参考价值的 M4 Pro 24GB 实测表显示：Qwen3 8B 约 **52 tok/s**、Qwen3 14B 约 **29 tok/s**、Gemma 3 12B 约 **31 tok/s**；这基本就是这台机器非常舒服的甜点区间。[GitHub](https://github.com/weklund/mlx-coding-bench?utm_source=chatgpt.com)

---

# 🥇 第一名：Qwen3-Coder 30B-A3B

**如果你主要是写代码，我第一推荐它。**

关键在这里：

> **30B ≠ 30B 全部计算。**

它是 MoE：

```
Qwen3-Coder
       │
       ├── 总参数 ~30B
       │
       └── Active parameters ~3B
```

所以它的特点非常适合 Mac：

```
模型容量：大
实际计算：小
```

目前针对 24GB Mac 的测试/经验里，它大约是 **17–21GB 内存级别**，速度约 **30 tok/s 左右**；有些配置需要调整 GPU wired memory 才能尽量避免 CPU spill。[GitHub+1](https://github.com/imagewize/ollama-opencode-setup/blob/main/docs/MLX-RUNTIME.md?utm_source=chatgpt.com)

### 最适合

```
Claude Code
Codex
OpenCode
Aider
Cursor 类 agent
```

比如：

> “把这个 Rust module 重构一下。”

它可以：

```
读代码
 ↓
理解结构
 ↓
修改多个文件
 ↓
运行 cargo test
 ↓
看错误
 ↓
继续修改
```

这才是我认为本地 LLM **真正开始产生生产力**的地方。

---

# 🥈 第二名：GPT-OSS 20B

这个我非常推荐你试。

它的定位不是单纯：

> chatbot

而是：

> **reasoning + tool use + coding**

所以比较适合：

```
复杂 bug
算法
架构设计
代码 review
数学/逻辑
Agent
```

尤其如果你的任务是：

> “帮我理解这个问题，然后自己一步一步推导。”

它比很多“小而快”的模型靠谱。

近期的本地模型测试也把 GPT-OSS 20B 列为 24GB Mac 上值得考虑的主力模型。[BSWEN](https://docs.bswen.com/blog/2026-03-25-best-local-llm-mac-mini-m4/?utm_source=chatgpt.com)

### 我会这样分工：

```
Qwen3-Coder 30B
       ↓
      写代码

GPT-OSS 20B
       ↓
   想问题 / Debug
```

这个组合非常好。

---

# 🥉 第三名：Gemma 4 12B

这个其实可能是：

> **24GB Mac 最舒服的“日常模型”。**

原因很简单：

```
12B
 ↓
内存压力低
 ↓
速度快
 ↓
还能保持相当不错的 intelligence
```

而且 Gemma 4 的一个优势是 **multimodal**。

也就是说以后你可以：

```
截图
 ↓
Gemma 4
 ↓
理解 UI / 图片 / 文档
```

而不只是纯文本。

近期用户在 M4 24GB 上的实际体验也显示，Gemma 4 12B 在 coding issue detection 上表现不错，只是某些 inference backend 下速度会偏慢。[Reddit](https://www.reddit.com/r/ollama/comments/1vi72aq/which_ollama_mlxgguf_model_is_best_for_macbook_m4/?utm_source=chatgpt.com)

---

# ④ Qwen3.5 27B

这个我会定义为：

> **“24GB 能跑，但我不建议作为默认模型。”**

因为它已经开始碰：

```
24GB
 ↓
macOS
 ↓
模型
 ↓
KV cache
 ↓
工具调用
```

的极限。

尤其你如果：

```
32K context
+
Agent
+
tool calling
+
代码库
```

很容易把内存吃得非常满。

所以：

### 单纯聊天

👍

### 长上下文 coding agent

⚠️

### 一直后台跑

❌ 不太舒服


# ⑥ Qwen3 14B

这个反而是我非常推荐的（如果其他app开的比较多，内存压力大)。

甚至我认为：

> **如果你只想安装一个“不折腾”的模型，它可能是最舒服的。**

实际 M4 Pro 24GB 测试约：

**29 tok/s**

而且只占约：

**9.3GB RAM**

[GitHub](https://github.com/weklund/mlx-coding-bench?utm_source=chatgpt.com)

这意味着：

```
Mac
├── macOS
├── VS Code
├── Browser
├── Docker
├── Ollama
└── Qwen3 14B
```

基本没什么压力。


## 最后给你一个“安装优先级”

如果你现在就准备搞：

### 第一梯队

```
🥇 Qwen3-Coder 30B-A3B
🥈 GPT-OSS 20B
🥉 Gemma 4 12B
```

### 第二梯队

```
Qwen3 14B
Qwen3 8B
```


**尤其是你这种程序员用途，我会优先把 Mac mini 变成一个“本地 coding agent server”，而不是本地 ChatGPT。**

如果你愿意，我下一步可以直接给你一套：

**「M4 Pro 24GB 本地 AI 开发环境」**

从 `Ollama + MLX → Qwen3-Coder → Claude Code/OpenCode → 让 AI 自己改代码、跑测试、修 bug`，给你一套可以直接复制执行的配置。

## User

从 `Ollama + MLX → Qwen3-Coder → OpenCode → 让 AI 自己改代码、跑测试、修 bug`，给你一套可以直接复制执行的配置。

## Assistant

可以。我给你一套我认为适合 **M4 Pro 24GB + macOS + Rust/C++/Go 项目**的方案。

先纠正一个关键点：**现在 Ollama 在 Apple Silicon 上已经有 MLX backend，但 MLX 支持仍处于 preview/快速演进状态**。Ollama 官方明确把 OpenCode、Claude Code、Codex 等 coding agents 列为 MLX backend 的目标场景。[Ollama+1](https://ollama.com/blog/mlx?utm_source=chatgpt.com)

另外，当前 OpenCode 已经可以**自动发现本机 Ollama 模型**，默认连接 `127.0.0.1:11434`，所以实际上不需要手工写一大堆 provider 配置。[OpenCode](https://opencode.ai/v2/docs/models?utm_source=chatgpt.com)

---

# 一、最终架构

我建议你最终搞成：

```
                         Mac mini M4 Pro 24GB
                                  │
                                  │
                              Ollama
                                  │
                              MLX backend
                                  │
                     ┌────────────┴────────────┐
                     │                         │
             Qwen3-Coder 30B-A3B          Qwen3 14B
                     │                         │
                     └────────────┬────────────┘
                                  │
                              OpenCode
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
                   Git          Shell          Files
                    │             │             │
                    └─────────────┼─────────────┘
                                  │
                              Your repo
                                  │
                         ┌────────┴────────┐
                         │                 │
                    cargo test          git diff
                    cmake/test           npm test
```

最终你坐在终端里说：

```
修复这个 bug。
```

OpenCode 可以：

```
读代码
  ↓
定位问题
  ↓
修改文件
  ↓
运行测试
  ↓
看到 compiler error
  ↓
继续修改
  ↓
重新测试
  ↓
告诉你结果
```

这才是这台 Mac mini 跑本地 LLM 最有意思的地方。

---

# 二、第一步：安装 Ollama

如果还没安装：

```
brew install ollama
```


```
ollama list
```

---

# 三、确认 Ollama 的 MLX backend

这里需要特别注意：

现在的 Ollama 已经把 MLX engine 集成进去。官方文档显示，Apple Silicon 上的 Ollama 会利用 unified memory，并针对 coding agents 做 cache 优化。[Ollama+1](https://ollama.com/blog/mlx?utm_source=chatgpt.com)

先确认版本：

```
ollama --version
```

建议使用当前最新版。

然后：

```
ollama serve
```


检查 API：

```
curl http://localhost:11434/api/tags
```

应该能看到：

```
{
  "models": [...]
}
```

---

# 四、先装一个“主力模型”

我建议第一步不要同时装 5 个。

直接：

```
ollama pull qwen3-coder:30b
# 或
ollama pull gpt-oss:20b
```

然后：

```
ollama run qwen3-coder:30b
```

测试：

```
写一个 Rust 函数，实现一个 3x3 matrix 的 D4 canonicalization。
```

如果模型能正常回答：

```
/bye
```

退出。

---

# 五、但是：24GB 不要一上来开 128K context

这是你这台机器最重要的 tuning。

OpenCode 官方对 Ollama 有一个特别重要的提示：

> 如果 tool calling 不正常，可以提高 Ollama 的 `num_ctx`，建议从 **16K–32K** 开始。[OpenCode+1](https://opencode.ai/docs/zh-cn/providers/?utm_source=chatgpt.com)

所以我建议：

```
num_ctx = 32768
```

而不是：

```
num_ctx = 128000
```

原因是：

```
模型 weights
+
KV cache
+
OpenCode tools
+
你的 source code
+
macOS
+
其他应用
```

全都要吃 unified memory。

---

# 六、给 Qwen3-Coder 设置一个专门的 Modelfile

新建：

```
mkdir -p ~/ai/models
cd ~/ai/models
```

创建：

```
nano Qwen3-Coder.modelfile
```

内容：

```
FROM qwen3-coder:30b

PARAMETER num_ctx 32768
PARAMETER temperature 0.2
PARAMETER top_p 0.9
```

Gpt-Oss coder 配置

```config
FROM gpt-oss:20b

# 推荐：48GB M4 Pro 从 32K 起；24GB 改为 16384；64GB+ 可改 49152 或 65536
PARAMETER num_ctx 32768

# 代码任务偏确定性：减少“花样”和无谓猜测
PARAMETER temperature 0.2
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER min_p 0.05
PARAMETER repeat_penalty 1.05

# 防止一次任务无限生成；复杂修改可在客户端临时提高
PARAMETER num_predict 4096

SYSTEM """
你是资深软件工程师，协助本地代码开发。

工作方式：
- 先阅读并理解用户提供的代码、错误、约束和项目结构；不确定时明确说明假设。
- 优先给出小而安全、可验证的改动，避免无关重构。
- 修改代码时说明：改了什么、为什么改、如何测试、可能的边界情况。
- 除非用户明确要求，不要编造不存在的文件、API、依赖版本或测试结果。
- 对涉及删除数据、生产环境、密钥、权限或外部副作用的操作，先提示风险并要求确认。
- 输出代码时保持与现有项目的语言、风格和格式一致。
"""
```


然后：

```
ollama create qwen3-coder-local -f Qwen3-Coder.modelfile

ollama create gpt-oss-local -f GptOss20b.modelfile
```

检查：

```
ollama list
```

应该出现：

```
qwen3-coder-local
```

测试：

```
ollama run qwen3-coder-local
```

---

# 七、为什么 temperature 我建议 0.2？

Coding agent 和聊天不一样。

聊天：

```
temperature 0.7
```

可以比较活泼。

Coding：

```
temperature 0.1 ~ 0.3
```

通常更合适。

因为我们希望：

```
稳定
可重复
少胡思乱想
少乱改代码
```

而不是：

```
“我觉得我们可以尝试一种全新的架构 😄”
```

😂

---

# 八、安装 OpenCode

这里建议直接使用官方安装方式，而不是固定某个旧 npm 版本。

[OpenCode 官方安装文档](https://opencode.ai/docs/?utm_source=chatgpt.com)

如果你用 Homebrew，可以先：

```
brew install opencode
```

然后：

```
opencode --version
```

如果 brew 里的版本明显落后，则按照 OpenCode 官方安装方式安装最新版。

---

# 九、进入你的项目

例如：

```
cd ~/src/my-project
```

然后：

```
opencode
```

第一次启动后：

```
/models
```

你应该能看到：

```
ollama/qwen3-coder-local
```

因为现在 OpenCode 会自动从本机 Ollama server 发现模型。[OpenCode](https://opencode.ai/v2/docs/models?utm_source=chatgpt.com)

选择它。

---

# 十、如果没有自动发现

这种情况下手工配置。


```
vi ~/.config/opencode/opencode.json
```

根据当前 OpenCode 文档，可以配置 Ollama：

```
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://127.0.0.1:11434/v1"
      },
      "models": {
        "qwen3-coder-local": {
          "name": "Qwen3-Coder 30B A3B"
        }
      }
    }
  },
  "model": "ollama/qwen3-coder-local"
}
```

这是 OpenCode 官方支持的 Ollama/OpenAI-compatible 配置方式。[OpenCode+1](https://opencode.ai/docs/zh-cn/providers/?utm_source=chatgpt.com)

不过**优先尝试自动发现**，因为新版 OpenCode 已经原生支持这个流程。[OpenCode](https://opencode.ai/v2/docs/models?utm_source=chatgpt.com)

---

# 十一、第一次千万不要直接让它改代码

先让它读。

启动：

```
opencode
```

然后：

```
分析一下这个项目的整体结构。

不要修改任何文件。

告诉我：
1. 项目的入口在哪里
2. 核心模块有哪些
3. 测试在哪里
4. 如果我要修改 XXX，应该从哪里开始
```

这一步非常重要。

你先观察：

```
它能不能正确理解 repo？
```

如果连 repo 都理解错了：

> **先不要让它自动修改。**

---

# 十二、然后开始真正的 Agent 模式

例如 Rust：

```
检查这个项目当前的测试。

先运行 cargo test。

如果有失败：
1. 分析失败原因
2. 找到相关源码
3. 修复问题
4. 再运行 cargo test

不要修改测试来掩盖问题。
```

这时候才开始真正有意思。

OpenCode 本身就是面向 agentic coding 的工具，可以调用 shell、读取文件、修改文件等；它的本地 Ollama 集成就是为了这种使用方式。[OpenCode+1](https://opencode.ai/docs/zh-cn/providers/?utm_source=chatgpt.com)

---

# 十三、我特别建议你建立一个 AGENTS.md

这是整个系统里非常值得做的一件事情。

项目：

```
my-project/
├── AGENTS.md
├── src/
├── tests/
├── Cargo.toml
└── ...
```

创建：

```
nano AGENTS.md
```

例如：

```
# Project Instructions

## Language

This is a Rust project.

Use modern stable Rust.

## Code Style

Prefer simple and idiomatic Rust.

Do not introduce unnecessary abstractions.

Avoid unsafe unless absolutely necessary.

## Testing

Before considering a change complete:

    cargo test

For formatting:

    cargo fmt --check

For linting:

    cargo clippy --all-targets --all-features -- -D warnings

## Git

Do not commit changes automatically.

Do not modify tests merely to make them pass.

When fixing a bug:

1. Reproduce it first.
2. Identify the root cause.
3. Make the smallest reasonable change.
4. Run tests.
5. Show the resulting diff.
```

这样以后每次 OpenCode 进入这个 repo：

```
OpenCode
    ↓
读取 AGENTS.md
    ↓
知道你的规则
```

这个效果非常好。

---

# 十四、然后给它一个真正的任务

比如你之前那个 matrix 项目。

你可以直接：

```
检查 canonicalMatrixU32 的实现。

目标：

1. 找出所有可能的 correctness bug
2. 检查 8 个 D4 transform 是否正确
3. 检查 compose table
4. 检查 inverse table
5. 添加必要的单元测试
6. 运行 cargo test

先分析，不要修改。
```

它分析完以后：

```
开始修复。

要求：
- 最小修改
- 不改变 public API
- 添加 regression test
- cargo fmt
- cargo test
```

然后它开始：

```
read
 ↓
edit
 ↓
cargo test
 ↓
error
 ↓
edit
 ↓
cargo test
 ↓
pass
```

**这才是 Qwen3-Coder 在你机器上的真正价值。**

---

# 十五、再装第二个模型

等第一套工作了，再：

```
ollama pull qwen3:14b
```

于是：

```
qwen3-coder-local
        ↓
coding agent

qwen3:14b
        ↓
快速 general purpose
```

我甚至建议以后让 OpenCode：

```
简单任务 → Qwen3 14B
复杂 coding → Qwen3-Coder
```

---

# 十六、还有一个很重要的技巧：别让 30B 模型负责所有事情

例如：

```
“这个 JSON 文件格式化一下”
```

没必要用 30B。

```
Qwen3 14B
```

就够。

但是：

```
“为什么这个 Rust async task 偶尔死锁？”
```

再：

```
Qwen3-Coder 30B-A3B
```

这样你的 Mac 会舒服很多。

---

# 十七、24GB 的推荐参数

我给你的第一版配置就是：

```
                 M4 Pro
                  24GB
                   │
                 Ollama
                   │
                  MLX
                   │
        ┌──────────┴──────────┐
        │                     │
 Qwen3-Coder 30B-A3B      Qwen3 14B
        │                     │
    32K context            32K context
        │                     │
        └──────────┬──────────┘
                   │
                OpenCode
```

### 不建议

```
128K context
+
30B
+
Chrome 30 tabs
+
Docker
+
Xcode
+
VS Code
```

😂

24GB 会直接开始内存压力。

---

# 十八、如何判断是不是“跑在 GPU / MLX”

你可以观察：

```
ollama ps
```

以及：

```
sudo powermetrics --samplers gpu_power -i 1000
```

或者直接观察：

```
Activity Monitor
    ↓
Memory
```

重点不是 CPU 使用率。

Apple Silicon 的 unified memory 架构下：

```
CPU
GPU
Neural Engine
    ↓
共享 memory
```

所以你看到：

```
CPU 20%
```

并不意味着：

> “AI 没用 GPU。”

---

# 十九、给你一个“一键启动”脚本

以后你可以：

```
~/bin/local-ai.sh
```

内容：

```
#!/bin/bash

set -e

echo "=== Ollama ==="

if ! curl -s http://127.0.0.1:11434/api/tags >/dev/null; then
    echo "Ollama is not running."
    echo "Start it with: open -a Ollama"
    exit 1
fi

echo
echo "=== Models ==="

ollama list

echo
echo "=== Current processes ==="

ollama ps

echo
echo "=== Starting OpenCode ==="

opencode
```

：

```
chmod +x ~/bin/local-ai.sh
```

以后：

```
cd ~/src/my-project
~/bin/local-ai.sh
```

就行。

---

# 二十、最终我建议你这样使用

你每天真正工作的流程：

```
                  你
                   │
                   ▼
              OpenCode
                   │
                   ▼
          Qwen3-Coder 30B
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
        Read      Edit     Shell
          │        │        │
          └────────┼────────┘
                   ▼
                 Tests
                   │
             ┌─────┴─────┐
             │           │
           PASS         FAIL
             │           │
             ▼           ▼
           Done       Analyze
                         │
                         ▼
                       Fix
                         │
                         └──────→ Tests
```

这已经不是：

> **“我在 Mac 上玩一个本地 ChatGPT。”**

而是：

> **“我有一个住在 Mac mini 里的 junior developer。”**

这就是我认为 **M4 Pro 24GB 最值得做的本地 AI 工作流**。

---

### 但我会再加一个非常重要的升级

**不要把 OpenCode 永远锁死在本地模型。**

OpenCode 本身支持很多 provider，也支持自定义 OpenAI-compatible endpoint。[OpenCode](https://opencode.ai/v2/docs/providers?utm_source=chatgpt.com)

所以最终可以做成：

```
                    OpenCode
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Ollama       OpenAI       Anthropic
       本地模型       云模型        云模型
          │            │            │
       便宜/私有       最强          最强
          │            │            │
          └────────────┼────────────┘
                       │
                    同一个 Agent
```

这样你可以先让 **Qwen3-Coder 本地跑**。

碰到：

> “这个问题它明显不会。”

直接切到云端模型。

**代码库、工具、OpenCode workflow 都不用换。**

这比“本地 AI vs 云端 AI”二选一合理得多。

另外，如果你想把这套东西做得更像一个真正的**家庭 AI server**，下一步还可以把 **Mac mini + Ollama + OpenCode 做成一个局域网 AI 服务**，然后 MacBook/iPad 上都能调用；不过这一步需要单独处理 Ollama 的监听地址、局域网访问和安全认证，不能直接把 `11434` 裸暴露到局域网。

## User

如果使用kilo 替代 opencode， 有哪些需要修改的地方？

## Assistant

可以。实际上如果换成 **Kilo Code**，你前面那套架构**几乎不用改**，因为 Kilo CLI 现在本身就是 OpenCode 的 fork，并且支持相同的配置体系。[Kilo+1](https://kilo.ai/docs/code-with-ai/platforms/cli?utm_source=chatgpt.com)

真正需要改的主要是：

> **`opencode` → `kilo`，配置文件 `opencode.json` → `kilo.json[c]`，以及一些 Kilo 特有的 agent / provider 配置。**

而且 Kilo 对 Ollama 有**原生 provider**，所以我反而建议你不要走 OpenAI-compatible 的绕路。[GitHub](https://github.com/kilo-org/kilocode/blob/main/packages/kilo-docs/pages/ai-providers/ollama.md?utm_source=chatgpt.com)

---

# 1. 最终架构不变

还是：

```
                         Mac mini M4 Pro 24GB
                                  │
                                  ▼
                                Ollama
                                  │
                           Apple Silicon / MLX
                                  │
                     ┌────────────┴────────────┐
                     │                         │
              Qwen3-Coder 30B              Qwen3 14B
                     │                         │
                     └────────────┬────────────┘
                                  │
                               Kilo CLI
                                  │
                  ┌───────────────┼───────────────┐
                  ▼               ▼               ▼
                Files           Shell            Git
                  │               │               │
                  └───────────────┼───────────────┘
                                  ▼
                              Your repo
                                  │
                         ┌────────┴────────┐
                         ▼                 ▼
                    cargo test          git diff
```

所以：

**Ollama、模型、MLX 那部分完全不用因为 Kilo 改动。**

---

# 2. 安装 Kilo

如果你之前按照我的方案装过 OpenCode：

```
brew install opencode
```

现在可以不用它了。

Kilo CLI 官方目前的安装包是：

```
npm install -g @kilocode/cli
```

[Kilo](https://kilo.ai/docs/code-with-ai/platforms/cli?utm_source=chatgpt.com)

所以：

```
npm uninstall -g opencode
npm install -g @kilocode/cli
```

检查：

```
kilo --version
```

---

# 3. Ollama 完全不变

继续：

```
open -a Ollama
```

确认：

```
curl http://127.0.0.1:11434/api/tags
```

然后：

```
ollama list
```

应该有：

```
qwen3-coder:30b
qwen3:14b
```

Kilo 官方目前明确支持：

```
ollama/<model_name>
```

例如：

```
ollama/qwen3-coder:30b
```

并默认连接：

```
http://localhost:11434/v1
```

不需要 API key。[GitHub](https://github.com/kilo-org/kilocode/blob/main/packages/kilo-docs/pages/ai-providers/ollama.md?utm_source=chatgpt.com)

---

# 4. Kilo 配置文件改成 `kilo.json`

这是和 OpenCode 最主要的区别之一。

全局：

```
~/.config/kilo/kilo.json
```

项目：

```
./kilo.json
```

或者：

```
./.kilo/kilo.json
```

现在 Kilo 官方文档也是这样定义的。[Kilo+1](https://kilo.ai/docs/code-with-ai/platforms/cli?utm_source=chatgpt.com)

所以我之前让你创建的：

```
opencode.json
```

建议改成：

```
kilo.json
```

---

# 5. 最简单的配置

其实第一版我建议你只写：

```
{
  "$schema": "https://kilo.ai/config.json",

  "provider": {
    "ollama": {
      "baseURL": "http://127.0.0.1:11434/v1"
    }
  },

  "model": "ollama/qwen3-coder:30b"
}
```

这就够了。

Kilo 官方的 Ollama 配置也是这个思路。[GitHub](https://github.com/kilo-org/kilocode/blob/main/packages/kilo-docs/pages/ai-providers/ollama.md?utm_source=chatgpt.com)

然后：

```
cd ~/src/my-project
kilo
```

进入以后选择：

```
ollama/qwen3-coder:30b
```

---

# 6. 但我更推荐显式告诉 Kilo：32K context

这一点非常重要。

Kilo 官方特别提醒：

> Ollama 默认 context 太短，建议至少 **32K**；context 越大，占用内存越多。[GitHub](https://github.com/kilo-org/kilocode/blob/main/packages/kilo-docs/pages/ai-providers/ollama.md?utm_source=chatgpt.com)

所以你的 M4 Pro 24GB，我建议：

```
{
  "$schema": "https://kilo.ai/config.json",

  "provider": {
    "ollama": {
      "baseURL": "http://127.0.0.1:11434/v1",

      "models": {
        "qwen3-coder:30b": {
          "name": "Qwen3-Coder 30B",
          "tool_call": true,
          "limit": {
            "context": 32768,
            "output": 8192
          }
        }
      }
    }
  },

  "model": "ollama/qwen3-coder:30b"
}
```

Kilo 官方的 custom Ollama model 配置就是使用 `tool_call`、`limit.context`、`limit.output` 这种字段。[GitHub](https://github.com/kilo-org/kilocode/blob/main/packages/kilo-docs/pages/ai-providers/ollama.md?utm_source=chatgpt.com)

---

# 7. 这里有一个容易混淆的地方

这个：

```
"limit": {
    "context": 32768
}
```

**不是在 Ollama 里面真正分配 32K。**

它主要告诉：

> **Kilo：这个模型允许我管理多大的 context。**

真正 Ollama 的 context 仍然涉及：

```
num_ctx
```

所以如果你要确保 Ollama 本身真的按照 32K 工作，可以检查/设置对应的模型配置。

例如：

```
Ollama
    │
    │ num_ctx = 32768
    ▼
Qwen3-Coder
    │
    ▼
Kilo
    │
    │ limit.context = 32768
    ▼
Agent
```

两边最好保持一致。

---

# 8. Kilo 比 OpenCode 多一个我很喜欢的东西：Profiles / Agents

这其实是我觉得你**值得从 OpenCode 换到 Kilo 的地方**。

你可以把不同工作模式分开。

比如：

```
Kilo
 │
 ├── coder
 │
 ├── reviewer
 │
 ├── debugger
 │
 └── architect
```

然后：

### coder

```
读代码
修改
运行测试
```

### reviewer

```
只读
不修改
寻找 bug
```

### debugger

```
运行测试
分析错误
修改
再次运行
```

### architect

```
只分析
不修改
设计方案
```

对于本地模型，这种约束尤其有用。

因为本地 20B/30B 模型相比顶级云模型，更容易在 agent loop 里面“自作聪明”。

---

# 9. `AGENTS.md` 也继续保留

这个：

```
AGENTS.md
```

不用改。

例如：

```
# Project Instructions

## Language

This is a Rust project.

Use modern stable Rust.

## Code Style

Prefer simple and idiomatic Rust.

Avoid unnecessary abstractions.

Avoid unsafe unless absolutely necessary.

## Testing

Before considering a change complete:

    cargo fmt --check

    cargo test

    cargo clippy --all-targets --all-features -- -D warnings

## Git

Do not commit automatically.

Do not modify tests merely to make them pass.

When fixing a bug:

1. Reproduce it first.
2. Identify the root cause.
3. Make the smallest reasonable change.
4. Run tests.
5. Show the resulting diff.
```

这个对 Kilo 一样适用。

---

# 10. 然后第一次测试不要直接让它改

进入：

```
cd ~/src/my-project
kilo
```

输入：

```
分析这个项目。

不要修改任何文件。

告诉我：

1. 项目结构
2. 程序入口
3. 核心模块
4. 测试在哪里
5. 如果我要修改 XXX，应该从哪里开始
```

看它能不能正确理解。

---

# 11. 然后测试真正的 Agent loop

例如：

```
检查当前项目。

先运行：

cargo test

如果测试失败：

1. 找到失败测试
2. 分析 root cause
3. 找到相关源码
4. 修改源码
5. 再运行 cargo test
6. 如果仍然失败，继续分析和修复

不要修改测试来掩盖 bug。

完成以后告诉我：
- root cause
- 修改了什么
- cargo test 结果
- git diff 摘要
```

如果模型能够稳定完成：

```
read
 ↓
shell
 ↓
edit
 ↓
shell
 ↓
edit
 ↓
test
 ↓
PASS
```

那么：

**恭喜，你的 M4 Pro 已经变成一台本地 coding agent machine 了。**

---

# 12. 我会对之前的方案做一个重要修改

之前我给你的方案是：

```
Ollama
 ↓
Qwen3-Coder
 ↓
OpenCode
```

如果现在选 Kilo，我会改成：

```
                         Kilo
                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
         Local Ollama   Cloud API    Other API
             │
       ┌─────┴─────┐
       ▼           ▼
 Qwen3-Coder    Qwen3
    30B          14B
```

也就是说：

> **Kilo 作为统一 Agent 层，Ollama 只是其中一个 provider。**

这点很重要。

Kilo 本身支持很多 provider，包括 Ollama、LM Studio、OpenAI-compatible endpoint、Anthropic、OpenAI、Gemini、OpenRouter 等。[Kilo](https://kilo.ai/docs/ai-providers?utm_source=chatgpt.com)

---

# 13. 所以你以后甚至可以这样玩

比如：

```
                    Kilo
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
        Local       OpenAI      Anthropic
       Ollama
          │
   Qwen3-Coder
```

### 普通任务

```
ollama/qwen3:14b
```

### Coding

```
ollama/qwen3-coder:30b
```

### 极难问题

```
Claude / GPT
```

而：

```
Files
Shell
Git
MCP
AGENTS.md
```

这些 Agent 层面的东西都不变。

---

# 14. 还有一个 Kilo 特别适合你的地方

你之前问过：

> Mac mini 能不能当 AI server？

**Kilo + Ollama 非常适合做这件事。**

比如：

```
                   Mac mini
                 M4 Pro / 24GB
                      │
                   Ollama
                      │
                Qwen3-Coder
                      │
                    Kilo
                      │
             ┌────────┼────────┐
             │        │        │
           MacBook   SSH      VSCode
```

不过这里要区分：

**Ollama 可以作为网络服务被其他机器调用；Kilo 不一定需要部署在 Mac mini 上。**

我更推荐：

```
MacBook
   │
   │ SSH / HTTP
   ▼
Mac mini
   │
 Kilo/Ollama
   │
Qwen3-Coder
```

或者：

```
MacBook
   │
 Kilo
   │
   │ HTTP
   ▼
Mac mini
   │
 Ollama
```

第二种其实更漂亮。

这样：

> **Mac mini 专门负责 AI inference，MacBook 负责开发。**

---

## 最后，我会这样选

如果你的目标就是：

> **“我想让 M4 Pro 24GB 真正成为我的本地 AI 程序员。”**

我现在更推荐：

```
              MacBook
                 │
                 │
               Kilo
                 │
                 │ HTTP
                 ▼
          ┌─────────────┐
          │ Mac mini    │
          │ M4 Pro 24GB │
          └──────┬──────┘
                 │
              Ollama
                 │
                MLX
                 │
        ┌────────┴────────┐
        │                 │
 Qwen3-Coder 30B       Qwen3 14B
        │
        ▼
     coding
     agent
```

**Kilo 和 OpenCode 在底层能力上不是“完全不同的东西”——Kilo CLI 官方明确说它是 OpenCode 的 fork。**所以从 OpenCode 切到 Kilo，最大的变化不是 Agent 能力，而是**配置/provider/生态层面的选择**。[Kilo](https://kilo.ai/docs/code-with-ai/platforms/cli?utm_source=chatgpt.com)

而且 Kilo 官方现在**直接推荐 Ollama 做本地模型 provider**，所以对于你这个 M4 Pro 24GB 场景，我会优先采用：

> **Kilo 原生 Ollama provider → `qwen3-coder:30b` → 32K context → AGENTS.md → Agent 自动执行 shell/test/git**

而不是再套一层 OpenAI-compatible。

[Kilo Code 官方 Ollama 配置文档](https://kilo.ai/docs/ai-providers/ollama?utm_source=chatgpt.com)

[Kilo CLI 官方文档](https://kilo.ai/docs/code-with-ai/platforms/cli?utm_source=chatgpt.com)


~/.config/kilo/local.json

```config
{
  "$schema": "https://app.kilo.ai/config.json",

  // 主 agent 模型
  "model": "ollama/qwen25-coder-14b-q5",

  // 防止 small model 回落到 Kilo Gateway / 云模型
  "small_model": "ollama/qwen25-coder-14b-q5",

  "provider": {
    "ollama": {
      "options": {
        "baseURL": "http://127.0.0.1:11434/v1",
        "timeout": 1200000
      },

      "models": {
        "qwen25-coder-14b-q5": {
          "name": "Qwen2.5-Coder 14B Q5 — Local Kilo",

          // 没有这个，Kilo 可能把模型按纯文本模型处理，
          // 无法可靠发起 read/edit/bash 等 agent 工具调用。
          "tool_call": true,

          // 必须与 Ollama Modelfile 中的 num_ctx 一致。
          "limit": {
            "context": 32768,
            "output": 4096
          }
        }
      }
    }
  },

  // 对小模型而言，尽早压缩旧对话，避免工具输出撑爆 8K 窗口。
  "compaction": {
    "auto": false,  // auto true 会在每次对话后压缩，可能失败
    "threshold_percent": 65,
    "prune": true,
    "tail_turns": 2
  }
}
```

