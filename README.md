# mvp

# Analytics Airflow powered by Astronomer

[![Astronomer CI - Deploy Code](https://github.com/vtex/analytics-astro/actions/workflows/deploy-astro-image.yaml/badge.svg?branch=main)](https://github.com/vtex/analytics-astro/actions/workflows/deploy-astro-image.yaml)

## Overview

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

## Project Contents

Your Astronomer project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes an example DAG that runs every 30 minutes and simply prints the current date. It also includes an empty 'my_custom_function' that you can fill out to execute Python code.
- Dockerfile: This file contains a versioned Astronomer Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.


## Setup development environment

> p.s. If you are on a Windows platform, please use the Git Bash instead of Prompt or Powershell.

### Requirements

* git
* Python 3.11 (Extra tip: use [pyenv](https://github.com/pyenv/pyenv) to install and manage your Python versions.)
* Container Daemon (ex.: [colima + docker engine community](https://github.com/vtex/analytics-platform/blob/main/docker_colima_install_guide.md))
* Astro CLI: Install using brew with the Makefile command: `make setup-astro-cli`.
If you are on a SO that doesn't support brew you can look for the installation steps [here](https://docs.astronomer.io/astro/install-cli/).
* AWS CLI: install using `brew install awscli`.
* node.js: install with `brew install node`.
* jq: install using `brew install jq`
