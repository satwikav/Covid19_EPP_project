## EPP Project (WiSe 2020/21): Covid-19 Policy Stringency Index in Germany
**Emily Anne Schwab and Satwika Vysetty**

This repository contains the final project submitted for the course Effective Programming Practices for Economists taught by Professor Hans-Martin von Gaudecker at the University of Bonn. We have used the [template](https://econ-project-templates.readthedocs.io/en/stable/index.html) provided by Professor Gaudecker for structuring our project. 

## Introduction
Need to take from Emily's write up

## Viewing the project
The project is structured such a way that all the input files are in the [src](https://github.com/s6emschw/EPP-Final-Project/tree/master/src) directory and all the output files are in the bld directory which would be generated in the project's root directory after running Pytask. Hence the best way to view this project is to clone it. 
```
$ git clone https://github.com/s6emschw/EPP-Final-Project.git
```
After cloning the project repository in the desired location, the environment needed for running this project has to be created.
```
$ conda env create -f environment.yml
$ conda activate visualizations_covid
```
The documentation can now be generated by running the following.
```
$ conda develop .
$ pytask
```

## Main tasks
1. Clean and manage the Covid-19 restriction policy data <br />
**Dependency:** `policy_data.csv` **Product:** `covid_policy.csv`
2. Create Sub-Score indicies and Stringency Index <br />
**Dependency:** `covid_policy.csv` **Product:** `stringency_index_data.csv`
3. Prepare data for visualizations <br />
**Dependency:** `stringency_index_data.csv`,`death_data.csv`,`DE_Mobility_Report.csv` **Product:** `df_visuals.csv`
4. Create visualizations <br />
**Dependency:** `df_visuals.csv` **Product:** 13 images in .png format
6. Create detailed documentation on data collection and index creation <br />

## Project paths
The [**src**](https://github.com/s6emschw/EPP-Final-Project/tree/master/src) directory has the subdirectories:
- [original_data](https://github.com/s6emschw/EPP-Final-Project/tree/master/src/original_data):
   - policy_data.csv
   - death_data.csv
   - DE_Mobility_Report.csv
- [data_management](https://github.com/s6emschw/EPP-Final-Project/tree/master/src/data_management):
   - task_create_data.py
   - task_prepare_data_for_plotting.py
- [analysis](https://github.com/s6emschw/EPP-Final-Project/tree/master/src/analysis):
   - task_create_index.py
- [final](https://github.com/s6emschw/EPP-Final-Project/tree/master/src/final):
   - task_create_visual_SI_Covid.py
   - task_create_visual_SI_Mobility.py
   - task_create_visual_SSI_time.py
   - task_create_visuals.py
- [sandbox](https://github.com/s6emschw/EPP-Final-Project/tree/master/src/sandbox):
   - covid_stringency_index_visualisations.ipynb
- [paper](https://github.com/s6emschw/EPP-Final-Project/tree/master/src/paper)
- [documentation](https://github.com/s6emschw/EPP-Final-Project/tree/master/src/documentation)

The **bld** directory which is generated after running Pytask has the subdirectories:
- data: contains `covid_policy.csv`,`df_visuals.csv`
- analysis: contains `stringency_index_data.csv`
- figures: contains visualizations 
- documentation: 
