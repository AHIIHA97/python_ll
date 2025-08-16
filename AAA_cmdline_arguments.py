#REALISTIC EXAMPLE:
'''
Imagine you have a Python script that generates a daily report and saves it to a file. 
Instead of editing the script every day to change the filename or the content, 
you can use command-line arguments to pass in the values when you run the script.

This will:
Create a file called daily_report.txt
Write the text "Sales increased by 12% today." into it
Print: Report saved to daily_report.txt

Why This Is Useful
You can reuse the same script for different reports.
You can automate it with a scheduler like Windows Task Scheduler or cron.
You can integrate it into larger workflows or pipelines.
'''
from argparse import ArgumentParser

parser = ArgumentParser(description="Generate a simple report")
parser.add_argument('--filename', '-f', required=True, help='Name of the output file')
parser.add_argument('--report', '-r', required=True, help='Content of the report')

args = parser.parse_args()

with open(args.filename, 'w') as file:
    file.write(args.report + '\n')

print(f'Report saved to {args.filename}')




'''
# when run, it creates a .txt file with some text

# cmd line arguments, lesson 11
from argparse import ArgumentParser

# ArgumentParser class allows to create an object that keeps track of all the arguments my program accepts
parser = ArgumentParser()
# parser is an instance of ArgumentParser class

# create new cmd-line argument "output", [full word so --(double dashes)]
parser.add_argument('--output', '-o', required=True, help='destination file for the output of this program')
parser.add_argument('--text', '-t', required=True, help='text to write to output file')

# specify arguments for output
args = parser.parse_args()

with open(args.output, 'w') as f:
    f.write(args.text+'\n')

print(f'wrote "{args.text}" to file "{args.output}"')
'''

