#!/bin/bash
 
if [ -f "/usr/share/ivs-calc/ivs-icon.png" ]; then
    echo "This file is already installed"
    else
    if which tkinter >/dev/null; then
        echo ""
    else
        echo "If you want to install calculator you need to install tkinter first. Do you want to install it now?(y/n)"
        read get
        if echo "$get" | grep -iq "^y" ;then
            sudo apt-get update 2>/dev/null
            sudo apt-get install python3-pip 2>/dev/null
            sudo apt-get install python3-tk 2>/dev/null
            sudo pip3 install pyinstaller 2>/dev/null
        else
            echo "Installation was not successful!"
            exit
        fi
    fi

    if which pyinstaller >/dev/null; then
        echo "You are going to install ivs-projekt. Do you want to install it?(y/n)"
        read get
        if echo "$get" | grep -iq "^y" ;then
            pyinstaller -F ../repo/src/calc.py
        else
            echo "Installation failed"
            exit
        fi
    else
        echo "If you want to install ivs-calc you need to install PyInstaller, do you want to install it now?(y/n)"
        read get
        if echo "$get" | grep -iq "^y" ;then
            sudo -H pip3 install pyinstaller 2>/dev/null

            echo "You are about to install ivs-calc, do you want to install it?(y/n)"
            read get
            if echo "$get" | grep -iq "^y" ;then
                pyinstaller -F ../repo/src/calc.py
            else
                echo "Installation failed"
                exit
            fi
        else
            echo "Installation was not successful"
            exit
        fi
    fi
    
   
    sudo mv ./dist/calc /usr/share/applications
    sudo mkdir /usr/share/ivs-calc
    sudo cp ../repo/ivs-icon.png /usr/share/ivs-calc/
    chmod u+x "uninstall.sh"
    sudo mv ./uninstall.sh /usr/share/applications/
    cp /usr/share/applications/uninstall.sh ./
    if [ ! -e "ivs-calc.desktop" ]; then
        echo "[Desktop Entry]" >> "ivs-calc.desktop"
        echo "Version=1.0" >> "ivs-calc.desktop"
        echo "Type=Application" >> "ivs-calc.desktop"
        echo "Terminal=false" >> "ivs-calc.desktop"
        echo "Exec=/usr/share/applications/calc" >> "ivs-calc.desktop"
        echo "Name=ivs-calc" >> "ivs-calc.desktop"
        echo "Comment=Calculator" >> "ivs-calc.desktop"
        echo "Icon=/usr/share/ivs-calc/ivs-icon.png" >> "ivs-calc.desktop"
        echo "Categories=Utility" >> "ivs-calc.desktop"
    fi 
    chmod u+x "ivs-calc.desktop"
    sudo mv ./ivs-calc.desktop /usr/share/applications

if [ ! -e "remove-calc.desktop" ]; then
        echo "[Desktop Entry]" >> "remove-calc.desktop"
        echo "Version=1.0" >> "remove-calc.desktop"
        echo "Type=Application" >> "remove-calc.desktop"
        echo "Terminal=true" >> "remove-calc.desktop"
        echo "Exec=/usr/share/applications/uninstall.sh" >> "remove-calc.desktop"
        echo "Name=remove-calc" >> "remove-calc.desktop"
        echo "Comment=Uninstaller for ivs-calc." >> "remove-calc.desktop"
        echo "Icon=/usr/share/ivs-calc/ivs-icon.png" >> "remove-calc.desktop"
        echo "Categories=Utility" >> "remove-calc.desktop"
    fi 
    chmod u+x "remove-calc.desktop"
    sudo mv ./remove-calc.desktop /usr/share/applications

sudo rm ./calc.spec
        sudo rm -rf dist
        sudo rm -rf build
        sudo rm -rf ../repo/src/__pycache__

    echo "Installation was successful"
fi
