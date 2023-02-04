import re
import json
import pandas as pd
#from multiprocessing import process
#import os
#from tqdm import tqdm
#from joblib import delayed, Parallel



# function to delete the roman numbers

def romans_preprocess(text): 
    """with space & dot"""
    #text = re.sub('\sI\.','',text)
    text = re.sub('\sII\.','',text)
    text = re.sub('\sIII\.','',text)
    text = re.sub('\sIV\.','',text)
    #text = re.sub('\sV\.','',text)
    text = re.sub('\sVI\.','',text)
    text = re.sub('\sVII\.','',text)
    text = re.sub('\sVIII\.','',text)
    text = re.sub('\sIX\.','',text)
    #text = re.sub('\sX\.','',text)
    
    text = re.sub('\sXI\.','',text)
    text = re.sub('\sXII\.','',text)
    text = re.sub('\sXIII\.','',text)
    text = re.sub('\sXIV\.','',text)
    text = re.sub('\sXV\.','',text)
    text = re.sub('\sXVI\.','',text)
    text = re.sub('\sXVII\.','',text)
    text = re.sub('\sXVIII\.','',text)
    text = re.sub('\sXIX\.','',text)
    text = re.sub('\sXX\.','',text)
    
    text = re.sub('\sXXI\.','',text)
    text = re.sub('\sXXII\.','',text)
    text = re.sub('\sXXIII\.','',text)
    text = re.sub('\sXXIV\.','',text)
    text = re.sub('\sXXV\.','',text)
    text = re.sub('\sXXVI\.','',text)
    text = re.sub('\sXXVII\.','',text)
    text = re.sub('\sXXVIII\.','',text)
    text = re.sub('\sXXIX\.','',text)
    text = re.sub('\sXXX\.','',text)
    
    text = re.sub('\sXXXI\.','',text)
    text = re.sub('\sXXXII\.','',text)
    text = re.sub('\sXXXIII\.','',text)
    text = re.sub('\sXXXIV\.','',text)
    text = re.sub('\sXXXV\.','',text)
    text = re.sub('\sXXXVI\.','',text)
    text = re.sub('\sXXXVII\.','',text)
    text = re.sub('\sXXXVIII\.','',text)
    text = re.sub('\sXXXIX\.','',text)
    text = re.sub('\sXL\.','',text)
    
    text = re.sub('\sXLI\.','',text)
    text = re.sub('\sXLII\.','',text)
    text = re.sub('\sXLIII\.','',text)
    text = re.sub('\sXLIV\.','',text)
    text = re.sub('\sXLV\.','',text)
    text = re.sub('\sXLVI\.','',text)
    text = re.sub('\sXLVII\.','',text)
    text = re.sub('\sXLVIII\.','',text)
    text = re.sub('\sXLIX\.','',text)
    #text = re.sub('\sL\.','',text)
    
    text = re.sub('\sLI\.','',text)
    text = re.sub('\sLII\.','',text)
    text = re.sub('\sLIII\.','',text)
    text = re.sub('\sLIV\.','',text)
    text = re.sub('\sLV\.','',text)
    text = re.sub('\sLVI\.','',text)
    text = re.sub('\sLVII\.','',text)
    text = re.sub('\sLVIII\.','',text)
    text = re.sub('\sLIX\.','',text)
    text = re.sub('\sLX\.','',text)

    
    text = re.sub('\sLXI\.','',text)
    text = re.sub('\sLXII\.','',text)
    text = re.sub('\sLXIII\.','',text)
    text = re.sub('\sLXIV\.','',text)
    text = re.sub('\sLXV\.','',text)
    text = re.sub('\sLXVI\.','',text)
    text = re.sub('\sLXVII\.','',text)
    text = re.sub('\sLXVIII\.','',text)
    text = re.sub('\sLXIX\.','',text)
    text = re.sub('\sLXXX\.','',text)
    
    text = re.sub('\sLXXI\.','',text)
    text = re.sub('\sLXXII\.','',text)
    text = re.sub('\sLXXIII\.','',text)
    text = re.sub('\sLXXIV\.','',text)
    text = re.sub('\sLXXV\.','',text)
    text = re.sub('\sLXXVI\.','',text)
    text = re.sub('\sLXXVII\.','',text)
    text = re.sub('\sLXXVIII\.','',text)
    text = re.sub('\sLXXIX\.','',text)
    text = re.sub('\sLXXX\.','',text)
    
    text = re.sub('\sLXXXI\.','',text)
    text = re.sub('\sLXXXII\.','',text)
    text = re.sub('\sLXXXIII\.','',text)
    text = re.sub('\sLXXXIV\.','',text)
    text = re.sub('\sLXXXV\.','',text)
    text = re.sub('\sLXXXVI\.','',text)
    text = re.sub('\sLXXXVII\.','',text)
    text = re.sub('\sLXXXVIII\.','',text)
    text = re.sub('\sLXXXIX\.','',text)
    text = re.sub('\sXC\.','',text)
    
    text = re.sub('\sXCI\.','',text)
    text = re.sub('\sXCII\.','',text)
    text = re.sub('\sXCIII\.','',text)
    text = re.sub('\sXCIV\.','',text)
    text = re.sub('\sXCV\.','',text)
    text = re.sub('\sXCVI\.','',text)
    text = re.sub('\sXCVII\.','',text)
    text = re.sub('\sXCVIII\.','',text)
    text = re.sub('\sXCIX\.','',text)
    #text = re.sub('\sC\.','',text)

    return text



