# #!/bin/bash

# for f in Data/*.mhd;
# do
# 	#echo 'Subject' "${f/.mhd}"
	
# 	'ScarProcessing/build/ScarProcessing' $f "${f/.mhd}_scar.vtk"
# done

#!/bin/bash

for f in Data/*.mhd; do
    # Chama o executável com o nome do arquivo e o novo nome
    ScarProcessing/build/ScarProcessing "$f" "${f/.mhd/_scar.vtk}"
done