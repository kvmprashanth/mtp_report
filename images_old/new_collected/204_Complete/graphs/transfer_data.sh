if mkdir ../collected/$1 ; then
        cp ../*.* ../collected/$1
        cp ../log ../collected/$1/log
        rm ../collected/$1/collector.py
        cp ../../run_experiment.sh ../collected/$1/
        cp ../../setup_experiment.sh ../collected/$1/
else
        echo "ERROR: Directory Exists"
fi
