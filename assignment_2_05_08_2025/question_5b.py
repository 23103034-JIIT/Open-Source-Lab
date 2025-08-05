def extsort(files):
    return sorted(files, key=lambda x: x.split('.')[-1] if '.' in x else '')

if __name__ == "__main__":
    files = ['a.txt', 'b.py', 'c.java', 'd.txt', 'e.py']
    sorted_files = extsort(files)
    print(sorted_files)