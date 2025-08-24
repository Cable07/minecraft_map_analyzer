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

def analyze_block(x, y, z):
    if(x < 0):
        x -= 1
    if(z < 0):
        z -= 1

    region_x = str(x // 512)
    region_z = str(z // 512)

    region = region_x + "." + region_z + ".mca"

    global_chunk_x = (x_coord // 16)
    global_chunk_z = (z_coord // 16)

    local_chunk_x = (global_chunk_x % 32)
    local_chunk_z = (global_chunk_z % 32)

    local_x_coord = (x_coord % 16)
    local_z_coord = (z_coord % 16)

    region = anvil.Region.from_file(file_path + region)

    chunk = anvil.Chunk.from_region(region, local_chunk_x, local_chunk_z)

    block = chunk.get_block(local_x_coord, y, local_z_coord)

    print(block.id)

Option = input("This is the block parser. \nEnter 1 if you would you like what kind of block is at a particular coordinate or enter 2 if you would like to know the block data for an area.\n")

world_name = input("\nWhat is the name of your world?\n")

file_path = "C:/Users/cstoc/AppData/Roaming/.minecraft/saves/" + world_name + "/region/r."

if Option == "1":
    x_coord = int(input("x = "))
    y_coord = int(input("y = "))
    z_coord = int(input("z = "))

    analyze_block(x_coord, y_coord, z_coord)

elif Option == "2":
    print("I'll do my best :(")
    x1 = int(input("\n1st x = "))
    y1 = int(input("\n1st y = "))
    z1 = int(input("\n1st z = "))

    x2 = int(input("\n\n2nd x = "))
    y2 = int(input("\n2nd y = "))
    z2 = int(input("\n2nd z = "))

    #normalize inputs so that smaller numbers are always assigned to x1, y1, z1
    #x1, x2 = min(x1, x2), max(x1, x2)
    ##z1, z2 = min(z1, z2), max(z1, z2)

    analyze_block(x1, y1, z1)
    analyze_block(x2, y2, z2)

    #calculates the region values for each coord
    region_x1 = str(x1 // 512)
    region_z1 = str(z1 // 512)
    region_x2 = str(x2 // 512)
    region_z2 = str(z2 // 512)

    region1 = region_x1 + "." + region_z1 + ".mca"
    region2 = region_x2 + "." + region_z2 + ".mca"

    #calculates the global chunk value
    global_chunk_x1 = x1 // 16
    global_chunk_z1 = z1 // 16
    global_chunk_x2 = x2 // 16
    global_chunk_z2 = z2 // 16

    #calculates the local chunk value within the region file
    local_chunk_x1 = global_chunk_x1 % 32
    local_chunk_z1 = global_chunk_z1 % 32
    local_chunk_x2 = global_chunk_x2 % 32
    local_chunk_z2 = global_chunk_z2 % 32

    local_x1 = x1 % 16
    local_z1 = z1 % 16
    local_x2 = x2 % 16
    local_z2 = z2 % 16

    region1 = anvil.Region.from_file(file_path + region1)

    chunk1 = anvil.Chunk.from_region(region1, local_chunk_x1, local_chunk_z1)

    block1 = chunk1.get_block(local_x1, y1, local_z1)

    region2 = anvil.Region.from_file(file_path + region2)

    chunk2 = anvil.Chunk.from_region(region2, local_chunk_x2, local_chunk_z2)

    block2 = chunk2.get_block(local_x2, y2, local_z2)

    print("\n\nBlock 1 is : " + block1.id)
    print("\nBlock 2 is : " + block2.id)


else:
    print("YOU WRONG")
