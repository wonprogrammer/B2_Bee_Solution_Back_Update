import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beesolution.settings')
django.setup()

import numpy as np
from PIL import Image
from PIL import ImageDraw, ImageFont
from article.models import Solution

def make_wise_image(idx):
    # 요청 정보 가져오기
    target = Solution.objects.get(id=idx)
    image_url = target.solution_image
    img = Image.open(f'media/{image_url}').convert('RGB')
    img = img.resize((550,400))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # 명언 정보 가져오기
    input_wise = target.wise
    wise_len = len(input_wise)
    
    # 폰트 40일때 12글자까지 / 30일때 15글자까지 / 폰트크기에 따라 줄간격 조정
    if wise_len > 40:
        fontsize = 30
        y_upper = 33
    else:
        fontsize = 40
        y_upper = 40
    
    # 개행 수에 따라 y축 정렬
    text = input_wise.split(',')
    if len(text) >= 5:
        x, y = 70, 90
    elif len(text) == 4:
        x, y = 70, 110
    elif len(text) == 3:
        x, y = 70, 130
    elif len(text) == 2:
        x, y = 70, 150
    else:
        x, y = 70, 200
    
    # 긴 문장 처리용
    for i in text:
        if len(i)>=15:
            fontsize = 27
            x = 50
            y_upper = 30
        else:
            continue
    
    font = ImageFont.truetype("fonts/NotoSerifKR-Bold.otf", fontsize)
    # 텍스트 삽입
    for i in text:
        
        # 텍스트 수에 따라 x축 중앙 정렬
        if len(i) <= 3:
            x = 230
        elif len(i) <= 4:
            x = 215
        elif len(i) <= 5:
            x = 200
        elif len(i) <= 6:
            x = 180
        elif len(i) <= 7:
            x = 160
        elif len(i) <= 8:
            x = 145
        elif len(i) <= 9:
            x = 130
        elif len(i) <= 10:
            x = 110
        elif len(i) <= 12:
            x = 90
        else:
            x = 70
            
        position = (x, y)
        bbox = draw.textbbox(position, i, font=font)
        draw.rectangle(bbox, fill=(0,0,0,150))
        draw.text(position, i, font=font, fill=(255,255,255))
        
        y+=y_upper
        
    img.save(f'./media/{image_url}', 'jpeg')