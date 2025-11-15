# Sorting_Package (Q3)

# Rinkesh Verma 2025201070 Mtech CSE

## 📦 Project Overview
This project implements a modular and extensible Python package for sorting algorithms as required in **Q3** of the assignment.  
It uses a clean object-oriented architecture with:
- An **abstract base class**
- Implementations of **Bubble Sort, Selection Sort, Quick Sort, Merge Sort**
- A **SortingSelector** factory class
- A **test suite**
- A `main.py` demonstration script  
- Full Git workflow with commits + tags

---

## 📁 Folder Structure

```
Sorting_Package/
│
├── src/
│   └── sorting_algorithms.py     # All sorting classes + selector
│
├── test/
│   └── test_sorting.py           # Automated correctness tests
│
├── reports/
│   └── (any reports go here)
│
├── main.py                       
├── README.md                     # This file
└── input.txt                     
```

---

## ⚙️ Requirements
- Python 3.10+
- No external packages needed  
- Optional: pytest for clean test execution

---

## 🚀 How to Run the Sorting Algorithms

### 1. Navigate to the Q3 Folder
```
cd <path of Q3>
```

### 2. Run the Demonstration Script
```
python3 main.py #for terminal output
python3 main.py > output.txt #for output in output.txt
```

Expected output:
- Original list
- Sorted ascending list
- Sorted descending list

You can switch algorithms by editing:
```
algo = "quick"
```
in `main.py`.

---

## 🧪 Running Tests (Correct Way)

Because relative imports are used, tests MUST be executed as a Python package.

### Step 1: Go to the **parent directory** of Sorting_Package
```
cd <path of Q3>
```

### Step 2: Run tests using module execution
```
python3 -m Sorting_Package.test.test_sorting
```

If all is good:
```
All tests passed!
```

---

## 🧬 Git Workflow (Recommended for Q3)

### Step 1 — Initialize Git
```
git init
git add .
git commit -m "Initial project structure"
git tag -a v0.1 -m "Added abstract base class for sorting algorithms"
```

### Step 2 — After adding Sorting Algorithms
```
git add src/sorting_algorithms.py
git commit -m "bubbleSort implemented"
git tag -a v0.3 -m "bubbleSort implemented"
```
### Step 3/4/5
```
tag v0.4 : SelectionSort implemented
tag v0.5 : QuickSort implemented
tag v0.6 : MergeSort implemented
```
### Step 6 — SortingSelector 
```
tag v0.7 : Added SortingSelector class for selecting algorithms dynamically.
```
### Step 7 — adding test_sorting.py
```
tag v0.8 : added simple test cases
```
### Step 8 — Adding Main
```
tag v1.0 : Added main demonstration script.
```

### Step 9 — Final Submission Tag / README updated
```
v1.1 : README updated.
```

---

## 📝 Assumptions
- All sorting algorithms operate **only** on integer lists if not then code will raise `Error` accordingly.
- Maximum list size: **< 2 × 10^5 elements**.
- Sorting must return **a new list**, not modify input.
- Ascending/descending mode must be supported.
- Tests assume deterministic behavior for all algorithms.

---

## 👨‍🏫 Notes for Evaluators
- All required components (ABC class, algorithm classes, selector class, tests, main script, Git usage) are included.
- Relative imports are used correctly (run via `python3 -m`).
- Folder structure follows assignment specification exactly.

---

## 🎉 End of README
This completes the documentation for **Q3 – Sorting Algorithms Package**.
