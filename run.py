import sys
import matrix

if __name__ == "__main__":

    exec(open("dataPreProcessing.py").read())

    kmin = int(sys.argv[1])
    kmax = int(sys.argv[2])
    
    for k in range(kmin, kmax+1):
        
        print("Run for k = " + str(k))
        matrix.create_matrix(k)