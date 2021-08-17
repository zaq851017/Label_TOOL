# Label_TOOL
# Usage
下方簡單解釋這些程式碼如何輔助你讓標記資料更加容易

### 程式碼解釋
    
    python3 code/label.py --input_path INPUT_FOLDER --output_path OUTPUT_FOLDER
label.py幫助你從原本是使用手寫板(或者其他圈選工具)所圈出的分割區域, 可以把分割區域轉為黑白的遮罩。
那這邊為了方便，我們希望所圈選分割區域為黃色或者綠色的邊界，如下圖所示:
![image](https://github.com/zaq851017/Label_TOOL/blob/main/label_example.png)

    python3 code/visualize.py --input_path INPUT_FOLDER 
visualize.py幫助你讓黑白遮罩可以更加視覺化，如下圖所示:
![image](https://github.com/zaq851017/Label_TOOL/blob/main/visualize_example.png)


