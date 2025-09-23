# 模板说明

## 基本信息

本模板适用于清华大学近代物理实验的实验报告撰写，基于 LaTeX 排版系统，提供了标准的格式和样式设置。

* `Report/thuemp.cls`：自定义的 LaTeX 类文件，定义了实验报告的格式和样式（原作者：Mingyu Li）。
* `Report/report.tex`：实验报告的主文件，包含了实验内容、数据分析和结论等部分。
* `Report/report.bib`：参考文献数据库文件，存储了实验报告中引用的文献条目。
* `Data/`：存放实验数据和绘图文件的目录。
* `Makefile`：用于编译 LaTeX 文档的脚本文件。

## 环境要求

请参考`.github/workflows/build.yml`中的依赖列表，确保安装了以下软件包：

* `texlive-latex-base`
* `texlive-latex-extra`
* `texlive-fonts-recommended`
* `texlive-fonts-extra`
* `texlive-lang-chinese`
* `texlive-xetex`
* `texlive-science`
* `texlive-pictures`
* `texlive-bibtex-extra`
* `texlive-luatex`
* `biber`
* `fonts-dejavu-core`
* `lmodern`
* `ttf-mscorefonts-installer`
* `fontconfig`

## 借助`GNU Make`在本地进行编译

确保系统中已安装`GNU Make`和`XeTeX`，然后在终端中运行以下命令：

```bash
make all
```

这将生成`Report/report.pdf`文件，即实验报告的最终版本。

## 借助`GitHub Actions`进行在线编译

本模板已配置`GitHub Actions`，每次推送代码到仓库时，系统会自动编译实验报告并生成 PDF 文件。编译成功后，生成的 PDF 文件将作为发布版本的附件上传。除此之外，在具有适当的`tag`时，还会触发release，形成一个新的发布版本。

这一编译的主要过程即为运行`make`。值得注意的是，为了保证Times New Roman字体的正确显示，编译环境中安装了`ttf-mscorefonts-installer`，并且借助`apt-utils`强制同意`Microsoft EULA`。

# 原实验报告内容概览：GMR实验报告

## 实验内容

* 磁阻特性测量：通过直接测量 GMR 元件的电阻-磁场曲线，观察显著的磁阻效应和磁滞现象。
* 传感器特性分析：
* 模拟传感器的线性磁电转换特性（灵敏度 $0.12\ \mathrm{V/mT}$）。
* 开关传感器的阈值特性（开关场约 $\pm 0.4\ \mathrm{mT}$）。
* 偏置磁场优化：探究偏置磁场对电流测量的影响。
* 角位移检测：利用梯度传感器实现角位移检测（周期 $24^\circ$）。
* 数据存储验证：通过磁读写组件验证二进制数据存储。
 
## 文件结构
`Report/`：实验报告的 LaTeX 源文件。
`data/`：实验数据文件，以及绘图。
`README.md`：仓库说明文件。

## 联系方式
作者：王驰
邮箱：chi-wang22@mails.tsinghua.edu.cn
