<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Experiments with SetFit & Few-Shot Classification

This project is an experiment with [spaCy](https://spacy.io) and few-shot text classification using [SetFit](http://archive.today/Kelkb)

Run project in colab for GPU: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CvGEZC0I9_v8gWrBxSJQ4Z8JGPJz-HYb?usp=sharing)


## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Convert data into spacy format |
| `pretrain_setfit` | Convert data into spacy format |
| `generate_configs` | Create the configs for training comparison |
| `eval_setfit` | Evaluate the setfit model |
| `train_cpu` | Train the CPU based model |
| `train_cpu_acc` | Train the CPU accuracy model |
| `train_gpu_base` | Train the GPU base (roberta) model |
| `train_gpu_setfit` | Train the GPU SetFit model |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `setup` | `preprocess` &rarr; `generate_configs` &rarr; `pretrain_setfit` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/sst-train-raw.tsv` | URL | SST2 Training Data |
| `assets/sst-dev-raw.tsv` | URL | SST2 Test Data |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->