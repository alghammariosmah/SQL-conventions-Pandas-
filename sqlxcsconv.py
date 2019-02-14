# -*- coding: utf-8 -*-

import os, unicodedata, datetime
import pandas as pd
import numpy as np

characterList = [u'€',u'%','\n','.',' ','-','/','#']
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    if isinstance(mainString, int):
        return mainString
    elif isinstance(mainString, float):
        return mainString
    elif isinstance(mainString, datetime.datetime):
        return mainString
    if isinstance(mainString, unicode) or isinstance(mainString,str):
        for elem in toBeReplaces:
            # Check if string is in the main string
            mainString = u''.join(mainString)
            mainString = mainString.lower()
            """ Normalize unicode data in Python to remove umlauts, accents etc. """
            mainString = unicodedata.normalize('NFKD', mainString).encode('ASCII', 'ignore')
            mainString = " ".join(mainString.split())
            if elem in mainString:
                # Replace the string
                if elem == u'€':
                    mainString = mainString.replace(u'€', "Euro")
                elif elem == u'%':
                    mainString = mainString.replace(u'%', "percent")
                elif elem == ' ':
                    mainString = mainString.replace(' ', '_')
                elif elem == '-':
                    mainString = mainString.replace('-', '_')
                else:
                    mainString = mainString.replace(elem, newString)
    return  mainString


def tablesConcat(sourceFile, filesEndWith, outputFileName, destDir):
    sourceFile = '{}/'.format(sourceFile)
    files = [filename for filename in os.listdir(str(sourceFile)) if filename.endswith(str(filesEndWith))]

    list_ = []
    for file_ in files:
        df = pd.read_excel(file_, index_col=None)
        df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
        # df.dropna(axis=1, how='all', inplace=True)
        nanIndex = np.where(df.ix[:,0].isna()) # Index all Nan rows
        df.drop(df.index[nanIndex[0]], inplace=True)
        df = df.reset_index(drop=True)
        df.columns = [replaceMultiple(x.lower(),characterList, " ") for x in df.columns]
        for i in range(len(df.values)):
            df.at[i] = [replaceMultiple(x, characterList, " ") for x in df.values[i]]
        df = df.set_index(df.columns[0])
        list_.append(df)
    frame = pd.concat(list_, axis=0)
    outputFileName = '{}/{}'.format(destDir,outputFileName)
    frame.to_excel(str(outputFileName), engine='xlsxwriter')
    return frame




if __name__ == '__main__':
    tablesConcat("sourceFile", ".xlsx", "output.xlsx"/
                 ,"destDir")