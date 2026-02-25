# Machine Learning Practical 1: Find-S Algorithm

## Overview
This repository contains the implementation of the **Find-S Algorithm**, a fundamental concept learning method in Machine Learning. [cite_start]The algorithm's primary goal is to find the **most specific hypothesis** that fits all positive training examples provided in a dataset[cite: 68].

## Concept Learning
[cite_start]Concept learning is the process of finding a rule or pattern that helps a machine decide whether an example belongs to a specific group based on past data[cite: 10]. In this practical, we teach the machine to identify **Edible Trees** based on physical attributes.

## How the Algorithm Works
1. [cite_start]**Initialize**: Start with the most specific hypothesis $h = \{\phi, \phi, \phi, \phi\}$[cite: 76, 79].
2. [cite_start]**Positive Examples**: When a positive example is found, the algorithm generalizes the hypothesis if the current rule is too specific[cite: 81].
3. [cite_start]**Negative Examples**: The algorithm completely ignores negative examples, assuming the current specific rule already excludes them[cite: 80].
4. [cite_start]**Wildcards**: Attributes that vary across positive examples are replaced with a `?` (wildcard), indicating any value is acceptable[cite: 72].



## Dataset Description
The model is trained on a custom dataset of trees with the following attributes:
- **Has Fruit**: YES / NO
- **Leaf Shape**: Oval, Pointed, Heart
- **Bark**: Smooth, Rough
- **Thorny**: YES / NO
- **Target (Edible)**: YES / NO

## Results
After processing the training data, the algorithm produces a final hypothesis that defines the requirements for an edible tree. In this specific simulation, the machine learned that a tree is edible if it **Has Fruit** and is **Not Thorny**, regardless of leaf shape or bark texture.

## Files
- `find_s.py`: The Python implementation of the algorithm.
- `find_s_practical.txt`: Text version of the code and execution logic.

## Requirements
- Python 3.x
