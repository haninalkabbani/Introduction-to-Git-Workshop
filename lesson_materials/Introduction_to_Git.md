# Introduction to Git Workshop

Welcome to the Introduction to Git Workshop! In this comprehensive tutorial, you'll learn the fundamentals of Git version control system through hands-on command line exercises.

## What You'll Learn

By the end of this workshop, you'll be able to:
- Configure Git on your local machine
- Create and initialize Git repositories
- Make commits and track changes
- Work with remote repositories
- Use branching and merging workflows
- Create and manage pull requests
- Collaborate effectively using Git

## Prerequisites

- Basic command line knowledge
- Git installed on your machine
- A text editor of your choice

Let's get started!

## Section 1: Set Up Git Configuration

Before using Git, you need to configure your identity. This information will be associated with your commits.

### Commands to Run:

```bash
# Configure your name (replace with your actual name)
git config --global user.name "Your Name"

# Configure your email (replace with your actual email)
git config --global user.email "your.email@example.com"

# Verify your configuration
git config --global user.name
git config --global user.email

# View all configuration
git config --list
```

### Expected Output:
- Your name and email should be displayed when you run the verification commands
- The `git config --list` command shows all your Git configuration settings

## Section 2: Initialize a New Git Repository

Let's create a new Git repository from scratch. This involves creating a directory and initializing it with Git.

### Commands to Run:

```bash
# Create a new directory for your project
mkdir git-workshop-demo

# Navigate into the directory
cd git-workshop-demo

# Initialize a Git repository
git init

# Check that .git directory was created
ls -la
# On Windows: dir /a
```

### What Happens:
- A new `.git` directory is created (this is where Git stores all version control information)
- Your directory is now a Git repository
- The `.git` directory contains subdirectories like `objects`, `refs`, `hooks`, etc.

## Section 3: Create and Stage Files

Now let's create our first Python file and learn how to stage files for commit.

### Commands to Run:

```bash
# Create a simple main.py file
# Use your favorite text editor (nano, vim, code, notepad, etc.)
nano main.py
# Or: code main.py
# Or: vim main.py
```

### Content to Add to main.py:

```python
# Simple Calculator
x = 1
y = 2

print(f"The sum of x and y is: {x + y}")
```

### Git Commands:

```bash
# Check Git status (see untracked files)
git status

# Stage the file for commit
git add main.py

# Check Git status again (see staged files)
git status

# Alternative: Stage all files
# git add .
```

### Expected Output:
- First `git status`: Shows `main.py` as an untracked file in red
- After `git add`: Shows `main.py` as staged for commit in green

## Section 4: Make Your First Commit

A commit is a snapshot of your repository at a specific point in time. Let's create our first commit!

### Commands to Run:

```bash
# Create your first commit
git commit -m "Initial commit: Add basic calculator"

# View commit history (one line format)
git log --oneline

# View detailed commit information
git log

# Check current status
git status
```

### Expected Output:
- Commit message confirms 1 file changed
- `git log` shows your commit with author, date, and message
- `git status` shows "nothing to commit, working tree clean"

### Good Commit Message Practices:
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- First line should be 50 characters or less
- Use imperative mood ("Fix bug" not "Fixes bug")

## Section 5: Choose Your Remote Repository Setup

Remote repositories allow you to collaborate with others and backup your code. Before connecting to a remote, you need to choose your approach and set up authentication.

### Setup (Choose One):

**Option A: Create a new repository on GitHub:**
1. Go to github.com
2. Click "New repository"
3. Name it "git-workshop-demo"
4. Don't initialize with README (we already have content)
5. Copy the repository URL
6. **Next step**: You'll link your local repository to this remote in Section 6

**Option B: Use this workshop's repository:**
1. Go to github.com/Revolution-Data-Platforms/Introduction-to-Git-Workshop
2. Click "Fork" button (top right of the repository page)
3. This creates your own copy of the repository under your GitHub account
4. Use your forked repository URL for the exercises
5. **Important**: Don't clone the original repository directly - always fork first so you have write permissions
6. **Next step**: You'll clone your forked repository in Section 6

### Authenticating Git with GitHub

Before you can push to or pull from GitHub, you need to authenticate your Git client. GitHub no longer accepts passwords for Git operations as of August 2021. Here are the recommended authentication methods:

#### Option 1: Personal Access Token (HTTPS)

