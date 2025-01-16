#!/bash/bin
# it needs to be run in build/
for t in 1 4 8 12 16
do
    for p in "lru" "clock" "2Q"
    do
        echo "-------policy: ${p}----------thread number: ${t}-------"
        ./build/main -p ${p} -t ${t}
        echo "----------------------------------------------------"
    done
done