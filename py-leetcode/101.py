
def main(root):
    def is_mirror(tn1, tn2):
        if (tn1 == None) and (tn2 == None):
            return True
        elif (tn1 == None) ^ (tn2 == None):
            return False
        return (tn1.val == tn2.val) and is_mirror(tn1.left, tn2.right) and is_mirror(tn1.right, tn2.left)
    return is_mirror(root, root)
