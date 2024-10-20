import pandas as pd

def pdn():
    #Crear una Serie
    s=pd.Series([1,2,3,5,7,9], index=["a","b","c","d","e","f"])
    print(s)

    #Crear un dataframe
    data={'Nombre':['Juan','Pau','Geraldene'],'Edad':[20,25,21],'Ciudad':['Madrid','Mexico','Guadalajara']}
    df=pd.DataFrame(data)
    print(df[["Nombre","Edad"]])


if __name__ == '__main__':
    pdn()



