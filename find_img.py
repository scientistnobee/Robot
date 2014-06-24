
import os
import glob
newest = max(glob.iglob('*.[j][p][g]'), key=os.path.getctime)
print(newest)
