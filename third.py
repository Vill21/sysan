import json
import sys

def read_json(file_path: str):
    with open(file_path) as f:
        data = json.load(f)
    
    return data

def print_group(group_name):
    sys.stdout.write(str(group_name[0]))
    for i in range(1, len(group_name)):
        sys.stdout.write(" < ")
        sys.stdout.write(str(group_name[i]))

def main():
    data = read_json("third.json")
    A = data["A"]
    B = data["B"]

    print_group(A)
    print()
    print_group(B)
        

if __name__ == "__main__":
    main()