from github import Github
from git import Repo
import os

# 配置参数
repo_path = "/path/to/local/folder"  # 本地仓库路径
token = "ghp_xxxx"                   # GitHub Token
repo_name = "your_username/repo_name"  # 格式：用户名/仓库名

# 初始化本地仓库（若未初始化）
if not os.path.exists(os.path.join(repo_path, ".git")):
    repo = Repo.init(repo_path)
else:
    repo = Repo(repo_path)

# 手动同步函数
def manual_sync():
    try:
        repo.git.add("--all")
        repo.git.commit("-m", "Auto commit by Python")
        origin = repo.remote(name="origin")
        origin.push()
        print("同步成功！")
    except Exception as e:
        print(f"错误：{str(e)}")

# 执行同步
manual_sync()