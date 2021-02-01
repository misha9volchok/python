# PROGRAMMER MICHAEL VOLCHOK
def write_to_file(file_path: str, contents_to_write: str):
    """
    Function writes the passed contents into the specific file
    :param file_path: A file to write to
    :param contents_to_write: Contents to write
    :return: None
    """

    try:
        with open(file_path, 'a') as f:
            f.write(str(contents_to_write))  # Casting if the given value is not a string
    except PermissionError:
        # error if the user don't have the permission to create file
        raise PermissionError("You don't have the permissions to write to the file")
