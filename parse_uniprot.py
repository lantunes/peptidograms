
if __name__ == '__main__':
    with open("/Users/luis/Downloads/uniprot_sprot.dat", "rt") as f, open("out/uniprot_corpus.txt", "wt") as out:

        curr_seq = []
        in_seq = False
        for line in f.readlines():

            line = line.strip()
            if line.startswith("SQ   "):
                in_seq = True

            if line.startswith("//") and in_seq:
                in_seq = False

                full_seq = " ".join(curr_seq[1:])
                full_seq = full_seq.replace(" ", "")
                out.write("".join([i + " " for i in full_seq]).strip() + "\n")

                curr_seq = []

            if in_seq:
                curr_seq.append(line)

        out.flush()
