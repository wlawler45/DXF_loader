import dxfgrabber
import math
import matplotlib
import matplotlib.pyplot as plt

def distance_calculator(start,end):
    return math.sqrt( (start[0]-end[0])**2 + (start[1]-end[1])**2)

def dxf_grabber_readfile(filename):
    dxf=dxfgrabber.readfile(filename)
    layer_count = len(dxf.layers)
    print(layer_count)
    print(len(dxf.blocks))
    all_blocks= [entity for entity in dxf.entities if entity.dxftype == 'INSERT']
    all_splines=[entity for entity in dxf.entities if entity.dxftype == 'SPLINE']
    print(all_blocks[0].name)
    test_block=dxf.blocks[all_blocks[0].name]
    all_polylines= [entity for entity in test_block if entity.dxftype == 'POLYLINE']
    for entity in test_block:
        print(entity.dxftype)
    print(len(all_polylines))
    x=0
    colors=['b','g','r','c','m','y','k']
    for entity in all_polylines:
        color=colors[x]
        for i in range(len(entity.points)-1):
            plt.plot([entity.points[i][0],entity.points[i+1][0]],[entity.points[i][1],entity.points[i+1][1]],color)
            #m=(entity.points[i+1][1]-entity.points[i][1])/(entity.points[i+1][0]-entity.points[i][0])
            print(entity.points[i+1][0]-entity.points[i][0])
            magnitude=distance_calculator(entity.points[i],entity.points[i+1])
            print(magnitude)
            if(magnitude!=0.0):
                plt.arrow(entity.points[i][0],entity.points[i][1],-(entity.points[i+1][1]-entity.points[i][1])/magnitude,(entity.points[i+1][0]-entity.points[i][0])/magnitude)
        x+=1
        
        if(x+1>len(colors)):
            x=0
        print("end")
        for tangent in entity.tangents:
            print(tangent)
        
    plt.show()
    """if(all_lines[0].start[0]>all_lines[1].start[0]):
        bottom_hem=all_lines[0]
        waist_hem=all_lines[1]
    else:
        bottom_hem=all_lines[1]
        waist_hem=all_lines[0]
    print(bottom_hem.start)
    print(bottom_hem.end)
    print(distance_calculator(all_lines[0].start,all_lines[0].end))
    print(waist_hem.start)
    print(waist_hem.end)
    print(distance_calculator(all_lines[1].start,all_lines[1].end))
    for control_points in all_splines[0].fit_points:
        print(control_points)
        
    """
    
    
def line_length_finder(line_number):
    i=0


def main():
    filename="ARM_PANT_DXF.dxf"
    file=dxf_grabber_readfile(filename)
    

if __name__ == "__main__":
	main()