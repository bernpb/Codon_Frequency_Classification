# Build out the dictionary of RNA codon to amino acid translations

translation = {'UUU': 'Phe',
'UUC': 'Phe',
'UUA': 'Leu',
'UUG': 'Leu',
'CUU': 'Leu',
'CUC': 'Leu',
'CUA': 'Leu',
'CUG': 'Leu',
'AUU': 'Ile',
'AUC': 'Ile',
'AUA': 'Ile',
'AUG': 'Met',
'GUU': 'Val',
'GUC': 'Val',
'GUA': 'Val',
'GUG': 'Val',
'UCU': 'Ser',
'UCC': 'Ser',
'UCA': 'Ser',
'UCG': 'Ser',
'CCU': 'Pro',
'CCC': 'Pro',
'CCA': 'Pro',
'CCG': 'Pro',
'ACU': 'Thr',
'ACC': 'Thr',
'ACA': 'Thr',
'ACG': 'Thr',
'GCU': 'Ala',
'GCC': 'Ala',
'GCA': 'Ala',
'GCG': 'Ala',
'UAU': 'Tyr',
'UAC': 'Tyr',
'UAA': 'Stop',
'UAG': 'Stop',
'CAU': 'His',
'CAC': 'His',
'CAA': 'Gln',
'CAG': 'Gln',
'AAU': 'Asn',
'AAC': 'Asn',
'AAA': 'Lys',
'AAG': 'Lys',
'GAU': 'Asp',
'GAC': 'Asp',
'GAA': 'Glu',
'GAG': 'Glu',
'UGU': 'Cys',
'UGC': 'Cys',
'UGA': 'Stop',
'UGG': 'Trp',
'CGU': 'Arg',
'CGC': 'Arg',
'CGA': 'Arg',
'CGG': 'Arg',
'AGU': 'Ser',
'AGC': 'Ser',
'AGA': 'Arg',
'AGG': 'Arg',
'GGU': 'Gly',
'GGC': 'Gly',
'GGA': 'Gly',
'GGG': 'Gly'}

# Get a list of all codons
codons = list(translation.keys())

##################################################################


def RNA_to_AA(numeric_columns):

    """
    Translate an RNA codon to its corresponding amino acid
    """

    return translation[codon]


####################################################################

def get_AA(df, columns = codons):
    
    """
    Produce new columns representing amino acid frequency for each observation.
    
    Inputs: 
    df - Dataframe containing codon frequencies that we wish get amino acid frequencies for
    columns - A list of column labels representing codons
    
    Output: 
    
    A new dataframe containing both the codon frequencies and the amino acid frequencies
    
    """

    # Append 'SpeciesName' to the columns list
    
    columns.append('SpeciesName')
    
    # Build a new dataframe with the where the columns are labelled by the amino acid they represent 
    # rather than the codon they represent
    df_AA = df[columns].rename(translation,
                     axis = 1)
    
    # Group columns representing the same amino acid by their sums
    df_AA = df_AA.groupby(lambda x: x,
                         axis = 1).sum()
    # Merge df_AA with df
    df = df.merge(df_AA,
            on = 'SpeciesName')
    return df