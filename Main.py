from BruteForceMouseInput import BruteForceNumpadMouseInput
from sys import argv


print("BruteForceNumpadMouseInput INIT")
BruteForceProcess = BruteForceNumpadMouseInput(int(argv[1]), int(argv[2]))
print("BruteForceNumpadMouseInput RUN")
BruteForceProcess.run()
