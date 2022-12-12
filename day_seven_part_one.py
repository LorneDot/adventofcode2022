class Folder:
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        self.folders = {}
        self.files = {}

    def size(self):
        s = sum([file.size for file in list(self.files.values())])
        for folder in self.folders.values():
            s += folder.size()
        return s

class File:
    def __init__(self,name,size):
        self.size = int(size)
        self.name = name

def create_file_system(commands):

    currentFolder = None
    rootFolder = None

    for command in commands:
        command = command.strip()

        if '$ ls' == command[:4]:
            continue

        if command == '$ cd ..':
            currentFolder = currentFolder.parent
            continue

        if '$ cd' == command[:4]:
            if currentFolder is None and '$ cd /' == command:
                currentFolder = Folder(
                    command.split(' ')[2],
                    None
                    )
                rootFolder = currentFolder
                continue
            
            if '$ cd /' == command:
                currentFolder = rootFolder
                continue
            
            currentFolder = currentFolder.folders[command.split(' ')[2]]
            continue

        if 'dir' == command[:3]:
            currentFolder.folders[
                command.split(' ')[1]
            ] = Folder(
                    command.split(' ')[1],
                    currentFolder
                )
            continue

        currentFolder.files[
            command.split(' ')[1]
        ] = File(
                command.split(' ')[1],
                command.split(' ')[0]
            )

    return rootFolder

def traverse_file_system(folder,target_folders):

    if folder.size() <= 100000:
        target_folders.append(folder.size())

    for f in folder.folders.values():
        traverse_file_system(f,target_folders)


if __name__ == '__main__':

    path = '/Users/lornedauterman/Desktop/commands'

    commands =  open(path,'r').readlines()

    rootFolder = create_file_system(commands)

    target_folders = []

    traverse_file_system(rootFolder,target_folders)

    print(sum(target_folders))

