# grab stats
sudo bash monitor.bash 
# make purty picture
python3 plotdata.py -run 30
# send to website (key added already) 
scp cpu.png gpu.png pkekeneshuskey@pkhlab.sites.luc.edu:~/public_html/files/

