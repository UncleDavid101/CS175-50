def read_file(file_path, search_term):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if search_term in content:
                raise Exception(f"Search term '{search_term}' found in file content.")
            print("File read successfully.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except IsADirectoryError:
        print("Error: The specified path is a directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'example.txt'
search_term = 'search_term'
read_file(file_path, search_term)