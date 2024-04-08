from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf8') as f:
    long_description = f.read()


setup(
    name='fastmrz',
    version='0.0.1',
    author='Sivakumar Mahalingam',
    description='Extracts the Machine Readable Zone (MRZ) data from document images',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sivakumar-mahalingam/fastmrz',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers"
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development"
    ],
    install_requires=[
        "absl-py>=2.1.0",
        "astunparse>=1.6.3",
        "certifi>=2024.2.2",
        "charset-normalizer>=3.3.2",
        "flatbuffers>=24.3.25",
        "gast>=0.5.4",
        "google-pasta>=0.2.0",
        "grpcio>=1.62.1",
        "h5py>=3.10.0",
        "idna>=3.6",
        "keras>=3.1.1",
        "libclang>=18.1.1",
        "Markdown>=3.6",
        "markdown-it-py>=3.0.0",
        "MarkupSafe>=2.1.5",
        "mdurl>=0.1.2",
        "ml-dtypes>=0.3.2",
        "namex>=0.0.7",
        "numpy>=1.26.4",
        "opencv-python>=4.9.0.80",
        "opt-einsum>=3.3.0",
        "optree>=0.11.0",
        "packaging>=24.0",
        "pillow>=10.2.0",
        "protobuf>=4.25.3",
        "Pygments>=2.17.2",
        "pytesseract>=0.3.10",
        "requests>=2.31.0",
        "rich>=13.7.1",
        "six>=1.16.0",
        "tensorboard>=2.16.2",
        "tensorboard-data-server>=0.7.2",
        "tensorflow>=2.16.1",
        "tensorflow-io-gcs-filesystem>=0.31.0",
        "termcolor>=2.4.0",
        "typing_extensions>=4.10.0",
        "urllib3>=2.2.1",
        "Werkzeug>=3.0.1",
        "wrapt>=1.16.0"
    ],
)
