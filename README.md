To upload pickles larger than 25 MB you will need Git Large File Storage

# Debian and Ubuntu

Ubuntu 18.04, Debian 10, and newer versions of those OSes offer a git-lfs package. If you'd like to use that and don't need the latest version, skip step 1 below.

    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    sudo apt-get install git-lfs
    git lfs install

# Mac OSX

    You may need to brew update to get all the new formulas
    brew install git-lfs
    git lfs install

# Windows

    Download the windows installer from here
    Run the windows installer
    Start a command prompt/or git for windows prompt and run git lfs install

After that you can use:

```
git lfs track "*.pkl"
cd the path of the directory
git init
git add "rf_regressor.pkl"
git commit -m "Upload model"
git remote add origin *remote repository URL*
git remote -v
git push -u origin master
```
