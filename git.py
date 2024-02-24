import git
 
def git_clone(repo_url, destination_path):
    git.Repo.clone_from(repo_url, destination_path)
 
# Example usage:
repo_url = "https://github.com/example_user/example_repo.git"
destination_path = "./folder"
 
git_clone(repo_url, destination_path)