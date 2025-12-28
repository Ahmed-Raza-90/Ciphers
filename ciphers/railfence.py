def encrypt(text, rails):
    fence = ['' for _ in range(rails)]
    row, step = 0, 1
    for c in text:
        fence[row] += c
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step
    return ''.join(fence)

def decrypt(text, rails):
    pattern = list(range(rails)) + list(range(rails-2, 0, -1))
    rail_len = [0]*rails
    for i in range(len(text)):
        rail_len[pattern[i % len(pattern)]] += 1
    rails_text, idx = [], 0
    for r in rail_len:
        rails_text.append(text[idx:idx+r])
        idx += r
    result, rail_idx = "", [0]*rails
    for i in range(len(text)):
        r = pattern[i % len(pattern)]
        result += rails_text[r][rail_idx[r]]
        rail_idx[r] += 1
    return result
