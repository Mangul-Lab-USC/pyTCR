# `pyTCR`
 pyTCR is a comprehensive [jupyter notebook](https://docs.jupyter.org/en/latest/index.html) based platform for T-Cell receptor (TCR) data analysis to facilitate reproducibility and rigor of immunogenomics research.

---

## Why `pyTCR`?
- **Take a more visual approach to data analysis** through jupyter notebooks rather than writing tons of lines of code.
- **Modify any notebook functionality with a few clicks** to customize the notebook for your needs.
- **Speed**. Current benchmarks show up to 14x faster performance than other TCR-seq analysis tools.
- **Run it anywhere.** The flexibility of Jupyter notebooks allow them to be run anywhere, from your local computer to the cloud.

## Table of Contents

- [Introduction](#introduction)
- [Quick Start](#quick-start)
- [Setting up your data](#setting-up-your-data)

---

## Quick Start

### Running in the cloud
The preferred method of running pyTCR is in the cloud. pyTCR provides explicit support for use in **Google Colab** environments which is free to use.

#### Google Colab Usage:
1. Set up a [Google Colab](https://colab.research.google.com/) account.
2. From Google Colab, you can upload pyTCR notebooks by clicking **file > upload notebook**. From there, you have multiple different options to upload the notebooks:
     - **Google Drive**: Upload the notebooks directly to your Google Drive, and then select them from the upload prompt.
     - **GitHub**: You can use the notebooks without ever downloading them through GitHub. Select the GitHub tab from the upload prompt and Paste the following `url` into the search: 

         `https://github.com/Mangul-Lab-USC/pyTCR/tree/main/`

         From there, it will list all available notebooks, and allow you to select which ones you want to use.

     - **Upload**: This option allows you to upload the notebooks from your local computer into Google Colab.

#### Other Cloud environments:
There are many cloud based Jupyter notebook platforms that will allow you to run the notebooks just as easily. Some options are:
- [Jupyter's official platform](https://jupyter.org/try)

### Running locally
Due to the nature of Jupyter notebooks, they can be run anywhere `python` is supported. We recommend following [Jupyter's official installation guide](https://jupyter.org/install) to get it up and running locally.

## Setting up your data
By nature, all notebooks can be modified to fit any data format. However, pyTCR comes with a preset format if you are not comfortable altering the notebook cells to fit your data. The `data_adapter.ipynb` notebook can be used to convert existing data formats such as VDJtools, trust4, or any other tabular format, to the pyTCR format. PyTCR expects the following columns in your data file and are required for the notebooks to work out of the box.

| column | name | description                                               |
|--:|:---------|:-----------------------------------------------------------|
| 1   | `sample`  | The name of the sample (required)                       |
| 2   | `freq`    | The share of clonotypes in the sample (required)        |
| 3   | `#count`  | The number of reads (required)                          |
| 4   | `cdr3aa`  | CDR3 amino acid clonotype (required)                    |
| 5   | `cdr3nt`  | CDR3 nucleotide (required)                              |
| 6   | `v`       | V gene (required)                                       |
| 7   | `d`       | D gene (required)                                       |
| 8   | `j`       | J gene (required)                                       |
| ... | optional fields | any other fields intended for your use (optional) |

Specific Instructions on how to convert your data to the pyTCR format is available inside the `data_adapter.ipynb` notebook. The notebooks are written with the pyTCR format by default, but can be altered to fit any data requirements.