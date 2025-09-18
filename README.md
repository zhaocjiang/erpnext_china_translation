# ERPNext China Translation - 仅翻译功能模块

这是从ERPNext China模块中提取的纯翻译功能模块，专注于解决以下翻译需求：

1. 提供完整的zh.csv翻译文件，优化官方的机器翻译
2. 特别处理workspace中不支持通过标准zh.csv文件汉化的位置，如：
   - Your Shortcuts → 快捷入口
   - Reports & Masters → 功能&报表
   - Quick Access → 快捷入口
   - Masters & Reports → 功能&报表

## 安装方法

在ERPNext环境中，使用bench命令安装此模块：

```bash
# 切换到bench目录
cd /path/to/your/bench

# 获取此应用（假设模块在当前目录下）
bench get-app erpnext_china_translation e:/github/erpnext_china/erpnext_china_translation

# 安装应用到指定站点
bench --site your_site_name install-app erpnext_china_translation
```

## 功能说明

1. **标准翻译**：通过translations/zh.csv文件提供系统界面的中文翻译
2. **特殊位置汉化**：安装后自动处理workspace文件，汉化无法通过标准翻译机制处理的位置

## 注意事项

1. 此模块仅包含翻译功能，不包含ERPNext China的其他功能
2. 安装后，如需更新翻译，只需更新translations/zh.csv文件并运行bench更新命令
3. 如果系统升级后翻译失效，可能需要重新安装此模块

## 维护

如需添加或修改翻译内容，请编辑translations/zh.csv文件，遵循现有的CSV格式。