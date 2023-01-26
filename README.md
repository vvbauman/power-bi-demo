# sample-work-loan-application
## Preamble
The goal of this repository is to provide a sample of my software development and machine learning work

This readme includes descriptions of the dataset used in this repo, the branches in this repo, and descriptions of the files in this branch

## Dataset description
The dataset used in this repo is the PKDD'99 Financial dataset (https://relational.fit.cvut.cz/dataset/Financial) that contains 606 successful and 76 unsuccessful loans along with transactional and other details. The data are relational data with 8 tables that are all available from MariaDB database. The tables are also included in this repo

## Repo branches
```
- main : peer-reviewed code
- feature/data-ingestion : ingesting the 8 tables and merging to create a silver table *(most up-to-date branch)*
```
*Note:* the intended workflow of this repo is to create a feature branch from the main branch for any new development and for all production-ready code to be in the *src* folder in the main branch. Once the feature is complete and the feature branch is ready to be merged in the main branch, it would usually undergo peer review. However, since this is a toy project, feature branches are not peer reviewed before being merged with the main branch

Also, after branches are merged with the main branch, they are not deleted. The order that branches have been merged with main follows the order in the code block above

## Repo Directories & Files descriptions
```
- dataset : directory containing all datasets necessary for this project
- notebooks : directory containing .ipynb notebooks used in EDA and development, as preambles to refactored code development
- src : directory containing production-ready code
└─ ingestion : refactored .py scripts for data ingestion and merging. Includes ingestion_main.py script for use in AML/sklearn pipeline
└─ utils : scripts with utility functions used throughout the codebase
└─ validation : scripts with panderas schemas and functions with data validation checks used throughout the codebase
- unit_tests : directory containing scripts with pytest unit tests, to test functionality of utility functions
- UML_diagram.png : UML diagram depicting relationships between classes in src
- ingestion_config.yml : configuration file for scripts in src/ingestion/. Contains constants so they are not hard-coded in the scripts
- setup.py : script to run to enable relative imports
```
