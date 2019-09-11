
print("================")
print("     BANNER     ")
print("    By Ciera    ")
print("================")
print("")

def banner(subject, author):
    subject_length = len(subject)
    by_line = f"By {author}"
    banner_length = subject_length = 4
    print("================")
    print(f"     {subject}     ")
    print(f"    {by_line}    ")
    print("================")
    print("")

banner("HELLO WORLD", "Ciera")