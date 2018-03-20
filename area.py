#this program calculates the perimeter and area of a rectangle
print("calculate information about a rectangle")
length=float( input("length :"))#python 3.x,input returs a string so height and length are string you need to convert them to either integers or floa
width= float(input("width :"))
area=length * width
print("area" ,area)
perimeter=2 * length + 2 *  width
print("perimeter",perimeter )
radius=float(input("radius :"))
area=radius*2*3.14
print("area" , area)