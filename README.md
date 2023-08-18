# Tools

This repository contains various scripts that you may find interesting.

```
var_svg.py
```

This script allows you to add variables in a SVG file with the format @@VARIABLE_NAME.
Then in a CSV file with this format you can declare the values you want to assign
| Var1        | Var2        | ...          |
| :---        |    :----:   |         ---: |
| value1      | value3      |...           |
| value2      | value4      | ...          |

It will generate as many files as you have lines in the csv file and replace @@Var1, @@Var2, etc by the values of each line.
Usage:
```
python var_svg.py input.svg data.csv outputname
```
