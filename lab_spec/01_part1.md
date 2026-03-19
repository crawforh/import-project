# Import is Important Tutorial
## Lab: Animal Classification System

## Part 1: Understanding Packages vs. Modules

### Task 1.1: Create the Basic Structure
1. Design a directory hierarchy that represents the animal classification system in the diagram below
1. Create the necessary directories and files to make your hierarchy into valid Python packages
1. Create only the package structure - you'll create the modules in later tasks

![Vertebrates Classification Diagram](../.devcontainer/vertebrates.png)

**Hints:**
- Think about how to represent the hierarchical relationship: animals → vertebrates → temperature regulation → specific classification → individual animals
- What file is needed in each directory to make it a regular package?
- Would a namespace package work better? Why or why not?

##### Success
You'll know you succeeded when:
1. You can import your package hierarchy without errors
1. Running `python3.14 -c "import vertebrates"` completes without error

### Task 1.2: Create Your First Module
Let's start with a simple example: create a module for the shark.

1. Decide where the shark module should live in your hierarchy
1. Create the module file and add attributes that describe a shark (e.g., the attributes from the diagram). The attributes can be represented with any names and data types you choose.
1. Add a `print` statement to the shark module to observe when it gets imported. This is usually the first line in the file so it runs before any `import` statements.
1. Import the shark module in `animal-classification/main.py` (create this file if you haven't already) and add print statements to display shark attributes

##### Success
You'll know you succeeded when:
1. Running `main.py` prints the shark's attributes without errors.

##### Reflection
- Are you accessing the attributes with the fully qualified import (e.g., `vertebrates.cold_blooded.fish.shark.has_fins`)? If so, how can you change the `import` statement so you can refer just to the attribute (e.g., `has_fins`)? How would the `import` statement change if you wanted to refer to them with the animal name (e.g., `shark.has_fins`)?
- When does each `print` statement execute? Was this what you expected? Why or why not?
- What's the full path needed to access attributes?
- What happens if you import the same module twice?
   - Consider examining the output of `sys.modules` and `locals().keys()`
- What exception do you get if you try to import an attribute that doesn't exist?

---

Next Up: [Part 2: Sharing Attributes Within a Package](02_part2.md)