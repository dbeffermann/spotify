virtualenv "`dirname $0`/virtual";
source "`dirname $0`/virtual/bin/activate";
pip list;
pip install -r "`dirname $0`/requirements.txt";
echo "_____INSTALANDO___";
streamlit run "`dirname $0`/main.py"