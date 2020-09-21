import os

def read_fasta_file(fn):
    
    data = []

    with open(fn, 'r') as fh:
        
        lines = []
        
        for line in fh:
            if line[0] != '>':
                lines.append(line.rstrip())

            else:
                data.append(''.join(lines))
                lines = []

    
        data.append(''.join(lines))
    
    del data[0]
            
    return data


def save_results_to_file(data, name, outputFolder):
    
    currPath = os.getcwd()
    os.chdir(outputFolder)
    
    if os.path.exists(name):
        os.remove(name)
    
    with open(name, 'w') as f:
        for item in data:
            f.write("%s\n" % item)
    

    os.chdir(currPath)
    
    return


if __name__ == "__main__":

    files = [f for f in os.listdir('files/') if f.endswith('.fasta')]
    file = files[0]
    filename = file[0:-6]
    filename_txt = filename + '.txt'
    if not os.path.exists('files/'+filename_txt):
        data = read_fasta_file('files/' + file)
        save_results_to_file(data, filename_txt, 'files')