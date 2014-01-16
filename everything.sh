cd xlrd
echo "Moved to xlrd"
sudo python setup.py install
echo "Library Installed"
cd ..
echo "Moved Back"
python sqlconvert.py ~/Documents/nitw_prof_phone/Test.xlsx
echo "Ran Test File."
echo "Generated Sheet1.sql"