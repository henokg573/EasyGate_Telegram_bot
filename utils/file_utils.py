def validate_file(document):
    file_name = document.file_name.lower()
    if not (file_name.endswith('.pdf') or file_name.endswith(('.jpg', '.jpeg', '.png'))):
        return False
    if document.file_size > 10 * 1024 * 1024:
        return False
    return True