**Step 1: Create a Personal Access Token**
1. Go to GitHub.com and log in
2. Click your profile picture → Settings
3. Scroll down to "Developer settings" in the left sidebar
4. Click "Personal access tokens" → "Tokens (classic)"
5. Click "Generate new token" → "Generate new token (classic)"
6. Give it a descriptive name like "Git Workshop Token"
7. Set expiration (30 days recommended for learning)
8. Select scopes: at minimum check "repo" for repository access
9. Click "Generate token"
10. **Important**: Copy the token immediately (you won't see it again!)

**Step 2: Configure Git to use the token**
```bash
# When prompted for password during git operations, use your token instead
# Or configure Git to store credentials (cache for 15 minutes)
git config --global credential.helper cache

# For longer caching (cache for 1 hour)
git config --global credential.helper 'cache --timeout=3600'

# On Windows, you can use the credential manager
git config --global credential.helper manager-core
```

#### Personal Access Token vs SSH Key: Quick Comparison

| Aspect               | Personal Access Token (HTTPS)      | SSH Key                               |
| -------------------- | ---------------------------------- | ------------------------------------- |
| **Setup Complexity** | Simple - just create token         | Moderate - generate key pair          |
| **Security**         | Good - token can be scoped         | Excellent - public key cryptography   |
| **Convenience**      | Need to enter token periodically   | Seamless after setup (with ssh-agent) |
| **Firewall/Proxy**   | Works through corporate firewalls  | May be blocked (port 22)              |
| **Expiration**       | Tokens expire (security feature)   | Keys don't expire automatically       |
| **Portability**      | Easy to use on multiple machines   | Need to copy private key securely     |
| **Best for**         | Temporary access, CI/CD, beginners | Daily development, experienced users  |

**Quick Recommendation:**
- **New to Git?** Start with Personal Access Token (easier setup)
- **Regular developer?** Use SSH keys (better long-term experience)
- **Corporate environment?** Check with IT - some block SSH, prefer HTTPS

#### Option 2: SSH Key (Recommended for regular use)

**Step 1: Generate SSH Key**
```bash
# Generate a new SSH key (replace with your GitHub email)
ssh-keygen -t ed25519 -C "your.email@example.com"

# When prompted for file location, press Enter for default
# When prompted for passphrase, you can enter one or leave blank

# Start the ssh-agent
eval "$(ssh-agent -s)"
# On Windows Git Bash: eval `ssh-agent -s`

# Add your SSH private key to the ssh-agent
ssh-add ~/.ssh/id_ed25519
```

**Step 2: Add SSH Key to GitHub**
```bash
# Copy your public key to clipboard
cat ~/.ssh/id_ed25519.pub
# On Windows: type %USERPROFILE%\.ssh\id_ed25519.pub
# On Mac: pbcopy < ~/.ssh/id_ed25519.pub
```

1. Go to GitHub.com → Settings → SSH and GPG keys
2. Click "New SSH key"
3. Give it a title like "My Laptop - Git Workshop"
4. Paste your public key into the "Key" field
5. Click "Add SSH key"

**Step 3: Test SSH Connection**
```bash
# Test your SSH connection
ssh -T git@github.com

# You should see: "Hi username! You've successfully authenticated..."
```

**Step 4: Use SSH URLs for repositories**
```bash
# Use SSH URLs instead of HTTPS (format: git@github.com:username/repo.git)
git remote add origin git@github.com:your-username/git-workshop-demo.git
```

#### Authentication Troubleshooting

**Common Issues:**
- **"Authentication failed"**: Check if your token/SSH key is correct
- **"Permission denied"**: Verify you have write access to the repository
- **"Host key verification failed"**: Run `ssh -T git@github.com` and accept the host key

**Helpful Commands:**
```bash
# Check current remote URL
git remote -v

# Change from HTTPS to SSH
git remote set-url origin git@github.com:username/repository.git

# Change from SSH to HTTPS
git remote set-url origin https://github.com/username/repository.git

# Test Git credentials
git ls-remote origin
```

## Section 6: Clone or Link to Your Remote Repository

Now that you've chosen your repository setup and configured authentication, it's time to connect your local work with the remote repository. The approach depends on which option you chose in Section 5.

### Approach A: Link Your Local Repository to a New Remote (Option A from Section 5)

If you created a new repository on GitHub, you need to link your existing local repository to it.

#### Commands to Run:

```bash
# Add remote origin (replace with your repository URL)
git remote add origin https://github.com/your-username/git-workshop-demo.git

# Verify remote was added
git remote -v

# Push your code to the remote repository
git push -u origin main
# Note: Some repositories use 'master' instead of 'main'
```

#### What Happens:
- Your local repository is linked to the remote repository
- The remote is named "origin" (standard convention)
- Your commits are uploaded to GitHub
- Future pushes will go to this remote repository

### Approach B: Clone Your Forked Repository (Option B from Section 5)

If you forked the workshop repository, you need to clone your fork and work within that directory.

#### Commands to Run:

```bash
# Navigate to a different directory (outside your current repo)
cd ..

# Clone your forked repository (replace with your fork's URL)
git clone https://github.com/your-username/Introduction-to-Git-Workshop.git workshop-clone

# Navigate into the cloned repository
cd workshop-clone

# Explore the repository structure
ls -la
git log --oneline
git remote -v
git branch -a
```

#### What Happens:
- Git downloads the entire repository history from your fork
- A new directory is created with the repository name
- The remote "origin" is automatically configured to point to your fork
- You get a complete working copy of the project

### Key Differences Between the Approaches

| Aspect             | Link Local to Remote (Option A)      | Clone Forked Repository (Option B) |
| ------------------ | ------------------------------------ | ---------------------------------- |
| **Starting Point** | Your existing local repository       | Empty local directory              |
| **Content**        | Your work from previous sections     | Pre-existing workshop content      |
| **Remote Setup**   | Manual `git remote add`              | Automatic during clone             |
| **Initial Push**   | Required (`git push -u origin main`) | Not needed initially               |
| **Best For**       | Learning from scratch                | Working with existing projects     |
| **Next Steps**     | Continue with your main.py           | Start from existing files          |

### Authentication Notes:
- You may need to authenticate with GitHub during push/clone operations
- Use the Personal Access Token or SSH key you set up in Section 5
- GitHub no longer accepts passwords for Git operations

### Expected Output:
- **Option A**: `git remote -v` shows your origin URL, `git push` uploads your commits
- **Option B**: Clone downloads files, `git remote -v` shows your fork URL

### When to Use Each Approach:
- **Link Local to Remote**: Building a project from scratch, learning Git basics
- **Clone Repository**: Contributing to existing projects, working on team repositories

## Section 7: Create and Switch to a New Branch

Branching allows you to work on features without affecting the main codebase. This is essential for safe collaborative development.

### Commands to Run:

```bash
# Check current branch
git branch

# Create and switch to a new branch in one command
git checkout -b feature/refactor-calculator

# Alternative modern syntax (Git 2.23+):
# git switch -c feature/refactor-calculator

# Verify you're on the new branch
git branch

# See all branches (including remote)
git branch -a
```

### Branch Naming Conventions:
- `feature/description` - for new features
- `bugfix/description` - for bug fixes
- `hotfix/description` - for urgent fixes
- Use hyphens instead of spaces
- Be descriptive but concise

### Expected Output:
- `git branch` shows your current branch with an asterisk (*)
- After creating the branch, you'll be on `feature/refactor-calculator`

## Section 8: Modify Files and Create Commits on Branch

Now let's refactor our main.py file to use the improved code structure, demonstrating how to work on features in separate branches.

### Update main.py with this content:

```python
def add(x, y):
    """
    Add two numbers together.

    Args:
        x (int | float): The first number to add
        y (int | float): The second number to add

    Returns:
        int | float: The sum of x and y
    """
    return x + y


def get_number_input(prompt):
    """
    Get numeric input from user with automatic int/float conversion.

    Args:
        prompt (str): The prompt message to display to the user

    Returns:
        int | float: The numeric value entered by the user

    Raises:
        ValueError: If the input cannot be converted to a number
    """
    user_input = input(prompt)
    try:
        return int(user_input)
    except ValueError:
        return float(user_input)


def main():
    """Main function to demonstrate the calculator."""
    try:
        x = get_number_input("Enter the first number (x): ")
        y = get_number_input("Enter the second number (y): ")

        result = add(x, y)
        print(f"The sum of {x} and {y} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    main()
```

### Commands to Run:

```bash
# Edit the file with your preferred editor
code main.py
# Or: nano main.py, vim main.py, etc.

# After editing, check what changed
git status
git diff

# Stage the changes
git add main.py

# Create a commit with a descriptive message
git commit -m "Refactor: Add functions and input validation to calculator

- Extract addition logic into reusable function
- Add user input functionality with type conversion
- Add proper error handling for invalid input
- Improve code organization and documentation"

# View the commit history
git log --oneline
```

### What Changed:
- Hard-coded values replaced with user input
- Logic extracted into reusable functions
- Added proper documentation
- Included error handling
- Better code organization

## Section 9: Push Branch to Remote Repository

Now let's push our feature branch to the remote repository so others can see our work.

### Commands to Run:

```bash
# Push the feature branch to remote
git push origin feature/refactor-calculator

# Alternative: Set upstream and push
git push -u origin feature/refactor-calculator

# Check remote branches
git branch -r

# Check all branches (local and remote)
git branch -a
```

### Expected Output:
- Git uploads your branch to the remote repository
- You'll see the branch listed in remote branches
- The branch will be visible on GitHub/GitLab in the web interface

### Benefits of Pushing Branches:
- Backup your work in the cloud
- Allow team members to review your code
- Enable collaboration on the feature
- Create pull requests for code review

## Section 10: Create a Pull Request

Pull requests (or merge requests in GitLab) are how you propose changes to be merged into the main branch. This enables code review and discussion.

### Steps to Create a Pull Request:

**Using GitHub Web Interface:**
1. Go to your repository on github.com
2. You'll see a prompt "Compare & pull request" for your recent branch
3. Click "Compare & pull request" or go to "Pull requests" → "New pull request"
4. Select your feature branch as the source and main as the target
5. Add a descriptive title and description
6. Click "Create pull request"

### Pull Request Best Practices:

**Title:** "Refactor calculator with functions and input validation"

**Description:**
```
## Changes
- Refactored main.py to use functions instead of inline code
- Added user input functionality with automatic int/float conversion
- Implemented error handling for invalid input
- Added comprehensive documentation

## Testing
- Tested with integer inputs: 5, 3 → 8
- Tested with float inputs: 2.5, 1.5 → 4.0
- Tested error handling with invalid input: "abc" → Error message

## Motivation
This refactoring makes the code more maintainable, reusable, and user-friendly.
```

### Alternative: Using Git Commands

```bash
# Create pull request using GitHub CLI (if installed)
gh pr create --title "Refactor calculator with functions and input validation" --body "See description above"

# View pull requests
gh pr list
```

## Section 11: Review and Merge the Pull Request

This section covers the review process and merging the pull request into the main branch.

### Review Process (Web Interface):

1. **Review the changes:**
   - Click on "Files changed" tab
   - Review line-by-line changes
   - Add comments on specific lines if needed

2. **Test the changes:**
   - Checkout the branch locally to test
   - Run the code to verify it works

3. **Approve or request changes:**
   - Click "Review changes"
   - Choose "Approve", "Comment", or "Request changes"

### Commands to Test Locally:

```bash
# Switch to main branch
git checkout main

# Pull latest changes from remote
git pull origin main

# Switch to feature branch
git checkout feature/refactor-calculator

# Test the code
python main.py
```

### Merge the Pull Request:

**Option 1: Web Interface (Recommended)**
1. Click "Merge pull request" button
2. Choose merge type:
   - "Create a merge commit" - preserves branch history
   - "Squash and merge" - combines all commits into one
   - "Rebase and merge" - replays commits on main
3. Click "Confirm merge"

**Option 2: Command Line**
```bash
# Switch to main branch
git checkout main

# Pull latest changes
git pull origin main

# Merge the feature branch
git merge feature/refactor-calculator

# Push the merged changes
git push origin main
```

## Section 12: Clean Up and Pull Latest Changes

After merging, it's good practice to clean up branches and ensure your local repository is up to date.

### Commands to Run:

```bash
# Switch to main branch
git checkout main

# Pull the latest changes from remote (including our merged changes)
git pull origin main

# Verify our changes are in main
git log --oneline

# Delete the feature branch locally (it's been merged)
git branch -d feature/refactor-calculator

# Delete the feature branch from remote
git push origin --delete feature/refactor-calculator

# Clean up remote tracking branches
git remote prune origin

# View remaining branches
git branch -a
```

### Final Verification:

```bash
# Test the updated main.py
python main.py

# Check repository status
git status

# View final commit history
git log --oneline --graph
```

### What We Accomplished:
- Configured Git with our identity
- Created and initialized a Git repository
- Made commits to track changes
- Connected to a remote repository
- Created and worked on a feature branch
- Pushed changes to remote
- Created and merged a pull request
- Cleaned up branches and synced changes

You now have a complete understanding of the Git workflow used in professional development teams!

## Additional Git Commands Reference

Here are some additional useful Git commands you might need:

### Viewing Information:
```bash
# Show detailed status
git status -v

# Show commit history with graph
git log --graph --oneline --all

# Show differences between commits
git diff HEAD~1 HEAD

# Show what files changed in a commit
git show --name-only <commit-hash>
```

### Undoing Changes:
```bash
# Unstage a file
git reset HEAD <file>

# Discard changes in working directory
git checkout -- <file>

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

### Working with Remotes:
```bash
# Fetch changes without merging
git fetch origin

# Pull with rebase instead of merge
git pull --rebase origin main

# Push all branches
git push --all origin
```

### Branch Management:
```bash
# Rename current branch
git branch -m new-name

# Create branch from specific commit
git checkout -b new-branch <commit-hash>

# Force delete branch (even if not merged)
git branch -D branch-name
```

## Next Steps

Now that you've completed this workshop, consider:

1. **Practice**: Create more repositories and practice the workflow
2. **Learn advanced features**: Rebasing, cherry-picking, stashing
3. **Explore Git GUIs**: GitHub Desktop, SourceTree, GitKraken
4. **Team workflows**: GitFlow, GitHub Flow, feature branches
5. **Integration**: CI/CD pipelines, automated testing

Happy coding!
