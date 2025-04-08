#!/usr/bin/env python3
"""
Script to create folder structure for stock market data analysis project.
"""

import os
import sys

def create_directory(path):
    """Creates a directory if it doesn't exist."""
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")
        else:
            print(f"Directory already exists: {path}")
    except Exception as e:
        print(f"Error creating directory {path}: {e}")

def create_empty_file(path):
    """Creates an empty file if it doesn't exist."""
    try:
        # Ensure the directory exists
        dir_path = os.path.dirname(path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                pass  # Creates empty file
            print(f"Created empty file: {path}")
        else:
            print(f"File already exists: {path}")
    except Exception as e:
        print(f"Error creating file {path}: {e}")

def create_project_structure():
    """Creates the project folder structure."""
    
    # Get current directory
    base_dir = os.getcwd()
    
    # Define project name and path
    project_name = "stock-analysis-project"
    project_path = os.path.join(base_dir, project_name)
    
    print(f"Creating project structure in: {project_path}")
    
    # Create main project directory
    create_directory(project_path)
    
    # Create subdirectories
    directories = [
        os.path.join(project_path, "data", "raw"),
        os.path.join(project_path, "data", "processed"),
        os.path.join(project_path, "notebooks"),
        os.path.join(project_path, "scripts"),
        os.path.join(project_path, "results", "figures"),
        os.path.join(project_path, "results", "reports"),
        os.path.join(project_path, "utils")
    ]
    
    for directory in directories:
        create_directory(directory)
    
    # Create empty script files
    script_files = [
        os.path.join(project_path, "scripts", "download_data.py"),
        os.path.join(project_path, "scripts", "process_data.py"),
        os.path.join(project_path, "scripts", "analyze_data.py"),
        os.path.join(project_path, "scripts", "visualize_data.py"),
        os.path.join(project_path, "scripts", "main.py"),
        os.path.join(project_path, "utils", "__init__.py"),
        os.path.join(project_path, "utils", "api_helpers.py"),
        os.path.join(project_path, "utils", "indicators.py"),
        os.path.join(project_path, "config.py"),
        os.path.join(project_path, "README.md"),
        os.path.join(project_path, "requirements.txt"),
        os.path.join(project_path, ".gitignore")
    ]
    
    for file_path in script_files:
        create_empty_file(file_path)
    
    print(f"\nProject structure '{project_name}' has been successfully created.")
    print(f"Next step: cd {project_name}")

if __name__ == "__main__":
    try:
        create_project_structure()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)