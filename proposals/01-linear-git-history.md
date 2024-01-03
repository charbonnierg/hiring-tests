# Preserving Git history


1. Checkout `master` branch:

```bash
git checkout master
````

2. Create a new branch:

```bash
git checkout -b feat/add_questions_python
```

3. Merge dangling feature branch:

```bash
git merge origin/addQuestionsPython
```

4. Rewrite commit message:

```bash
git commit --amend
```
