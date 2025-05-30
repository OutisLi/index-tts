import platform
from setuptools import find_packages, setup


setup(
    name="indextts",
    version="0.1.1",
    author="Index SpeechTeam",
    author_email="xuanwu@bilibili.com",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    description="An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech System",
    url="https://github.com/index-tts/index-tts",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "torch>=2.6.0",
        "torchaudio",
        "transformers==4.48.3",
        "accelerate",
        "tokenizers",
        "einops",
        "matplotlib",
        "omegaconf",
        "sentencepiece",
        "librosa",
        "numpy",
        "wetext" if platform.system() != "Linux" else "WeTextProcessing",
    ],
    extras_require={
        "webui": ["gradio"],
    },
    entry_points={
        "console_scripts": [
            "indextts = indextts.cli:main",
        ]
    },
    license="Apache-2.0",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
