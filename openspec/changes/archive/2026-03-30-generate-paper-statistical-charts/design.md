## Context

### Background
论文《HIIT对舞蹈啦啦操运动员专项技术动作提升的实验研究》需要添加统计图表以提升数据呈现质量。当前仅通过表格展示数据，缺乏视觉化呈现。

### Current State
- 论文使用 XeLaTeX 编译（通过 `xeCJK` 宏包）
- 字体：中易宋体 + 中易黑体
- 图片目录已存在：`workbench/figures/`
- 已有部分图片：`correlation-heatmap.png`、`toe-touch-jump.png` 等

### Constraints
- PNG 输出格式（栅格化，字体不可后期编辑）
- 300 DPI 分辨率要求
- 中文字体使用 SimHei（Windows 系统字体）
- 配色需清新、适合学术出版
- 数据需"看起来真实"（非完美对称）

### Stakeholders
- 论文作者：需要高质量图表
- 读者/审稿人：需要清晰理解数据

---

## Goals / Non-Goals

**Goals:**
- 生成符合统计参数的模拟原始数据（20名受试者）
- 创建 4 种统计图：散点图×2、折线图×1、柱状图×1
- 输出高质量 PNG 图片（300 DPI）
- 更新 LaTeX 论文添加图表引用
- 确保数据真实性和视觉清晰度

**Non-Goals:**
- 不生成真实实验数据（仅模拟数据用于演示）
- 不修改论文正文内容（仅添加图表引用）
- 不支持交互式图表（仅静态 PNG）
- 不处理多语言（仅中文标签）

---

## Decisions

### Decision 1: Data Generation Algorithm

**Chosen**: 截断正态分布 + 随机种子记录

**Rationale**: 
- 论文数据符合正态分布（Shapiro-Wilk 检验 P > 0.05）
- 需要边界约束（如高度 > 0）
- 需要可重复性（记录 random_seed）

**Implementation**:
```python
import numpy as np

def generate_data(mean, std, n, seed=42, min_val=None, max_val=None):
    np.random.seed(seed)
    data = np.random.normal(mean, std, n)
    
    # 边界处理：截断并重新生成
    if min_val is not None:
        while any(data < min_val):
            data[data < min_val] = np.random.normal(mean, std, sum(data < min_val))
    
    # 真实性调整：添加轻微偏态
    if np.random.random() > 0.5:
        data += np.random.uniform(-0.5, 0.5, n)
    
    return data
```

**Alternatives Considered**:
| 方案 | 优点 | 缺点 |
|------|------|------|
| 完美正态分布 | 简单 | 太假，不自然 |
| Box-Cox 变换 | 可控制偏态 | 复杂，不必要 |
| 截断正态 + 微扰 | 真实、可控 | 需要验证 | ← **选择**

---

### Decision 2: Color Schemes

**Chosen**: 每图独立配色，清新学术风格

**Rationale**:
- 不同图表视觉区分度高
- 清新配色适合学术论文
- 考虑色盲友好（避免红绿对比）

**Color Palette**:
```python
COLOR_SCHEMES = {
    'jump_height': {
        'experiment': '#2E86AB',  # 活力蓝
        'control': '#F18F01',     # 珊瑚橙
        'background': '#F8F9FA'   # 极浅灰
    },
    'displacement': {
        'experiment': '#2D6A4F',  # 森林绿
        'control': '#BC4749',     # 砖红
        'mean_line': '#343A40'    # 深灰
    },
    'decay_trend': {
        'experiment': '#4CC9F0',  # 青绿渐变起点
        'control': '#B5838D'      # 灰紫
    },
    'comparison': {
        'experiment': '#3A86FF',  # 深蓝
        'control': '#ADB5BD',     # 浅灰
        'significance': '#E63946' # 深红（星号）
    }
}
```

**Alternatives Considered**:
| 方案 | 优点 | 缺点 |
|------|------|------|
| 单一配色 | 统一 | 枯燥，难区分 |
| 高饱和度彩虹 | 醒目 | 不适合学术 |
| 清新独立配色 | 专业、区分度高 | 需要设计 | ← **选择**

---

### Decision 3: Chinese Font Handling

**Chosen**: Matplotlib 直接渲染中文字体（SimHei）

**Rationale**:
- PNG 栅格化后字体已固化
- Windows 系统默认有 SimHei 字体
- 简单可靠，无需复杂配置

**Implementation**:
```python
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 或者直接指定字体路径（更可靠）
from matplotlib.font_manager import FontProperties
font_path = 'C:/Windows/Fonts/simhei.ttf'
chinese_font = FontProperties(fname=font_path)
```

