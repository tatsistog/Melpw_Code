import numpy as np
import pandas as pd
import os
import dataPreProcessing
import sys


def findInput():

    files = [f for f in os.listdir('files/') if f.endswith('.fasta')]
    file = files[0]
    filename = file[0:-6]
    filename_txt = filename + '.txt'
    if not os.path.exists('files/'+filename_txt):
        data = dataPreProcessing.read_fasta_file('files/' + file)
        dataPreProcessing.save_results_to_file(data, filename_txt, 'files')
        del data

    path = 'files/' + filename_txt
    return path


def create_matrix(best_k):

    filehandle = open(findInput(),"r")
    # Start with an empty dictionary
    counts = {}
    seq=0

    for row in filehandle:
        seq=seq+1
        seq_id="seq_{}".format(seq)
        counts[seq_id]={}
        counts =count_kmers(seq_id,row,best_k,counts)
        
    
    matrix_data = pd.DataFrame(counts)
    filehandle.close
    
    # Create info file
    info = open("results/matrix-{}.txt".format(best_k),'a') 
    info.write(matrix_data.to_string(na_rep='0'))
    info.close()
    
    return



def count_kmers(id,read,k,counts):
    """Count kmer occurrences in a given sequence.

        Parameters
        ----------
        id: number of sequence.
        read : string
            A single DNA sequence.
        k : int
            The value of k for which to count kmers.
        counts : dictionary, {'string': int}
            A dictionary of counts keyed by their individual kmers (strings
            of length k).
        Returns
        -------
        counts : dictionary, {'string': int}
            A dictionary of counts keyed by their individual kmers (strings
            of length k).

        Examples
        --------
        >>> count_kmers("GATGAT", 3)
        {'ATG': 1, 'GAT': 2, 'TGA': 1}
    """

    # Calculate how many kmers of length k there are	
    read = read[0:-1]
    num_kmers = len(read) - k + 1
    # Loop over the kmer start positions
    for i in range(num_kmers):
        # Slice the string to get the kmer
        kmer = read[i:i+k]
        # Add the kmer to the dictionary if it's not there
        if kmer not in counts[id]:
            counts[id][kmer] = int(0)
            
        # Increment the count for this kmer
        counts[id][kmer] =int(counts[id][kmer])+ int(1)
        
    return counts


if __name__ == "__main__":

    k = int(sys.argv[1])
    create_matrix(k)