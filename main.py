from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 244, 200, 66 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', edges, transform, screen, color )
