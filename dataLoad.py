import numpy as np
import pandas as pd

def loadData(fileName):     #  读取数据
    dataMat=[]
    df=open(fileName)
    for line in df.readlines():
        lineArr=line.strip().split(',')
        dataMat.append(lineArr)
    col=dataMat[0]
    dataMat=dataMat[1:]
    return col,dataMat

col,dataMat=loadData('ETCHER_DATA.txt')

data=pd.DataFrame(data=dataMat,columns=col,dtype='float')


