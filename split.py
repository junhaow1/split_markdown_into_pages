def split_markdown(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        sections = content.split("## ")
        for idx, section in enumerate(sections[1:]):
            with open(f'page{idx+1}.md', 'w') as new_file:
                new_file.write("## " + section)

file_path = 'input.md'  # Replace this with the path to your Markdown file
split_markdown(file_path)
