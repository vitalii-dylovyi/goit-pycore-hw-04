def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                _, salary = line.strip().split(',')
                total += int(salary)
                count += 1
        if count == 0:
            return 0, 0
        average = total / count
        return total, average
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    except ValueError:
        print("Invalid data format in the file")
        return 0, 0

# Example usage
if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")