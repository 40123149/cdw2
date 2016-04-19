# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
a40123141_task1 = Blueprint('a40123141_task1', __name__, url_prefix='/ag7', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@a40123141_task1.route('/a40123141_task1')
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
#H   
    basic71 = cmbr.dup()
    basic71.rotate(180)
    basic71.translate(180, -110)
    basic72 = cmbr.dup()
    basic72.rotate(0)
    basic72.translate(180, -130)
    
    basic73 = cmbr.dup()
    basic73.rotate(0)
    basic73.translate(180, -70)
    
    basic74 = cmbr.dup()
    basic74.rotate(180)
    basic74.translate(220,-110)
    
    basic75 = cmbr.dup()
    basic75.rotate(90)
    basic75.translate(180, -110)

    basic76 = cmbr.dup()
    basic76.rotate(0)
    basic76.translate(220, -110)
    
    basic77 = cmbr.dup()
    basic77.rotate(90)
    basic77.translate(200, -110)
    
    basic79 = cmbr.dup()
    basic79.rotate(180)
    basic79.translate(220, -90)
    
    basic710 = cmbr.dup()
    basic710.rotate(0)
    basic710.translate(220, -130)
    basic711 = cmbr.dup()
    basic711.rotate(0)
    basic711.translate(180, -110)
#I
    basic81 = cmbr.dup()
    basic81.rotate(180)
    basic81.translate(0, 100)
    basic82 = cmbr.dup()
    basic82.rotate(0)
    basic82.translate(0, 80)
    
    basic83 = cmbr.dup()
    basic83.rotate(0)
    basic83.translate(0, 140)
    
    basic84 = cmbr.dup()
    basic84.rotate(0)
    basic84.translate(0, 100)
#J 
    basic91 = cmbr.dup()
    basic91.rotate(180)
    basic91.translate(60, 100)
    basic92 = cmbr.dup()
    basic92.rotate(180)
    basic92.translate(60, 80)
    
    basic93 = cmbr.dup()
    basic93.rotate(0)
    basic93.translate(60, 140)
    
    basic94 = cmbr.dup()
    basic94.rotate(-90)
    basic94.translate(50, 62.5)
    
    basic95 = cmbr.dup()
    basic95.rotate(-30)
    basic95.translate(60, 80)
    
    basic99 = cmbr.dup()
    basic99.rotate(30)
    basic99.translate(20, 80)
    basic910 = cmbr.dup()
    basic910.rotate(30)
    basic910.translate(20, 80)

#H   
    cmbr.appendPath(basic71)
    cmbr.appendPath(basic72)
    cmbr.appendPath(basic73)
    cmbr.appendPath(basic74)
    cmbr.appendPath(basic75)
    cmbr.appendPath(basic76)
    cmbr.appendPath(basic77)
    cmbr.appendPath(basic79)
    cmbr.appendPath(basic710)
    cmbr.appendPath(basic711)
#I   
    cmbr.appendPath(basic81)
    cmbr.appendPath(basic82)
    cmbr.appendPath(basic83)
    cmbr.appendPath(basic84)
#J
    cmbr.appendPath(basic91)
    cmbr.appendPath(basic92)
    cmbr.appendPath(basic93)
    cmbr.appendPath(basic94)
    cmbr.appendPath(basic95)
    cmbr.appendPath(basic99)
    cmbr.appendPath(basic910)
    
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
    

    
    
