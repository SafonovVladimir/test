def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


print(DNA_strand("AAAA"))
