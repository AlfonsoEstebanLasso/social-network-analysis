# Social Network Analysis with NetworkX

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
![Python 3](https://img.shields.io/badge/Python%203-3776AB?style=flat-square&logo=python&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-2C7FB8?style=flat-square)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

**From 1.42M tweets to a polarized retweet core: graph metrics, k-core filtering, community detection and epidemic simulations with NetworkX 🕸️**

Coursework project — BSc in Applied Data Science, Universitat Oberta de Catalunya (UOC), Social Network Analysis course, 2023.

Three Jupyter notebooks (developed on Google Colab) applying graph analysis with NetworkX, from basic metrics to a full pipeline on a 1.4M-tweet dataset.

> Notebook narrative translated to English from the original Spanish; printed outputs and figure labels are shown as originally executed (in Spanish).

## Objective

- Build graphs from heterogeneous sources (JSON, CSV, edge lists, Pajek) and characterize them with standard metrics: density, clustering, weighted degree, degree distributions, and degree / betweenness / closeness / PageRank centralities.
- Detect communities with modularity-based methods and compare them against a known ground-truth partition using Shannon entropy.
- Simulate epidemic spreading on a real network and quantify the effect of interventions (social distancing, random vs. hub-targeted vaccination).
- Apply the full workflow to a large real-world Twitter dataset: cleaning, graph construction, filtering, k-core extraction, community detection, and visualization.

## Notebooks

| Notebook | Contents |
|---|---|
| [`twitter_network_analysis.ipynb`](twitter_network_analysis.ipynb) | Main project. Retweet network from ~1.42M tweets about the Spanish "trans law" debate: weighted directed graph of retweets, giant component, edge-weight and centrality filtering, k-core (k = 10) extraction, community detection, four centrality measures, node reach, and five large network visualizations. |
| [`network_metrics_basics.ipynb`](network_metrics_basics.ipynb) | Marvel character interaction network (graph construction from JSON, weighted degree, centralities, group-level aggregated graph, GEXF export for Gephi, Erdős–Rényi models) and a retweet network from the 2019 Spanish general election (#28A). |
| [`communities_and_epidemics.ipynb`](communities_and_epidemics.ipynb) | Corporate e-mail network: giant component, modularity-based communities, Shannon entropy of communities vs. the 42 real departments. Epidemic simulations on a US airport network: transmission probability and duration sweeps, social distancing via edge removal, random and hub-targeted vaccination via node removal. |

## Data

No datasets are included in this repository. All were loaded from Google Drive in the original Colab environment:

- **Spanish trans-law Twitter dataset** (~1.42M tweets, 2021–2022): an academic Twitter collection containing personal data of real users. It is **not included and cannot be redistributed** (Twitter/X terms of service and data-protection constraints). Only aggregate results and anonymized visualizations appear in the notebook; the one preview of raw rows had its output removed.
- **Marvel interaction network** (JSON, 50 characters) and **RT-28A retweet network** (CSV, 2019 Spanish general election, user IDs pre-anonymized): provided by the course.
- **Corporate e-mail network** (`mails.txt` edge list + `departments.txt`, anonymous numeric nodes, 42 departments): provided by the course; structurally similar to the [SNAP email-Eu-core dataset](https://snap.stanford.edu/data/email-Eu-core.html).
- **US airport network** (`airports.net`, Pajek format): provided by the course.

## Key results (Twitter retweet network)

As reported in `twitter_network_analysis.ipynb`:

- From ~1.42M tweets, a weighted directed retweet graph was reduced (giant component → edge-weight filter → degree-centrality filter → self-loop removal → k-core with k = 10) to a dense core suitable for analysis.
- The k-core has density ≈ 0.0087 and average clustering ≈ 0.177.
- Community detection on the core finds 3 communities of 1,336, 981 and 73 nodes, consistent with a polarized debate with a small bridging group.
- Degree, betweenness, closeness and PageRank centralities and node reach identify a small set of accounts (kept as numeric IDs) that concentrate retweet activity.

## Tech stack

Python 3, pandas, NetworkX, matplotlib, NumPy, Google Colab. Gephi (via GEXF export) for external visualization.

## How to run

The notebooks were written on Google Colab and read data from `/content/drive/MyDrive/...`; those paths (and the `google.colab` drive-mount cells) must be adapted to your environment and data locations.

```bash
pip install -r requirements.txt
jupyter notebook   # run from the repository root
```

Running from the repository root matters for `communities_and_epidemics.ipynb`, which imports `provided/propagate.py`. All notebooks keep their original outputs, so the analyses and figures can be inspected without re-running anything.

## Repository structure

```
.
├── README.md
├── requirements.txt
├── twitter_network_analysis.ipynb
├── network_metrics_basics.ipynb
├── communities_and_epidemics.ipynb
└── provided/
    └── propagate.py   # epidemic propagation function provided by course materials (not my code)
```

## Provenance notes

- The original UOC assignment scaffolding (course header/logo, exercise statements and scoring) has been removed; the remaining code and analysis text are my own work.
- `provided/propagate.py` contains the one function supplied by the course materials, kept separate and labeled as such.
