def Ps_LXX(Ps_TM):
    """
    This function takes a list of Psalms in the TM (Traditional Masoretic) numbering
    and returns the corresponding Psalms in the LXX (Septuagint) numbering.
    """
    # Mapping of TM to LXX Psalm numbers

    # Build a dictionary: keys are TM Psalm numbers, values are LXX Psalm numbers
    tm_to_lxx = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
                 '6': '6', '7': '7', '8': '8', '9': '9A', '10': '9B'}

    for i in range(11, 114):
        tm_to_lxx[str(i)] = str(i - 1)

    tm_to_lxx['114'] = '113A'
    tm_to_lxx['115'] = '113B'
    tm_to_lxx['116A'] = '114'
    tm_to_lxx['116B'] = '115'

    for i in range(117, 147):
        tm_to_lxx[str(i)] = str(i - 1)

    tm_to_lxx['147A'] = '146'
    tm_to_lxx['147B'] = '147'
    tm_to_lxx['148'] = '148'
    tm_to_lxx['149'] = '149'
    tm_to_lxx['150'] = '150'
    tm_to_lxx['151'] = '151'

    return [tm_to_lxx.get(psalm, psalm) for psalm in Ps_TM]




# ------------ Example usage:

# import numpy as np

# # create a list of Psalms in TM numbering
# ps = [str(i) for i in range(1, 151)]
# ps[115] = '116A'
# ps = np.insert(ps, 116, ['116B'])
# ps[147] = '147A'
# ps = np.insert(ps, 148, ['147B'])

# print(ps)
# print(Ps_LXX(ps))
