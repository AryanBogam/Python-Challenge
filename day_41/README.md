# 🐙 Day 41/300 – GitHub Logic Systems in Python

Today, I built the **core logic behind GitHub’s main features** — from counting stars and forks to tracking commit history and checking repository activity.

It felt like breaking down GitHub into **backend logic modules**, simulating how the platform works under the hood with simple Python scripts.

---

## ✅ Topics Practiced

- ⭐ Repository star counting  
- 🏆 Finding the most popular repository  
- 🐞 Open issues tracking  
- 🔄 Pull request filtering  
- 📜 Commit history management  
- 🍴 Fork count calculation  
- 👥 Contributor list sorting  
- ⏱ Repository activity status check  
- 🖥 Language usage statistics  
- 🔍 Repository keyword search  

---

## 🔍 What I Solved Today

1. **Repository Star Counter**  
   → Calculated the total number of stars across all repositories

2. **Most Popular Repository Finder**  
   → Found the repository with the highest stars

3. **Open Issues Counter**  
   → Counted how many issues are still open

4. **Pull Request Merger**  
   → Filtered only merged pull requests

5. **Commit History Tracker**  
   → Displayed commit messages in reverse (most recent first)

6. **Fork Counter**  
   → Calculated the total forks across multiple repositories

7. **Contributor List Formatter**  
   → Sorted contributor names alphabetically

8. **Last Commit Time Checker**  
   → Checked if a repository is “Active” or “Inactive” based on last commit time

9. **Language Usage Counter**  
   → Counted how many repositories use each programming language

10. **Repository Search by Keyword**  
    → Returned all repositories containing a specific keyword in their description

---

## 💭 Daily Reflection

Today showed me that **GitHub’s magic is just structured data and smart conditions**.  
Every button we click — stars, forks, merges — is powered by simple but well-planned logic.

By simulating GitHub in Python, I’m thinking like a **software engineer who designs collaborative platforms** that can scale to millions of developers.

Tomorrow? More building.  
Because **the code you push today could power the world tomorrow**.

---

## 🧠 Sample – Repository Star Counter

```python
def total_stars(repositories):
    return sum(repo["stars"] for repo in repositories)

# Example:
repos = [
    {"name": "AI-Project", "stars": 120},
    {"name": "Web-App", "stars": 85},
    {"name": "Game-Engine", "stars": 200}
]
print("Total Stars:", total_stars(repos))
# Output: Total Stars: 405
