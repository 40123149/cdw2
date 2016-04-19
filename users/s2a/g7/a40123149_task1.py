# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
a40123149_task1 = Blueprint('a40123149_task1', __name__, url_prefix='/ag7', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@a40123149_task1.route('/a40123149_task1')
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
  #K
    basic101 = cmbr.dup()
    basic101.rotate(180)
    basic101.translate(80, 100)
    basic102 = cmbr.dup()
    basic102.rotate(0)
    basic102.translate(80, 80)
    
    basic103 = cmbr.dup()
    basic103.rotate(0)
    basic103.translate(80, 140)
    
    basic105 = cmbr.dup()
    basic105.rotate(90)
    basic105.translate(80, 100)

    basic107 = cmbr.dup()
    basic107.rotate(30)
    basic107.translate(100, 100)
    
    basic108 = cmbr.dup()
    basic108.rotate(150)
    basic108.translate(100, 100)
    
    basic1011 = cmbr.dup()
    basic1011.rotate(150)
    basic1011.translate(110.5, 118)
    
    basic1012 = cmbr.dup()
    basic1012.rotate(32.5)
    basic1012.translate(110.5, 82)
    basic1013 = cmbr.dup()
    basic1013.rotate(0)
    basic1013.translate(80, 100)
#L
    basic1101 = cmbr.dup()
    basic1101.rotate(180)
    basic1101.translate(145, 100)
    basic1102 = cmbr.dup()
    basic1102.rotate(0)
    basic1102.translate(145, 80)
    
    basic1103 = cmbr.dup()
    basic1103.rotate(0)
    basic1103.translate(145, 140)

    basic1106 = cmbr.dup()
    basic1106.rotate(90)
    basic1106.translate(145, 60)
    
    basic1110 = cmbr.dup()
    basic1110.rotate(90)
    basic1110.translate(165, 60)
    basic1111 = cmbr.dup()
    basic1111.rotate(0)
    basic1111.translate(145, 100)
#M
    basic1201 = cmbr.dup()
    basic1201.rotate(180)
    basic1201.translate(-70, 0)
    basic1202 = cmbr.dup()
    basic1202.rotate(0)
    basic1202.translate(-70, -20)
    
    basic1203 = cmbr.dup()
    basic1203.rotate(0)
    basic1203.translate(-70, 40)
    
    basic1204 = cmbr.dup()
    basic1204.rotate(180)
    basic1204.translate(-10, 0)
    
    basic1205 = cmbr.dup()
    basic1205.rotate(30)
    basic1205.translate(-70, 40)

    basic1206 = cmbr.dup()
    basic1206.rotate(0)
    basic1206.translate(-10, 0)
    
    basic1207 = cmbr.dup()
    basic1207.rotate(30)
    basic1207.translate(-60, 22.5)
    
    basic1208 = cmbr.dup()
    basic1208.rotate(30)
    basic1208.translate(-50, 5.5)
    
    basic1209 = cmbr.dup()
    basic1209.rotate(180)
    basic1209.translate(-10, 20)
    
    basic1210 = cmbr.dup()
    basic1210.rotate(0)
    basic1210.translate(-10, -20)
    
    basic1211 = cmbr.dup()
    basic1211.rotate(-30)
    basic1211.translate(-10, 40)
    
    basic1212 = cmbr.dup()
    basic1212.rotate(-30)
    basic1212.translate(-20, 22.5)
    
    basic1213 = cmbr.dup()
    basic1213.rotate(-30)
    basic1213.translate(-30, 5.5)
    basic1214 = cmbr.dup()
    basic1214.rotate(0)
    basic1214.translate(-70, 0)
#N
    basic1301 = cmbr.dup()
    basic1301.rotate(180)
    basic1301.translate(-100, 0)
    basic1302 = cmbr.dup()
    basic1302.rotate(0)
    basic1302.translate(-100, -20)
    
    basic1303 = cmbr.dup()
    basic1303.rotate(0)
    basic1303.translate(-100, 40)
    
    basic1304 = cmbr.dup()
    basic1304.rotate(180)
    basic1304.translate(-145, 0)
    
    basic1305 = cmbr.dup()
    basic1305.rotate(48)
    basic1305.translate(-115, -7)

    basic1306 = cmbr.dup()
    basic1306.rotate(0)
    basic1306.translate(-145, 0)
    
    basic1307 = cmbr.dup()
    basic1307.rotate(48)
    basic1307.translate(-145, 20)
    
    basic1308 = cmbr.dup()
    basic1308.rotate(48)
    basic1308.translate(-130, 6.5)
    
    basic1309 = cmbr.dup()
    basic1309.rotate(180)
    basic1309.translate(-145, 20)
    
    basic1310 = cmbr.dup()
    basic1310.rotate(0)
    basic1310.translate(-145, -20)
    basic1311 = cmbr.dup()
    basic1311.rotate(0)
    basic1311.translate(-100, 0)

    
  #K
    cmbr.appendPath(basic101)
    cmbr.appendPath(basic102)
    cmbr.appendPath(basic103)
    cmbr.appendPath(basic105)
    cmbr.appendPath(basic107)
    cmbr.appendPath(basic108)
    cmbr.appendPath(basic1011)
    cmbr.appendPath(basic1012)
    cmbr.appendPath(basic1013)
#L
    cmbr.appendPath(basic1101)
    cmbr.appendPath(basic1102)
    cmbr.appendPath(basic1103)
    cmbr.appendPath(basic1106)
    cmbr.appendPath(basic1110)
    cmbr.appendPath(basic1111)
#M
    cmbr.appendPath(basic1201)
    cmbr.appendPath(basic1202)
    cmbr.appendPath(basic1203)
    cmbr.appendPath(basic1204)
    cmbr.appendPath(basic1205)
    cmbr.appendPath(basic1206)
    cmbr.appendPath(basic1207)
    cmbr.appendPath(basic1208)
    cmbr.appendPath(basic1209)
    cmbr.appendPath(basic1210)
    cmbr.appendPath(basic1211)
    cmbr.appendPath(basic1212)
    cmbr.appendPath(basic1213)
    cmbr.appendPath(basic1214)
#N
    cmbr.appendPath(basic1301)
    cmbr.appendPath(basic1302)
    cmbr.appendPath(basic1303)
    cmbr.appendPath(basic1304)
    cmbr.appendPath(basic1305)
    cmbr.appendPath(basic1306)
    cmbr.appendPath(basic1307)
    cmbr.appendPath(basic1308)
    cmbr.appendPath(basic1309)
    cmbr.appendPath(basic1310)
    cmbr.appendPath(basic1311)    
    
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
    

    
    
