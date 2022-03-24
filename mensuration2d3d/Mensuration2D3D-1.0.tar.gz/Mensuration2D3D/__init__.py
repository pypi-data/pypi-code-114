from math import pi

#====================================2D SHAPES==================================

#---------------------------------QUADRILATERALS----------------------------------    
class Square:

    """

    Area & Perimeter will be calculated for the given side or iterable
    of sides.

    """
    
    def area(args):

        """

        Calculate the Area of a Sqaure with given side.
        :param args: Side.
        :type args: int or float or iterable of Side.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #Checking if the Argument passed is an Iterable...
        #...and Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [dimension*dimension for dimension in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return dimension*dimension
    
    def perimeter(args):

        """

        Calculate the Perimeter of a Sqaure with given side.
        :param args: Side.
        :type args: int or float or iterable of Side.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [4*dimension for dimension in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 4*dimension
        
class Rectangle:

    """

    Area & Perimeter will be calculated for the given Length & Breadth or iterable
    of dimensions.

    """
    
    def area(*args):

        """

        Calculate the Area of a Rectangle with given Length & Breadth.
        :param args: Length & Breadth.
        :type args: int or float or iterable of Length & Breadth.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [length*breadth for length,breadth in list_dimension]

        if len(args) == 2:                
            length, breadth = args[0], args[1]
            return length*breadth
        

    def perimeter(*args):

        """

        Calculate the Perimeter of a Rectangle with given Length & Breadth.
        :param args: Length & Breadth.
        :type args: int or float or iterable of Length & Breadth.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
        
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [2*(length+breadth) for length,breadth in list_dim]

        if len(args) == 2:                
            length,breadth = args[0], args[1]
            return 2*(length+breadth)

class Rhombus:

    """

    Area & Perimeter will be calculated for the given diagonals or iterable
    of diagonlas & side or iterable of sides frespectively.

    """
    
    def area(*args):

        """

        Calculate the Area of a Rhombus with given diagonals.
        :param args: Diagonal_1 & Diagonal_2.
        :type args: int or float or iterable of Diagonal_1 & Diagonal_2.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
        """

        if len(args) == 1:
            list_dimension = [diagonal for arg in args for diagonal in arg]
            return [0.5*diagonal_1*diagonal_2 for diagonal_1,diagonal_2 in list_dimension]

        if len(args) == 2:                
            diagonal_1,diagonal_2 = args[0], args[1]
            return 0.5*diagonal_1*diagonal_2

    def perimeter(args):

        """

        Calculate the Perimeter of a Rhombus with given diagonals.
        :param args: Side.
        :type args: int or float or iterable of Side.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
        
        """

        if type(args) is list or type(args) is tuple or type(args) is set:
            return [4*dimension for dimension in args]
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 4*dimension
    

class Parallelogram:

    """

    Area will be calculated for the given Base & Height or iterable
    of Base & Height.
    
    Perimeter will be calculated for the given Length & Breadth or iterable
    of Length & Breadth.
    
    """
    

    def area(*args):

        """

        Calculate the Area of a Parallelogram with given Base & Height.
        :param args: Base & Height.
        :type args: int or float or iterable of Base & Height.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [base*height for base,height in list_dimension]

        if len(args) == 2:                
            base, height = args[0], args[1]
            return base*height
        
    def perimeter(*args):

        """

        Calculate the Perimeter of a Parallelogram with given Length & Breadth.
        :param args: Length & Breadth.
        :type args: int or float or iterable of Length & Breadth.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [2*(length+breadth) for length,breadth in list_dim]

        if len(args) == 2:                
            length, breadth = args[0], args[1]
            return 2*(length+breadth)

class Trapezium:

    """

    Area will be calculated for the given Two parallel sides (a, c) & height or iterable
    of Two parallel sides (a, c) & height.
    :Order: a, c, height 
    
    Perimeter will be calculated for the given 4 sides or iterable of 4 sides
    (a, b, c, d). 
    
    """


    def area(*args):

        """

        Calculate the Area of a Trapezium with given Two parallel sides & height.
        :param args: Two parallel sides (a, c) & height.
        :type args: int or float or iterable of Two parallel sides (a, c) & height.
        :Order: a, c, height
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])

        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [0.5*height*(a+c) for a,c,height in list_dimension]

        if len(args) == 3:                
            a, c, height = args[0], args[1], args[2]
            return 0.5*height*(a+c)

    def perimeter(*args):

        """

        Calculate the Perimeter of a Trapezium with given 4 sides (a, b, c, d).
        :param args: 4 sides (a, b, c, d).
        :type args: int or float or iterable of 4 sides (a, b, c, d).
        :e.g.: (2, 3, 5, 7) or (2.0, 3.1, 5, 7.6) or
        ([(2, 3.0, 5, 7.2), {3.1, 4.2, 7, 9}, [1, 2.2, 4.3, 5]])

        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [a+b+c+d for a,b,c,d in list_dim]

        if len(args) == 4:                
            a, b, c, d = args[0], args[1], args[2], args[3]
            return (a+b+c+d)

#------------------------------------CIRCLES------------------------------------ 

class Circle:

    """

    Area & Perimeter will be calculated for the given radius or iterable of radius.
    
    """

    def area(args):

        """

        Calculate the Area of a Circle with given radius.
        :param args: radius.
        :type args: int or float or iterable of radius.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
 
        """

        if type(args) is list or type(args) is tuple or type(args) is set:
            return [pi*radius*radius for radius in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return pi*radius*radius

    def perimeter(args):

        """

        Calculate the Perimeter of a Circle with given radius.
        :param args: radius.
        :type args: int or float or iterable of radius.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))

        """

        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [2*pi*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 2*pi*radius

class SemiCircle:

    """

    Area & Perimeter will be calculated for the given radius or iterable of radius.
    
    """

    def area(args):

        """

        Calculate the Area of a Semi-Circle with given radius.
        :param args: radius.
        :type args: int or float or iterable of radius.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        if type(args) is list or type(args) is tuple or type(args) is set:
            return [0.5*pi*radius*radius for radius in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 0.5*pi*radius*radius

    def perimeter(args):

        """

        Calculate the Perimeter of a Semi-Circle with given radius.
        :param args: radius.
        :type args: int or float or iterable of radius.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))

        """

        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [pi*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return pi*radius

#---------------------------------TRIANGLES---------------------------------- 

class ScaleneTriangle:

    """

    Area & Perimeter will be calculated for the given sides (a, b, c) or
    iterable of sides (a, b, c).
    
    """

    def area(*args):

        """

        Calculate the Area of a Scalene Triangle with given sides (a, b, c).
        :param args: sides (a, b, c).
        :type args: int or float or iterable of sides (a, b, c).
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])

        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return ([(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))**0.5
                     for a,b,c in list_dimension])
            #return [(s*(s-a)*(s-b)*(s-c))**0.5 for a,b,c in list_dimension]
        if len(args) == 3:                
            a, b, c = args[0], args[1], args[2]
            return (((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*
                    (((a+b+c)/2)-c))**0.5

    def perimeter(*args):

        """

        Calculate the Perimeter of a Scalene Triangle with given sides (a, b, c).
        :param args: sides (a, b, c).
        :type args: int or float or iterable of sides (a, b, c).
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])

        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [a+b+c for a,b,c in list_dim]

        if len(args) == 3:                
            a, b, c = args[0], args[1], args[2]
            return (a+b+c)

class IsoscelesTriangle:

    """

    Area will be calculated for the given base & height or iterable of
    base & height.

    Perimeter will be calculated for the given One of equal side (a) & base or
    iterable of One of equal side (a) & base.
    :Order: a, base

    """

    def area(*args):

        """

        Calculate the Area of a Isosceles Triangle with given base & height.
        :param args: base & height.
        :type args: int or float or iterable of base & height.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])        
    
        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [0.5*base*height for base,height in list_dimension]

        if len(args) == 2:                
            base, height = args[0], args[1]
            return 0.5*base*height

    def perimeter(*args):

        """

        Calculate the Perimeter of a Isosceles Triangle with given One of equal side (a) & base.
        :param args: One of equal side (a) & base.
        :type args: int or float or iterable of One of equal side (a) & base.
        :Order: a, base
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [(2*a)+base for a,base in list_dim] #a = One of parallel sides

        if len(args) == 2:                
            a, base = args[0], args[1]
            return (2*a)+base

class EquilateralTriangle:

    """

    Area & Perimeter will be calculated for the given side or iterable of side.

    """

    def area(args):

        """

        Calculate the Area of a Equilateral Triangle with given side.
        :param args: side.
        :type args: int or float or iterable of side.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))

        """

        #Checking if the Argument passed is an Iterable...
        #...if Yes, Returning also an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [((3/4)**0.5)*(dimension**2) for dimension in args]

        #Checking if the Argument passed is an Int or a Float...
        #...if Yes, Returning also an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return ((3/4)**0.5)*(dimension**2)

    def perimeter(args):

        """

        Calculate the Perimeter of a Equilateral Triangle with given side.
        :param args: side.
        :type args: int or float or iterable of side.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))

        """

        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [3*dimension for dimension in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 3*dimension

class RightAngleTriangle:

    """

    Area will be calculated for the given base & height or iterable of
    base & height.

    Perimeter will be calculated for the given sides (a, b, c) or iterable of
    sides (a, b, c).

    """

    def area(*args):

        """

        Calculate the Area of a Right-Angle Triangle with given base & height.
        :param args: base & height.
        :type args: int or float or iterable of base & height.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])

        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [0.5*base*height for base,height in list_dimension]

        if len(args) == 2:                
            base, height = args[0], args[1]
            return 0.5*base*height

    def perimeter(*args):

        """

        Calculate the Perimeter of a Right-Angle Triangle with given
        sides (a, b, c).
        :param args: sides (a, b, c).
        :type args: int or float or iterable of sides (a, b, c).
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])
 
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [a+b+c for a,b,c in list_dim]

        if len(args) == 3:                
            a, b, c = args[0], args[1], args[2]
            return (a+b+c)
        
#====================================3D SHAPES==================================

#---------------------------------------CUBE------------------------------------
    
class Cube:

    """

    Volume, Curved Surface Area, Total Surface Area will be calculated for the
    given side or iterable of sides.

    """

    def volume(args):

        """

        Calculate the Volume of a Cube with given side.
        :param args: Side.
        :type args: int or float or iterable of Side.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #Checking if the Argument passed is an Iterable...
        #...and Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [dimension*dimension*dimension for dimension in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return dimension*dimension*dimension

    def curvedSurfaceArea(args):

        """

        Calculate the Curved Surface Area of a Cube with given side.
        :param args: Side.
        :type args: int or float or iterable of Side.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [4*dimension*dimension for dimension in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 4*dimension*dimension

    def totalSurfaceArea(args):

        """

        Calculate the Total Surface Area of a Cube with given side.
        :param args: Side.
        :type args: int or float or iterable of Side.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [6*dimension*dimension for dimension in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            dimension = args
            return 6*dimension*dimension

#----------------------------------CUBOID---------------------------------------

class Cuboid:

    """

    Volume, Curved Surface Area, Total Surface Area will be calculated for the
    given Length, Breadth & Height or iterable of Length, Breadth & Height.

    """


    def volume(*args):

        """

        Calculate the Volume of a Cuboid with given Length, Breadth & Height.
        :param args: Length, Breadth & Height.
        :type args: int or float or iterable of Length, Breadth & Height.
        :Order: Length, Breadth, Height 
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])

        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [length*breadth*height for length,breadth,height in list_dimension]

        if len(args) == 3:                
            length, breadth, height = args[0], args[1], args[2]
            return length*breadth*height
        

    def curvedSurfaceArea(*args):

        """

        Calculate the Curved Surface Area of a Cuboid with given Length, Breadth & Height.
        :param args: Length, Breadth & Height.
        :type args: int or float or iterable of Length, Breadth & Height.
        :Order: Length, Breadth, Height 
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])

        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return ([2*height*(length+breadth)
                     for length,breadth,height in list_dim])

        if len(args) == 3:                
            length, breadth, height = args[0], args[1], args[2]
            return 2*height*(length+breadth)

    def totalSurfaceArea(*args):

        """

        Calculate the Total Surface Area of a Cuboid with given Length, Breadth & Height.
        :param args: Length, Breadth & Height.
        :type args: int or float or iterable of Length, Breadth & Height.
        :Order: Length, Breadth, Height 
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])

        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return ([2*(length*breadth + breadth*height + height*length)
                     for length,breadth,height in list_dim])

        if len(args) == 3:                
            length, breadth, height = args[0], args[1], args[2]
            return 2*(length*breadth + breadth*height + height*length)

#------------------------------------SPHERES------------------------------------- 

class Sphere:

    """

    Volume & Curved Surface Area will be calculated for the given Radius or
    iterable of Radius.

    """

    
    def volume(args):

        """

        Calculate the Volume of a Sphere with given Radius.
        :param args: Radius.
        :type args: int or float or iterable of Radius.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #Checking if the Argument passed is an Iterable...
        #...and Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [(4/3)*pi*radius*radius*radius for radius in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return (4/3)*pi*radius*radius*radius

    def curvedSurfaceArea(args):

        """

        Calculate the Curved Surface Area of a Sphere with given Radius.
        :param args: Radius.
        :type args: int or float or iterable of Radius.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [4*pi*radius*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 4*pi*radius*radius

class HemiSphere:

    """

    Volume, Curved Surface Area, Total Surface Area will be calculated for the
    given Radius or iterable of Radius.

    """
    
    def volume(args):

        """

        Calculate the Volume of a Hemisphere with given Radius.
        :param args: Radius.
        :type args: int or float or iterable of Radius.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #Checking if the Argument passed is an Iterable...
        #...and Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [(2/3)*pi*radius*radius*radius for radius in args]

        #Checking if the Argument passed is an Int or a Float...
        #...and Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return (2/3)*pi*radius*radius*radius

    def curvedSurfaceArea(args):

        """

        Calculate the Curved Surface Area of a Hemisphere with given Radius.
        :param args: Radius.
        :type args: int or float or iterable of Radius.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [2*pi*radius*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 2*pi*radius*radius

    def totalSurfaceArea(args):

        """

        Calculate the Total Surface Area of a Hemisphere with given Radius.
        :param args: Radius.
        :type args: int or float or iterable of Radius.
        :e.g.: (2) or (2.0) or ((2, 3.0, 4))
    
        """

        #if the Argument passed is an Iterable...
        #...then Returning an Iterable
        if type(args) is list or type(args) is tuple or type(args) is set:
            return [3*pi*radius*radius for radius in args]

        #if the Argument passed is an Int or a Float...
        #...then Returning an Int or a Float
            
        elif type(args) is int or type(args) is float:
            radius = args
            return 3*pi*radius*radius

#------------------------------------CYLINDER------------------------------------- 

class Cylinder:

    """

    Volume, Curved Surface Area, Total Surface Area will be calculated for the
    given Radius & Height or iterable of Radius & Height.

    """


    def volume(*args):

        """

        Calculate the Volume of a Cylinder with given Radius & Height.
        :param args: Radius & Height.
        :type args: int or float or iterable of Radius & Height.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return [pi*radius*radius*height for radius,height in list_dimension]

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return pi*radius*radius*height
        

    def curvedSurfaceArea(*args):

        """

        Calculate the Curved Surface Area of a Cylinder with given Radius & Height.
        :param args: Radius & Height.
        :type args: int or float or iterable of Radius & Height.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [2*pi*radius*height for radius,height in list_dim]

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return 2*pi*radius*height

    def totalSurfaceArea(*args):

        """

        Calculate the Total Surface Area of a Cylinder with given Radius & Height.
        :param args: Radius & Height.
        :type args: int or float or iterable of Radius & Height.
        :Order: Radius, Height        
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [2*pi*radius*(radius+height) for radius,height in list_dim]

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return 2*pi*radius*(radius+height)

