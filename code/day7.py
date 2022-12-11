test = False

num_dirs = 0
all_dirs = []

class Directory:
    def __init__(self, id, parent):
        self.id = id
        self.files = {}
        self.directories = {}
        self.parent_directory = parent

    def add_sizes(self, directory_sizes):
        total = 0
        for file, size in self.files.items():
            total += size
        for directory in self.directories.values():
            total += directory.add_sizes(directory_sizes)
        directory_sizes.append(total)
        return total


file_system = Directory('/', None)
with open('../test_input_files/day7test.txt' if test else '../input_files/day7input.txt','r') as f:
    current_directory = None
    listing_contents = False
    for line in f:
        line = line.rstrip().split()

        if line[0] == 'dir':
            num_dirs += 1
            all_dirs.append(line[1])

        if line[0] == '$':
            listing_contents = False
            if line[1] == 'cd':
                match line[2]:
                    case '/':
                        current_directory = file_system
                    case '..':
                        current_directory = current_directory.parent_directory
                    case _:
                        if line[2] in current_directory.directories.keys():
                            current_directory = current_directory.directories[line[2]]
            else:
                listing_contents = True
        else:
            if listing_contents:
                if line[0] == 'dir':
                    current_directory.directories[line[1]] = Directory(line[1], current_directory)
                else:
                    current_directory.files[line[1]] = int(line[0])

directory_sizes = []
size = file_system.add_sizes(directory_sizes)
print(num_dirs)
print(len(all_dirs))

total = 0

for directory_size in directory_sizes:
    if directory_size <= 100000:
        total += directory_size
print(total)

space_needed = 30000000 - (70000000 - max(directory_sizes))
directory_sizes = sorted(directory_sizes)
for directory_size in directory_sizes:
    if directory_size >= space_needed:
        print(directory_size)
