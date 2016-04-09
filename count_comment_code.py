import os

codes_path = "codes/"

def line_counter(dir):
    codes = os.listdir(dir)
    print codes
    code_lines = 0
    empty_lines = 0
    comment_lines = 0
    for i in codes:
        with open(dir + i) as code_file:
            codes_lines = code_file.readlines()

            for line in codes_lines:
                line = line.strip()
                if line.startswith("#"):
                    comment_lines += 1
                elif line == "":
                    empty_lines += 1
                else:
                    code_lines += 1
    print("There are " +
          str(code_lines) + " code lines, " +
          str(comment_lines) + " comment lines, and " +
          str(empty_lines) + " empty lines.")

if __name__ == '__main__':
    line_counter(codes_path)
