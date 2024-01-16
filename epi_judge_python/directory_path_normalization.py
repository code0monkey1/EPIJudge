from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:

   stack=[]

   path = path.replace('//','/')

   for token in path.split('/'):
       
       if token=='..' :
           if stack and stack[-1]!='..' :
               stack.pop()
           else:
               stack.append(token)
       
       elif token !='.' and token !='':
           stack.append(token)
   
   result=''
   
   while stack:
       res=stack.pop()
       result=('/' if stack else '')+res+result

   if path and path[0]=='/':
       result='/'+result

   return result

           


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
