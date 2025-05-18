import os
import shutil
from markdown_to_html import markdown_to_html_node, extract_h1

def main():
    copy_files_to_public()
    generate_page("./content/index.md", "./content/template.html", "./public/index.html")


def copy_files_to_public():
    if (os.path.exists("./static") != True):
        raise Exception("No static directory")
    
    shutil.rmtree("./public")
    os.mkdir("./public")

    copy_files()
    

def copy_files(current_directory="./static"):
    dir_content = os.listdir(current_directory)
    for item in dir_content:
        file_path = current_directory + "/" + item
        if os.path.isfile(file_path):
            new_location = file_path.replace("static", "public")
            shutil.copy(file_path, new_location)
        else:
            os.mkdir(file_path.replace("static", "public"))
            copy_files(file_path)



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    with open(from_path, 'r') as file:
        markdown = file.read()
    child_html_nodes = markdown_to_html_node(markdown)
    inner_html = child_html_nodes.to_html()
    title = extract_h1(markdown)

    template = ""
    with open(template_path, 'r') as file:
        template = file.read()
    
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", inner_html)

    # dirname = os.path.dirname(dest_path)
    # os.makedirs(dirname)
    html_file = open(dest_path, 'w')
    html_file.write(template)
    html_file.close()

    




main()