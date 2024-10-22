import gmsh
import sys

# Inicializa o Gmsh
gmsh.initialize()

# Carrega os dois arquivos .msh (o volume do coração e o volume da fibrose)
gmsh.merge("/home/daniel/3D-heart-models/teste/meshFiles/Patient_1_scarvol.msh")
gmsh.merge("/home/daniel/3D-heart-models/teste/meshFiles/Patient_1.msh")

# Criar o novo modelo no Gmsh e definir volumes
gmsh.model.add("boolean_operation")

# Extrai as entidades físicas dos dois arquivos mesh
entities_heart = gmsh.model.getEntities(13)  # volume = 3
entities_scar = gmsh.model.getEntities(3)

# Realizar a operação Boolean Difference: subtraindo a fibrose do coração
vol_heart = entities_heart[0][1]  # Volume do coração
vol_scar = entities_scar[0][1]    # Volume da fibrose

# BooleanDifference: Subtrai a fibrose do coração
gmsh.model.occ.booleanDifference([(3, vol_heart)], [(3, vol_scar)])

# Sincroniza para garantir que as mudanças são aplicadas
gmsh.model.occ.synchronize()

# Gerar a malha novamente para o novo volume
gmsh.model.mesh.generate(3)

# Salvar o novo arquivo mesh resultante
gmsh.write("new_patient_model_with_hole.msh")

# Finaliza o Gmsh
gmsh.finalize()
