# Daily Programmer
# 5-20-18
# https://www.reddit.com/r/dailyprogrammer/comments/8jvbzg/20180516_challenge_361_intermediate_elsiefour/

import numpy as np

def elsie_four(key, text, decryption=True):
    # marker = m, with position (i, j)
    # text character = a, with position (r, c)
    # decrypted/encrypted char = b, with position (x, y)

    if text.startswith('%'):
        decryption = False
        text = text[1:]

    alphabet = '#_23456789abcdefghijklmnopqrstuvwxyz'
    vectors = {i:[n%6, n//6] for n, i in enumerate(alphabet)}   # create dictionary of vectors

    if len(key) != 36:                                          # check for invalid key length
        return '--Error: Please provide a 36-char key--'
    if len(set(alphabet + key + text)) > 36:                    # Check for invalid characters
        return '--Error: Invalid characters in key/text--'

    grid = np.array(list(key)).reshape(6, 6)                    # initialise grid
    m, i, j = key[0], 0, 0                                      # set marker position

    res = ''
    for a in text:                                              # input character
        r, c = np.ravel(np.where(grid == a))

        if decryption:
            x, y = np.subtract([r, c], vectors[m][::-1])%6      # -vectors for decryption
            b = grid[x][y]                                      # decrypted character
            row, col, tile = x, c, a
        else:
            x, y = np.add([r, c], vectors[m][::-1])%6           # +vectors for encryption
            b = grid[x][y]                                      # encrypted character
            row, col, tile = r, y, b 
        res += b

        grid[row] = np.roll(grid[row], 1)                       # rotate row
        col = np.where(grid == tile)[1] 
        grid[:,col] = np.roll(grid[:,col], 1)                   # rotate column

        i, j = np.ravel(np.where(grid == m))                    # find marker
        i, j = np.add([i, j], vectors[tile][::-1])%6            # set new position
        m = grid[i][j]                                          # new marker character

    return res 

print(elsie_four('s2ferw_nx346ty5odiupq#lmz8ajhgcvk79b', 'tk5j23tq94_gw9c#lhzs'))
#print(elsie_four('#o2zqijbkcw8hudm94g5fnprxla7t6_yse3v', 'b66rfjmlpmfh9vtzu53nwf5e7ixjnp'))
#print(elsie_four('9mlpg_to2yxuzh4387dsajknf56bi#ecwrqv', 'grrhkajlmd3c6xkw65m3dnwl65n9op6k_o59qeq'))
#print(elsie_four('7dju4s_in6vkecxorlzftgq358mhy29pw#ba', '%the_swallow_flies_at_midnight'))
