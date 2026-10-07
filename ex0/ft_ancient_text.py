import sys
import typing


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ft_ancient_text.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
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
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
