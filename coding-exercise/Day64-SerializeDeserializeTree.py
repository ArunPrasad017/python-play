def serialize(self, root):
    """Encodes a tree to a single string
    :type root: TreeNode
    :rtype: str
    """
    def serialize(root):
        def recurse_serialize(root, lst):
            if root is None:
                lst.append = ['None']
            else:
                lst.append(root.val)
                if root.left:
                    recurse_serialize(root.left, lst)
                if root.right:
                    recurse_serialize(root.right, lst)
            return "".join(lst)
        return recurse_serialize(root,[])
    
    def deserialize(data):
        def recurse_deserialize(lst):
            if lst[0] == 'None':
                lst.pop(0)
                return None
            root = TreeNode(lst[0])
            lst.pop(0)
            root.left = recurse_deserialize(lst)
            root.right = recurse_deserialize(lst)
            return root
        data_list = data.split(',')
        root = recurse_deserialize(data_list)
        return root
