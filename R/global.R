library(reticulate)
library(data.table)
library(tidyverse)
library(lubridate)
library(shiny)
library(shinycssloaders)

# Python Environment Setup ---------------------------------------------
PYTHON_DEPENDENCIES = c('datetime', 'pandas', 'riotwatcher')

# Create a virtual environment selecting your desired python version
virtualenv_create(envname = "example_env_name", python= "python") #python=c(python,python3)
# Explicitly install python libraries that you want to use, e.g. pandas, numpy
virtualenv_install("example_env_name", packages = c('pandas','datetime','riotwatcher'))
                   # Select the virtual environment
                   use_virtualenv("example_env_name", required = TRUE)

virtualenv_dir = Sys.getenv('VIRTUALENV_NAME')
python_path = Sys.getenv('PYTHON_PATH')

reticulate::use_virtualenv('example_env_name', required = T)

print(reticulate::py_config())
source_python('./Py/Get API Data.py')

# -------------------------------------------------------------------
