# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
a40023234_task1 = Blueprint('a40023234_task1', __name__, url_prefix='/ag7', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@a40023234_task1.route('/a40023234_task1')
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
    #W
    basic2101 = cmbr.dup()
    basic2101.rotate(30)
    basic2101.translate(-120, -107.5)
    basic2102 = cmbr.dup()
    basic2102.rotate(30)
    basic2102.translate(-130, -90)
    
    basic2103 = cmbr.dup()
    basic2103.rotate(30)
    basic2103.translate(-110, -125)
    
    basic2104 = cmbr.dup()
    basic2104.rotate(180)
    basic2104.translate(-70, -90)

    basic2106 = cmbr.dup()
    basic2106.rotate(-30)
    basic2106.translate(-80, -107.5)
    
    basic2109 = cmbr.dup()
    basic2109.rotate(-30)
    basic2109.translate(-70, -90)
    
    basic2110 = cmbr.dup()
    basic2110.rotate(-30)
    basic2110.translate(-90, -125)
    
    basic2111 = cmbr.dup()
    basic2111.rotate(30)
    basic2111.translate(-60, -107.5)

    basic2112 = cmbr.dup()
    basic2112.rotate(30)
    basic2112.translate(-70, -90)
    
    basic2113 = cmbr.dup()
    basic2113.rotate(30)
    basic2113.translate(-50, -125)
    
    basic2114 = cmbr.dup()
    basic2114.rotate(180)
    basic2114.translate(-10, -90)
    basic2115 = cmbr.dup()
    basic2115.rotate(-30)
    basic2115.translate(-20, -107.5)
    basic2116 = cmbr.dup()
    basic2116.rotate(-30)
    basic2116.translate(-10, -90)
    
    basic2117 = cmbr.dup()
    basic2117.rotate(-30)
    basic2117.translate(-30, -125)
    basic2118 = cmbr.dup()
    basic2118.rotate(0)
    basic2118.translate(-130, -70)
    
    #W
    cmbr.appendPath(basic2101)
    cmbr.appendPath(basic2102)
    cmbr.appendPath(basic2103)
    cmbr.appendPath(basic2104)
    cmbr.appendPath(basic2106)
    cmbr.appendPath(basic2109)
    cmbr.appendPath(basic2110)
    cmbr.appendPath(basic2111)
    cmbr.appendPath(basic2112)
    cmbr.appendPath(basic2113)
    cmbr.appendPath(basic2114)
    cmbr.appendPath(basic2115)
    cmbr.appendPath(basic2116)
    cmbr.appendPath(basic2117)
    cmbr.appendPath(basic2118)
    
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
    

    
    
