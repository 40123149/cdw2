# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
a40123255_task1 = Blueprint('a40123255_task1', __name__, url_prefix='/ag7', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@a40123255_task1.route('/a40123255_task1')
def task1():
    outstring = '''

from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    #A
    basic1 = cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(90)
    basic1.translate(0, -20)
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0, -20)
    
    basic3 = cmbr.dup()
    basic3.rotate(90)
    basic3.translate(20, -20)
    
    basic4 = cmbr.dup()
    basic4.rotate(0)
    basic4.translate(40, -20)
    
    basic5 = cmbr.dup()
    basic5.rotate(0)
    basic5.translate(40, 0)

    basic6 = cmbr.dup()
    basic6.rotate(90)
    basic6.translate(10, 40)

    basic7 = cmbr.dup()
    basic7.rotate(167)
    basic7.translate(0, 0)  
   
    basic8 = cmbr.dup()
    basic8.rotate(-14)
    basic8.translate(10, 40)  

    basic9 = cmbr.dup()
    basic9.rotate(-167)
    basic9.translate(40, 0)  
   
    basic10 = cmbr.dup()
    basic10.rotate(14)
    basic10.translate(30, 40)

#B
    basic11 = cmbr.dup()
    # basic1 轉 120 度
    basic11.rotate(180)
    basic11.translate(60, 0)
    basic12 = cmbr.dup()
    basic12.rotate(0)
    basic12.translate(60, -20)
    
    basic13 = cmbr.dup()
    basic13.rotate(0)
    basic13.translate(60, 40)
    
    basic14 = cmbr.dup()
    basic14.rotate(90)
    basic14.translate(60, 40)
    
    basic15 = cmbr.dup()
    basic15.rotate(90)
    basic15.translate(60, 0)

    basic16 = cmbr.dup()
    basic16.rotate(90)
    basic16.translate(60, -40)
    
    basic17 = cmbr.dup()
    basic17.rotate(60)
    basic17.translate(80, 0)
    
    basic18 = cmbr.dup()
    basic18.rotate(120)
    basic18.translate(80, 0)
    
    basic19 = cmbr.dup()
    basic19.rotate(60)
    basic19.translate(80, 40)
    
    basic110 = cmbr.dup()
    basic110.rotate(120)
    basic110.translate(80, -40)
    
    basic111 = cmbr.dup()
    basic111.rotate(0)
    basic111.translate(97.5, 30)
    
    basic112 = cmbr.dup()
    basic112.rotate(180)
    basic112.translate(97.5, -30)
    basic113 = cmbr.dup()
    basic113.rotate(0)
    basic113.translate(60, 0)
#C
    basic21 = cmbr.dup()
    basic21.rotate(165)
    basic21.translate(120, 10)
    basic22 = cmbr.dup()
    basic22.rotate(15)
    basic22.translate(120, -10)
    
    basic23 = cmbr.dup()
    basic23.rotate(135)
    basic23.translate(125.5, 30)
    
    basic24 = cmbr.dup()
    basic24.rotate(90)
    basic24.translate(140, 44)
    
    basic25 = cmbr.dup()
    basic25.rotate(90)
    basic25.translate(140, -44)

    basic26 = cmbr.dup()
    basic26.rotate(45)
    basic26.translate(125.5, -30)
    basic27 = cmbr.dup()
    basic27.rotate(0)
    basic27.translate(120, 10)
    
#A
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
#B
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic110)
    cmbr.appendPath(basic111)
    cmbr.appendPath(basic112)
    cmbr.appendPath(basic113)
#C
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)    
    cmbr.appendPath(basic27)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 0.5, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 0.5, rot)

O(0, 0, 0, 0, 0, "lightyellow", True, 4)

'''
    return outstring
    

    
    
