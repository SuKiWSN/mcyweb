import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('../static/video.csv', header=0, index_col=0, sep=',')
    videoUrl = df.loc[:, 'videoUrl']
    print(videoUrl)
    videoUrl.to_csv('./videoUrl.txt', index=False)