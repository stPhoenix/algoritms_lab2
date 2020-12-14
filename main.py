from enum import Enum

Color = Enum("Color", "WHITE GREY BLACK")


class Vertex:
    color = Color.WHITE

    def __init__(self, n):
        self.name = n

def search(vList, vListItem, v:Vertex):
    v.color = Color.GREY
    for vi in vListItem:
        if vi.color == Color.WHITE: return str(v.name)+ " " + search(vList, vList[vi.name], vi)
    v.color = Color.BLACK
    return str(v.name)

if __name__ == "__main__":

    vs = [Vertex(x) for x in range(6)]


    vList = [
                None,
                [vs[2], vs[5], vs[4]],  #1
                [vs[1], vs[3]],         #2
                [vs[2], vs[4], vs[5]],  #3
                [vs[3], vs[1], vs[5]],  #4
                [vs[4], vs[3], vs[1]],  #5
    ]
    print(search(vList, vList[1], vs[1])[::-1])
    

