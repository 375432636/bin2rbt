# 原始作者: moo
# 参与修改者：John Huang

import datetime
import click


head_line = "Lattice Semiconductor Corporation ASCII Bitstream\r\n"
gen_time  = "Date:"+f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"+"\r\n"*6


def int2bin_list(int_number_list):
    # convert the binary code to binary text one by one
    return "".join(["{0:08b}".format(i) for i in int_number_list])

@click.command()
@click.option('--binfile', default='binfile.bin', help='binfile.bin')
@click.option('--rbtfile', default='rbtfile.txt', help='rbtfile.txt.')
def bin2rbt(binfile, rbtfile):
    # read file 
    with open(binfile, "rb") as bf:
        bin_data = bf.read()

    # process text
    # convert the binary code to binary text every 10 byte. 
    binlines = ""
    for i in range(len(bin_data)-6):
        if i%10 == 0:
            binlines = binlines + "\r\n"
        binlines += int2bin_list([bin_data[i]])
    binlines+= "\r\n"
    
    # the laste 6 byte need specific format
    endline1 = int2bin_list(bin_data[-6:-4]) + "\r\n"
    endline2 = int2bin_list(bin_data[-4:])+"\r\n"

    # save the text to file 
    with open(rbtfile, "wb") as rf:
        context_lines = head_line + \
                gen_time + binlines + \
                endline1 + endline2 
        context_lines = "".join(context_lines).encode()
        rf.write(context_lines)


if __name__ == '__main__':
    bin2rbt()

