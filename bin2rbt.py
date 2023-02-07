# 原始作者: moo
# 参与修改者：John Huang

import datetime
import click


head_line = "Lattice Semiconductor Corporation ASCII Bitstream\r\n"
gen_time  = "Date:"+"\r\n"*6

endline1 = ""
endline2 = ""

def int2bin(int_number):
    return "{0:08b}".format(int_number)

def int2bin_list(int_number_list):
    return "".join(["{0:08b}".format(i) for i in int_number_list])

@click.command()
@click.option('--binfile', default='binfile.bin', help='binfile.bin')
@click.option('--rbtfile', default='rbtfile.txt', help='rbtfile.txt.')
def bin2rbt(binfile, rbtfile):
    binlines =   ""
    with open(binfile, "rb") as bf:
        bin_data = bf.read()
        for i in range(len(bin_data)-6):
            if i%10 == 0:
                binlines = binlines + "\r\n"
            binlines += int2bin(bin_data[i])
            
        endline1 = "\r\n"+int2bin_list(bin_data[-6:-4]) + "\r\n"
        endline2 = int2bin_list(bin_data[-4:])
        for i in range(6):
            print(bin_data[(i-6)])
        print( endline1)
        print( endline2)
    
    with open(rbtfile, "wb") as rf:
        context_lines = []
        context_lines.append(head_line)
        context_lines.append(gen_time)
        context_lines.append(binlines)
        context_lines.append(endline1)
        context_lines.append(endline2)
        context_lines = "".join(context_lines).encode()
        rf.write(context_lines)


if __name__ == '__main__':
    bin2rbt()

