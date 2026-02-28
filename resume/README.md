# 简历管理指南

## 📁 文件结构

```
resume/
├── README.md                  # 本文件
├── resume_template.md         # 简历模板（参考）
├── resume.md                  # 当前主简历
├── resume_cn.pdf              # 中文PDF版本
├── resume_en.pdf              # 英文PDF版本
├── versions/                  # 历史版本存档
│   ├── resume_2024_Q1.pdf
│   └── resume_2024_Q2.pdf
└── custom/                    # 针对不同公司的定制版本
    ├── accenture.md
    ├── microsoft.md
    └── goldman_sachs.md
```

---

## 🚀 快速开始

### 1. 复制模板创建你的简历
```bash
cd "/Users/boom/Desktop/my_bussiness/resume"
cp resume_template.md resume.md
vim resume.md  # 修改为你的信息
```

### 2. 生成PDF（方法A - 在线工具）
1. 打开 [Dillinger](https://dillinger.io/)
2. 复制粘贴 `resume.md` 内容
3. 点击 "Export" → "PDF"

### 3. 生成PDF（方法B - 本地工具）
```bash
# 安装pandoc（首次使用）
brew install pandoc
brew install --cask basictex  # LaTeX引擎

# 生成PDF
pandoc resume.md -o resume.pdf --pdf-engine=xelatex \
  -V mainfont="PingFang SC" \
  -V geometry:margin=2cm
```

### 4. 版本控制
```bash
# 提交更新
git add resume.md
git commit -m "Update: Add new project experience"
git push origin main

# 创建存档版本
cp resume.pdf "versions/resume_$(date +%Y%m%d).pdf"
```

---

## 📝 日常使用工作流

### 场景1：更新简历（常规修改）
```bash
# 1. 编辑简历
vim resume.md

# 2. 生成PDF
pandoc resume.md -o resume.pdf --pdf-engine=xelatex

# 3. 提交到Git
git add resume.md resume.pdf
git commit -m "Update: Add XX company experience"
git push origin main
```

### 场景2：针对特定公司定制
```bash
# 1. 复制主简历
cp resume.md custom/accenture.md

# 2. 针对性修改（突出相关经验）
vim custom/accenture.md

# 3. 生成定制版PDF
pandoc custom/accenture.md -o custom/accenture.pdf --pdf-engine=xelatex

# 4. 提交
git add custom/accenture.md custom/accenture.pdf
git commit -m "Add: Accenture customized resume"
git push origin main
```

### 场景3：季度存档
```bash
# 每季度结束，创建存档
cp resume.pdf "versions/resume_2024_Q1.pdf"
git add versions/
git commit -m "Archive: Q1 2024 resume"
git push origin main
```

---

## 🎨 简历模板推荐

### 在线工具（无需安装）

| 工具 | 特点 | 链接 |
|------|------|------|
| **Resume.io** | 模板丰富，拖拽编辑 | https://resume.io |
| **Canva** | 设计精美，中文支持好 | https://www.canva.cn |
| **超级简历** | 专为中国求职者设计 | https://www.wondercv.com |
| **Markdown Resume** | Markdown在线转PDF | https://mszep.github.io/pandoc_resume/ |

### 开源工具（本地使用）

```bash
# 方案A: Pandoc + 模板
git clone https://github.com/mszep/pandoc_resume.git
cd pandoc_resume
make resume.pdf

# 方案B: LaTeX模板
git clone https://github.com/posquit0/Awesome-CV.git
cd Awesome-CV/examples
xelatex resume.tex

# 方案C: HTML简历
git clone https://github.com/sproogen/modern-resume-theme.git
```

---

## 📊 Markdown vs Word 对比

| 特性 | Markdown | Word |
|------|----------|------|
| **版本控制** | ✅ 完美（可看每行改动） | ❌ 差（只知道改了） |
| **文件大小** | ✅ 小（几KB） | ⚠️ 大（几百KB） |
| **学习成本** | ✅ 低（30分钟上手） | ✅ 低（都会用） |
| **排版灵活性** | ⚠️ 中等 | ✅ 高 |
| **多人协作** | ✅ 好（Git分支） | ⚠️ 需要其他工具 |
| **跨平台** | ✅ 完美 | ⚠️ 格式可能变 |
| **专业度** | ✅ 技术岗位加分 | ✅ 传统行业认可 |

---

## 💡 最佳实践

### 1. 命名规范
```bash
✅ 好的命名
resume_张三_数据分析师_2024.pdf
resume_ZhangSan_DataAnalyst_EN.pdf

❌ 不好的命名
简历.pdf
new_resume_final_final2.pdf
```

### 2. 版本管理策略
```bash
# 主简历
resume.md              # 源文件
resume.pdf             # 最新PDF

# 语言版本
resume_cn.pdf          # 中文版
resume_en.pdf          # 英文版

# 历史版本（按季度）
versions/resume_2024_Q1.pdf
versions/resume_2024_Q2.pdf

# 定制版本（按公司）
custom/accenture.pdf
custom/microsoft.pdf
```

### 3. 提交信息规范
```bash
✅ 清晰的commit信息
git commit -m "Update: Add Pandas project experience"
git commit -m "Fix: Correct company name typo"
git commit -m "Add: English version of resume"

❌ 不清晰的commit信息
git commit -m "update"
git commit -m "改了一些东西"
```

---

## 🔧 常见问题

### Q: 中文PDF乱码怎么办？
```bash
# 使用中文字体
pandoc resume.md -o resume.pdf \
  --pdf-engine=xelatex \
  -V CJKmainfont="PingFang SC"  # macOS
  # 或 -V CJKmainfont="Microsoft YaHei"  # Windows
```

### Q: 生成的PDF不够美观？
使用在线工具或LaTeX模板：
- [Awesome-CV](https://github.com/posquit0/Awesome-CV)
- [ModernCV](https://github.com/xdanaux/moderncv)

### Q: 想要更精细的排版控制？
考虑使用 LaTeX 或 HTML+CSS

### Q: 不想安装本地工具？
使用在线Markdown编辑器：
- [Dillinger](https://dillinger.io/)
- [StackEdit](https://stackedit.io/)

---

## 🎯 针对不同岗位的建议

### 数据分析师 / 数据工程师
- ✅ 使用 Markdown（展示技术能力）
- 突出项目经验和技术栈
- 包含 GitHub 链接

### 商业分析师 / 产品经理
- ⚠️ Markdown 或精美的在线模板
- 突出业务成果和数据
- 可视化项目成果

### 传统行业 / 非技术岗位
- 可以使用 Word 或在线模板
- 注重格式美观和专业性

---

## 📚 学习资源

- [Markdown语法教程](https://markdown.com.cn/)
- [简历写作指南](https://www.indeed.com/career-advice/resumes-cover-letters)
- [技术简历最佳实践](https://github.com/resumejob/awesome-resume)

---

**最后更新**: 2024年2月28日
