sudo apt-get update
sudo apt-get install -y install gcc python3 python3-pip python3-devel git
git clone https://github.com/thesunbg/inet-tools.git
cd inet-tools
pip3 install -r requirements.txt
python3 main.py