import anvil

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


file_path = "C:/Users/cstoc/AppData/Roaming/.minecraft/saves/MapDataTest/region/r."
Option = input("This is the block parser. \nEnter 1 if you would you like what kind of block is at a particular coordinate or enter 2 if you would like to know the block data for an area.\n")

if Option == "1":
    print("Great Choice, ez \n")
    x_coord = int(input("x = "))
    y_coord = int(input("y = "))
    z_coord = int(input("z = "))

    if(x_coord < 0):
        x_coord -= 1
    if(z_coord < 0):
        z_coord -= 1

    region_x = str(x_coord // 512)
    region_z = str(z_coord // 512)

    region = region_x + "." + region_z + ".mca"

    global_chunk_x = (x_coord // 16)
    global_chunk_z = (z_coord // 16)

    local_chunk_x = (global_chunk_x % 32)
    local_chunk_z = (global_chunk_z % 32)

    local_x_coord = (x_coord % 16)
    local_z_coord = (z_coord % 16)

    region = anvil.Region.from_file(file_path + region)

    chunk = anvil.Chunk.from_region(region, local_chunk_x, local_chunk_z)

    block = chunk.get_block(local_x_coord, y_coord, local_z_coord)

    #print(block) # <Block(minecraft:air)>
    print(block.id) # air
    #print(block.properties) # {}
    

elif Option == "2":
    print("Yikerz")
else:
    print("YOU WRONG")
