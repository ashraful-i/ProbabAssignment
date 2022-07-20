import pandas as pd
from PIL import Image
import numpy as np
from pprint import pprint
from os import listdir
from os.path import isfile, join

def train(df):
    # print(df)
    prob_B = pd.DataFrame()
    prob_G = pd.DataFrame(columns=["p_g"])
    prob_R = pd.DataFrame(columns=["p_r"])
    total_p = pd.DataFrame(columns=["p_r"])
    count_row = df.shape[0]
    total_prob = count_row/16386810


    df_B_Skin = pd.crosstab(df.B, df.Skin, normalize='columns')
    df_Skin_B = pd.crosstab(df.Skin, df.B, normalize='columns')
    df_G_Skin = pd.crosstab(df.G, df.Skin, normalize='columns')
    df_Skin_G = pd.crosstab(df.Skin, df.G, normalize='columns')
    df_R_Skin = pd.crosstab(df.R, df.Skin, normalize='columns')
    df_Skin_R = pd.crosstab(df.Skin, df.R, normalize='columns')
    print(df_Skin_B)
    print(df_B_Skin[1][100])
    total_p_b = df_B_Skin/total_prob
    print(total_p_b)
    im = Image.open('man3.jpg')  # Can be many different formats.
    pix = im.load()
    print(im.size)  # Get the width and hight of the image for iterating over
    im_w = im.size[0]
    im_h = im.size[1]
    for x in range(im_w):
        for y in range(im_h):
            R = pix[x, y][0]
            G = pix[x, y][1]
            B = pix[x, y][2]

            sum_of_2 = df_B_Skin[1][B] + df_G_Skin[1][G] + df_R_Skin[1][R]
            if sum_of_2 > 0.015:
                pix[x, y] = (0, 0, 0)

    im.save('mask2.png')  # Save the modified pixels as .png

if __name__ == "__main__":
    #dataset = pd.read_csv('Skin_NonSkin.txt', sep='\t', names=['B', 'G', 'R', 'Skin', ])
    #df = pd.DataFrame(dataset)
    #train(df)


    mypath= "D:\ibtd\ibtd\Mask"
    #path1 = "\ibtd"
    maskImages = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #df_im = pd.DataFrame()
    cols = ['B', 'G', 'R', 'Skin']
    init_val = []



    '''for x in range(255):
        for y in range(255):
            for z in range(255):
                init_val.append([x,y,z,2])'''
    df1 = pd.DataFrame(init_val, columns=cols)
    cols = ['B', 'G', 'R', 'Skin']
    lst = []
    
    
    for maskimg in maskImages:
        #print(maskimg)
        im = Image.open(mypath + "\\" + maskimg)
        pix = im.load()
        #print(im.size)  # Get the width and hight of the image for iterating over
        im_w = im.size[0]
        im_h = im.size[1]
        #print(im_h, im_w)
        for x in range(im_w):
            for y in range(im_h):
                B = pix[x, y][0]
                G = pix[x, y][1]
                R = pix[x, y][2]
                #df1.loc[df1['B'] == B, df1['G'] == G, df1['R'] == R, 'Skin'] = 1
                #df1.at[B, G, R, 'Skin'] = 1

                if(R > 250 and G>230 or B > 200):
                    continue
                #print(R, G, B)
                else:
                    lst.append([R, G, B, 1])

    df1 = pd.DataFrame(lst, columns=cols)
    print(df1)
    train(df1)