#-------------------------------------CONE-------------------------------------- 

class Cone:

    """

    Volume will be calculated for the given Radius & Height or iterable of Radius & Height.
    Curved Surface Area will be calculated for the given Radius & Slant Height or iterable of Radius & Slant Height.
    Curved Surface Area will be calculated for the given Radius & Height or iterable of Radius & Height.
    Total Surface Area will be calculated for the given Radius & Slant Height or iterable of Radius & Slant Height.
    Slant Height will be calculated for the given Radius & Height or iterable of Radius & Height.

    """

    def volume(*args):

        """

        Calculate the Volume of a Cone with given Radius & Height.
        :param args: Radius & Height.
        :type args: int or float or iterable of Radius & Height.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return ([(1/3)*pi*radius*radius*height
                     for radius,height in list_dimension])

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return (1/3)*pi*radius*radius*height

    def curvedSurfaceArea_withSlantHeight(*args):

        """

        Calculate the Curved Surface Area of a Cone with given Radius & Slant Height.
        :param args: Radius & Slant Height.
        :type args: int or float or iterable of Radius & Slant Height.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [pi*radius*length for radius,length in list_dim]

        if len(args) == 2:                
            radius, length = args[0], args[1]
            return pi*radius*length

    def curvedSurfaceArea_withHeight(*args):

        """

        Calculate the Curved Surface Area of a Cone with given Radius & Height.
        :param args: Radius & Height.
        :type args: int or float or iterable of Radius & Height.
        :Order: Radius, Height
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return ([pi*radius*((radius**2 + height**2)**0.5)
                     for radius,height in list_dim])
        if len(args) == 2:                
            radius, height = args[0], args[1]
            return pi*radius*((radius**2 + height**2)**0.5)

    def totalSurfaceArea(*args):

        """

        Calculate the Total Surface Area of a Cone with given Radius & Slant Height.
        :param args: Radius & Slant Height.
        :type args: int or float or iterable of Radius & Slant Height.
        :Order: Radius, Slant Height
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [pi*radius*(radius+length) for radius,length in list_dim]

        if len(args) == 2:                
            radius, length = args[0], args[1]
            return pi*radius*(radius+length)

    def slantHeight(*args):

        """

        Calculate the Slant Height of a Cone with given Radius & Height.
        :param args: Radius & Height.
        :type args: int or float or iterable of Radius & Height.
        :e.g.: (2, 3) or (2.0, 3.1) or ([(2, 3.0), {3.1, 4.2}, [1, 2.2]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [(radius**2 + height**2)**0.5 for radius,height in list_dim]

        if len(args) == 2:                
            radius, height = args[0], args[1]
            return (radius**2 + height**2)**0.5
        
#------------------------------------FRUSTUM------------------------------------

class Frustum:

    """

    Volume will be calculated for the given Inner Radius, Outer Radius & Height or iterable of Inner Radius, Outer Radius & Height.
    Curved Surface Area will be calculated for the given Inner Radius, Outer Radius & Slant Height or iterable of Inner Radius, Outer Radius & Slant Height.
    Curved Surface Area will be calculated for the given Inner Radius, Outer Radius & Height or iterable of Inner Radius, Outer Radius & Height.
    Total Surface Area will be calculated for the given Inner Radius, Outer Radius & Slant Height or iterable of Inner Radius, Outer Radius & Slant Height.
    Slant Height will be calculated for the given Inner Radius, Outer Radius & Height or iterable of Radius & Height.

    """

    def volume(*args):

        """

        Calculate the Volume of a Frustum with given Inner Radius, Outer Radius & Height.
        :param args: Inner Radius, Outer Radius & Height.
        :type args: int or float or iterable of Inner Radius, Outer Radius & Height.
        :Order: Inner Radius, Outer Radius, Height
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])
    
        """

        if len(args) == 1:
            list_dimension = [dimension for arg in args for dimension in arg]
            return ([(1/3)*pi*height*(r**2+R**2+r*R)
                     for r,R,height in list_dimension])

        if len(args) == 3:                
            r, R, height = args[0], args[1], args[2]
            return (1/3)*pi*height*(r**2+R**2+r*R)

    def curvedSurfaceArea_withSlantHeight(*args):

        """

        Calculate the Curved Surface Area of a Frustum with given Inner Radius, Outer Radius & Slant Height.
        :param args: Inner Radius, Outer Radius & Slant Height.
        :type args: int or float or iterable of Inner Radius, Outer Radius & Slant Height.
        :Order: Inner Radius, Outer Radius, Slant Height
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [pi*length*(r+R) for r,R,length in list_dim]

        if len(args) == 3:                
            r, R, length = args[0], args[1], args[2]
            return pi*length*(r+R)

    def curvedSurfaceArea_withHeight(*args):

        """

        Calculate the Curved Surface Area of a Frustum with given Inner Radius, Outer Radius & Height.
        :param args: Inner Radius, Outer Radius & Height.
        :type args: int or float or iterable of Inner Radius, Outer Radius & Height.
        :Order: Inner Radius, Outer Radius, Height
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return ([pi*(r+R)*(height**2 + (R-r)**2)**0.5
                     for r,R,height in list_dim])
        if len(args) == 3:                
            r, R, height = args[0], args[1], args[2]
            return pi*(r+R)*(height**2 + (R-r)**2)**0.5

    def totalSurfaceArea(*args):

        """

        Calculate the Total Surface Area of a Frustum with given Inner Radius, Outer Radius & Slant Height.
        :param args: Inner Radius, Outer Radius & Slant Height.
        :type args: int or float or iterable of Inner Radius, Outer Radius & Slant Height.
        :Order: Inner Radius, Outer Radius, Slant Height
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [pi*length*(r+R)+pi*(r**2+R**2) for r,R,length in list_dim]

        if len(args) == 3:                
            r, R, length = args[0], args[1], args[2] 
            return pi*length*(r+R)+pi*(r**2+R**2)
        

    def slantHeight(*args):

        """

        Calculate the Slant Height of a Frustum with given Inner Radius, Outer Radius & Height.
        :param args: Inner Radius, Outer Radius & Height.
        :type args: int or float or iterable of Inner Radius, Outer Radius & Height.
        :Order: Inner Radius, Outer Radius, Height
        :e.g.: (2, 3, 5) or (2.0, 3.1, 5) or ([(2, 3.0, 5), {3.1, 4.2, 7}, [1, 2.2, 4.3]])
    
        """

        if len(args) == 1:
            list_dim = [dimension for arg in args for dimension in arg]
            return [(height**2 + (R-r)**2)**0.5 for r,R,height in list_dim]

        if len(args) == 3:                
            r, R, height = args[0], args[1], args[2]
            return (height**2 + (R-r)**2)**0.5