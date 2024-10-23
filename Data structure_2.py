#!/usr/bin/env python
# coding: utf-8

# <center><img src="bits-pilani-logo.png" alt="Drawing" style="width: 180px;"/></center>

# <center>
#     <B><h1><font color=blue>Birla Institute of Technology & Science, Pilani</font></h1></B>
#     <h3><font color=gray>Work-Integrated Learning Programmes Division<br>MTech in Data Science & Engineering<br>S1_2022-2023, DSECLZG519- Data Structures & Algorithms Design</font></h3>
# </center>
# 

# <h3><font color=blue><center><B>Assignment 1 – PS10 - My Paths<B></center></font></h3>

# <h4><B>Problem Statement</B></h4>You want to walk in a forest but you can only walk the paths where the sum is your lucky number (given).<br>You start at a fixed point forming a tree of paths. Don’t worry atleast one valid
# path will always be there.<br>Eg:<br>If the tree is "<font color=blue>5,4,8,11,null,9,4,-7,2,null,null,5,1</font>” which becomes

# <div style="max-width:400px;margin-left: auto; margin-right: auto;"> 
#     <img src="tree-1.png" alt="Drawing" style="width: 1500px;"/>
# </div> 

# Here if your lucky number was "<b><font color=red>22</font></b>" you can find three paths (paths have to be from root to leaf only):
# <br>"<b><font color=green>5,4,11,2;5,8,9;5,8,4,5</font></b>"
# <br><br><br>
# Another example:<br>Input: 1,4,3,null,null,-10,null,10,2::5

# <img src="tree-2.png" alt="Drawing" style="width: 300px;"/>

# Tree:
# <br>
# lucky number: 5
# <br>
# Paths: 1,4;1,3,-10,11
# <br><br><br>
# Another example:
# <br>
# Input: 1,2,3,4,5,null,-4,1::0

# <img src="tree-3.png" alt="Drawing" style="width: 300px;"/>

# Tree:
# <br>
# lucky number: 0
# <br>
# Paths: 1,3,-4

# <h4><B>Problem Solution:</B></h4>

# In[22]:


# Class TreeNode : Datastructure for the tree node/s
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# In[31]:


# construct_bst_from_input parse the input string and create Binary structured tree
# Parse Tree nodes with ',' and Luckey sum as separator ::
# input  : input string, i.e. 5,4,8,11,null,9,4,-7,2,null,null,5,1::22
# output : BST, luckey_sum 

def construct_bst_from_input(input_str):
    try:
        # Input string format: "node1,node2,node3::lucky_sum"
        nodes_str, lucky_sum_str = input_str.split("::")
        
        # Convert nodes string to a list of integers, ignoring 'null' values
        nodes = [int(val) if val != 'null' else None for val in nodes_str.split(",")]

        # Convert lucky sum string to an integer
        lucky_sum = int(lucky_sum_str)

        return construct_bst(nodes), lucky_sum
    except ValueError:
        raise ValueError("Invalid input format: {}".format(input_str))
        


# In[32]:


# construct_bst Constructs a Binary Structured Tree from a node list
# stack used to construct the BST
# input  : Node list which of BST need to be create 
# output : 'root' node returns

def construct_bst(nodes):

    if not nodes:
        return None

    root = TreeNode(nodes[0])
    stack = [root]
    i = 1

    while i < len(nodes):
        current_node = stack.pop(0)

        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            stack.append(current_node.left)

        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            stack.append(current_node.right)

        i += 1

    return root


# In[33]:


# dfsalgo_print_path prints all paths in the Binary tree which of sum matches to the lucky number.
# input  : root node, luckey_number, path and output file where result need to write.
# output : possible all paths as result written into the output_file.

def dfsalgo_print_path(root, lucky_number, path, output_file):
    
    if root is None:
        return

    # Add the current node to the path
    path.append(root.val)

    # If the current node is a leaf and the sum equals the lucky number, write the path to the output file
    if root.left is None and root.right is None and sum(path) == lucky_number:
        output_file.write(",".join(map(str, path)) + ";")

    # Recursively traverse the left and right subtrees
    dfsalgo_print_path(root.left, lucky_number, path.copy(), output_file)
    dfsalgo_print_path(root.right, lucky_number, path.copy(), output_file)


# In[34]:


# process_input_file read input from a text file, process each entry, and write output to another text file
# input  : input_file_path which contains input string one / more entries having node and luckey number  
#          output_file_path where all possible path printed for the input string
# output : raise an error for invalid format of string and input file not exist

def process_input_file(input_file_path, output_file_path):
    try:
        
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'r+') as output_file:
            for line in input_file:
                input_str = line.strip()
                root, lucky_number = construct_bst_from_input(input_str)
                             
                # Print paths with sum equal to the lucky number for each entry
                dfsalgo_print_path(root, lucky_number, [], output_file)
                
                #adding new line for new sring of data
                output_file.write("\n")
                                
    except FileNotFoundError:
        raise FileNotFoundError("Input file not found: {}".format(input_file_path))
    except Exception as e:
        raise RuntimeError("An error occurred: {}".format(str(e)))
        


# In[35]:


# outputfile_format updates output text file, extra ; removed from each line end 
# input  : output_file_path which contains result one / more entries of path/s  
# output : expexted result file format 

def outputfile_format(output_file_path):
    #reading each lines in read mode
    with open(output_file_path, 'r') as file:
        lines = file.readlines()
    
    #removing extra ';' from each end of line 
    with open(output_file_path, 'w') as file:
        for line in lines:
            line = line[:-2] + '\n'
            file.write(line)


# In[36]:


# process input file and generate output 
try:
    input_file_path  = "inputPS10.txt"
    output_file_path = "outputPS10.txt" 
    process_input_file(input_file_path, output_file_path)
    outputfile_format(output_file_path)
except Exception as e:
    print("Error: {}".format(str(e)))


# In[ ]:




