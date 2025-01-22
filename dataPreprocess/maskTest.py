import torch
from diff_gaussian_rasterization import GaussianRasterizer, GaussianRasterizationSettings
import matplotlib.pyplot as plt


# 设置光栅化参数
raster_settings = GaussianRasterizationSettings(
    image_height=512,
    image_width=512,
    tanfovx=0.5,
    tanfovy=0.5,
    bg=torch.tensor([0.5, 0.5, 0.5], device='cuda'),  # 背景颜色设置为灰色并放置在 GPU 上
    scale_modifier=1.0,
    viewmatrix=torch.eye(4, device='cuda'),  # 确保矩阵在 GPU 上
    projmatrix=torch.eye(4, device='cuda'),  # 确保矩阵在 GPU 上
    sh_degree=3,
    campos=torch.zeros(3, device='cuda'),  # 确保向量在 GPU 上
    prefiltered=False,
    debug=False,
    antialiasing=False,
)

# 创建 GaussianRasterizer 对象
rasterizer = GaussianRasterizer(raster_settings)

# 假设有一些三维点的均值和二维投影点
means3D = torch.rand(100, 3, device='cuda')  # 100 个三维点的均值，放置在 GPU 上
means2D = torch.rand(100, 2, device='cuda')  # 100 个二维投影点，放置在 GPU 上
opacities = torch.rand(100, device='cuda')  # 100 个不透明度值，放置在 GPU 上

# 设置颜色为灰色
colors_precomp = torch.full((100, 3), 0.5, device='cuda')  # 100 个灰色颜色值，放置在 GPU 上
cov3D_precomp = torch.rand(100, 3, 3, device='cuda')  # 100 个 3D 协方差矩阵，放置在 GPU 上

# 调用 rasterizer 进行光栅化
color, radii, _ = rasterizer(means3D, means2D, opacities, colors_precomp=colors_precomp, cov3D_precomp=cov3D_precomp)

# 显示渲染结果
# 调整 color 张量的维度顺序
color = color.permute(1, 2, 0)
# 将结果移动到 CPU 并转换为 numpy 数组
color_np = color.detach().cpu().numpy()

# 保存图像
plt.imsave('rasterized_image.png', color_np)