# #!/bin/bash

# for f in Data/*.mhd;
# do
# 	#echo 'Subject' "${f/.mhd}"
	
# 	'ScarProcessing/build/ScarProcessing' $f "${f/.mhd}_scar.vtk"
# done

#!/bin/bash

for f in Data/*.mhd; do
    # Extrai o nome base do arquivo sem a extensão
    base_name=$(basename "$f" .mhd)
    # Executa o comando com o nome correto
    ScarProcessing/build/ScarProcessing "$f" "Data/${base_name}_scar.vtk"
done
