import datetime
import click


head_line = "Lattice Semiconductor Corporation ASCII Bitstream\r\n"
gen_time  = "Date:"+"\r\n"*6
context_lines = []

endline1 = ""
endline2 = ""

def int2bin(int_number):
    res_str = ""
    binstr = bin(int_number)[2:]
    binstr_len = len(binstr)
    for i in range(8-binstr_len):
        res_str += '0'
    res_str += binstr
    return res_str

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
            
        endline1 = "\r\n"+int2bin(bin_data[-6]) + int2bin(bin_data[-5]) + "\r\n"
        endline2 = int2bin(bin_data[-4]) + int2bin(bin_data[-3]) + int2bin(bin_data[-2]) + int2bin(bin_data[-1]) + "\r\n"
        for i in range(6):
            print(bin_data[(i-6)])
        print( endline1)
        print( endline2)
    
    with open(rbtfile, "w+") as rf:
        context_lines.append(head_line)
        context_lines.append(gen_time)
        context_lines.append(binlines)
        context_lines.append(endline1)
        context_lines.append(endline2)
        rf.writelines(context_lines)


if __name__ == '__main__':
    bin2rbt()

