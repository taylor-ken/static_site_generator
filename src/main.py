from textnode import TextNode, TextType
import os
import shutil

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
    current_path = os.getcwd()
    parent_dir, current_folder = os.path.split(current_path)
    source = os.path.join(parent_dir, 'static')
    destination = os.path.join(parent_dir, 'public')
    copy_static(source, destination)

def copy_static(source, destination):
    if os.path.exists(destination):
        try:
            shutil.rmtree(public_path)
            print(f"Directory {public_path} has been removed successfully")
        except OSError as error:
            print(error)
            print(f"Directory {public_path} can not be removed")
    os.mkdir(destination)
    contents_to_copy = os.listdir(source)
    for item in contents_to_copy:
        if os.path.isfile(item):
            src = os.path.join(source, item)
            dst = os.path.join(destination, item)
            shutil.copy(src, dst)
        if os.path.isdir(item):
            src = os.path.join(source, item)
            dst = os.path.join(destination, item)
            copy_static(source, destination)


main()
