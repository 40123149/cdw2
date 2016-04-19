# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
a40123227_task1 = Blueprint('a40123227_task1', __name__, url_prefix='/ag7', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@a40123227_task1.route('/a40123227_task1')
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
   #S
    basic1801 = cmbr.dup()
    basic1801.rotate(120)
    basic1801.translate(-240, 130)
    basic1802 = cmbr.dup()
    basic1802.rotate(60)
    basic1802.translate(-240, 110)

    
    basic1804 = cmbr.dup()
    basic1804.rotate(180)
    basic1804.translate(-205, 70)
    
    basic1805 = cmbr.dup()
    basic1805.rotate(60)
    basic1805.translate(-222.5, 100)

    basic1806 = cmbr.dup()
    basic1806.rotate(-60)
    basic1806.translate(-205, 70)
    basic1807 = cmbr.dup()
    basic1807.rotate(90)
    basic1807.translate(-222.5, 140)

    basic1810 = cmbr.dup()
    basic1810.rotate(-90)
    basic1810.translate(-222.5, 60)

    basic1811 = cmbr.dup()
    basic1811.rotate(0)
    basic1811.translate(-240, 130)
    
#T
    basic1901 = cmbr.dup()
    basic1901.rotate(180)
    basic1901.translate(-30, 200)
    basic1902 = cmbr.dup()
    basic1902.rotate(0)
    basic1902.translate(-30, 180)
    
    basic1903 = cmbr.dup()
    basic1903.rotate(0)
    basic1903.translate(-30, 240)
    
    basic1904 = cmbr.dup()
    basic1904.rotate(90)
    basic1904.translate(-30, 240)
    
    basic1909 = cmbr.dup()
    basic1909.rotate(-90)
    basic1909.translate(-30, 240)
    basic1910 = cmbr.dup()
    basic1910.rotate(0)
    basic1910.translate(-30, 200)
#U
    basic2001 = cmbr.dup()
    basic2001.rotate(180)
    basic2001.translate(-110, 200)
    basic2002 = cmbr.dup()
    basic2002.rotate(30)
    basic2002.translate(-110, 180)
    
    basic2003 = cmbr.dup()
    basic2003.rotate(180)
    basic2003.translate(-110, 220)
    
    basic2004 = cmbr.dup()
    basic2004.rotate(180)
    basic2004.translate(-70, 200)
    
    basic2005 = cmbr.dup()
    basic2005.rotate(90)
    basic2005.translate(-100, 162.5)

    basic2006 = cmbr.dup()
    basic2006.rotate(0)
    basic2006.translate(-70, 200)
    
    basic2009 = cmbr.dup()
    basic2009.rotate(180)
    basic2009.translate(-70, 220)
    
    basic2010 = cmbr.dup()
    basic2010.rotate(-30)
    basic2010.translate(-70, 180)
    basic2011 = cmbr.dup()
    basic2011.rotate(0)
    basic2011.translate(-110, 200)
#V
    basic2201 = cmbr.dup()
    basic2201.rotate(30)
    basic2201.translate(-180, 202.5)
    basic2202 = cmbr.dup()
    basic2202.rotate(30)
    basic2202.translate(-190, 220)
    
    basic2203 = cmbr.dup()
    basic2203.rotate(30)
    basic2203.translate(-170, 185)
    
    basic2204 = cmbr.dup()
    basic2204.rotate(180)
    basic2204.translate(-130, 220)

    basic2206 = cmbr.dup()
    basic2206.rotate(-30)
    basic2206.translate(-140, 202.5)
    
    basic2209 = cmbr.dup()
    basic2209.rotate(-30)
    basic2209.translate(-130, 220)
    
    basic2210 = cmbr.dup()
    basic2210.rotate(-30)
    basic2210.translate(-150, 185)
    basic2211 = cmbr.dup()
    basic2211.rotate(0)
    basic2211.translate(-190, 240)
    
    
   #S
    cmbr.appendPath(basic1801)
    cmbr.appendPath(basic1802)
    cmbr.appendPath(basic1804)
    cmbr.appendPath(basic1805)
    cmbr.appendPath(basic1806)
    cmbr.appendPath(basic1807)
    cmbr.appendPath(basic1810)
    cmbr.appendPath(basic1811)
#T
    cmbr.appendPath(basic1901)
    cmbr.appendPath(basic1902)
    cmbr.appendPath(basic1903)
    cmbr.appendPath(basic1904)
    cmbr.appendPath(basic1909)
    cmbr.appendPath(basic1910)
#U
    cmbr.appendPath(basic2001)
    cmbr.appendPath(basic2002)
    cmbr.appendPath(basic2003)
    cmbr.appendPath(basic2004)
    cmbr.appendPath(basic2005)
    cmbr.appendPath(basic2006)
    cmbr.appendPath(basic2009)
    cmbr.appendPath(basic2010)
    cmbr.appendPath(basic2011)
#V
    cmbr.appendPath(basic2201)
    cmbr.appendPath(basic2202)
    cmbr.appendPath(basic2203)
    cmbr.appendPath(basic2204)
    cmbr.appendPath(basic2206)
    cmbr.appendPath(basic2209)
    cmbr.appendPath(basic2210)
    cmbr.appendPath(basic2211)
    
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
    

    
    
