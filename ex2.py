def Magnify_Image(scene,factor):
    MagnifiedImage=[]
    for row in scene:
        NewRow=[]
        for element in row:
            NewRow.append(element*factor)
        MagnifiedImage.append(NewRow)
    return MagnifiedImage
scene = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
factor = 3

result = Magnify_Image(scene, factor)
print(result)
    





























