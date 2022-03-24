import itertools

##
# Returns a list with an euclidean sequence.
# 
# http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf
#
# This algorythm is better explained with an example:
#
# steps = 13
# pulses = 5
#
# 1. Put all the ones to the left of a list:
#   [[1][1][1][1][1][0][0][0][0][0][0][0][0]]
#
# 2. Move the zeros (remainders) after each one to build sequences. In this step, the
#    remainder_index variable would have a value of 5 (It separates the
#    semi-complete sequences from the remainders):
#    [ [1 0] [1 0] [1 0] [1 0] [1 0] || [ 0 ] [ 0 ] [ 0 ] ]
#
# 3. Same, remainder_index would be 3.
#    [ [1 0 0] [1 0 0] [1 0 0] || [1 0] [1 0] ]
#
# 3. Same, remainder_index would be 2.
#    [ [1 0 0 1 0] [1 0 0 1 0] || [1 0 0] ]
#
# 4. Algorythm ends when there one or zero remainders.
def euclidean(steps, pulses, rotation):
    pulses = int(pulses)
    steps = int(steps)
    rotation = int(rotation)

    if pulses < 0:
        pulses = 0

    if steps < 1:
        steps = 1

    if rotation < 0:
        rotation = 0

    if pulses > steps:
        pulses = steps

    # Initial sequence, ones to the left, zeros to the right.
    sequences = []
    num_ones = pulses
    num_zeros = steps - pulses
    for i in range(0, num_ones):
        sequences.append([1])
    for i in range(0, num_zeros):
        sequences.append([0])
    remainder_index = num_ones

    while True:
        # Finish if num remainders is 1 or 0
        num_remainders = len(sequences) - remainder_index
        if num_remainders <= 1:
            break

        # Move remainders to the end of sequences
        num_sequences = remainder_index
        num_moves = min(num_remainders, num_sequences)
        for i in range(0, num_moves):
            remainder = sequences.pop(remainder_index)
            sequences[i] = sequences[i] + remainder
            num_remainders = num_remainders - 1

        # Calculate new remainder_index
        for i in range(1, len(sequences)):
            left_len = len(sequences[i - 1])
            right_len = len(sequences[i])
            if left_len > right_len:
                remainder_index = i
                break

    # Flatten the sequence and return.
    sequence = sum(sequences, [])
    sequence = rotate(sequence, rotation)
    return sequence


##
# Rotates a list to the right, removing n elements from the end and putting
# them at the beginning
def rotate(lst, n):
    index = len(lst) - n
    return lst[index:] + lst[:index]


