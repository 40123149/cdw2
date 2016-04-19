# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
a40123119_task1 = Blueprint('a40123119_task1', __name__, url_prefix='/ag7', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@a40123119_task1.route('/a40123119_task1')
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
   #D
    basic31 = cmbr.dup()
    basic31.rotate(180)
    basic31.translate(180, 0)
    basic32 = cmbr.dup()
    basic32.rotate(0)
    basic32.translate(180, -20)
    
    basic33 = cmbr.dup()
    basic33.rotate(0)
    basic33.translate(180, 40)
    
    basic34 = cmbr.dup()
    basic34.rotate(90)
    basic34.translate(180, 40)

    basic36 = cmbr.dup()
    basic36.rotate(90)
    basic36.translate(180, -40)
    
    basic37 = cmbr.dup()
    basic37.rotate(0)
    basic37.translate(222.8, 10)
    
    basic39 = cmbr.dup()
    basic39.rotate(60)
    basic39.translate(200, 40)
    
    basic310 = cmbr.dup()
    basic310.rotate(120)
    basic310.translate(200, -40)
    
    basic311 = cmbr.dup()
    basic311.rotate(15)
    basic311.translate(217.5, 30)
    
    basic312 = cmbr.dup()
    basic312.rotate(165)
    basic312.translate(217.5, -30)
    
    basic313 = cmbr.dup()
    basic313.rotate(0)
    basic313.translate(180, 0)
#E
    basic41 = cmbr.dup()
    basic41.rotate(0)
    basic41.translate(0, -110)
    basic42 = cmbr.dup()
    basic42.rotate(0)
    basic42.translate(0, -130)
    
    basic43 = cmbr.dup()
    basic43.rotate(0)
    basic43.translate(0, -70)
    
    basic44 = cmbr.dup()
    basic44.rotate(90)
    basic44.translate(0, -70)
    
    basic45 = cmbr.dup()
    basic45.rotate(90)
    basic45.translate(0, -110)

    basic46 = cmbr.dup()
    basic46.rotate(90)
    basic46.translate(0, -150)
    
    basic49 = cmbr.dup()
    basic49.rotate(90)
    basic49.translate(20, -70)
    
    basic410 = cmbr.dup()
    basic410.rotate(90)
    basic410.translate(20, -150)
    basic411 = cmbr.dup()
    basic411.rotate(0)
    basic411.translate(0, -90)
#F
    basic51 = cmbr.dup()
    basic51.rotate(180)
    basic51.translate(60, -110)
    basic52 = cmbr.dup()
    basic52.rotate(0)
    basic52.translate(60, -130)
    
    basic53 = cmbr.dup()
    basic53.rotate(0)
    basic53.translate(60, -70)
    
    basic54 = cmbr.dup()
    basic54.rotate(90)
    basic54.translate(60, -70)
    
    basic55 = cmbr.dup()
    basic55.rotate(90)
    basic55.translate(60, -110)
    basic59 = cmbr.dup()
    basic59.rotate(90)
    basic59.translate(80, -70)
    basic510 = cmbr.dup()
    basic510.rotate(0)
    basic510.translate(60, -110)
#G
    basic61 = cmbr.dup()
    basic61.rotate(165)
    basic61.translate(120,-100)
    basic62 = cmbr.dup()
    basic62.rotate(15)
    basic62.translate(120, -120)
    
    basic63 = cmbr.dup()
    basic63.rotate(120)
    basic63.translate(125.5, -80)
    
    basic64 = cmbr.dup()
    basic64.rotate(90)
    basic64.translate(143, -70)
    
    basic65 = cmbr.dup()
    basic65.rotate(90)
    basic65.translate(143, -150)

    basic66 = cmbr.dup()
    basic66.rotate(60)
    basic66.translate(125.5, -140)
    
    basic67 = cmbr.dup()
    basic67.rotate(0)
    basic67.translate(163, -130)

    basic68 = cmbr.dup()
    basic68.rotate(0)
    basic68.translate(163, -110)

    basic69 = cmbr.dup()
    basic69.rotate(90)
    basic69.translate(143, -110)
    basic610 = cmbr.dup()
    basic610.rotate(0)
    basic610.translate(120, -100)
    
#D
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic310)
    cmbr.appendPath(basic311)
    cmbr.appendPath(basic312)
    cmbr.appendPath(basic313)
#E
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)
    cmbr.appendPath(basic43)
    cmbr.appendPath(basic44)
    cmbr.appendPath(basic45)
    cmbr.appendPath(basic46)
    cmbr.appendPath(basic49)
    cmbr.appendPath(basic410)
    cmbr.appendPath(basic411)
#F
    cmbr.appendPath(basic51)
    cmbr.appendPath(basic52)
    cmbr.appendPath(basic53)
    cmbr.appendPath(basic54)
    cmbr.appendPath(basic55)
    cmbr.appendPath(basic59)
    cmbr.appendPath(basic510)
#G
    cmbr.appendPath(basic61)
    cmbr.appendPath(basic62)
    cmbr.appendPath(basic63)
    cmbr.appendPath(basic64)
    cmbr.appendPath(basic65)
    cmbr.appendPath(basic66)
    cmbr.appendPath(basic67)
    cmbr.appendPath(basic68)
    cmbr.appendPath(basic69)
    cmbr.appendPath(basic610)
    
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
    

    
    
