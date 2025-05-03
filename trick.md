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