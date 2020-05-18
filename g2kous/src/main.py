import sys
from predictor import ScoringService
from PIL import Image
import argparse
import json
import glob
from timeit import default_timer as timer

if __name__ == '__main__':
  """
Predict method
 
Args:
    input (str): path to the video file you want to make inference from
 
Returns:
     dict: Inference for the given input.
     format:
            - filename []:
            - category_1 []:
            - id: int
            - box2d: [left, top, right, bottom]
              ...
     Notes:
            - The categories for testing are "Car" and "Pedestrian".
              Do not include other categories in the prediction you will make.
            - If you do not want to make any prediction in some frames,
              just write "prediction = {}" in the prediction of the frame in the sequence(in line 65 or line 67).
  """

  data_path = '../data'#読みこむデータのパスを記載

  #複数のファイルに対応済み
  videos = glob.glob(data_path+'/*.mp4')
  Output_list = ''
  
  for i in range(len(videos)):
    start_mp4 = timer()
    
    video_path = videos[i]
    ScoringService.get_model()
    Output = ScoringService.predict(video_path)
    print(Output)
    
    if i == 0:#最初はキーを指定して辞書作成
        Output_list = Output
    else:#2個目以降はキーを指定して辞書追加
        Output_list.update(Output)

    print("＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊")
    end_mp4 = timer()
    print("1mp4 file の処理時間 = ", end_mp4 - start_mp4)

  with open('../output/prediction.json', 'w') as f:
    json.dump(Output_list, f)

