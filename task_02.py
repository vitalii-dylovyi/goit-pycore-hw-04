def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
        return cats_info
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print("Invalid data format in the file")
        return []

# Example usage
if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)