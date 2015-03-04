#author: James Teague II
#date: Spring 2015
#description: graphics.py - methods to render a graph of 
#proposed points ( of ):

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

def graph():
    """ Finds last line in text file and graphs the attendance """
    infile = open("simProgression.txt","r")
    # Get last line of file and format it
    last_line_arr = format_line(tail(infile))
    # map y-values to ints and plot
    plot_simulation(list(map(int,last_line_arr)))
    

def plot_simulation(attendance):
    """ Generates graph of Simulation attendance and saves to PDF """
    # Open PDF to save graph to
    pdf = PdfPages('Bar_Attendance.pdf')
    # generate list of x-values
    ndxs = list(range(1,len(attendance)+1))
    # generate line for convergence
    line = []
    for x in range(0,len(attendance)+2):
        line.append(6)
    # plot points
    plt.plot(ndxs, attendance, linestyle="none", marker="o", color="r", markersize=10)
    # plot line
    plt.plot(line,linestyle="-",color="b",linewidth=3)
    # set range
    plt.ylim(0,10)
    # set domain
    plt.xlim(0,len(attendance)+.5)
    # write axis labels
    plt.xlabel("Weeks")
    plt.ylabel("Attendance")
    # save graph to PDF
    pdf.savefig()
    # close PDF
    pdf.close()

def format_line(line):
    """ Format line from file to an array for graph """ 
    line = line.replace("[","")
    line = line.replace("]","")
    line = line.replace(" ","")
    line_arr = line.split(",")
    return line_arr

def tail(f, lines=1):
    """
        Grabs the last n lines of a text file
        Arguments:
            f: file to be searched
            lines: number of lines to return; defaults to 1

        I found this online as a solution from:
            http://stackoverflow.com/questions/136168/get-last-n-lines-of-a-file-with-python-similar-to-tail
    """
    # number of lines to return
    total_lines_wanted = lines

    # size to cap?
    BLOCK_SIZE = 1024
    # set pointer to end of file
    f.seek(0, 2)
    
    block_end_byte = f.tell()
    lines_to_go = total_lines_wanted
    block_number = -1
    blocks = [] # blocks of size BLOCK_SIZE, in reverse order starting
                # from the end of the file
    while lines_to_go > 0 and block_end_byte > 0:
        if (block_end_byte - BLOCK_SIZE > 0):
            # read the last block we haven't yet read
            f.seek(block_number*BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE))
        else:
            # file too small, start from begining
            f.seek(0,0)
            # only read what was not read
            blocks.append(f.read(block_end_byte))
        lines_found = blocks[-1].count('\n')
        lines_to_go -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -= 1
    all_read_text = ''.join(reversed(blocks))
    return '\n'.join(all_read_text.splitlines()[-total_lines_wanted:])