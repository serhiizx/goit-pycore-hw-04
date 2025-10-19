

def get_cats_info(path):
    try:
        with open(path) as fh:
            result = []
            lines = [line.strip() for line in fh.readlines()]

            for line in lines:
                id, name, age = line.split(",")
                result.append({
                    'id': id,
                    'name': name,
                    'age': age
                })

            return result
    except FileNotFoundError:
        print("File fot found.")
    except:
        print("Unknown error.")


print(get_cats_info('./data.txt'))