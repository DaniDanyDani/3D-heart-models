import os,glob,shutil,sys,re


# Date='Data-'+str(sys.argv[2])
# pat_nr=int(sys.argv[1])
# patname="Patient_{}".format(pat_nr)
root='/home/daniel/3D-heart-models'
# mat_data=root+'/Matlab_Process/Data/'
# mat_scar=mat_data+'ScarImages/MetaImages'
# mat_txt=mat_data+'Texts'
# mat_seg=mat_data+'Seg/'
# pre_folder=root+'/Files/'+Date
surf='/home/daniel/3D-heart-models/Files/Patient_1 copy/Patient_1'
vtk_srf=surf+'/vtkFiles'
msh_srf=surf+'/mshFiles'
scar_srf=surf+'/scarFiles'
temp_srf=root+'/tempFiles'
stl_srf=temp_srf+'/stlFiles'
# vtxpath=surf+'/PreFiberFiles'
# pre_fem=root+'/FEM/'+Date
# fem=root+'/FEM/'+Date+'/'+patname
# conv=root+'/Convertion_Process'
# scar=root+'/Scar_Process'
# script=root+'/scripts/'
# program=os.getenv('HOME')+'/Programs'
gmsh='/home/daniel/Programs/gmsh/build/gmsh' 
i = 1

lv_endo='{}/Patient_{}-LVEndo-Frame_1.vtk'.format(vtk_srf,i)
rv_endo='{}/Patient_{}-RVEndo-Frame_1.vtk'.format(vtk_srf,i)
rv_epi='{}/Patient_{}-RVEpi-Frame_1.vtk'.format(vtk_srf,i)
scar_vtk='{}/Patient_{}_scar.vtk'.format(vtk_srf,i)
msh='{}/Patient_{}.msh'.format(msh_srf,i)
msh_srf_heart='{}/Patient_{}_surf.msh'.format(msh_srf,i)
msh_heart='{}/Patient_{}_model.msh'.format(msh_srf,i)
stl_scar='{}/Patient_scar.stl'.format(stl_srf,i)
out='{}/Patient_{}.out.txt'.format(msh_srf,i)
biv_mesh_heart='{}/scripts/biv_mesh_teste.geo'.format(root)
biv_mesh='{}/scripts/biv_mesh.geo'.format(root)
biv_msh='{}/scripts/biv_msh_teste.geo'.format(root)
biv_stl_scar='/home/daniel/3D-heart-models/scripts/biv_stl_scar.geo'
# os.system('{} -3 {} -merge {} {} {} -o {} 2>&1 {}'.format(gmsh, lv_endo, rv_endo, rv_epi, biv_mesh, msh, out))

# Gerando o .msh com as superfícies do coração e usando merge na fibrose pra gerar o modelo: -------------------------
# os.system('{} -3 {} {} -o {}'.format(gmsh, scar_vtk, biv_stl_scar, stl_scar))
# os.system('{} -3 {} -merge {} {} {} -o {}'.format(gmsh, lv_endo, rv_endo, rv_epi, biv_mesh_heart, msh_srf_heart))
os.system('{} -3 {} -merge {} -o {}'.format(gmsh, msh_srf_heart, biv_msh, msh_heart))
# ----------------------------------------------------- Tá dando certo, mas preciso conferir