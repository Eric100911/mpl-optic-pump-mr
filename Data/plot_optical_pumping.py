#! /usr/local/bin/python3.11

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import matplotlib.ticker as ticker

# ==========================================
# 配置部分
# ==========================================
BASENAME = "optic_pump_mr_data_03_vertical_field"
CSV_FILE = BASENAME + ".csv"
OUTPUT_PNG = BASENAME + ".png"
OUTPUT_PDF = BASENAME + ".pdf"

# 设置绘图风格以匹配 LaTeX / ROOT 风格
# 启用 Times New Roman 字体
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix' # 'stix' 提供了最接近 LaTeX 的渲染效果
plt.rcParams['axes.unicode_minus'] = False # 处理负号显示
plt.rcParams['font.size'] = 14

def plot_optical_pumping():
    print(f"正在读取文件: {CSV_FILE} ...")
    
    # ==========================================
    # 1. 读取与预处理数据
    # ==========================================
    try:
        # 读取CSV
        # header=0 表示第一行为表头
        # names=['I', 'Upp'] 强制指定列名，防止表头有特殊字符
        # usecols=[0, 1] 只读取前两列，忽略行尾逗号产生的空列
        df = pd.read_csv(CSV_FILE, header=0, names=['I', 'Upp'], usecols=[0, 1])
    except FileNotFoundError:
        print(f"错误: 找不到文件 {CSV_FILE}")
        return

    # 数据清洗：去除可能的空值
    df = df.dropna()
    
    # *** 关键步骤：排序 ***
    # 按照电流 I (x轴) 从小到大排序
    df = df.sort_values(by='I')
    
    # 转换为 numpy 数组方便计算
    x = df['I'].values
    y = df['Upp'].values

    if len(x) == 0:
        print("错误: 数据为空")
        return

    # ==========================================
    # 2. 计算平滑曲线 (模拟 ROOT 的 Draw("C"))
    # ==========================================
    # 使用 B-Spline (样条插值) 生成平滑曲线
    # 在原始 x 的范围内生成更密集的点（例如 300 个点）
    x_smooth = np.linspace(x.min(), x.max(), 300)
    
    # k=3 表示三次样条插值 (Cubic Spline)，也就是平滑曲线
    try:
        spl = make_interp_spline(x, y, k=3) 
        y_smooth = spl(x_smooth)
    except Exception as e:
        print(f"警告: 数据点过少无法进行平滑插值，将绘制折线。({e})")
        x_smooth = x
        y_smooth = y

    # ==========================================
    # 3. 创建画布与绘图
    # ==========================================
    # figsize=(8, 6) 对应 ROOT 的 800x600 比例
    fig, ax = plt.subplots(figsize=(8, 6))

    # 绘制平滑曲线 (黑色细线) -> 对应 ROOT LineColor(kBlack)
    ax.plot(x_smooth, y_smooth, color='black', linewidth=1.5, zorder=1, label='_nolegend_')

    # 绘制原始数据点 (红色十字) -> 对应 ROOT MarkerStyle(2), MarkerColor(kRed)
    # marker='+' 对应十字，s=100 控制大小 (对应 ROOT MarkerSize)
    ax.scatter(x, y, color='red', marker='+', s=120, linewidths=1.5, zorder=2)

    # ==========================================
    # 4. 设置坐标轴与刻度 (复刻 ROOT 风格)
    # ==========================================
    
    # 设置刻度朝内 (Direction In)
    ax.tick_params(direction='in', which='both', top=True, right=True, length=6, width=1, labelsize=14)
    
    # 设置坐标轴标签 (LaTeX 格式)
    # r"..." 表示原始字符串，防止转义
    # \mathrm{} 用于正体单位，\it{} 用于斜体变量
    # Matplotlib 处理 \perp 即使不加空格通常也不会重叠，但加上 \, (小间距) 更保险
    ax.set_xlabel(r'$I_{\perp} \cdot \mathrm{A}^{-1}$', fontsize=16, labelpad=10)
    ax.set_ylabel(r'$U_{pp} \cdot \mathrm{mV}^{-1}$', fontsize=16, labelpad=10)

    # 调整边距 (对应 ROOT SetLeftMargin 等)
    plt.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.95)

    # 开启网格 (可选，若不需要可注释掉)
    # ax.grid(True, linestyle='--', alpha=0.5)

    # ==========================================
    # 5. 保存图像
    # ==========================================
    print(f"正在保存为 {OUTPUT_PNG} 和 {OUTPUT_PDF} ...")
    plt.savefig(OUTPUT_PNG, dpi=300)
    plt.savefig(OUTPUT_PDF) # PDF 为矢量图，完美支持 LaTeX
    
    # 显示图像
    # plt.show()

if __name__ == "__main__":
    plot_optical_pumping()