# Environment Setup

## 1. Download this repository:

```bash
git clone git@github.com:OutisLi/index-tts.git
```

## 2. Install dependencies:

### 2.1 Linux

```bash
conda create -n index-tts python=3.12 -y
conda activate index-tts
pip install -r requirements.txt
conda install libstdcxx-ng -c conda-forge -y
pip install -e .
```

### 2.2 Mac

```bash
conda create -n index-tts python=3.12 -y
conda activate index-tts
pip install -r requirements.txt
pip install -e .
```

### 2.3 Windows

```bash
conda create -n index-tts python=3.12 -y
conda activate index-tts
pip install -r requirements.txt
pip install -e .
```

## 3. Download models:

### 3.1 Download by `modelscope`:

```shell
modelscope download --model IndexTeam/Index-TTS --local_dir ./checkpoints
```

```shell
wget -P checkpoints \
  https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/bigvgan_discriminator.pth \
  https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/bigvgan_generator.pth \
  https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/bpe.model \
  https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/dvae.pth \
  https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/gpt.pth \
  https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/unigram_12000.vocab
```

```shell
wget https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/bigvgan_discriminator.pth -P checkpoints
wget https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/bigvgan_generator.pth -P checkpoints
wget https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/bpe.model -P checkpoints
wget https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/dvae.pth -P checkpoints
wget https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/gpt.pth -P checkpoints
wget https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/unigram_12000.vocab -P checkpoints
```

-   for windows user:

```shell
winget install --id GNU.Wget2
wget2 https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/bigvgan_discriminator.pth -P checkpoints
wget2 https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/bigvgan_generator.pth -P checkpoints
wget2 https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/bpe.model -P checkpoints
wget2 https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/dvae.pth -P checkpoints
wget2 https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/gpt.pth -P checkpoints
wget2 https://modelscope.cn/models/IndexTeam/Index-TTS/resolve/main/unigram_12000.vocab -P checkpoints
```

### 3.2 Download by `huggingface-cli`:

```bash
huggingface-cli download IndexTeam/Index-TTS \
  bigvgan_discriminator.pth bigvgan_generator.pth bpe.model dvae.pth gpt.pth unigram_12000.vocab \
  --local-dir checkpoints
```

Recommended for China users. 如果下载速度慢，可以使用镜像：

```bash
export HF_ENDPOINT="https://hf-mirror.com"
```

-   Or by `wget`:

```bash
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/bigvgan_discriminator.pth -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/bigvgan_generator.pth -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/bpe.model -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/dvae.pth -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/gpt.pth -P checkpoints
wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/unigram_12000.vocab -P checkpoints
```

## 4. Run test script:

```bash
python demo.py
```

# Use as command line tool:

```bash
# Make sure pytorch has been installed before running this command
pip install -e .
indextts "大家好，我现在正在bilibili 体验 ai 科技，说实话，来之前我绝对想不到！AI技术已经发展到这样匪夷所思的地步了！" \
  --voice reference_voice.wav \
  --model_dir checkpoints \
  --config checkpoints/config.yaml \
  --output output.wav
```

Use `--help` to see more options.

```bash
indextts --help
```

# Web Demo

```bash
pip install -e ".[webui]"
python webui.py
```

Open your browser and visit `http://127.0.0.1:7860` to see the demo.
