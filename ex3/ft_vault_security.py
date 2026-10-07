def secure_archive(filename, action='r', content=''):
    try:
        if action == 'r':
            with open(filename, 'r') as file_stream:
                data = file_stream.read()
            return (True, data)
        elif action == 'w':
            with open(filename, 'w') as file_stream:
                file_stream.write(content)
            return (True, 'Content sucessfully written to file')
    except OSError as e:
        return (False, f"{e}")


def main():
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 'r'))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd', 'r'))
    print("\nUsing 'secure_archive' to read from a regular file:")
    read_result = secure_archive('ancient_fragment.txt', 'r')
    print(read_result)
    print("Using 'secure_archive' to write previous content to a new file:")
    if read_result[0] is True:
        print(secure_archive('new_vault_file.txt', 'w', read_result[1]))


if __name__ == "__main__":
    main()
