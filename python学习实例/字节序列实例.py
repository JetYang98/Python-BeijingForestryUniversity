import struct
def main():
    file=open('binFile','wb')
    s1='王涛'.encode('utf-8')
    s2='机械11'.encode('utf-8')
    print(len(s1))
    print(type(s1))
    print(s1,s2)
    byte=struct.pack('!6s8si',s1,s2,128)
    print(byte)
    file.write(byte)
    file.close()

    file=open('binFile','rb')
    a,b,c=struct.unpack('!6s8si',file.read(18))
    file.close()
    print(a.decode('utf-8'),b.decode('utf-8'),c)
    
main()      #执行主函数
