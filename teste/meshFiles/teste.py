import os,glob,shutil,sys,re

root='/home/daniel/3D-heart-models'

surf = '/home/daniel/3D-heart-models/Files/Data-21.11-13.12/Patient_1'
vtk_srf=surf+'/vtkFiles'
msh_srf='/home/daniel/3D-heart-models/teste/meshFiles'
stl_files = '/home/daniel/3D-heart-models/teste/stlFiles'
scar_srf=surf+'/scarFiles'
gmsh='/home/daniel/Programs/gmsh/build/gmsh' 

i = 1
lv_endo='{}/Patient_{}-LVEndo-Frame_1.vtk'.format(vtk_srf,i)
rv_endo='{}/Patient_{}-RVEndo-Frame_1.vtk'.format(vtk_srf,i)
rv_epi='{}/Patient_{}-RVEpi-Frame_1.vtk'.format(vtk_srf,i)
scar='{}/Patient_{}_scar.vtk'.format(vtk_srf, i)


msh='{}/Patient_{}_teste.stl'.format(msh_srf,i)
msh_scar='{}/Patient_{}_scar_teste.stl'.format(msh_srf, i)
msh_final='{}/Patient_{}_final_teste.msh'.format(msh_srf, i)
msh_teste ='/home/daniel/3D-heart-models/Files/Data-21.11-13.12/Patient_1/vtkFiles/teste.msh'

stl_base='{}/base.stl'.format(stl_files, i)
stl_epi='{}/epi.stl'.format(stl_files, i)
stl_rv='{}/endoRv.stl'.format(stl_files, i)
stl_lv='{}/endoLv.stl'.format(stl_files, i)
stl_scar='{}/scar.stl'.format(stl_files, i)


biv_mesh='{}/scripts/biv_mesh.geo'.format(root)
biv_scar='{}/scripts/scar_vol.geo'.format(root)
biv_stl='{}/scripts/convert_to_stl.geo'.format(root)
biv_mesh_scar='{}/scripts/biv_mesh_scar.geo'.format(root)
biv_mesh_base='{}/scripts/biv_mesh_base.geo'.format(root)
biv_malha_fibrose='{}/malha-fibrose.geo'.format(stl_files)
biv_teste='{}/teste.geo'.format('/home/daniel/3D-heart-models/Files/Data-21.11-13.12/Patient_1/vtkFiles/teste.geo')

# Gera os stls:
os.system('{} -3 {} -merge {} {} {} {} -o {}'.format(gmsh, lv_endo, rv_endo, rv_epi, scar, biv_teste, msh_teste))



# os.system('{} -3 {} -merge {} {} {} -o {}'.format(gmsh, lv_endo, rv_endo, rv_epi, biv_mesh_base, stl_base))
# os.system('{} -3 {} -merge {} -o {}'.format(gmsh, rv_epi, biv_stl, stl_epi))
# os.system('{} -3 {} -merge {} -o {}'.format(gmsh, rv_endo, biv_stl, stl_rv))
# os.system('{} -3 {} -merge {} -o {}'.format(gmsh, lv_endo, biv_stl, stl_lv))
# os.system('{} -3 {} -merge {} -o {}'.format(gmsh, scar, biv_stl, stl_scar))


# # Gera o coração
# os.system('{} -3 {}'.format(gmsh, biv_malha_fibrose))



# os.system('{} -3 {} -merge {} {} {} -o {}'.format(gmsh, lv_endo, rv_endo, rv_epi, biv_mesh, msh))
# os.system('{} -3 {} -merge {} -o {}'.format(gmsh, scar, biv_scar, msh_scar))
# os.system('{} -3 {} -merge {} {} -o {}'.format(gmsh, msh, scar, biv_mesh_scar, msh_final))



