"""
Author: Serhii Zhdaniuk
Date: 2025-10-19
"""

def get_file_content(file):
    try:
        with open(file, 'r') as fh:
            lines = fh.readlines()
            result = []

            for line in lines:
                result.append(line.strip())

            return result
    except FileNotFoundError:
        raise "File Not Found"

def total_salary(path):
    try:
        content = get_file_content(path)
        salary = []

        for line in content:
            _, salary_value = line.split(',')
            salary.append(int(salary_value))

        total = sum(salary)
        average = int(total / len(salary))

        return f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    except:
        print("Couldn't load content from file.")


print(total_salary('data.txt'))