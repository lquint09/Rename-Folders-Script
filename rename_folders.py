import os
import sys

def rename_folders_recursively(root_dir, replaced_char, new_char):
    """
    Walks through a directory tree from the bottom up and renames
    any directories that contain spaces, replacing them with underscores.
    """
    if not os.path.isdir(root_dir):
        print(f"Error: Path '{root_dir}' is not a valid directory.")
        return

    print(f"Scanning directory: {root_dir}\n")
    
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            if replaced_char in dirname:
                old_path = os.path.join(dirpath, dirname)
                new_name = dirname.replace(f"{replaced_char}", f"{new_char}")
                new_path = os.path.join(dirpath, new_name)
                
                print(f"Renaming: '{old_path}'")
                print(f"      to: '{new_path}'")
                
                try:
                    os.rename(old_path, new_path)
                    print("  ...Success.\n")
                except OSError as e:
                    print(f"  ...Error renaming '{old_path}': {e}\n")

def main():
    # Get the target directory from the user
    target_directory = input("Please enter the full path to the directory you want to process: ")
    clearScreen()
    replaced_character = input("Please enter the chacracter you would like to replace:")
    clearScreen()
    new_character = input(f"Please enter the character you woukd like to replace '{replaced_character}' with:")
    clearScreen()
    
    # Clean up the path (e.g., remove trailing slashes or quotes)
    target_directory = target_directory.strip().strip("'\"")
    
    if not os.path.isdir(target_directory):
        print(f"Error: The path you entered is not a valid directory.")
        print("Please run the script again.")
        sys.exit(1)
        
    # Ask for confirmation before proceeding
    print("\n--- WARNING ---")
    print(f"You are about to rename all subfolders containing {replaced_character} inside:")
    print(f"{target_directory}")
    print("This action cannot be undone automatically.")
    
    confirm = input("Are you sure you want to continue? (y/n): ").lower().strip()
    
    if confirm == 'y':
        print("\nStarting rename process...")
        rename_folders_recursively(target_directory, replaced_character, new_character)
        print("\nProcess complete.")
    if confirm == 'n':
        print("\nOperation cancelled. No changes were made.")
    else:
        print("Please enter 'y' or 'n'")

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()