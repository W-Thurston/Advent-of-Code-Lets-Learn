# 🎄 Advent of Code: Let’s Learn Series

### *A multi-year exploration of problem solving, clean code, and teaching through Advent of Code.*

Welcome to **Let’s Learn Advent of Code**, a long-term project where I solve Advent of Code puzzles year after year, not just to get the answers, but to **learn**, **refine**, and **teach** better ways to think about programming.

Each day’s puzzle is an opportunity to:

* develop better problem-solving intuition
* explore multiple solution strategies
* refactor and improve code quality
* write about the concepts behind the puzzle
* document insights, mistakes, and breakthroughs
* build a growing knowledge base of algorithmic patterns

This repository is structured so that **every puzzle becomes a mini-lesson**, for myself and for anyone following along.

---

## 🌟 Project Philosophy

This repo is not a race for stars - it's a study in:

* clarity
* correctness
* software craftsmanship
* thoughtful explanation
* reproducible problem-solving

For each day:

1. I write a **first-draft working solution**.
2. I reflect and analyze what the puzzle *really* required.
3. I produce a **clean, refactored final solution**.
4. I write a **learning journal entry**.
5. I create a **teaching-friendly blog-style post**.

AoC shapes the daily topics.

---

## 🗂 Repository Structure

This repo supports **multiple years** of Advent of Code.
Each year includes:

* **solutions/** - first-pass daily solutions and refactored, polished versions
* **posts/** - teaching-oriented write-ups
* **tests/** - optional tests per day

Shared utilities live under `src/aoc/utils/`.

```
advent-of-code-lets-learn/
│
├── src/
│   └── aoc/
│       ├── utils/
│       │   ├── parsing.py
│       │   ├── grid.py
│       │   └── graph.py
│       └── runner.py
│   └── aoc2025/                    # or 2024, 2023, etc.
│   │   ├── posts/                      # blog-style daily write-ups
│   │   │   ├── day01.md
│   │   │   └── ...
│   │   ├── solutions/
│   │   │   ├── day01/
│   │   │   │   ├── Description.txt # ignored - Puzzle text
│   │   │   │   ├── example.txt     # example from puzzle text
│   │   │   │   ├── input.txt       # ignored - personal puzzle input
│   │   │   │   ├── notes.md        # journal entry
│   │   │   │   ├── optimized.py    # optimized solutions
│   │   │   │   ├── solution.py     # first-draft daily solutions
│   │   │   └── ...
│   └── tests/
│       ├── test_day01.py     # Optional tests
│       └── ...
├── .gitignore
├── .python-version
├── LICENSE
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## ⚙️ Development Setup

This project uses **uv**, a fast Python package and environment manager.

### Clone and install:

```bash
git clone https://github.com/W-Thurston/advent-of-code-lets-learn.git
cd advent-of-code-lets-learn
uv sync
```

Run any solution:

```bash
uv run python -m src.aoc.runner yyyy dd
```

(This runs *Year 2025, Day 1* using your first-draft implementation.)

---

## 🧰 Shared Utilities

Common helpers (grid navigation, parsing, BFS/DFS, etc.) live in:

```
src/aoc/utils/
```

These are reusable across all years and help keep solutions clean.

---

## 🧪 Tests

You can create tests under each year’s `tests/` directory.
Running them:

```bash
uv run pytest
```

---

## 🧠 Daily Workflow

### For each day:

1. **Solve first.**
   Don’t worry about elegance, just get a working solution.

2. **Reflect.**
   What patterns did the problem hide?
   What did you misinterpret at first?

3. **Refactor.**
   Create a polished version focusing on clarity, readability, and structure.

4. **Write your learning journal.**
   (Saved under `solutions/dayXX/notes.md`.)

5. **Write your teaching post.**
   A cleaned-up narrative with explanations and example code.

This process creates a consistent, high-signal archive of insights and improvements.

---

## ✨ Goals of This Project

* Build a **lasting educational archive** of AoC lessons
* Develop stronger **algorithmic and coding intuition**
* Practice **code clarity, refactoring, and maintainability**
* Grow as a **teacher**, not just a solver
* Produce content that helps others on their programming journey
* Create a personal record of improvement across years

---

## 💬 Contributions

This is primarily a personal learning project, but:

* feedback
* bug reports
* alternative solutions
* educational suggestions

are welcome.

---

## 📝 License

This project contains **my own code and writing**, which I release under the MIT license.

Puzzle descriptions belong to **Advent of Code**! Please do not redistribute their content or your private inputs.

---

## 🎁 Final Thoughts

Advent of Code is more than a puzzle set, it's an opportunity to:

* explore algorithms
* practice reasoning
* improve design
* write better software
* share what you learn

This repo is my evolving attempt to do that deliberately and joyfully.

Thanks for stopping by and happy coding! 🎄✨
