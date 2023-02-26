import os
# import re
#
# # 定义正则表达式模式，用于匹配Markdown标题
# heading_pattern = re.compile('^(#+)\s*(.*?)\s*(?:#+)?$', re.MULTILINE)
#
# # 定义Table of Contents的格式
# toc_template = '\n# {}\n\n{}\n'
#
#
# def generate_toc(file_path):
#     # 读取文件内容
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#
#     # 从内容中查找所有标题
#     headings = []
#     for match in heading_pattern.finditer(content):
#         level = len(match.group(1))  # 计算标题级别
#         text = match.group(2)  # 获取标题文本
#         headings.append((level, text))
#
#     # 如果没有找到标题，直接返回
#     if not headings:
#         return
#
#     # 生成Table of Contents
#     toc_items = []
#     for level, text in headings:
#         if text == ft:
#             continue
#
#         # 生成锚点链接
#         anchor = re.sub('[^\w]+', '-', text.lower())
#
#         # 添加Table of Contents条目
#         toc_items.append('{}- [{}](#{})'.format('  ' * (level - 1), text, anchor))
#
#     toc = toc_template.format(ft, '\n'.join(toc_items))
#
#     if '\n'.join(toc_items) in content:
#         print("目录不变")
#         return
#
#     # 将Table of Contents插入到文件开头
#     content = re.sub('^#', toc + '#', content, count=1, flags=re.MULTILINE)
#
#     # 将更新后的内容写回文件
#     with open(file_path, 'w', encoding='utf-8') as f:
#         f.write(content)


# 文件目录生成#############################################


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


##############################################

if __name__ == '__main__':
    #
    # # 定义文件路径
    # file_path = '面试题/README.md'
    # ft = file_path.split('/')[-2]
    # # 判断文件是否存在
    # if not os.path.exists(file_path):
    #     # 如果文件不存在，则创建多级目录和文件
    #     os.makedirs(os.path.dirname(file_path), exist_ok=True)
    #     open(file_path, 'w').close()
    #     print('文件已创建')
    # else:
    #     print('文件已存在')
    #     # 调用generate_toc函数处理Markdown文件
    #     generate_toc(file_path)

    # 文件目录生成#############################################
    # Call the tree() function with the current directory as the root
    tree('.')
    with open('''./README.md''', 'w') as f:
        f.write('\n'.join(lst))
    ##############################################
