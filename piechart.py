import matplotlib.pyplot as pit
import numpy as np
y=np.array([66,27,72,10])
datas=["naruto","spyxfamily","tokyorevengers","others"]
mexplode=[0.7,0,0.9,0.1]
pit.pie(y, labels=datas,explode=mexplode ,shadow=True)
pit.show()
