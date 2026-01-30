# Git Workshop Conceptual Check-in Assessment

This whiteboard assessment checks your understanding of Git concepts and mental models. Focus on explaining ideas clearly rather than memorizing syntax.

## 1. Git Identity Concept

**Whiteboard Prompt:** Explain why Git needs to know "who you are" before you can make commits. What information does Git track with each commit and why is this important for collaboration?

**Discussion Points:**
- What happens if multiple people work on the same project?
- How does Git track the history of changes?

---

## 2. Git Workflow Mental Model

**Whiteboard Prompt:** Draw the Git workflow and explain what happens in each area:
- Working Directory
- Staging Area
- Local Repository

**Then explain the flow:**
- Where do you edit files?
- What does "staging" mean conceptually?
- What happens when you commit?

**Follow-up:** Why does Git have a staging area? Why not commit changes directly?

---

## 3. File Lifecycle in Git

**Whiteboard Prompt:** Draw and explain the lifecycle of a file in Git:
- Untracked
- Staged
- Committed
- Modified

**Scenario:** You create a new file in your project. Walk through what Git "knows" about this file at each stage and what transitions move it between states.

---

## 4. Understanding What Gets Committed

**Whiteboard Prompt:** You're working on two files in your project:
- `calculator.py` (you've made changes)
- `README.md` (you've also made changes)

You stage only `calculator.py` and then commit with the message "Fix division bug"

**Explain:**
- What's included in this commit?
- What happens to the changes in `README.md`?
- Why is this behavior useful?

---

## 5. Repository Structure Concept

**Whiteboard Prompt:** Explain what it means to "initialize a Git repository" in a folder.

**Discussion Points:**
- What changes about the folder?
- What is Git now able to track?
- What's the difference between a regular folder and a Git repository?

**Scenario:** Draw what happens when you transform a regular project folder into a Git repository.

---

## 6. Branching as Safe Experimentation

**Whiteboard Prompt:**
1. Explain why branching is called "safe experimentation"
2. Draw a scenario showing:
   - Main branch with stable code
   - Feature branch with experimental changes
   - What happens if the experiment fails vs. succeeds

**Discussion:** How does branching solve the problem of "I want to try something but don't want to break what's working"?

---

## 7. Local vs. Remote Concepts

**Whiteboard Prompt:** Draw and explain the relationship between:
- Your local Git repository
- A remote repository (like on GitHub)

**Discussion Points:**
- Why might you want a remote repository?
- What happens to your work if your computer crashes?
- How do multiple developers share code?
- What does "origin" represent conceptually?

---

## 8. Pull Request Concept and Workflow

**Whiteboard Prompt:** Explain the pull request process as a conversation:

**Scenario:** You've built a new feature on a branch. Walk through:
1. Why you can't just merge it directly
2. What a pull request represents
3. Who's involved in the process
4. What happens during code review
5. How the feature gets into the main codebase

**Focus:** What problem does this process solve for teams?

---

## 9. Branch Lifecycle Management

**Whiteboard Prompt:** After a feature is successfully merged into main, explain:

**Concepts to cover:**
- What happened to the feature branch's commits?
- Why is it safe to delete the feature branch?
- How do you get those changes into your local copy?
- What's the difference between local and remote branches?

**Draw:** The before and after state of branches during this process.

---

## 10. Commit Messages as Communication

**Whiteboard Prompt:** Compare these commit messages and explain what makes a good commit message:
- "stuff"
- "changes"
- "Add user input validation to prevent calculator crashes"

**Discussion:**
- Who reads commit messages?
- When would you read them?
- What information is helpful?
- Why does this matter for teamwork?

---

## Synthesis: Git Mental Model

**Final Whiteboard Challenge:**

Draw the complete Git workflow showing:
1. A developer working locally (working directory → staging → commits)
2. Multiple branches for different features
3. Connection to remote repository
4. Pull request process
5. How changes get back to other developers

**Explain each part and how it all connects to enable team collaboration on code.**
