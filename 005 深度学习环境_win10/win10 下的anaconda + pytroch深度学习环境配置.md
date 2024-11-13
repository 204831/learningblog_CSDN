# win10 下的anaconda + pytroch深度学习环境配置

## 1 引言

### 1.1 环境介绍

显卡： NVIDIA GeForce RTX 4060 Ti 16G

软件：Win10专业版，conda=23.7.4, VSCode=1.82

### 1.1 教程目的

1. 使用anaconda搭建虚拟环境，熟悉虚拟环境的管理及conda常用命令；
2. 配置jupyter notebook与VSCode使用anaconda的虚拟环境；
3. 在VSCode中配置git，远程管理GitHub仓库；
4. 明白本地安装cuda和cudnn和conda虚拟安装的区别并能进行配置；
5. 完成pytroch深度学习环境的成功搭建。

### 1.2 anaconda介绍

anaconda可以方便的进行软件包及环境的管理，这意味着你可以安装多个版本的软件包及依赖关系，并且可以轻松的进行切换。

### 1.3 VSCode介绍

VSCode（Visual Studio Code）是由微软开发的一款免费、开源的集成开发环境（IDE），它支持多种编程语言和框架，具有轻量级、可扩展性强和丰富的功能特性，使得开发者能够轻松地进行代码编辑、调试和版本控制等任务。

### 1.4 VSCode+anaconda+jupyter

anaconda集成了Python解释器以及众多科学计算相关的库，VSCode提供了代码编辑器和集成的调试功能，Jupyter则提供了交互式的数据可视化和分析环境。三者结合使用，可以提高编码的效率和质量。

### 1.5 pytorch、cuda及cudnn介绍

1. CUDA 是 NVIDIA 发明的一种并行计算平台和编程模型。它通过利用图形处理器 (GPU) 的处理能力，可大幅提升计算性能（百度百科）；

2. CUDNN是NVIDIA用于深度神经网络的GPU加速库。

**CUDA看作是一个工作台，cuDNN相对于工作台上的工具，有了他们才能在GPU上完成深度学习计算。**

## 2. 显卡驱动安装

根据自己的显卡及系统，去[NVIDIA驱动官网](https://www.nvidia.cn/geforce/drivers/)下载对于的显卡驱动：
![驱动下载](NVIDIA驱动下载\下载.png)

**注**：

- “**系统检查**”仅勾选“**NVIDIA 显卡驱动和GeForce Experience**”；

- “**安装选项**”选择“**精简**”。

其他默认即可。

安装完成后在cmd窗口输入：

```python
nvidia-smi
```

输出以下内容，既表示安装成功。
![安装验证](NVIDIA驱动下载\版本检查.png)

**其中“CUDA Version"是CUDA的驱动版本，我们后续要安装的是CUDA运行版，其版本号应低于驱动版本号。**

## 3. anaconda安装

### 3.1 conda下载

两个选择：

link1：[anaconda官网最新版下载](https://www.anaconda.com/download)  
link2：[清华大学镜像源选择需要的版本进行下载](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)  
  
这里我以官网最新版进行下载安装。

### 3.1 conda安装

① 双击运用安装包，注意以下部分，其余默认即可：

在这里需要记住安装路径，后面添加环境变量需要。
![ ](anaconda安装\4.jpg)

![ ](anaconda安装\5.jpg)
  
② 添加环境变量：  
**打开环境变量:** "控制面板"-->"系统"-->"高级系统设置"：

```python
# 需添加3条路径，记得替换成自己的安装路径：
D:\solfware\anaconda3 # anaconda安装路径
D:\solfware\anaconda3\Scripts 
D:\solfware\anaconda3\Library\bin

```

![ ](anaconda安装\10.jpg)

③ 测试是否安装成功：
点击"win+R"快捷键，输入"cmd",打开cmd窗口，输入 "***conda --version***" ,如果出现"conda + 版本号",则安装成功。
![ ](anaconda安装\11.jpg)

**成功后，我们可以在Windows开始菜单栏，使用管理员运行打开"Anaconda Navigator"进行虚拟环境的管理(但后面使用VSCode管理更方便)。此外，conda安装后，会附带安装"Spyder"和"jupyter notebook"两个IDE,如果不想用VSCode的同学到这里就可以停下了，其实Spyder+jupyter notebook也差不多够用，只是vscode功能会更加强大。**

![ ](anaconda安装\12.jpg)

如果打不开Anaconda-navigator，参考[Anaconda-navigator 打不开的解决方法（亲测有效！）](https://blog.csdn.net/qq_42489092/article/details/92208822)

## 4. VSCode安装

### 4.1 VSCode下载

目前为1.82版(2023年9月23日)：  
link：[官网最新版下载](https://code.visualstudio.com/Download)  

### 4.2 VSC安装

① 双击运用安装包，注意修改安装路径，其余默认即可：  
![ ](VSCode安装\2.jpg)

## 5. VSCode配置anaconda

### 5.1 VSCode安装中文及Python插件

直接在拓展中搜索安装即可：

- "chinese"中文插件：
![ ](VSCode安装\6.jpg)
- Python插件：
![ ](VSCode安装\7.jpg)

### 5.2 选择Python解释器

在VSCode界面按"ctrl+shift+P",输入 "***Select Interpreter***" ,选择有"conda"标识的的Python编辑器即可。

**VSCode会自动识别到conda的虚拟环境。**

### 5.3 VSCode中切换不同的conda虚拟环境

在VSCode右下角：
![ ](VSCode安装\8.jpg)

## 6. anaconda虚拟环境创建及切换

① 调出VSCode终端：
![ ](VSCode安装\9.jpg)

② 选择conda终端：
![ ](VSCode安装\10.jpg)

括号中的"base"表示当前的虚拟环境，base初始时便存在，我们一般不使用该环境。
![ ](VSCode安装\11.jpg)

③ 虚拟环境创建及切换命令：

```python
conda info -e # 查看已有的虚拟环境
conda create -n env_name python==3.7 # 创建虚拟环境，并安装指定的Python版本
conda remove --name env_name --all # 删除虚拟环境及依赖关系
conda activate env_name # 激活虚拟环境
conda deactivate env_name # 退出虚拟环境

```

## 7. anaconda虚拟环境下的包管理

有时下载很慢，可能是下载源的问题，更换镜像源即可，具体可参考：[Conda 替换镜像源方法尽头，再也不用到处搜镜像源地址](https://blog.csdn.net/adreammaker/article/details/123396951)

### 7.1 conda管理(推荐)

```python
# 首先应该切换到你需要安装包的环境：
conda list # 查看当前环境安装的所有包
conda install package_name # 安装包
conda uninstall package_name # 卸载包
```

### 7.2 pip管理

其实不怎么推荐pip下载的方法，容易安装到base类！！！

```python
# 首先应该切换到你需要安装包的环境：
pip list # 查看当前环境安装的所有包
pip install package_name # 安装包
pip uninstall package_name # 卸载包
```

但是pip方法是离线安装必备的！感兴趣的自行搜索-->（pip,离线安装）。

## 8. VSCode与配置git远程连接GitHub仓库

见我的另外一篇CSDN文章: [传送门](https://blog.csdn.net/qq_51555368/article/details/130518876)

## 9. jupyter使用anaconda的虚拟环境

见我的另外一篇CSDN文章: [传送门](https://blog.csdn.net/qq_51555368/article/details/131658070)

## 10. 安装CUDN及CUDNN

### 10.1 本地安装及conda虚拟环境安装区别

CUDN的安装可分为两种：

1. CUDA官网下载CUDA Toolkit Installer进行本地安装———安装的cuda模块更全面。
2. conda虚拟环境中通过命令行安装——模块不全，但用于一般的训练模型是足够的。但是如果想使用CUDA的拓展功能时，则需要安装本地安装完成的cuda Toolkit。

**如果就日常学习，在虚拟环境中安装即可。后续要用到拓展功能时再安装完整CUDA Toolkit即可。**

### 10.2 本地安装

① CUDA安装：

1. 打开[CUDA Toolkit下载官网](https://developer.nvidia.com/cuda-toolkit-archive)，选择适合你的版本，因为的cuda驱动版本为12.3，要选择比12.3更低的版本，我这里选择12.1。**这里安装的是运行版本，注意与cuda驱动版区分**：
![cuda包下载](cuda及cudnn安装\cuda-1.png)

2. 下载完成后，默认安装即可（我是默认安装到C盘）,**记住安装路径**，我的安装路径是"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1"。
3. 配置环境变量：
在系统变量中，查看是否有下面4个变量，缺的补上：

    **请根据自己的安装路径进行配置！！！**
    ![环境变量配置](cuda及cudnn安装\cuda-2.png)

4. 测试是否安装成功：
在cmd中输入" ***nvcc -V*** ",如果出现以下输出，则表示安装成功：
![安装验证](cuda及cudnn安装\验证安装.png)

② 安装CUDNN：

1. 去[NVIDIA developer官网](https://developer.nvidia.com/rdp/cudnn-download)下载对应版本的CUDNN版本，第一次登陆需要注册；
![cudnn下载](cuda及cudnn安装\cudnn安装.png)

2. 下载好之后解压压缩包，将文件中的bin，lib，include下的文件复制粘贴到CUDA安装目录（我的是：C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1）中的bin，lib，include文件夹下；

    **注意：是复制bin，lib，include里面的文件，并不是复制文件夹。如果出现是否替换选项，不要替换！！！**

3. 测试是否成功。在C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\extras\demo_suite下打开cmd窗口，输入 "**bandwidthTest.exe"**，出现以下显示，则表示安装成功：
![cudnn验证](cuda及cudnn安装\cudnn验证.jpg)

### 10.3 conda虚拟环境中安装

1. 进入[pytorch官网](https://pytorch.org/)，选择需要的Python版本：

    安装GPU版：
    ![GPU版](cuda及cudnn安装\pytorch_GPU.png)
    安装CPU版：
    ![CPU版](cuda及cudnn安装\pytorch_CPU.png)

    进入conda的虚拟环境，执行相应的conda 安装指令即可完成安装。

    **使用该安装方法，是CUDA与CUDNN同时安装的，不需要额外的安装！**

2. 验证是否安装成功：

    切换到安装了pytorch的安装环境，执行"import torch",看是否报错，无报错即表示安装成功。
