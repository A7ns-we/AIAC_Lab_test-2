"""
Agritech Matrix Rotation Utility
Rotates NxN matrix 90° clockwise in-place for UI component glyph rotation.
"""

def rotate_matrix_90_clockwise(matrix):
    """
    Rotate matrix 90° clockwise in-place using layer-by-layer approach.
    
    Args:
        matrix: List[List[int]] - NxN matrix to rotate in-place
    """
    n = len(matrix)
    
    # Process each layer from outer to inner
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        # Rotate elements in current layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            
            # 4-way swap
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top


def print_matrix(matrix, title="Matrix"):
    """Print matrix in readable format."""
    print(f"\n{title}:")
    for row in matrix:
        print(row)


if __name__ == "__main__":
    print("=" * 50)
    print("AGRITECH MATRIX ROTATION UTILITY")
    print("=" * 50)
    
    # Get matrix size
    while True:
        try:
            n = int(input("Enter matrix size (N for NxN matrix): "))
            if n > 0:
                break
            print("Matrix size must be positive.")
        except ValueError:
            print("Please enter a valid integer.")
    
    # Get matrix elements
    print(f"\nEnter {n}x{n} matrix elements (row by row):")
    print("Format: space-separated integers (e.g., 1 2 3)")
    
    matrix = []
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").split()))
                if len(row) == n:
                    matrix.append(row)
                    break
                print(f"Expected {n} elements, got {len(row)}.")
            except ValueError:
                print("Please enter valid integers.")
    
    # Display and rotate
    print_matrix(matrix, "Original")
    rotate_matrix_90_clockwise(matrix)
    print_matrix(matrix, "Rotated (90° clockwise)")
    
    print("\nRotation complete!")