# Replace kernel+dt of the built TWRP image with the stock ones (QCDT), keep TWRP ramdisk.
import struct,hashlib,sys,subprocess
built,out=sys.argv[1],sys.argv[2]
D='device/ruggear/rg740a/prebuilt/'
pg=lambda n,p:(n+p-1)//p*p
b=open(built,'rb').read()
assert b[:8]==b'ANDROID!'
ks,ka,rs,ra,ss,sa,ta,ps,hv=struct.unpack('<9I',b[8:44])
assert hv==0,'built image header version %d, need 0'%hv
rd=b[ps+pg(ks,ps):ps+pg(ks,ps)+rs]
k=open(D+'Image','rb').read(); dt=open(D+'dt.img','rb').read()
cmd=b'console=ttyHSL0,115200,n8 androidboot.console=ttyHSL0 androidboot.hardware=qcom msm_rtb.filter=0x237 ehci-hcd.park=3 androidboot.bootdevice=7824900.sdhci lpm_levels.sleep_disabled=1 earlyprintk'
h=hashlib.sha1()
for x in (k,rd,b'',dt): h.update(x); h.update(struct.pack('<I',len(x)))
hdr=b'ANDROID!'+struct.pack('<10I',len(k),0x80008000,len(rd),0x81000000,0,0x80f00000,0x80000100,2048,len(dt),0)
hdr+=b'\0'*16+cmd.ljust(512,b'\0')+h.digest().ljust(32,b'\0')+b'\0'*1024
o=hdr.ljust(2048,b'\0')
for x in (k,rd,dt): o+=x.ljust(pg(len(x),2048),b'\0')
open(out,'wb').write(o); print('wrote',out,len(o),'bytes (limit 33554432)')
assert len(o)<=33554432,'TOO BIG for recovery partition'
