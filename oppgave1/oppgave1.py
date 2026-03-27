# Previous active version kept for documentation purposes.
# # oppgave1.py - Caesar / ROT brute force for MC103 Exam
# c1 = "IJKLE LWPZQ LRTCW QFWWZ QDZFY OLYOQ FCJDT RYTQJ TYRYZ ESTYR"
# c2 = "QBBJXUMEHBTYIQIJQWUQDTQBBJXUCUDQDTMECUDCUHUBOFBQOUHI"
# c3 = "ZA z9 TcVmVi A5 3zE kyz4x9 r SzA sF vE6r4uz4x R26yrsvA r4u ruuz4x 4B3sv89"
# def caesar_brute_str(ciphertext, shift):
#     result = []
#     for ch in ciphertext:
#         if ch.isalpha():
#             base = ord("A") if ch.isupper() else ord("a")
#             result.append(chr((ord(ch) - base - shift) % 26 + base))
#         else:
#             result.append(ch)
#     return "".join(result)
# def caesar_brute(ciphertext, label):
#     print(f"\n{'=' * 60}")
#     print(f"CIPHER: {label}")
#     print(f"{'=' * 60}")
#     for shift in range(1, 26):
#         print(f"  Shift {shift:2d}: {caesar_brute_str(ciphertext, shift)}")
# def rot47(text):
#     result = []
#     for ch in text:
#         code = ord(ch)
#         if 33 <= code <= 126:
#             result.append(chr(33 + (code - 33 + 47) % 94))
#         else:
#             result.append(ch)
#     return "".join(result)
# def rot18(text):
#     result = []
#     for ch in text:
#         if "0" <= ch <= "9":
#             result.append(chr((ord(ch) - ord("0") + 5) % 10 + ord("0")))
#         elif "A" <= ch <= "Z":
#             result.append(chr((ord(ch) - ord("A") + 13) % 26 + ord("A")))
#         elif "a" <= ch <= "z":
#             result.append(chr((ord(ch) - ord("a") + 13) % 26 + ord("a")))
#         else:
#             result.append(ch)
#     return "".join(result)
# caesar_brute(c1, "C1 - store bokstaver")
# caesar_brute(c2, "C2 - lang streng")
# print(f"\n{'=' * 60}")
# print("CIPHER 3 - ROT47 forsøk:")
# print(f"{'=' * 60}")
# print(f"  ROT47: {rot47(c3)}")
# print(f"\n{'=' * 60}")
# print("CIPHER 3 - Extended Caesar (letters + digits alphabet):")
# print(f"{'=' * 60}")
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
# for shift in range(len(alphabet)):
#     rotated = alphabet[-shift:] + alphabet[:-shift]
#     table = str.maketrans(alphabet, rotated)
#     result = c3.translate(table)
#     print(f"  Shift {shift:2d}: {result}")
#     if "CLEVER" in result or "clever" in result:
#         print(f"\n  *** FOUND: shift={shift} ***")
#         print(f"  Plaintext: {result}")
#         break
# print(f"\n{'=' * 60}")
# print("CIPHER 3 - Caesar brute force:")
# caesar_brute(c3, "C3 - blandet")
# print("\n=== BESTE TREFF (automatisk scoring) ===")
# common_words = [
#     "the", "and", "is", "of", "to", "in", "it", "that", "this",
#     "with", "for", "are", "was", "have", "world", "all", "men",
#     "women", "stage",
# ]
# for label, cipher in [("C1", c1), ("C2", c2), ("C3", c3)]:
#     best_shift = 0
#     best_score = -1
#     best_text = ""
#     for shift in range(1, 26):
#         decrypted = caesar_brute_str(cipher, shift)
#         score = sum(decrypted.lower().count(word) for word in common_words)
#         if score > best_score:
#             best_score = score
#             best_shift = shift
#             best_text = decrypted
#     print(f"\n{label}: Beste shift = {best_shift} (score={best_score})")
#     print(f"     Plaintext: {best_text}")

# oppgave1.py - Caesar / ROT brute force for MC103 Exam