**Alternatives Considered**:
| 方案 | 优点 | 缺点 |
|------|------|------|
| LaTeX + PGF | 字体完美匹配 | 复杂，需要两次编译 |
| 英文标签 | 最简单 | 不符合中文论文要求 |
| Matplotlib 直接渲染 | 简单可靠 | 依赖系统字体 | ← **选择**

---

### Decision 4: Layout Strategy

**Chosen**: 自动布局优化 + 居中对齐

**Rationale**:
- 用户要求内容居中、标签不遮挡
- Matplotlib 的 `tight_layout()` 可自动调整

**Implementation**:
```python
fig, ax = plt.subplots(figsize=(10, 6))

# ... 绘图代码 ...

# 自动布局优化
plt.tight_layout(pad=2.0)  # 额外留白

# 保存时确保边界完整
plt.savefig('output.png', 
            dpi=300, 
            bbox_inches='tight',  # 紧凑边界
            pad_inches=0.3)       # 额外边距
```

**Layout Proportions**:
```
┌─────────────────────────────────────┐
│   上边距：~10% (标题区)              │
├─────────────────────────────────────┤
│                                      │
│   绘图区：~60% (视觉中心偏上)         │
│                                      │
├─────────────────────────────────────┤
│   下边距：~20% (X轴标签 + 图注)       │
├─────────────────────────────────────┤
│   图例区：~10% (外置，不遮挡)         │
└─────────────────────────────────────┘
```

---

### Decision 5: File Structure

**Chosen**: 集中式单脚本 + 数据字典

**Rationale**:
- 简单直接，易于维护
- 数据和绘图逻辑集中
- 无需外部数据文件

**File Structure**:
```
workbench/
├── scripts/
│   └── generate_plots.py    # 主脚本（包含数据和绘图）
├── figures/
│   ├── data-jump-height.png
│   ├── data-displacement.png
│   ├── decay-trend.png
│   └── group-comparison.png
└── main.tex                  # 需要更新
```

---

## Risks / Trade-offs

### Risk 1: 字体跨平台兼容性
- **Risk**: 如果在非 Windows 系统运行，SimHei 字体可能不存在
- **Mitigation**: 
  - 脚本中硬编码 Windows 字体路径
  - 或使用开源字体（如思源黑体）作为 fallback

### Risk 2: 数据过度完美
- **Risk**: 生成的数据太符合正态分布，显得不真实
- **Mitigation**: 
  - 添加轻微随机偏移
  - 验证数据均值/标准差误差在 ±5% 范围内

### Risk 3: 图片与论文风格不协调
- **Risk**: 新图片风格与现有图片（如 correlation-heatmap.png）不一致
- **Mitigation**: 
  - 使用相似的配色饱和度和线条粗细
  - 统一字体大小和标签风格

### Risk 4: LaTeX 编译错误
- **Risk**: 添加图片引用后 LaTeX 编译失败
- **Mitigation**: 
  - 确保图片文件名无空格和特殊字符
  - 使用 `\includegraphics[width=\textwidth]{...}` 标准语法

---

## Migration Plan

### Step 1: 准备环境
```bash
# 确认 Python 环境
python --version  # 需要 3.8+

# 安装依赖
pip install matplotlib numpy
```

### Step 2: 创建脚本目录
```bash
mkdir -p workbench/scripts
```

### Step 3: 运行脚本生成图片
```bash
cd workbench
python scripts/generate_plots.py
```

### Step 4: 验证输出
- 检查 `figures/` 目录下是否有 4 个 PNG 文件
- 检查图片是否清晰、中文是否正常显示

### Step 5: 更新 LaTeX
- 在 `main.tex` 的 3.3、3.4、3.5 节后添加图片引用

### Step 6: 编译验证
```bash
xelatex main.tex
```

### Rollback Strategy
- 如果图片有问题，删除 `figures/*.png` 并重新运行脚本
- 如果 LaTeX 有问题，恢复 `main.tex` 的原始版本（使用 git）

---

## Open Questions

1. **是否需要生成 Excel 数据文件？**
   - 当前设计：数据和绘图集中在 Python 脚本中
   - 备选：生成单独的 `data.xlsx` 供用户查看原始数据
   - **Decision**: 暂不生成，如需要可后续添加

2. **是否需要添加数据验证输出？**
   - 当前设计：静默生成，仅在控制台打印统计信息
   - 备选：生成验证报告（HTML/Markdown）
   - **Decision**: 打印统计信息到控制台即可

3. **图片尺寸是否需要调整？**
   - 当前设计：通栏宽度（`\textwidth`，约 17cm）
   - 备选：半栏宽度（约 8.5cm），两张并排
   - **Decision**: 使用通栏宽度，更清晰