import pandas as pd
import matplotlib
# pip install matplotlib pip install matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

air_quality = pd.read_csv("air-quality.csv", index_col=0, parse_dates=True)

air_quality.plot()

plt.show()


