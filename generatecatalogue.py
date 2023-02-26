import os

lst = ['''# zwz-doc''', '''个人文档''', '''## 目录''']


def tree(directory_path, padding=''):
    """
    Recursively prints the directory tree rooted at directory_path.
    """
    # Get the list of all items in the directory
    items = os.listdir(directory_path)
    # Sort the list alphabetically
    items.sort()
    # Loop through each item in the directory
    for item in items:
        # Get the full path of the item
        item_path = os.path.join(directory_path, item)
        # If the item is a directory, print its name and recursively call tree() on it
        if os.path.isdir(item_path) and not item.startswith('.') and not item.startswith('__'):
            result = (padding + '- ' + f'''[{item}]({item_path}/README.md)''')
            lst.append(result)
            tree(item_path, padding + '   ')


if __name__ == '__main__':
    # Call the tree() function with the current directory as the root
    tree('.')
    with open('''./README.md''', 'w') as f:
        f.write('\n'.join(lst))

