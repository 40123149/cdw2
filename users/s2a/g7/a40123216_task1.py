# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
a40123216_task1 = Blueprint('a40123216_task1', __name__, url_prefix='/ag7', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@a40123216_task1.route('/a40123216_task1')
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
   #O
    basic1401 = cmbr.dup()
    basic1401.rotate(180)
    basic1401.translate(-210, 0)
    basic1402 = cmbr.dup()
    basic1402.rotate(30)
    basic1402.translate(-210, -20)
    
    basic1403 = cmbr.dup()
    basic1403.rotate(150)
    basic1403.translate(-210, 20)
    
    basic1404 = cmbr.dup()
    basic1404.rotate(180)
    basic1404.translate(-170, 0)
    
    basic1405 = cmbr.dup()
    basic1405.rotate(90)
    basic1405.translate(-200, -37.5)

    basic1406 = cmbr.dup()
    basic1406.rotate(0)
    basic1406.translate(-170, 0)
    
    basic1407 = cmbr.dup()
    basic1407.rotate(90)
    basic1407.translate(-200, 37.5)
    
    basic1409 = cmbr.dup()
    basic1409.rotate(210)
    basic1409.translate(-170, 20)
    
    basic1410 = cmbr.dup()
    basic1410.rotate(-30)
    basic1410.translate(-170, -20)
    
    basic1411 = cmbr.dup()
    basic1411.rotate(0)
    basic1411.translate(-210, 0)
#P
    basic1501 = cmbr.dup()
    basic1501.rotate(180)
    basic1501.translate(-60, 100)
    basic1502 = cmbr.dup()
    basic1502.rotate(0)
    basic1502.translate(-60, 80)
    
    basic1503 = cmbr.dup()
    basic1503.rotate(0)
    basic1503.translate(-60, 140)
    
    basic1504 = cmbr.dup()
    basic1504.rotate(90)
    basic1504.translate(-60, 140)
    
    basic1505 = cmbr.dup()
    basic1505.rotate(90)
    basic1505.translate(-60, 100)
    
    basic1508 = cmbr.dup()
    basic1508.rotate(120)
    basic1508.translate(-40, 100)
    
    basic1509 = cmbr.dup()
    basic1509.rotate(60)
    basic1509.translate(-40, 140)

    basic1511 = cmbr.dup()
    basic1511.rotate(0)
    basic1511.translate(-22.5, 130)
    basic1512 = cmbr.dup()
    basic1512.rotate(0)
    basic1512.translate(-60, 100)
#Q
    basic1601 = cmbr.dup()
    basic1601.rotate(180)
    basic1601.translate(-120, 100)
    basic1602 = cmbr.dup()
    basic1602.rotate(30)
    basic1602.translate(-120, 80)
    
    basic1603 = cmbr.dup()
    basic1603.rotate(150)
    basic1603.translate(-120, 120)
    
    basic1604 = cmbr.dup()
    basic1604.rotate(180)
    basic1604.translate(-80, 100)
    
    basic1605 = cmbr.dup()
    basic1605.rotate(90)
    basic1605.translate(-110, 62.5)

    basic1606 = cmbr.dup()
    basic1606.rotate(0)
    basic1606.translate(-80, 100)
    
    basic1607 = cmbr.dup()
    basic1607.rotate(90)
    basic1607.translate(-110, 137.5)
    
    basic1608 = cmbr.dup()
    basic1608.rotate(30)
    basic1608.translate(-90, 62.5)
    
    basic1609 = cmbr.dup()
    basic1609.rotate(210)
    basic1609.translate(-80, 120)
    
    basic1610 = cmbr.dup()
    basic1610.rotate(-30)
    basic1610.translate(-80, 80)
    basic1611 = cmbr.dup()
    basic1611.rotate(0)
    basic1611.translate(-120, 100)
#R
    basic1701 = cmbr.dup()
    basic1701.rotate(180)
    basic1701.translate(-180, 100)
    basic1702 = cmbr.dup()
    basic1702.rotate(0)
    basic1702.translate(-180, 80)
    
    basic1703 = cmbr.dup()
    basic1703.rotate(0)
    basic1703.translate(-180, 140)
    
    basic1704 = cmbr.dup()
    basic1704.rotate(90)
    basic1704.translate(-180, 140)
    
    basic1705 = cmbr.dup()
    basic1705.rotate(90)
    basic1705.translate(-180, 100)
    
    basic1707 = cmbr.dup()
    basic1707.rotate(30)
    basic1707.translate(-160, 100)
    
    basic1708 = cmbr.dup()
    basic1708.rotate(120)
    basic1708.translate(-160, 100)
    
    basic1709 = cmbr.dup()
    basic1709.rotate(60)
    basic1709.translate(-160, 140)

    
    basic1711 = cmbr.dup()
    basic1711.rotate(0)
    basic1711.translate(-142.5, 130)
    
    basic1712 = cmbr.dup()
    basic1712.rotate(30)
    basic1712.translate(-150, 82.5)
    basic1713 = cmbr.dup()
    basic1713.rotate(0)
    basic1713.translate(-180, 100)
    
#O
    cmbr.appendPath(basic1401)
    cmbr.appendPath(basic1402)
    cmbr.appendPath(basic1403)
    cmbr.appendPath(basic1404)
    cmbr.appendPath(basic1405)
    cmbr.appendPath(basic1406)
    cmbr.appendPath(basic1407)
    cmbr.appendPath(basic1409)
    cmbr.appendPath(basic1410)
    cmbr.appendPath(basic1411)
#P
    cmbr.appendPath(basic1501)
    cmbr.appendPath(basic1502)
    cmbr.appendPath(basic1503)
    cmbr.appendPath(basic1504)
    cmbr.appendPath(basic1505)
    cmbr.appendPath(basic1508)
    cmbr.appendPath(basic1509)
    cmbr.appendPath(basic1511)
    cmbr.appendPath(basic1512)
#Q
    cmbr.appendPath(basic1601)
    cmbr.appendPath(basic1602)
    cmbr.appendPath(basic1603)
    cmbr.appendPath(basic1604)
    cmbr.appendPath(basic1605)
    cmbr.appendPath(basic1606)
    cmbr.appendPath(basic1607)
    cmbr.appendPath(basic1608)
    cmbr.appendPath(basic1609)
    cmbr.appendPath(basic1610)
    cmbr.appendPath(basic1611)
#R
    cmbr.appendPath(basic1701)
    cmbr.appendPath(basic1702)
    cmbr.appendPath(basic1703)
    cmbr.appendPath(basic1704)
    cmbr.appendPath(basic1705)
    cmbr.appendPath(basic1707)
    cmbr.appendPath(basic1708)
    cmbr.appendPath(basic1709)
    cmbr.appendPath(basic1711)
    cmbr.appendPath(basic1712)
    cmbr.appendPath(basic1713)
    
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
    

    
    
