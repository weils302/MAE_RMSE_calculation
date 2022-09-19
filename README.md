# MAE、RMSEの計算
 
*研究データ処理用*  

観測データと深層学習のトレーニング結果からMAE(mean absolute error)とRMSE(root mean squared error)を計算するプログラムです。

一回のトレーニングに対して500個の結果があり、トレーニング毎にフォルダーに保存されている。このプログラムが500個の結果からランダムで30個を抽出し、それらの平均値のMAEとRMSEを計算する。こんな作業が40回繰り返して結果をCSVファイルで記録する。

line 8 ```rootDir``` でトレーニング結果のroot directoryを入力。