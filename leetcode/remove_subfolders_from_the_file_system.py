'''
Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

    For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.



Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]

'''

class Solution:
    def removeSubfolders(self, folder) -> list[str]:
        # Create a set to store all folder paths for fast lookup
        folder_set = set(folder)
        result = []

        # Iterate through each folder to check if it's a sub-folder
        for f in folder:
            is_sub_folder = False
            prefix = f

            # Check all prefixes of the current folder path
            while not prefix == "":
                pos = prefix.rfind("/")
                if pos == -1:
                    break

                # Reduce the prefix to its parent folder
                prefix = prefix[0:pos]

                # If the parent folder exists in the set, mark as sub-folder
                if prefix in folder_set:
                    is_sub_folder = True
                    break

            # If not a sub-folder, add it to the result
            if not is_sub_folder:
                result.append(f)
        return result

folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]

sol=Solution()
print(sol.removeSubfolders(folder))