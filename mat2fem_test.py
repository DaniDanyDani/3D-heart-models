import os,glob,shutil,sys,re



def main():	
	root=os.getcwd()
	surf=root+'/tempFiles/teste'
	script=root+'/scripts/'
	program=os.getenv('HOME')+'/Programs'
	gmsh='~/Programs/gmsh/build/gmsh' 
	

	i_out = 7
	i_in = 1
	# Input .vtk Files =============================================
	lv_endo='{}/Patient_{}-LVEndo-Frame_1.vtk'.format(surf,i_in)
	lv_epi='{}/Patient_{}-LVEpi-Frame_1.vtk'.format(surf,i_in)
	rv_endo='{}/Patient_{}-RVEndo-Frame_1.vtk'.format(surf,i_in)
	rv_epi='{}/Patient_{}-RVEpi-Frame_1.vtk'.format(surf,i_in)
	septo_rv='{}/Patient_{}-Septo-Frame_1.vtk'.format(surf,i_in)
	scar='{}/fibrose.stl'.format(surf,i_out)
	lv_endo_stl='{}/lv.stl'.format(surf)
	lv_epi_stl='{}/LVepi.stl'.format(surf)
	rv_endo_stl='{}/rv.stl'.format(surf)
	rv_epi_stl='{}/epi.stl'.format(surf)
	base_stl='{}/base.stl'.format(surf)
	septo_stl='{}/septo.stl'.format(surf)
	parede_stl='{}/paredinha.stl'.format(surf)
	# =========================================================
	
	# Output Files =========================================
	msh_srf_Rv='{}/outputs/Patient_{}_surf_Rv.msh'.format(surf,i_out)
	msh_srf_Lv='{}/outputs/Patient_{}_surf_Lv.msh'.format(surf,i_out)
	msh_srf_heart='{}/outputs/Patient_{}_surf.msh'.format(surf,i_out)
	msh_heart_Rv_model='{}/outputs/Patient_{}_Rv_model.msh'.format(surf,i_out)
	msh_heart_Lv_model='{}/outputs/Patient_{}_Lv_model.msh'.format(surf,i_out)
	msh_heart_model='{}/outputs/Patient_{}_model.msh'.format(surf,i_out)
	stl_scar='{}/outputs/Patient_scar.stl'.format(surf,i_out)
	# =====================================================

	# Bivs to gmsh ========================================
	biv_msh_comfibrose='{}/scripts/biv_msh_comfibrose.geo'.format(root)
	biv_msh_semfibrose='{}/scripts/biv_msh_semfibrose.geo'.format(root)
	biv_msh_Lv='{}/scripts/biv_msh_Lv.geo'.format(root)
	biv_msh_Rv='{}/scripts/biv_msh_Rv.geo'.format(root)
	biv_mesh_heart='{}/scripts/biv_mesh.geo'.format(root)
	biv_mesh_Lv='{}/scripts/biv_mesh_Lv.geo'.format(root)
	biv_mesh_Rv='{}/scripts/biv_mesh_Rv.geo'.format(root)
	biv_stl_scar='{}/scripts/biv_stl_scar_test.geo'.format(root)
	biv_malha_fibrose='{}/malha-fibrose.geo'.format(surf)
	# =====================================================


	# print(f"\n Gerando stl da fibrose \n")
	# os.system('{} -3 {} {} -o {}'.format(gmsh, scar, biv_stl_scar, stl_scar)) # Transform scar.vtk in scar.stl
	# print(f"\n ------------ \n")

	# print(f"\n Gerando superficie só com RV \n")
	# os.system('{} -3 {} -merge {} {} -o {}'.format(gmsh, rv_endo, rv_epi, biv_mesh_Rv, msh_srf_Rv)) # Create Surf_heart_Rv.msh
	# print(f"\n ------------ \n")

	# print(f"\n Merge RV \n")
	# os.system('{} -3 {} -merge {} -o {}'.format(gmsh, msh_srf_Rv, biv_msh_Rv, msh_heart_Rv_model)) # Merging scar with heart Surfaces
	# print(f"\n ------------ \n")

	# print(f"\n Gerando superfície só com LV \n")
	# os.system('{} -3 {} -merge {} {} -o {}'.format(gmsh, lv_endo, lv_epi, biv_mesh_Lv, msh_srf_Lv)) # Create Surf_heart_Lv.msh
	# print(f"\n ------------ \n")

	# print(f"\n Merge LV\n")
	# os.system('{} -3 {} -merge {} -o {}'.format(gmsh, msh_srf_Lv, biv_msh_Lv, msh_heart_Lv_model)) # Merging scar with heart Surfaces
	# print(f"\n ------------ \n")

	print(f"\n Gerando superfície completa\n")
	os.system('{} -3 {} -merge {} {} {} -o {}'.format(gmsh, lv_endo, rv_endo, rv_epi, biv_mesh_heart, msh_srf_heart)) # Create suf_heart.msh
	print(f"\n ------------ \n")

	# print(f"\n Merge full \n")
	# os.system('{} -3 {} -merge {} -o {}'.format(gmsh, msh_srf_heart, biv_msh_comfibrose, msh_heart_model)) # Merging scar with heart Surfaces
	# print(f"\n ------------ \n")

	print(f"\n Merge full sem fibrose \n")
	os.system('{} -3 {} -merge {} -o {}'.format(gmsh, msh_srf_heart, biv_msh_semfibrose, msh_heart_model)) # Merging scar with heart Surfaces
	print(f"\n ------------ \n")

	# print(f"\n Merge full \n")
	# os.system('{} -3 {} -merge {} {} {} {} {} -o {}'.format(gmsh, rv_epi_stl, rv_endo_stl, lv_endo_stl, base_stl, septo_stl, biv_malha_fibrose, msh_heart_model)) # Merging scar with heart Surfaces
	# os.system('{} -3 {} -merge {} {} {} {} -o {}'.format(gmsh, rv_epi_stl, rv_endo, lv_endo_stl, base_stl, biv_malha_fibrose, msh_heart_model)) # Merging scar with heart Surfaces
	# os.system('{} -3 {} -merge {} {} {} {} {} -o {}'.format(gmsh, rv_endo_stl, septo_stl, lv_endo_stl, rv_epi_stl, base_stl, biv_malha_fibrose, msh_heart_model)) # Merging scar with heart Surfaces
	# os.system('{} -3 {} -o {}'.format(gmsh, biv_malha_fibrose, msh_heart_model)) # Merging scar with heart Surfaces
	# print(f"\n ------------ \n")


if __name__ == "__main__":
	main()