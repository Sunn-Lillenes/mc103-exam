#!/usr/bin/env python3


def rail_fence_decrypt(ciphertext, rails):
    """Rail Fence Cipher decryption."""
    text = "".join(ch for ch in ciphertext if ch.isalpha())
    length = len(text)

    pattern = []
    row = 0
    direction = 1
    for _ in range(length):
        pattern.append(row)
        row += direction
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

    row_counts = [0] * rails
    for rail in pattern:
        row_counts[rail] += 1

    rows = []
    idx = 0
    for count in row_counts:
        rows.append(list(text[idx: idx + count]))
        idx += count

    decrypted = []
    for rail in pattern:
        decrypted.append(rows[rail].pop(0))

    return "".join(decrypted)


def main():
    ciphertext = "Teu cgeno jmsvr hlz dghqi kref xup oete ayo."
    print(f"Ciphertext: {ciphertext}")
    print("Trying rail counts from 2 to 10...\n")

    best_rails = None
    best_text = None

    for rails in range(2, 11):
        result = rail_fence_decrypt(ciphertext, rails)
        print(f"Rails={rails}: {result}")
        if rails == 2:
            best_rails = 2
            best_text = result

    if best_rails:
        print("\n----\n")
        print(f"*** The best decryption (rails={best_rails}) is:\n{best_text}\n")


if __name__ == "__main__":
    main()
