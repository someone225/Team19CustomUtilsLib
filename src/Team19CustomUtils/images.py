import math as m
def a_reduce_dim(input):
    output = [0] *( len(input) * len(input[0]) )
    k = 0
    for i in range(0, len(input)):
        for j in range(0, len(input[0])):
            output[k] = input[i][j]
            k += 1
    return output

def normalize(ch_input):
    """
    normalizes an input array according to the rgb linearlization algorithm
    Args:
        ch_input: a 2d array containing pixel values of one rgb channel

    Returns: 
        void

    Dependencies: 
        requires 'pow' module from library 'math' to linearlize bright pixels
    """
    for i in range(0, len(ch_input)):
        for j in range(0, len(ch_input[0])):
            if(ch_input[i][j] <= 0.0405):
                ch_input[i][j] = ch_input[i][j] / 12.92
            else:
                ch_input[i][j] = m.pow( ((ch_input[i][j] + 0.055)/1.055), 2.4 )  
