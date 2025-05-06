#### huggingface.co下载模型问题：

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

永久写入系统变量

```bash
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
source ~/.bashrc
```

------

#### pip下载出问题： 

```bash
pip install --use-pep517 /path/to/version_pkg
```

或结合 `--no-build-isolation`（如果依赖项需要）：

----------

#### 解决终端只能使用 `python3` 而不能使用 `python` 的问题

创建符号链接

```bash
sudo ln -s $(which python3) /usr/local/bin/python
```

---------

#### 安装Anaconda时的编码报错

```bash
RuntimeError: Failed to extract /root/anaconda3/pkgs/sphinx-7.3.7-py312h5eee18b_0.conda: 'ascii' codec can't encode character '\xe4' in position 90: ordinal not in range(128)
[7181] Failed to execute script 'entry_point' due to unhandled exception!
```

这个错误是由于 Python 在处理包含非 ASCII 字符（如德语的 'ä' 字符 '\xe4'）的文件路径时，尝试使用 ASCII 编码导致的。以下是解决方案：

##### 原因分析

1. 错误发生在尝试提取 conda 包 `sphinx-7.3.7-py312h5eee18b_0.conda` 时
2. 路径中包含非 ASCII 字符（'\xe4' 即 'ä'）
3. 系统默认编码设置为 ASCII，无法处理这些字符

##### 在运行脚本前，设置正确的环境变量：

```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

-----------

```bash
RuntimeError: Failed to import diffusers.models.autoencoders.autoencoder_kl because of the following error (look up to see its traceback):
module 'torch' has no attribute 'float8_e4m3fn'
```

`float8_e4m3fn` 是 PyTorch 2.2 及以上版本才引入的新数据类型（8-bit 浮点数格式），如果你的 PyTorch 版本较低，就会报错。

解决方案：

```bash
pip install torch --upgrade
```

--------

#### GitHub clone报错：fatal: Unsupported SSL backend 'openssl'. Supported SSL backends: gnutls

**解决方法**：在终端中取消这个设置：

```bash
unset GIT_SSL_BACKEND
```
