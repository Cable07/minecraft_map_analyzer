import anvil
from collections import Counter

""" 
Region parser needs to get user input of coords and determine the
margin that the analyzer and block_counter needs to process.
"""

"""
e.g. User inputs x=-1000, y=20, z=-1000 TO x=500, y=80, z=500 

Process:
-1000 / 512 = -2 --- 500 / 512 = 0

REQUIRED REGION FILES AT COORDS -> r.0.0.mca , r.-2.-2.mca 

REQUIRED REGION FILES IN BETWEEN -> r.0.-1.mca , r.0.-2.mca , r.-1.0.mca , r.-1.-1.mca , r.-1.-2.mca , r.-2.0.mca , r.-2.-1.mca
"""

def analyze_block(x, y, z):
    if(x < 0):
        x -= 1
    if(z < 0):
        z -= 1

    region_x = str(x // 512)
    region_z = str(z // 512)

    region = region_x + "." + region_z + ".mca"

    global_chunk_x = (x // 16)
    global_chunk_z = (z // 16)

    local_chunk_x = (global_chunk_x % 32)
    local_chunk_z = (global_chunk_z % 32)

    local_x_coord = (x % 16)
    local_z_coord = (z % 16)

    region = anvil.Region.from_file(file_path + region)

    chunk = anvil.Chunk.from_region(region, local_chunk_x, local_chunk_z)

    block = chunk.get_block(local_x_coord, y, local_z_coord)

    #print(block.id)
    return(block.id)

Option = input("\nThis is the block parser. \n\nEnter 1 if you would you like what kind of block is at a particular coordinate or enter 2 if you would like to know the block data for an area.\n")
world_name = input("\nType the name of your world: ")

file_path = "C:/Users/cstoc/AppData/Roaming/.minecraft/saves/" + world_name + "/region/r."
block_counts = Counter()

if Option == "1":
    x_coord = int(input("x = "))
    y_coord = int(input("y = "))
    z_coord = int(input("z = "))

    analyze_block(x_coord, y_coord, z_coord)

elif Option == "2":
    x1 = int(input("\n1st x = "))
    y1 = int(input("\n1st y = "))
    z1 = int(input("\n1st z = "))

    x2 = int(input("\n\n2nd x = "))
    y2 = int(input("\n2nd y = "))
    z2 = int(input("\n2nd z = "))

    #normalize inputs so that smaller numbers are always assigned to x1, y1, z1
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    z1, z2 = min(z1, z2), max(z1, z2)

    og_y = y1
    og_z = z1

    while(x1 <= x2):
        while(y1 <= y2):
            while(z1 <= z2):
                block_id = analyze_block(x1, y1, z1)
                if block_id in block_counts:
                    block_counts[block_id] += 1
                else:
                    block_counts[block_id] = 1
                z1+=1
            y1+=1
            z1 = og_z
        x1+=1
        y1 = og_y

    for block, count in block_counts.most_common():
        print(f"{block}: {count}")

else:
    print("YOU WRONG")
