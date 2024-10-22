import gmsh

# Inicializa o GMSH
gmsh.initialize()

# Carrega os dois arquivos .msh (volume do coração e da cicatriz)
gmsh.merge("/home/daniel/3D-heart-models/teste/meshFiles/Patient_1_scarvol.msh")
gmsh.merge("/home/daniel/3D-heart-models/teste/meshFiles/Patient_1.msh")

# Sincroniza o modelo
gmsh.model.occ.synchronize()

# Obtém as entidades físicas (volumes) do coração e da cicatriz
entities_heart = gmsh.model.getEntities(3)  # Volume = 3
entities_scar = gmsh.model.getEntities(3)

# Define os volumes
vol_heart = entities_heart[0][1]  # Volume do coração
vol_scar = entities_scar[1][1]    # Volume da cicatriz

print(f'{vol_heart=}')
print(f'{vol_scar=}')

gmsh.model.occ.booleanDifference([(3, vol_heart)], [(3, vol_scar)])

# Sincroniza as operações
gmsh.model.occ.synchronize()

# Gera a nova malha para o volume modificado
gmsh.model.mesh.generate(3)

# Salva o novo arquivo mesh
gmsh.write("new_patient_model_without_scar.msh")

# Finaliza o GMSH
gmsh.finalize()
