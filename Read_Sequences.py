def read_sequences(sequence_file):
    
    """
    Read in a FASTA sequence file, return a string containing just the bases of the 
    antisense strand of the sequence
    """
    
    # read in the sequence data
    sequence = open(sequence_file, 'r')
    lines = sequence.readlines()
    
    # Drop the description line
    lines.pop(0)

    # Convert the sequence data to a continuous string
    # Remove newline char
    out = ''.join([str(line[:-1]) for line in lines])

    
    return out

# ------------------------------


def transcription(sequence):
    
    '''
    Given a valid DNA antisense sequence, return the sense sequence 
    in RNA bases.
    '''
    
    # Make a dictionary of transcription values
    base_dict = {'A': 'U',
            'T': 'A',
            'C': 'G',
            'G': 'C'}
    
    # Make an ordered list of all bases in the sequence
    valid_bases = ['A', 'T', 'C', 'G']
    base_list = []
    for i in range(len(sequence)):
        if sequence[i] not in valid_bases:
            return "Not a valid DNA sequence"
        base_list.append(sequence[i])
    
    # transcribed_list
    transcribed_list = []
    for base in base_list:
        transcribed_list.append(base_dict[base])
        
    return ''.join(transcribed_list)

#-------------------------------------

def get_reading_frames(sequence):
    
    """
    Check that input is a valid RNA sequence.  Search for the start codon
    establish a reading frame.  Output a list of valid reading frames.
    
    """ 
    valid_bases = ['A', 'U', 'C', 'G']
    stop = ['UAA', 'UAG', 'UGA']  # List of possible stop codons
    frame_list = [] # List of reading frames
    for idx in range(len(sequence)):
        if sequence[idx] not in valid_bases:
            return 'Not a valid RNA sequence'
        else:
            if sequence[idx : idx + 3] == 'AUG': # Start new reading frame
                in_frame = 'AUG'
                current_frame = []
                current_frame.append(in_frame) 
                idx += 3 # Advance the index by 3 bases 
                while in_frame not in stop:
                    in_frame = sequence[idx : idx + 3]
                    print(in_frame)
                    current_frame.append(in_frame)
                    idx += 3 # Advance the index by 3 bases
                if in_frame in stop:
                    current_frame.append(in_frame)
                    idx += 3 # Advance the index by 3 bases
                frame_list.append(current_frame) # Add current frame to list of reading frames
    
    return frame_list
            
            
    