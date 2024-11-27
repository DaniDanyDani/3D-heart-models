
GlRuleFibers=GlRuleFibers
par_folder=/mnt/hgfs/par_files
model=$1

###############################################

#Start calculating fiber orientation

carpentry +F $par_folder/l_ab.par -meshname "$model" >> fibers.log
carpentry +F $par_folder/l_epi.par -meshname "$model" >> fibers.log
carpentry +F $par_folder/l_lv.par -meshname "$model" >> fibers.log
carpentry +F $par_folder/l_rv.par -meshname "$model" >> fibers.log

datasets="L_AB L_EPI_2 L_LV L_RV"
for i in $datasets
do
     cd $i
     igbextract -o ascii_1pL -O vm.tdat phie.igb>> fibers.log
     mv -f vm.tdat ../$i.dat
     cd ../
done

$GlRuleFibers -m "$model" -a L_AB.dat -e L_EPI_2.dat -l L_LV.dat -r L_RV.dat --alpha_endo 30 --alpha_epi 30 --beta_endo 40 --beta_epi 40 -o "$model"_done.lon>> fibers.log 


# GlRuleFibers=GlRuleFibers
# par_folder=/mnt/hgfs/par_files
# model=$1

# ###############################################

# # Start calculating fiber orientation

# carpentry +F $par_folder/l_ab.par -meshname "$model" >> fibers.log
# carpentry +F $par_folder/l_epi.par -meshname "$model" >> fibers.log
# carpentry +F $par_folder/l_lv.par -meshname "$model" >> fibers.log
# carpentry +F $par_folder/l_rv.par -meshname "$model" >> fibers.log

# # Process for L_AB
# cd L_AB
# igbextract -o ascii_1pL -O vm.tdat phie.igb >> ../fibers.log
# mv -f vm.tdat ../L_AB.dat
# cd ../

# # Process for L_EPI_2
# cd L_EPI_2
# igbextract -o ascii_1pL -O vm.tdat phie.igb >> ../fibers.log
# mv -f vm.tdat ../L_EPI_2.dat
# cd ../

# # Process for L_LV
# cd L_LV
# igbextract -o ascii_1pL -O vm.tdat phie.igb >> ../fibers.log
# mv -f vm.tdat ../L_LV.dat
# cd ../

# # Process for L_RV
# cd L_RV
# igbextract -o ascii_1pL -O vm.tdat phie.igb >> ../fibers.log
# mv -f vm.tdat ../L_RV.dat
# cd ../

# # Run GlRuleFibers
# $GlRuleFibers -m "$model" -a L_AB.dat -e L_EPI_2.dat -l L_LV.dat -r L_RV.dat --alpha_endo 30 --alpha_epi 30 --beta_endo 40 --beta_epi 40 -o "${model}_done.lon" >> fibers.log
