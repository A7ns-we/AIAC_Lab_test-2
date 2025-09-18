"""
Agritech Change Review Utility
Shows added/removed lines between versions.
"""

def get_line_diff(old_lines, new_lines):
    """Get added and removed lines with stable ordering."""
    old_set = set(old_lines)
    new_set = set(new_lines)
    
    added = [line for line in new_lines if line not in old_set]
    removed = [line for line in old_lines if line not in new_set]
    
    return added, removed


if __name__ == "__main__":
    print("AGRITECH CHANGE REVIEW UTILITY")
    print("=" * 40)
    
    # Get old lines
    print("\nOld version lines (press Enter twice to finish):")
    old_lines = []
    while True:
        line = input()
        if line == "" and old_lines:
            break
        if line != "":
            old_lines.append(line)
    
    # Get new lines
    print("\nNew version lines (press Enter twice to finish):")
    new_lines = []
    while True:
        line = input()
        if line == "" and new_lines:
            break
        if line != "":
            new_lines.append(line)
    
    # Calculate and show diff
    added, removed = get_line_diff(old_lines, new_lines)
    
    print(f"\nAdded: {added}")
    print(f"Removed: {removed}")