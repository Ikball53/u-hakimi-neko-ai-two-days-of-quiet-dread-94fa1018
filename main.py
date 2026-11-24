import os

# Single fixed line: a flat approval carrying quiet dread. No input, no
# randomness, no network — the same bytes are written on every run.
LINE = "Approved. The test passes for reasons nobody remembers, and I stopped asking."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))

if __name__ == "__main__":
    main()
