    """Given a string path, which is an absolute path (starting with a slash '/') 
    to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
    In a Unix-style file system, a period '.' refers to the current directory, 
    a double period '..' refers to the directory up a level, and any multiple 
    consecutive slashes (i.e. '//') are treated as a single slash '/'. 
    For this problem, any other format of periods such as '...' are treated as file/directory names."""

class Solution:
  def simplifyPath(self, path: str) -> str:

    # Use a stack to store the path
    stack = []

    for str in path.split('/'):

      if str in ('', '.'):
        continue

      # Pop one element of the path whenever user types two dots
      elif str == '..':
        if stack:
          stack.pop()

      # Otherwise, push a path element to the stack
      else:
        stack.append(str)

    # Return simplified path
    return '/' + '/'.join(stack)

# Alternately, you can do the following
class Solution:
  def simplifyPath(self, path: str) -> str:
    return os.path.realpath(path)