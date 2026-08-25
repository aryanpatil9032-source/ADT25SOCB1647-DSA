# Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
def create_tree():
    category = input("Enter category/book name (or NULL): ")

    # If no category/book exists
    if category.upper() == "NULL":
        return None

    # Create new node
    new_node = Node(category)

    # Create left subcategory
    print("Enter left subcategory of", category)
    new_node.left = create_tree()

    # Create right subcategory
    print("Enter right subcategory of", category)
    new_node.right = create_tree()

    return new_node


# Inorder Traversal
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Preorder Traversal
def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# Postorder Traversal
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# Main Algorithm
def main():
    # Initialize tree
    root = None

    # Create library catalog
    print("===== Create Library Catalog =====")
    root = create_tree()

    # Inorder Traversal
    print("\n\n===== Book Categories (Inorder) =====")
    inorder(root)

    # Preorder Traversal
    print("\n\n===== Catalog Structure (Preorder) =====")
    preorder(root)

    # Postorder Traversal
    print("\n\n===== Archive/Delete Order (Postorder) =====")
    postorder(root)

    print("\n\nProgram Ended.")


# Run the program
main()

