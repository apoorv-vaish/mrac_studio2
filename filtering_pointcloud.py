import os
from pyntcloud import PyntCloud
import numpy
import pandas as pd

path = os.getcwd()
cloud = PyntCloud.from_file(path + "/valldaura_site_2.ply")

# Reducing data points
voxel_grid_id = cloud.add_structure("voxelgrid", n_x=400, n_y=400, n_z=400)
voxel_grid = cloud.structures[voxel_grid_id]
voxel_grid_nearest = cloud.get_sample("voxelgrid_nearest", voxelgrid_id=voxel_grid_id, as_PyntCloud=True)
print(voxel_grid_nearest)

#print(voxel_grid_nearest.points)

# KDTree
mykdtree_id = voxel_grid_nearest.add_structure("kdtree",leafsize=16, compact_nodes=False, balanced_tree=False)
mykdtree = voxel_grid_nearest.structures[mykdtree_id]

# Filtering Outliers
voxel_grid_nearest.get_filter("SOR", kdtree_id=mykdtree_id, k = 50 , z_max= 1, and_apply=True)
print(voxel_grid_nearest)

# Saving the file
#voxel_grid_nearest.to_file(filename='site_cloud_filtered.ply', also_save=None)

# Splitting
#voxel_grid_nearest.split_on("z", and_return=True, save_format="ply",save_path=path+("/filtered_z"))

# Viewing as HTML
voxel_grid_nearest.plot(backend="threejs")
