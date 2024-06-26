import git
 
def git_clone(repo_url, destination_path):
    git.Repo.clone_from(repo_url, destination_path)
 
# Example usage:
repo_url = "https://github.com/manohar890/pythontest"
destination_path = "./folder"
 
git_clone(repo_url, destination_path)