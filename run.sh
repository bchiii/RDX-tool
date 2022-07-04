clear

cyan='\033[0;36m'

printf "${cyan}[+] RDX tool for {brute_forcing} instagram account's."
echo ""
echo ""
echo -e -n "${cyan}[+] a) run the tool.
[+] b) setup the tool.
[+] c) exit."
echo ""
echo ""

printf "${cyan}$ " ; read input

if [[ $input == "A" || $input == "a" ]]; then
    clear
    printf "${cyan} ..."
    clear
    python main.py

elif [[ $input == "B" || $input == "b" ]]; then
    clear
    printf "${cyan} ..."
    clear
    python setup\\setup.py


elif [[ $input == "C" || $input == "c" ]]; then
    clear
    printf "${cyan}[+] quitting RDX tool."
    sleep 2
    clear
    exit
fi