N = 1000

import sys

# Main
def main():
    for a in range(500):
        for b in range(500):
            c = N - (a + b)
            if a ** 2 + b ** 2 == c ** 2:
                # 31875000
                print a * b * c               
                sys.exit() 
        
if __name__ == "__main__":
    main()