"""
you can customize the pattern you want to remove.

i.e.) without space on the front of the pattern

def romans_preprocess(text): 
    
    #text = re.sub('I\.','',text)
    text = re.sub('II\.','',text)
    text = re.sub('III\.','',text)
    text = re.sub('IV\.','',text)
    #text = re.sub('V\.','',text)
    text = re.sub('VI\.','',text)
    text = re.sub('VII\.','',text)
    text = re.sub('VIII\.','',text)
    text = re.sub('IX\.','',text)
    #text = re.sub('X\.','',text)
    
    text = re.sub('XI\.','',text)
    text = re.sub('XII\.','',text)
    text = re.sub('XIII\.','',text)
    text = re.sub('XIV\.','',text)
    text = re.sub('XV\.','',text)
    text = re.sub('XVI\.','',text)
    text = re.sub('XVII\.','',text)
    text = re.sub('XVIII\.','',text)
    text = re.sub('XIX\.','',text)
    text = re.sub('XX\.','',text)
    
    text = re.sub('XXI\.','',text)
    text = re.sub('XXII\.','',text)
    text = re.sub('XXIII\.','',text)
    text = re.sub('XXIV\.','',text)
    text = re.sub('XXV\.','',text)
    text = re.sub('XXVI\.','',text)
    text = re.sub('XXVII\.','',text)
    text = re.sub('XXVIII\.','',text)
    text = re.sub('XXIX\.','',text)
    text = re.sub('XXX\.','',text)
    
    text = re.sub('XXXI\.','',text)
    text = re.sub('XXXII\.','',text)
    text = re.sub('XXXIII\.','',text)
    text = re.sub('XXXIV\.','',text)
    text = re.sub('XXXV\.','',text)
    text = re.sub('XXXVI\.','',text)
    text = re.sub('XXXVII\.','',text)
    text = re.sub('XXXVIII\.','',text)
    text = re.sub('XXXIX\.','',text)
    text = re.sub('XL\.','',text)
    
    text = re.sub('XLI\.','',text)
    text = re.sub('XLII\.','',text)
    text = re.sub('XLIII\.','',text)
    text = re.sub('XLIV\.','',text)
    text = re.sub('XLV\.','',text)
    text = re.sub('XLVI\.','',text)
    text = re.sub('XLVII\.','',text)
    text = re.sub('XLVIII\.','',text)
    text = re.sub('XLIX\.','',text)
    #text = re.sub('L\.','',text)
    
    text = re.sub('LI\.','',text)
    text = re.sub('LII\.','',text)
    text = re.sub('LIII\.','',text)
    text = re.sub('LIV\.','',text)
    text = re.sub('LV\.','',text)
    text = re.sub('LVI\.','',text)
    text = re.sub('LVII\.','',text)
    text = re.sub('LVIII\.','',text)
    text = re.sub('LIX\.','',text)
    text = re.sub('LX\.','',text)

    
    text = re.sub('LXI\.','',text)
    text = re.sub('LXII\.','',text)
    text = re.sub('LXIII\.','',text)
    text = re.sub('LXIV\.','',text)
    text = re.sub('LXV\.','',text)
    text = re.sub('LXVI\.','',text)
    text = re.sub('LXVII\.','',text)
    text = re.sub('LXVIII\.','',text)
    text = re.sub('LXIX\.','',text)
    text = re.sub('LXXX\.','',text)
    
    text = re.sub('LXXI\.','',text)
    text = re.sub('LXXII\.','',text)
    text = re.sub('LXXIII\.','',text)
    text = re.sub('LXXIV\.','',text)
    text = re.sub('LXXV\.','',text)
    text = re.sub('LXXVI\.','',text)
    text = re.sub('LXXVII\.','',text)
    text = re.sub('LXXVIII\.','',text)
    text = re.sub('LXXIX\.','',text)
    text = re.sub('LXXX\.','',text)
    
    text = re.sub('LXXXI\.','',text)
    text = re.sub('LXXXII\.','',text)
    text = re.sub('LXXXIII\.','',text)
    text = re.sub('LXXXIV\.','',text)
    text = re.sub('LXXXV\.','',text)
    text = re.sub('LXXXVI\.','',text)
    text = re.sub('LXXXVII\.','',text)
    text = re.sub('LXXXVIII\.','',text)
    text = re.sub('LXXXIX\.','',text)
    text = re.sub('XC\.','',text)
    
    text = re.sub('XCI\.','',text)
    text = re.sub('XCII\.','',text)
    text = re.sub('XCIII\.','',text)
    text = re.sub('XCIV\.','',text)
    text = re.sub('XCV\.','',text)
    text = re.sub('XCVI\.','',text)
    text = re.sub('XCVII\.','',text)
    text = re.sub('XCVIII\.','',text)
    text = re.sub('XCIX\.','',text)
    #text = re.sub('C\.','',text)

    return text


"""

# open file as dataframe
df = pd.read_csv('{your directory}', encoding='utf-8', sep='\n', header=None)

# check
df.head()
df.shape
df.columns

# divied the df line by line
dfff = df[0]
dfff.head()
type(dfff)


# preprocess the dataframe
for i in range({total length}):
    dfff[i] = romans_preprocess(dfff[i])

# save the dataframe
dfff.to_csv('{your directory}', sep='\n', index=False, header=False)

