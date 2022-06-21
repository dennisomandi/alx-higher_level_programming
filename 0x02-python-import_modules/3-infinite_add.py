#!/usr/bin/python3
# 3-infinite_add.py

<<<<<<< HEAD

=======
>>>>>>> 4df73bd45a00a07c367c69068cbd7295e3c4b755
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
