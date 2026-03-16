
## **Stretch Goal** Part 5: Testing Your Package Structure

### Task 5.1: Create a Comprehensive Test Script
Expand your `main.py` file that you created in Task 1.2 to demonstrate that you can:

1. **Import entire classifications** and access their shared attributes
1. **Access individual animals** through their classification packages
1. **Compare different classifications** by showing attributes from different groups
1. **Show the full hierarchy** by accessing attributes at multiple levels (package level and module level)

Your test script should clearly demonstrate that:
- Shared attributes are accessible at the classification level
- Individual animals can be accessed through their packages
- Each animal has both shared attributes and unique attributes
- The hierarchy works for both warm-blooded and cold-blooded vertebrates

### Task 5.2: Experiment with Different Import Styles
Python offers multiple ways to import modules and attributes. Experiment with different import styles to understand their trade-offs:

**Experiment with:**
1. Importing the full path to a module
2. Importing with an alias
3. Importing a package and accessing modules through it
4. Using `from ... import ...` syntax
5. Importing specific attributes directly

**For each style, consider:**
- Readability: How clear is it where the attribute comes from?
- Convenience: How much typing is required?
- Namespace pollution: What names are added to your current namespace?
- Flexibility: How easy is it to access multiple items?

#### Deliverable (Optional)
Create a file called `import_experiments.py` that demonstrates each import style with comments explaining the trade-offs you observed.

---

Next Up: [Part 6: Reflection](06_part6.md)


