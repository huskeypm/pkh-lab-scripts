
DAYS=30
ITV=`bc <<< "$DAYS+1"`


#cmsh -c "device; dumpmonitoringdata -${DAYS}d now gpu_utilization:gpu0 -n node01..node10 -i $ITV —avg"
CMSH=/cm/local/apps/cmd/bin/cmsh
for GPU in {0..3}
do
  #echo "$GPU"
  $CMSH -c "device; dumpmonitoringdata -${DAYS}d now gpu_utilization:gpu$GPU -n node01..node10 -i $ITV --avg" > GPU$GPU
done 

$CMSH -c "device; dumpmonitoringdata -${DAYS}d now loadone -n node01..node10 -i $ITV --avg" > CPU


