import anvil

file_path = "C:/Users/cstoc/AppData/Roaming/.minecraft/saves/MapDataTest/region/r."

region = anvil.Region.from_file(file_path + "0.0.mca")

chunk = anvil.Chunk.from_region(region, 22, 27)

block = chunk.get_block(4, 68, 9)

print(block) # <Block(minecraft:air)>
print(block.id) # air
print(block.properties) # {}
