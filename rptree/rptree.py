import os
import pathlib

PIPE = "|"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:
    def __init__(self, root_dir, dir_only = False):
        self._generator = _TreeGenerator(root_dir, dir_only)

    def generate(self):
        tree = self._generator.buildTree()
        for entry in tree:
            print(entry)

class _TreeGenerator:
    def __init__(self, root_dir, dir_only = False):
        self.root_dir = pathlib.Path(root_dir)
        self.dir_only = dir_only
        self.tree = []

    def buildTree(self):
        self._tree_head()
        self._tree_body(self.root_dir)
        return self.tree

    def _tree_head(self):
        self.tree.append(f"{self.root_dir}{os.sep}")
        self.tree.append(PIPE)

    def _prepare_entries(self, directory):
        entries = directory.iterdir()
        if(self.dir_only):
            entries = [entry for entry in entries if entry.is_dir()]
            return entries

        entries= sorted(entries, key = lambda entry: entry.is_file())
        return entries

    def _tree_body(self, directory, prefix=""):
        entries = self._prepare_entries(directory)
        entries_count = len(entries)                                            #Calculating the number of files/dirs in the directory

        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE            #Initializing the connector for tree
            if entry.is_dir():                                                  #Adding sub-directory to tree
                self._add_directory(
                    entry, index, entries_count, prefix, connector
                )
            else:
                self._add_file(                                                #Adding file to the tree
                    entry, prefix, connector
                )

    def _add_directory(self, directory, index, entries_count, prefix, connector):
        self.tree.append(f"{prefix}{connector} {directory.name}{os.sep}")               #Printing the name of the directory

        if(index != entries_count-1):
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX

        self._tree_body(
            directory = directory,
            prefix = prefix)

        self.tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        self.tree.append(f"{prefix}{connector} {file.name}")