c1 = "IJKLE LWPZQ LRTCW QFWWZ QDZFY OLYOQ FCJDT RYTQJ TYRYZ ESTYR"
c2 = "QBBJXUMEHBTYIQIJQWUQDTQBBJXUCUDQDTMECUDCUHUBOFBQOUHI"
c3 = "ZA z9 TcVmVi A5 3zE kyz4x9 r SzA sF vE6r4uz4x R26yrsvA r4u ruuz4x 4B3sv89"


def caesar_brute_str(ciphertext, shift):
    result = []
    for ch in ciphertext:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def group_text(text, group_size=5):
    return " ".join(text[i:i + group_size] for i in range(0, len(text), group_size))


def format_c2_readable(text):
    words = [
        "ALL", "THE", "WORLD", "IS", "A", "STAGE", "AND", "ALL",
        "THE", "MEN", "AND", "WOMEN", "MERELY", "PLAYERS",
    ]
    compact = "".join(words)
    if text.upper() == compact:
        return " ".join(words)
    return text


def caesar_brute(ciphertext, label, group_size=None):
    print(f"\n{'=' * 60}")
    print(f"CIPHER: {label}")
    print(f"{'=' * 60}")
    for shift in range(1, 26):
        decrypted = caesar_brute_str(ciphertext, shift)
        if group_size is not None:
            decrypted = group_text(decrypted, group_size)
        print(f"  Shift {shift:2d}: {decrypted}")


def rot47(text):
    result = []
    for ch in text:
        code = ord(ch)
        if 33 <= code <= 126:
            result.append(chr(33 + (code - 33 + 47) % 94))
        else:
            result.append(ch)
    return "".join(result)


caesar_brute(c1, "C1 - uppercase only")
caesar_brute(c2, "C2 - long string", group_size=5)

print("\nAdding some spaces for readability:")
print(format_c2_readable(caesar_brute_str(c2, 16)))


print(f"\n{'=' * 60}")
print("CIPHER 3 - ROT47 attempt:")
print(f"{'=' * 60}")
print(f"  ROT47: {rot47(c3)}")


# ─── C3: Extended Caesar with alphanumeric alphabet (letters + digits) ──────
# Standard Caesar only shifts letters (a-z, A-Z).
# C3 contains digits mixed into words, so we use an extended 62-character
# alphabet that includes digits. This allows the cipher to shift digits too.
print(f"\n{'=' * 60}")
print("CIPHER 3 - Extended Caesar (alphanumeric alphabet, all shifts):")
print(f"{'=' * 60}")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

correct_shift = None
correct_plaintext = None

for shift in range(len(alphabet)):
    rotated = alphabet[-shift:] + alphabet[:-shift]
    table = str.maketrans(alphabet, rotated)
    result = c3.translate(table)
    print(f"  Shift {shift:2d}: {result}")
    if "clever" in result.lower() and correct_shift is None:
        correct_shift = shift
        correct_plaintext = result

print(f"\n{'=' * 60}")
print("CIPHER 3 - RESULT:")
print(f"{'=' * 60}")
if correct_shift is not None:
    print(f"  Found at shift = {correct_shift}")
    print(f"  Plaintext: {correct_plaintext}")
else:
    print("  No clean plaintext found.")


print("\n=== BEST SHIFT (automatic scoring) ===")

common_words = [
    "the", "and", "is", "of", "to", "in", "it", "that", "this",
    "with", "for", "are", "was", "have", "world", "all", "men",
    "women", "stage", "players", "girl", "sound", "fury",
]

for label, cipher in [("C1", c1), ("C2", c2)]:
    best_shift = 0
    best_score = -1
    best_text = ""
    for shift in range(1, 26):
        decrypted = caesar_brute_str(cipher, shift)
        score = sum(decrypted.lower().count(word) for word in common_words)
        if score > best_score:
            best_score = score
            best_shift = shift
            best_text = decrypted
    print(f"\n{label}: Best shift = {best_shift} (score={best_score})")
    print(f"     Plaintext: {best_text}")

print(f"\nC3: Best shift = {correct_shift} (extended alphanumeric alphabet)")
print(f"     Plaintext: {correct_plaintext}")
