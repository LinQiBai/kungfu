# 感统星功坊

八段锦功法 **智能识评** 桌面系统。基于 MediaPipe 姿态估计，结合八式标准模板，实现式别辨识与身法标准度打分。界面采用 **中医养生** 主题配色。

## 环境

```powershell
conda activate gongfa
cd d:\summary_vacation\gongwubuke
python main.py
```

或双击 `run.bat`。

## 打包为 EXE

在 `gongfa` 环境中双击 `build.bat`，或执行：

```powershell
conda activate gongfa
cd d:\summary_vacation\gongwubuke
pyinstaller build_exe.spec --noconfirm --clean
```

打包完成后：

- 目录：`dist\感统星功坊\`
- 启动：`dist\感统星功坊\感统星功坊.exe`

**分发时请复制整个「感统星功坊」文件夹**（内含依赖库），不要只拷贝单个 exe。

打包前会自动运行 `scripts/verify_imports.py` 校验依赖。若 exe 无法启动，请查看同目录下的 **`感统星功坊_crash.log`**。

已规避的常见打包错误：

| 问题 | 处理方式 |
|------|----------|
| `jaraco.text` 缺失 | 运行时映射 setuptools 内置 jaraco |
| `matplotlib` 缺失 | pose 模块改用 OpenCV 绘骨架 + matplotlib 占位 |
| Qt 平台插件缺失 | 打包 PyQt5 `plugins` 并设置 `QT_PLUGIN_PATH` |
| OpenCV DLL | `add_dll_directory` 加载 cv2 / numpy 库路径 |

## 功能

- 练功区实时摄象预览
- 抓拍识评 / 载入图片
- 可选「实时经络」骨架叠加
- 自动识形或手动选定八式
- 标准度评分、身法分项与养生调息建议

## 界面布局

- **顶栏**：感统星功坊 · 八段锦功法智能识评
- **左栏**：练功预览、摄象控制、式别选择
- **右栏**：评分卡片、识评详览 / 八式玄机（分页签）

## 项目结构

```
gongwubuke/
├── main.py
├── gui/
│   ├── main_window.py
│   ├── theme.py          # 养生主题配色
│   ├── workers.py
│   └── utils.py
└── core/                 # 识评核心逻辑
```

## 说明

标准模板依据八段锦规范身法定义，适用于教学与练功辅导。可通过标定 `core/templates.py` 提升精度。
