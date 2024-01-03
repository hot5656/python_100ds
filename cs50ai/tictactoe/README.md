``` bash
pip3 install -r requirements.txt
python.exe -m pip install --upgrade pip

# select python
Ctrl+Shift+P --> python interpreter --> select ...

# submit degress
git init
git add .
git commit -m "first version"
# gihub create res
D:\work\run\me50-ai50\degrees>git remote add origin https://github.com/hot5656/cs50ai-degrees.git
git push -u origin master
# add brench - ai50/projects/2024/x/degrees
# check out brench ai50/projects/2024/x/degrees
git checkout -b ai50/projects/2024/x/degrees

# push
D:\work\run\me50-ai50\degrees>git push -u https://github.com/me50/hot5656 ai50/projects/2024/x/degrees
    Username for 'https://github.com': hot5656
    Password for 'https://hot5656@github.com':
    Enumerating objects: 9, done.
    Counting objects: 100% (9/9), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (8/8), done.
    Writing objects: 100% (9/9), 3.04 KiB | 445.00 KiB/s, done.
    Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
    remote:
    remote: Create a pull request for 'ai50/projects/2024/x/degrees' on GitHub by visiting:
    remote:      https://github.com/me50/hot5656/pull/new/ai50/projects/2024/x/degrees
    remote:
    To https://github.com/me50/hot5656
    * [new branch]      ai50/projects/2024/x/degrees -> ai50/projects/2024/x/degrees
    branch 'ai50/projects/2024/x/degrees' set up to track 'https://github.com/me50/hot5656/ai50/projects/2024/x/degrees'.

# 2nd push - tictactoe
git add .
git commit -m "add action exception"
git push -u https://github.com/me50/hot5656 ai50/projects/2024/x/tictactoe
```