import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import numpy as np



def main():
    data = pd.read_excel(
        "./API_NY.GDP.MKTP.CD_DS2_zh_excel_v2_10577368.xls", 
        sheet_name="Data", 
        skiprows=3, 
        index_col="Country Name"
        )
    data = data.loc[["中国", "美国", "日本"], "1960":"2017"]
    Tdata = data.T.rename(columns={
    "中国": "China", 
    "日本": "Japan", 
    "美国": "America"}
    )
    # plt.style.use("bmh")
    Tdata.plot( 
        linewidth=2, 
        figsize=(10, 8), 
        title="GDP in the top three countries of GDP in recent years from 1960 to 2017"
        )
    ax = plt.gca()
    ax.set_ylabel("GDP/$")
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    plt.tick_params(bottom='off',left='off')
    ax.set_ylim((0, 2*10**13))
    plt.savefig("./picture4.png")
    plt.show()


if __name__ == "__main__":
    main()