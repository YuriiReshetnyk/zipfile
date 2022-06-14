import re
import zipfile


def main():
    # \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} ERROR .* \[.*\] \(.*\) WFLYCTL\d{4}:.*
    pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} [A-Z]* .* \[.*\] \(.*\) WFLYCTL\d{4}:.*'

    with zipfile.ZipFile("logs.zip", "r") as myfile:
        candidates_list = re.findall(pattern, myfile.read("server.txt").decode())
        
    for line in candidates_list:
        if line:
            print(line)


if __name__ == '__main__':
    main()
