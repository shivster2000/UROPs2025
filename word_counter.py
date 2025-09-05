file_path = "/Users/shivan/Documents/UROPs/BabyLM_Corpora/Combined CEFR txt docs/combined-A-clean.txt"  # update this

word_count = 0
with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        line = line.strip()  # remove leading/trailing whitespace
        if line:  # skip empty lines
            words = line.split()
            word_count += len(words)

print(f"✅ Word count for {file_path}: {word_count}")