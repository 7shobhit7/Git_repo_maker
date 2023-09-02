from github import Github

def push_to_github(github_username, repo_name, github_token):
    # Local path to the Markdown file you want to push
    file_path = 'output.md'

    # Initialize a GitHub instance with your token
    g = Github(github_token)

    # Get the repository
    repo = g.get_repo(f'{github_username}/{repo_name}')

    # Read the content of the local file
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    try:
        # Create a new file in the repository
        repo.create_file(
            path='output.md',  # Remote file path
            message='Add output.md',  # Commit message
            content=file_content,  # File content as base64-encoded string
            branch='main'  # Branch where you want to create the file
        )

        return f'File "{file_path}" has been pushed to the "{github_username}/{repo_name}" repository.'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == "__main__":
    # Example usage:
    github_username = 'YourGitHubUsername'
    repo_name = 'YourGitHubRepoName'
    github_token = 'YourGitHubToken'

    result = push_to_github(github_username, repo_name, github_token)
    print(result)
