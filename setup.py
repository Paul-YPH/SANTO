import setuptools

setuptools.setup(
    name="SANTO",
    version="0.0.2",
    author="Haoyang Li",
    author_email="lihy1995@gmail.com",
    description="SANTO: a coarse-to-fine stitching and alignment method for spatial omics",
    url="https://github.com/leihouyeung/SANTO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[],
    python_requires='>=3.7',
)
