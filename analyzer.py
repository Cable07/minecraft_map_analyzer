import anvil

region = anvil.Region.from_file("C:/Users/cstoc/AppData/Roaming/.minecraft/saves/MapDataTest/region/r.0.0.mca")

chunk = anvil.Chunk.from_region(region, 22, 27)

block = chunk.get_block(5, 65, 8)

print(block) # <Block(minecraft:air)>
print(block.id) # air
print(block.properties) # {}
