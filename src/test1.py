from src.main.impl.com.ftd.wow.util.Map_Util import Map_Util,\
    MapSize_Enum

Map_Util.generate_random_map(MapSize_Enum.SIZE_SMALL)


listaa = {1:None,2:None,3:None,4:None}
if 3 in listaa.keys():
    print(listaa[3])