# streamlit_apps

# Reproducing the streamlit app
To recreate this app on your own computer, you'll need conda and a compatible version of Python; the latest version of conda and Python 3.9.12 is recommended, as later releases are not continuously supported.  These steps can be repeated and modified for different repos + apps with variable requirements, but be sure you're using compatible versions of both conda and python to avoid errors.


### Start by cloning the repository.
```
git clone https://github.com/baokiddy/streamlit_apps.git
```
### We'll use this as our directory:
```
cd streamlit_apps
```
### If you need to update the repository in the future, you can do so by executing:
```
$ git pull
$ git checkout main
```
### Create conda environment
Create a conda environment called *firstapp* (or frankly, you can name it whatever you'd like because it's local. Go wild.)
```
conda create -n firstapp python=3.9.12
```
We'll use this virtual environment to run the app.
```
conda activate firstapp
```
### Install prerequisite libraries

Download requirements.txt file
```
pip3 install -r requirements.txt
```

###  Download and unzip contents from GitHub repo

Download and unzip contents from https://github.com/baokiddy/streamlit_apps/archive/refs/heads/main.zip

###  Launch the app

```
streamlit run ~/your_path/rounds_analysis.py
```
