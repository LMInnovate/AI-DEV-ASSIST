""""
Task 1: AI-Powered Code Completion

This script shows two versions of sorting a list of dictionaries by a specific key:
1. Manual implementation
2. AI-suggested (simulated) implementation

We'll compare both for readability and efficiency.
"""

#Sample data
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

#  Manual Implementation
def manual_sort(lst, key):
    return sorted(lst, key=lambda x: x[key])

print("Manual sort by age:")
print(manual_sort(data, "age"))


# AI-Suggested (Copilot-style) Implementation
def ai_suggested_sort(lst, key):
    """Uses built-in sorted() with key argument for clarity"""
    return sorted(lst, key=lambda item: item.get(key, 0))

print("\nAI-suggested sort by age:")
print(ai_suggested_sort(data, "age"))


#  Comparison/Analysis
analysis = """
Comparison:

- Manual implementation is minimalistic but assumes key is always present.
- AI-suggested version uses .get(), safer for missing keys.
- Both have O(n log n) time complexity.
- Copilot-suggested code is cleaner, more robust, easier to maintain.
- AI tools reduce dev time by suggesting best practices instantly.

Conclusion:
AI-powered completion is valuable for writing safer, clearer code faster.
"""

print("\nAnalysis:")
print(analysis)
