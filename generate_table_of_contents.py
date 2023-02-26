import os
import re

# 定义正则表达式模式，用于匹配Markdown标题
heading_pattern = re.compile('^(#+)\s*(.*?)\s*(?:#+)?$', re.MULTILINE)

# 定义Table of Contents的格式
toc_template = '\n## 面试题\n\n{}\n'

def generate_toc(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 从内容中查找所有标题
    headings = []
    for match in heading_pattern.finditer(content):
        level = len(match.group(1))  # 计算标题级别
        text = match.group(2)  # 获取标题文本
        headings.append((level, text))

    # 如果没有找到标题，直接返回
    if not headings:
        return

    # 生成Table of Contents
    toc_items = []
    for level, text in headings:
        # 生成锚点链接
        anchor = re.sub('[^\w]+', '-', text.lower())

        # 添加Table of Contents条目
        toc_items.append('{}- [{}](#{})'.format('  ' * (level-1), text, anchor))

    toc = toc_template.format('\n'.join(toc_items))

    # 将Table of Contents插入到文件开头
    content = re.sub('^#', toc + '#', content, count=1, flags=re.MULTILINE)

    # 将更新后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    # 调用generate_toc函数处理Markdown文件
    file_path = '面试题/README.md'
    generate_toc(file_path)
