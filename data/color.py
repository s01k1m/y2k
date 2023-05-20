# pip install colorthief

from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

'''
[1] (r, g, b)값 뽑아서 딕셔너리로 저장
최댓값, 중간값, 최솟값을 키로 찾을 수 있도록
'''
ct = ColorThief("beige.jpg")
r, g, b = ct.get_color(quality=1)
rgb = {'r': r, 'g': g, 'b': b}
still_color = 'WHITE'
print(rgb)
plt.imshow([[(r, g, b)]])
plt.show()

'''
[2] 최댓값, 중간값, 최솟값 찾기
rgb 딕셔너리의 키로 활용할 수 있도록 문자로 저장
'''
max, mid, min = '', '', ''
if r >= g and r >= b:                       # r값이 제일 클 경우
    if g >= b:
        max, mid, min = 'r', 'g', 'b'
    else:
        max, mid, min = 'r', 'b', 'g'
elif g >= r and g >= b:                     # g값이 가장 클 경우
    if r >= b:
        max, mid, min = 'g', 'r', 'b'
    else:
        max, mid, min = 'g', 'b', 'r'
else:                                       # b값이 가장 클 경우
    if r >= g:
        max, mid, min = 'b', 'r', 'g'
    else:
        max, mid, min = 'b', 'g', 'r'

'''
[3] 흰색, 회색, 검정색 or OTHERS
'''
if rgb[min] >= 200 and rgb[max] - rgb[min] <= 16:
    '''[4] 흰색
    모든 값이 200 이상이고, 값 차이가 16 이내이면 하양
    '''
    still_color = 'WHITE'

elif rgb[max] - rgb[min] <= 10:
    '''
    [5] 흰색, 회색, 검정색
    색상끼리의 차이가 10이내이면 모노톤
    '''
    if rgb[min] >= 200:                     # 최솟값이 200 이상일 경우 <<하양>>
        still_color = 'WHITE'
    elif rgb[max] <= 64:                    # 최댓값이 64 이하일 경우 <<검정>>
        still_color = 'BLACK'
    else:                                   # 그 외는 모두 <<회색>>
        still_color = 'GREY'

else:
    if max == 'r':
        '''
        [6] 빨간 계열
        빨강, 주황, 노랑, 분홍, 보라
        '''
        if mid == 'g':                      # 빨강, 주황, 노랑
            if rgb[mid] <= 64:              # <<빨강>>
                still_color = 'RED'
            elif rgb[mid] <= 191:           # <<주황>>
                still_color = 'ORANGE'
            else:                           # <<노랑>>
                still_color = 'YELLOW'
        else:                               # 빨강, 분홍, 보라
            if rgb[mid] <= 32:              # <<빨강>>
                still_color = 'RED'
            elif rgb[max] <= 128:           # <<보라>>
                still_color = 'PURPLE'
            else:                           # <<분홍>>
                still_color = 'PINK'

    elif max == 'g':
        '''
        [7] 초록 계열
        초록
        '''
        still_color = 'GREEN'

    else: 
        '''
        [8] 파랑 계열
        파랑, 분홍, 보라
        '''
        if mid == 'r':                      # 파랑, 분홍, 보라
            if rgb[mid] >= 191:             # <<분홍>>
                still_color = 'PINK'
            if rgb[max] - rgb[mid] <= 128:  # <<보라>>
                still_color = 'PURPLE'
            else:                           # <<파랑>>
                still_color = 'BLUE'
        else:                               # <<파랑>>
            still_color = 'BLUE'


print(still_color)
# dominant_color = img.imread(request.FILES['still_image'])
# print(dominant_color.shape)
