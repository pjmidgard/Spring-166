from time import time
Times_change_info=0
import os
import binascii
namez = input("c  for compress or e for extract: ")
#@Author Jurijus Pacalovas
class compression:
    def cryptograpy_unpack(self):
                

        
            
    
                self.name = "@Author: Jurijus Pacalovas"
                print(self.name)
                if namez=="e":
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                           print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit                    
                    namea=""
                    namem=""
                    namema="?"
                    Times_of_compression1=0
                    
                    
                    Times1=0
                    
                    
                    INFO4=""
                        
                   
                    
                    count3=0
                    count4=-1
                   
                    Times1=0
                    Times3=0
                    Times_of_compression=0
                    
              

                    Times=0
                    
                    
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    
                    Save_name=len(nameas)

                    Times_of_compression=0
                    
                    countraz=0
                    Times=0
                    Times_change_info=2
                    Times_change_info1=0
                    s=""
                    c=2
                    
                    
                    count4=-1
                 
                    INFO3=""
                    INFO2=""

                    ssTimes_change_info=0
                    
                    

                    block=2
                    

                    count_time_of_copression=0
                    countraz=0
                    Times_change_info=2
                    Times_change_info1=0
                    s=""
                                        
                    
                    c=2
                    
                    
                       
                    INFO3=""

                    ssTimes_change_info=0
                        
                    

                    block=0

                    x=0
                    x1=0
                    x2=0
                    x = time()

            
                    
                    with open(nameas, "w") as f4:
                            f4.write(s)
                   
                    with open(name, "rb") as binary_file:

           
                  
                        # Read the whole file at once
                        
                        data = binary_file.read()
                        
                    
                        
                        s=str(data)
                        
            
                  
                        long_file1=len(data)
                        long_file5=len(data)
                        
            
                  
                        
                        if long_file1>((2**32)-1)+((2**48)-1):
                            print("This file is too big");
                            raise SystemExit
                        if long_file1==0:
                            
                            raise SystemExit

                        Times_Finish=0
                        Times_Plus=0
                        
            
                   
                        while Times_Finish<10:
                       
                            
                            

                
           
                    
                            Times_change_info=Times_change_info+1
                            
                
                    
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]#data to binary
                                    long_file=len(INFO)
                                    long_file1=len(data)
                                
                                    xc=(long_file1*8)-long_file
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            INFO="0"+INFO
                                            z=z+1

      
                                    
                                    
                                    INFO=INFO+INFO2

                                    if countraz==1:
                                        INFO2=INFO
                            
                                    n = int(INFO2, 2)
                                
                                    binary_to_data=len(INFO2)
                                    binary_to_data=(binary_to_data/8)*2
                                    binary_to_data=str(binary_to_data)
                                    binary_to_data="%0"+binary_to_data+"x"
                             
                                    jl=binascii.unhexlify(binary_to_data % n)
                                    size_of_file_count=len(jl)
                                    
                                    data=jl
                                    Times_Plus=Times_Plus+1
                                    
                                
                                    
                                    if countraz==1:

                                        
                                        
                                        

                                        long_file5=len(data)

                                    INFO=bin(int(binascii.hexlify(data),16))[2:]
                                    long_file=len(INFO)

                                    long_file1=len(data)
                                
                                    xc=(long_file1*8)-long_file
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            INFO="0"+INFO
                                            z=z+1


                                    
                                    INFO2=INFO

                                    long_file3=len(INFO2)
                                long_file2=len(INFO2)
                                
                                
                                
                                Long_file=int(INFO2[32:64],2)
                                #print(Long_file)

                                
                                    
                                Byte_Divide=32
                                
                                

                                
                                #print(Long_file)
                                Times_compress=int(INFO2[64:112],2)
                                
                                Divide_Number=int(INFO2[0:32],2)
                                #print(Divide_Number)
                                C1="0"+str(Long_file*8)+"b"
                                N_Start=0
                                Start_file=""
                                Finish_file=""
                                Finish_file1=""
                                Finish_file2=""
                                
                                Start_file=format(N_Start,C1)
                                Finish_file1=INFO2
                              
                                    	#print(Start_file)
                                
                                while Finish_file1!=Finish_file2:
                                    if Times3==0:
                                    	  
                                    	  Start_file=format(N_Start,C1)
                                    	  INFO2=Start_file
                                    	  
                                    

                                    block3=0
                                    INFO3=""
                                    INFO5=""
                                    INFO8=""
                                    
                                    #INFO4=""
                                    
                                    count3+=1
                                    #print(count4)
                                    #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                    #print(len(INFO2))
                                    F=0
                                    B=0
                                    count4=-1
                                 
                                    long_file2=len(INFO2)
                                    #print(long_file2)
                                    N2=-1
                                    N1=1
                                    N5=0
                                    long2=1
                                    
                                    N8=len(INFO2)
                                    long_file14=N8+1
                                    while N1!=0:
                                        N2+=1
                                        long_file14-=1
                                        
                                        long=len(INFO2)
                                        long2=long-N2
                                        if long2<=0:
                                            B=1
                                            N1=0
                                        if B==0:
                                            N=int(INFO2[:long-N2],2)
                                            if N==0:
                                                B=1
                                                N1=0
                                            N5=N//long_file14
                                            N1=N%long_file14
                                    	#print(N2)
                                    Bias=bin(N5)[2:]
                                    if N5==0:
                                    	B=1
                                    long61=len(Bias)
                                    long62=0
                                    if B==0:
                                    	long62=len(INFO2[long-N2:])
                                    NS=long61
                                    NS1=N8-long62
                                    NS2=NS1-1-long61
                                    Nj=len(bin(N2)[2:])
                                    #print(N2)
                                    if Nj>(2**64)-1:
                                        B=1
                                    
                                    
                                    
                                    B6="0"+str((2**6)-1)+"b"
                                    if Times3==0:
                                    	Bias2=format(N2,B6)
                                    	N11=Divide_Number
                                    	
                                    
                                    		
                                    		
                                    	
                                    	
                                    	
                               
                                    	
                                        
                                    	  
                                       
                                        
                                
                                                            
                                    
                                    
                                    Bias3=format(N2,B6)
                                    
                                    Minus1=len(INFO2)
                                    INFO5=Bias+INFO2[long-N2:]
                                    #print(len(INFO5))
                                    Minus1_1=int(INFO5,2)
                                    Minus1-=3
                                    C1="0"+str(Minus1)+"b"
                                    C2="0"+str(Minus1+3)+"b"
                                    INFO4=format(Minus1_1,C1)
                                    INFO6=format(Minus1_1,C2)
                                    Minus1_1_1=len(INFO4)
                                    if Minus1==Minus1_1_1 and B==0:
                                        B=0
                                    else:
                                        B=1
                                  
                                  
                                        
                                    
                                    	   
                               
                                    if B==0:#compress
                                    	INFO3="1"+INFO4
                                    #print(N2)
                                    if B==1:#not_compress
                                    	INFO3="0"+INFO6
                                    
                                    	   
                               
                               
                                 
                                    
                                    INFO8=""
                                    Circle=0
                                    Long888=len(INFO3)
                                    while Circle<Long888:
                                      if INFO3[Circle:Circle+1]=="0":
                                        
                                        INFO8=INFO8+"1"
                                      if INFO3[Circle:Circle+1]=="1":  
                                        INFO8=INFO8+"0"
                                      Circle+=1


                                    INFO3=INFO8

                                    
                                    INFO2=INFO3
                                    #print(INFO3)
                                    #n = int(INFO2, 2)
                                                                                                    
                                            
                                    #n = int(INFO2, 2)                                                                                     
                                            
                                    #binary_to_data=len(INFO2)
                                    #binary_to_data=(binary_to_data/8)*2
                                    #binary_to_data=str(binary_to_data)
                                    #binary_to_data="%0"+binary_to_data+"x"
                                    #jl=binascii.unhexlify(binary_to_data % n)
                                    #print(len(jl))
                                    #
                                    #
                                    #print(len(jl))
                                    
                                    Times3+=1  
                                    #print(Times3)
                                    if len(INFO2)<=256 or Times3==((2**48)-1):

                                       INFO3="1"+Bias3+Bias2+INFO3
                                       long_file=len(INFO3)
                                       add_bits118=""
                                       count_bits=8-long_file%8
                                       z=0
                                       if count_bits!=8:
                                           while z<count_bits:
                                               add_bits118="0"+add_bits118
                                               z=z+1
                                       INFO3=add_bits118+INFO3
                                       B1=format(Long_file,'032b')
                                       B5=format(Times3,'048b')
                                       B7="0"+str(Byte_Divide)+"b"
                                       B4=format(N11,B7)
                                       INFO3=B4+B1+B5+INFO3
                                       Finish_file2=INFO3
                                       Times3=0
                                       #print(Times3)
                                       if Finish_file1==Finish_file2:
                                           INFO3=Start_file
                                           Times=1
                                       else:
                                           N_Start=N_Start+Divide_Number
											                                                                                            
											                                                                                            
											                                                                                            
                                    
                                    
                                    #print(Times)
                                if Times==1:
                                        

                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(INFO2)
                                        #os.system("pause")
                                        
                                        
                                            
               
                                        n = int(INFO3, 2)
                                        binary_to_data=len(INFO3)
                                        binary_to_data=(binary_to_data/8)*2
                                        binary_to_data=str(binary_to_data)
                                        binary_to_data="%0"+binary_to_data+"x"
                                        jl=binascii.unhexlify(binary_to_data % n)
                                        #
                                        #
                                        #print(len(jl))
                                            
                                      
                                        Times1=1
                                     
                                            
                                            
                                            #print(Times1)
                                            
                                        if Times1==1:
                                        
                                                Times_Finish=10
                                                if Times_Finish==10:
                                                       

                                                       
                                                   
                                                       
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)                                  

                           
    
            
    def cryptograpy_compression(self):                       
                    if namez=="c":
                        name = input("What is name of file? ")
                        if os.path.exists(name):
                           print('Path is exists!')
                        else:
                            print('Path is not exists!')
                            raise SystemExit
                        namea=""
                        namem=""
                        namema="?"
                        
                        
                       
                        
                        count3=0
                        count4=-1
                       
                        Times1=0
                        Times3=0
                        Times_of_compression=0
                        
              

                        Times=0
                        
                        
                        nameas=name
                        
                        Save_name=len(nameas)

                        long=len(name)
                   
                        name_cut=len(".bin")
                    
                        nameas=name+".bin" 
                        countraz=0
                        Times_change_info=2
                        Times_change_info1=0
                        s=""
                        
                        
                        
                        c=2
                        
                        
                       
                        INFO3=""

                        ssTimes_change_info=0
                        
                        

                        block=0

                        x=0
                        x1=0
                        x2=0
                        x = time()
                       
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            
                            data = binary_file.read()

                        
                            s=str(data)
                            long_file1=len(data)
                            #print(long_file1)
                            
                            

                            if long_file1<2**24:
                                Long_Divide_size_of_file=2**24
                                Byte_Divide=32

                            elif long_file1<2**32:
                                Long_Divide_size_of_file=2**32
                                Byte_Divide=32
                                
                            long_file5=len(data)
                            
                            if long_file1>(2**32)-1:
                                print("This file is too big");
                                raise SystemExit
                            if long_file1==0:
                            	raise SystemExit
                            
                            Times_Finish=0
                            
                            Times_Plus=0
                            while Times_Finish<10:
                          
                                
                                
                                
                                Times_change_info=Times_change_info+1
                                
                                countraz=countraz+1

                                with open(nameas, "ab") as f2:
                                    if countraz==1:
                                        INFO=bin(int(binascii.hexlify(data),16))[2:]
                                        long_file=len(INFO)
                                        
                                        long_file1=len(data) 
                                        xc=(long_file1*8)-long_file
                                        z=0
                                        if xc!=0:
                                            while z<xc:
                                                INFO="0"+INFO
                                                z=z+1
                                        INFO2=INFO
                                        long_file3=len(INFO2)
                                    long_file2=len(INFO2)  
                                    block3=0
                                    INFO3=""
                                    INFO5=""
                                    INFO8=""
                                    INFO4=""
                                    
                                    count3+=1
                                    #print(count4)
                                    #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                    #print(len(INFO2))
                                    F=0
                                    B=0
                                    count4=-1
                                 
                                    long_file2=len(INFO2)
                                    #print(long_file2)
                                    N2=-1
                                    N1=1
                                    N5=0
                                    long2=1
                                    
                                    N8=len(INFO2)
                                    long_file14=N8+1
                                    while N1!=0:
                                        N2+=1
                                        long_file14-=1
                                        long=len(INFO2)
                                        long2=long-N2
                                        if long2<=0:
                                            B=1
                                            N1=0
                                        if B==0:
                                            N=int(INFO2[:long-N2],2)
                                            if N==0:
                                                B=1
                                                N1=0
                                            N5=N//long_file14
                                            N1=N%long_file14
                                    	#print(N2)
                                    Bias=bin(N5)[2:]
                                    if N5==0:
                                    	B=1
                                    long61=len(Bias)
                                    long62=0
                                    if B==0:
                                    	long62=len(INFO2[long-N2:])
                                    NS=long61
                                    NS1=N8-long62
                                    NS2=NS1-1-long61
                                    Nj=len(bin(N2)[2:])
                                    #print(N2)
                                    if Nj>(2**64)-1:
                                        B=1
                                    
                                    
                                    
                                    B6="0"+str((2**6)-1)+"b"
                                    if Times3==0:
                                    	Bias2=format(N2,B6)
                                    	
                                    	
                                    	
                                    	N1=1
                                    	N5=0
                                    	N6=0
                                    	N11=Long_Divide_size_of_file
                                    	#print(N11)
                                       
                                        
                                     
                                       
                                    	
                                    	long=len(INFO2)
                                    	N=int(INFO2,2)
                                    	while N6!=1:
                                    		N11-=1
                                    		#print(N11)
                                    	
	                                    	
	                                    
	                                    	
	                                    	
	                                    	#print(N)
	                                    	if N==0:
	                                    		N11=1
	                                    		N6=1	                                    
	                                    	if N11==0:
	                                    		N11=(Long_Divide_size_of_file)-1
	                                 
	                                    	N5=N//(N11)
	                                    	
	                                    	N1=N%(N11)
	                                    	
	                                 
	                                   
	                                  
	                                	                                   
	                                    	#print(N5)
	                                    	if N1==0 and N5!=0:
	                                    		N6=1
                                                            
                                    Bias3=format(N2,B6)
                                    
                                    Minus1=len(INFO2)
                                    INFO5=Bias+INFO2[long-N2:]
                                    #print(len(INFO5))
                                    Minus1_1=int(INFO5,2)
                                    Minus1-=3
                                    C1="0"+str(Minus1)+"b"
                                    C2="0"+str(Minus1+3)+"b"
                                    INFO4=format(Minus1_1,C1)
                                    INFO6=format(Minus1_1,C2)
                                    Minus1_1_1=len(INFO4)
                                    if Minus1==Minus1_1_1 and B==0:
                                        B=0
                                    else:
                                        B=1
                                  
                                    
                                    	   
                               
                                    if B==0:#compress
                                    	INFO3="1"+INFO4
                                    #print(N2)
                                    if B==1:#not_compress
                                    	INFO3="0"+INFO6
                                    
                                    INFO8=""
                                    Circle=0
                                    Long888=len(INFO3)
                                    while Circle<Long888:
                                      if INFO3[Circle:Circle+1]=="0":
                                        
                                        INFO8=INFO8+"1"
                                      if INFO3[Circle:Circle+1]=="1":  
                                        INFO8=INFO8+"0"
                                      Circle+=1

                                    INFO3=INFO8
                                    INFO2=INFO3
                                    #print(len(INFO3))
                                    #n = int(INFO2, 2)
                                                                                                    
                                            
                                    #n = int(INFO2, 2)                                                                                     
                                            
                                    #binary_to_data=len(INFO2)
                                    #binary_to_data=(binary_to_data/8)*2
                                    #binary_to_data=str(binary_to_data)
                                    #binary_to_data="%0"+binary_to_data+"x"
                                    #jl=binascii.unhexlify(binary_to_data % n)
                                    #print(len(jl))
                                    #
                                    #
                                    #print(len(jl))
                                    
                                    Times3+=1  
                                    if len(INFO2)<=256 or Times3==((2**48)-1):
                                        #print(Bias2)

                                        INFO3="1"+Bias3+Bias2+INFO3
                                        long_file=len(INFO3)
                                        add_bits118=""
                                        count_bits=8-long_file%8
                                        z=0
                                        if count_bits!=8:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                        INFO3=add_bits118+INFO3
                                        Times=1
                                        B1=format(long_file1,'032b')
                                        B5=format(Times3,'048b')
                                        B7="0"+str(Byte_Divide)+"b"
                                    
                                        B4=format(N11,B7)
                                        INFO3=B4+B1+B5+INFO3
                                    
                                    
                                    #print(Times)
                                    if Times==1:
                                        

                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(INFO2)
                                        #os.system("pause")
                                        
                                        
                                            
               
                                        n = int(INFO3, 2)
                                        binary_to_data=len(INFO3)
                                        binary_to_data=(binary_to_data/8)*2
                                        binary_to_data=str(binary_to_data)
                                        binary_to_data="%0"+binary_to_data+"x"
                                        jl=binascii.unhexlify(binary_to_data % n)
                                        #
                                        #
                                        #print(len(jl))
                                            
                                      
                                        Times1=1
                                     
                                            
                                            
                                            #print(Times1)
                                            
                                        if Times1==1:
                                        
                                                Times_Finish=10
                                                if Times_Finish==10:
                                                       

                                                       
                                                   
                                                       
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)        
                                                                                  														    
                                         



   



            
                     

d=compression()

xw1=d.cryptograpy_unpack()
print(xw1)

xw=d.cryptograpy_compression()
print(xw)
