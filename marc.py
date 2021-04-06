import os
import sys

print ('Path : '+os.getcwd());



print('-----------------------FILE IO-----------------------');

#oFile = open('C:\\python\\tt.mrc', "r", encoding='utf-16');
#marc = oFile.read().split('');

#oFile = open('D:\\GitHub\\samples\\193201반출.mrc', "r", encoding='utf-16');
oFile = open('D:\\GitHub\\samples\\코라스반출_16le.mrc', "r", encoding='utf-16');
marc = oFile.readlines();

#marc=[marc2.rstrip() for marc2 in marc]



print ('--------------------------MARC---------------');
print (marc);
print ('---------------------------------------------');
marc_num = int((len(marc)+1)/2);

count =0;


print ("marc num : ",marc_num);

num=0;
directory_num = 0;
comp =0;
len_245 =0;
start_245 =0;
start_data=0;
while num<marc_num*2-1 :
    print ('--------------------------MARC[',num,']---------------');
    start_data = int (str(marc[num][12])+str(marc[num][13])+str(marc[num][14])+str(marc[num][15])+str(marc[num][16]));
#    print ('start_data : ',str(marc[num][12]),str(marc[num][13]),str(marc[num][14]),str(marc[num][15]),str(marc[num][16]));
    print ('start_data : ',start_data);
    #디렉토리 갯수 확인
    directory_num= int ((start_data-25)/12);
    print ('directory_num : ',directory_num);
    #print ('directory num :',(int(str(marc[num][12])+str(marc[num][13])+str(marc[num][14])+str(marc[num][15])+str(marc[num][16]))-25)/12);


    
    #디렉토리 기호 찾기
    while directory_num > 0 :
        comp = int (marc[num][24+12*(directory_num-1)]+marc[num][25+12*(directory_num-1)]+marc[num][26+12*(directory_num-1)]);
 #       print (comp);
        #245 tag 찾기
        if comp == 245 :
            start_245 = int (marc[num][24+12*(directory_num-1)+7]+marc[num][24+12*(directory_num-1)+8]+marc[num][24+12*(directory_num-1)+9]+marc[num][24+12*(directory_num-1)+10]+marc[num][24+12*(directory_num-1)+11]);
            
            len_245 = int (marc[num][24+12*(directory_num-1)+3]+marc[num][24+12*(directory_num-1)+4]+marc[num][24+12*(directory_num-1)+5]+marc[num][24+12*(directory_num-1)+6]);
           
            print ('245 tag start :',start_245);
            print ('245 tag length :',len_245);

        directory_num = directory_num -1;
    
    
    
    tag_245="";
    point =0;
    while len_245 > point :
#        print(marc[num][start_data+start_245+point], end='');
        tag_245=tag_245+marc[num][start_data+start_245+point];
        point = point + 1;
        
    print('245 tag :',tag_245);  
    
    tag_a="";
    tag_b="";
    #tag a 시작 반환
    if tag_245.find("a") > -1:
        print("tag a 시작위치 : ",tag_245.find("a"));
    
    #tag b 시작 반환
    if tag_245.find(":b") > -1:
        print("tag b 시작위치 : ",tag_245.find(":b"));
    
    
    
    
    
 #   print('245 tag : ',marc[num][start_data+start_245],marc[num][start_data+start_245+1],marc[num][start_data+start_245+2],marc[num][start_data+start_245+3],marc[num][start_data+start_245+4],marc[num][start_data+start_245+5],marc[num][start_data+start_245+6],marc[num][start_data+start_245+7],marc[num][start_data+start_245+8],marc[num][start_data+start_245+9],marc[num][start_data+start_245+10]);
    
    print (marc[num]);
    print ('------------------------------------------------------'); 
    
    num = num+2;

oFile.close();





#print (int(str(marc[0][24])+str(marc[0][25])+str(marc[0][26])));





#print (sys.getdefaultencoding());

#sys.setdefaultencoding(ascii);

#print (sys.getdefaultencoding());