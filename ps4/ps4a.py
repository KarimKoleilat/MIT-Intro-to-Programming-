# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1: 
        return sequence
    else: 
        ## Take the first letter 
        first_letter = sequence[0]
        remaining_letters = sequence[1:]
        ## Get the permutations of all of the remaining letters (Recursive call) 
        remaining_perm = get_permutations(remaining_letters)
        ## insert letter into each position of every word and return the modified list
        perm_list = []

        for perm in remaining_perm:
            temp_perm = []
            for idx in range(len(perm)+1):
                new_perm = perm[:idx] +first_letter + perm[idx:]
                temp_perm.append(new_perm)
            perm_list.extend(temp_perm)
        return list(set(perm_list))





if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

