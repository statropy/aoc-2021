#!/bin/zsh
echo "Creating python for Day $1"
touch input$1.txt
touch test$1.txt
sed "s/{{n}}/$1/g" template.src > day$1.py 
