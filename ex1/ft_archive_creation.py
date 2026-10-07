import sys
import typing


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ft_archive_creation.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        file_stream: typing.IO = open(filename, 'r')
        content = file_stream.read()
        print("---")
        print(content, end="")
        if len(content) > 0 and content[-1] != '\n':
            print()
        print("---")
        file_stream.close()
        print(f"File '{filename}' closed.")
        print("Transform data:")
        print("---")
        transformed = ""
        for i in range(len(content)):
            if content[i] == '\n':
                transformed += "#\n"
            else:
                transformed += content[i]
        if len(content) > 0 and content[-1] != '\n':
            transformed += "#"
        print(transformed, end="")
        if len(content) > 0 and content[-1] != '\n':
            print()
        print("---")
        new_filename = input("Enter new file name (or empty): ")
        if new_filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            try:
                out_stream: typing.IO = open(new_filename, 'w')
                out_stream.write(transformed)
                out_stream.close()
                print(f"Data saved in file '{new_filename}'.")
            except OSError as e:
                print(f"Error writing to file '{new_filename}': {e}")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
