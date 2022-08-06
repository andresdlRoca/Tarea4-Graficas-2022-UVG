from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, gourad

width = 1920
height = 1080

rend = Renderer(width, height)

rend.active_shader = flat
rend.active_texture = Texture("models/mcblock1.bmp")

rend.glLoadModel("models/mcblock.obj",
                 translate = V3(width/2, 350, 0),
                 rotate = V3(50, 60, 0), 
                 scale = V3(300,300,300))

rend.glFinish("output.bmp")

