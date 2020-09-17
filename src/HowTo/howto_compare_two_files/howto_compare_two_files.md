# Comparing two files

You can use **`VS Code`** to compare two files.

```bash
# option-1
code -d <file1> <file2>
# option-2
code -diff <file1> <file2>
```

## Example Output

```bash
# go to target directory
cd ./src/HowTo/howto_compare_two_files/resources
# check diff
code -d test_file_1.txt test_file_2.txt
```

[![Comparing two files in VS Code][#compare-files-vscode]][#compare-files-vscode]

[#compare-files-vscode]: resources/comparing_two_files_in_vscode.PNG