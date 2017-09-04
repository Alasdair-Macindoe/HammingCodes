source env/bin/activate
echo ""
echo -e "\e[34mGathering data and creating graphs!"
echo -e "\e[0m"
python3 experiment.py
echo ""
echo -e "\e[34mFinished! Note: The graphing library may not return control,
just force exit if this happens. (Crlt+C on labs)"
echo -e "\e[0m"
