#!/bin/bash

tree() {
    local directory_path=$1
    local padding=$2
    local result

    # Get the list of all items in the directory
    local items=$(ls "$directory_path" | sort)

    # Loop through each item in the directory
    for item in $items; do
        # Get the full path of the item
        local item_path="$directory_path/$item"

        # If the item is a directory, print its name and recursively call tree() on it
        if [[ -d "$item_path" && ! $item == .* && ! $item == __* ]]; then
            result="$padding- [$item]($item_path/README.md)"
            lst+=("$result")
            tree "$item_path" "$padding   "
        fi
    done
}

# Clear the existing contents of the README.md file
> ./README.md

# Define the initial content
lst=('# zwz-doc' '基于GitHub Flavored Markdown的在线文档' '## 目录')

# Call the tree function starting from the current directory
tree .

# Write the contents of lst to the README.md file
printf "%s\n" "${lst[@]}" >> ./README.md
