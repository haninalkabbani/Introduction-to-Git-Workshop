# Introduction to Git Workshop

Welcome to the Introduction to Git Workshop! This comprehensive tutorial teaches the fundamentals of Git version control system through hands-on command line exercises.

## Workshop Overview

This workshop provides a complete introduction to Git, covering everything from basic configuration to advanced collaborative workflows. Students will learn by doing, executing real Git commands and working through practical examples.

## What You'll Learn

By completing this workshop, you will be able to:

- Configure Git on your local machine
- Set up authentication with GitHub (Personal Access Tokens and SSH keys)
- Create and initialize Git repositories
- Make commits and track changes over time
- Work with remote repositories (GitHub/GitLab)
- Use branching strategies for feature development
- Create and manage pull requests
- Collaborate effectively using Git workflows
- Apply Git best practices in professional environments

## Workshop Structure

The workshop is organized into 12 progressive sections:

1. **Set Up Git Configuration** - Configure your Git identity
2. **Initialize a New Git Repository** - Create repositories from scratch
3. **Create and Stage Files** - Learn the staging process
4. **Make Your First Commit** - Create snapshots of your work
5. **Connect to a Remote Repository** - Link local and remote repos, including GitHub authentication setup
6. **Clone an Existing Repository** - Work with existing projects
7. **Create and Switch to a New Branch** - Feature branch workflows
8. **Modify Files and Create Commits on Branch** - Practical refactoring exercise
9. **Push Branch to Remote Repository** - Share your work
10. **Create a Pull Request** - Propose changes for review
11. **Review and Merge the Pull Request** - Collaborative review process
12. **Clean Up and Pull Latest Changes** - Maintain repository hygiene

## Prerequisites

Before starting this workshop, ensure you have:

- Basic command line knowledge
- Git installed on your machine
- A text editor of your choice (VS Code, nano, vim, etc.)
- A GitHub account (for remote repository exercises)
- Ability to create Personal Access Tokens or SSH keys for GitHub authentication

## Files in This Repository

- **`README.md`** - This file, providing workshop overview and instructions
- **`main.py`** - Simple calculator script used as the starting point for exercises
- **`lesson_materials/`** - Workshop materials and examples
  - **`Introduction_to_Git.md`** - Complete step-by-step tutorial
  - **`main_updated.py`** - Refactored calculator with functions (target for exercises)

## Getting Started

### Option 1: Follow the Tutorial
Navigate to [`lesson_materials/Introduction_to_Git.md`](lesson_materials/Introduction_to_Git.md) for the complete step-by-step tutorial with commands and explanations.

### Option 2: Fork and Practice
1. Fork this repository to your GitHub account
2. Clone your fork locally
3. Follow the workshop exercises using your own repository

### Option 3: Create New Repository
1. Create a new repository following Section 2 of the tutorial
2. Use the provided `main.py` as your starting point
3. Work through the refactoring exercises

## Practical Exercise: Calculator Refactoring

The workshop includes a hands-on refactoring exercise where you'll transform a simple calculator script from:

**Before (main.py):**
```python
# Simple Calculator
x = 1
y = 2
print(f"The sum of x and y is: {x + y}")
```

**After (using concepts from main_updated.py):**
```python
def add(x, y):
    """Add two numbers together."""
    return x + y

def get_number_input(prompt):
    """Get numeric input with automatic type conversion."""
    # Implementation details...

def main():
    """Main calculator function with user input."""
    # Implementation details...
```

This exercise demonstrates real-world Git workflows including:
- Feature branch creation
- Code refactoring and commits
- Push/pull operations
- Pull request workflow
- Code review and merging

## Key Concepts Covered

### Git Fundamentals
- Repository initialization and structure
- Staging area and commit process
- Working directory vs. repository state
- Git configuration and identity management

### Branching and Merging
- Feature branch workflows
- Branch creation and switching
- Merge strategies and conflict resolution
- Branch cleanup and management

### Remote Repositories
- Origin and upstream concepts
- Push and pull operations
- GitHub authentication methods (Personal Access Tokens vs SSH keys)
- Authentication setup and troubleshooting
- Collaborative workflows

### Best Practices
- Commit message conventions
- Branch naming strategies
- Code review processes
- Repository maintenance

## Additional Resources

After completing this workshop, consider exploring:

- **Advanced Git features**: Rebasing, cherry-picking, stashing
- **Git GUIs**: GitHub Desktop, SourceTree, GitKraken
- **Team workflows**: GitFlow, GitHub Flow, feature branches
- **Integration tools**: CI/CD pipelines, automated testing
- **Git hosting platforms**: GitHub, GitLab, Bitbucket

## Workshop Duration

- **Estimated time**: 2-3 hours for complete tutorial
- **Format**: Self-paced with hands-on exercises
- **Skill level**: Beginner to intermediate

## Getting Help

If you encounter issues during the workshop:

1. Check the troubleshooting sections in the tutorial
2. Review Git documentation: `git --help` or `man git`
3. Search Git documentation online
4. Practice commands in a safe test repository

## Contributing

This workshop is designed to be a comprehensive learning resource. If you find areas for improvement or have suggestions, please feel free to contribute by opening issues or submitting pull requests.

## License

This workshop content is available for educational use. Feel free to adapt and share for learning purposes.

---

**Happy learning!** This workshop will give you a solid foundation in Git that you can apply immediately in your development projects.
