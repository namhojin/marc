import os
import sys

print ('Path : '+os.getcwd());


print('-----------------------FILE IO-----------------------');

#읽어오기

oFile = open(sys.argv[1], "r", encoding='utf-16');
marc = oFile.readlines();

#쓰기
NewFile = open(sys.argv[1][:-4]+'_940.mrc', "w", encoding='utf-16');

def list_marc(marc):
    count =0;
    marc1=[];
    while len(marc)>count :
        if marc[count] != "\n":
            marc1.append(marc[count]);
        count=count+1;
    return marc1
    
#코라스 반출시 \n 값이 같이 나와서 짝수만 리스트업
marc = list_marc(marc);

print ('--------------------------MARC---------------');
print (marc);
print ('---------------------------------------------');

marc_num = len(marc);


print ("marc num : ",marc_num);

num=0;
directory_num = 0;
comp =0;
len_245 =0;
start_245 =0;
start_data=0;
len_total=0;
change_marc=[];

while num<marc_num :
    print ('--------------------------MARC[',num,']---------------');

    start_data = int (str(marc[num][12:17]));
    print ('start_data : ',start_data);
    
    len_total = int(str(marc[num][0:5]));
    
    #디렉토리 갯수 확인
    directory_num= int ((start_data-25)/12);
    print ('directory_num : ',directory_num);

    print("Last directory : ",marc[num][start_data-13:start_data-1]);

    #디렉토리 기호 찾기
    while directory_num > 0 :
        comp = int (marc[num][12*(directory_num-1)+24:12*(directory_num-1)+27]);
        #245 tag 찾기
        if comp == 245 :
            start_245 = int (marc[num][24+12*(directory_num-1)+7:24+12*(directory_num-1)+12]);
            
            len_245 = int (marc[num][24+12*(directory_num-1)+3:24+12*(directory_num-1)+7]);
           
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
    
    #tag b 시작 반환
    if tag_245.find(":b") > -1:
        find_b=tag_245.find(":b")+3;
        print("tag b 시작위치 : ",find_b);
        #print(tag_245[tag_245.find(":b")]);
        print("tag b : ",end='');
        while tag_245[find_b] != "":
            tag_b=tag_b+tag_245[find_b];
            find_b=find_b+1;
        tag_b=tag_b[:-1];
        print(tag_b);
        #tag a 시작 반환
        if tag_245.find("a") > -1:
            find_a=tag_245.find("a")+2;
            print("tag a 시작위치 : ",find_a);
            print("tag a : ",end='');
            while tag_245[find_a] != "":
                tag_a=tag_a+tag_245[find_a];
                find_a=find_a+1;
            tag_a=tag_a[:-1];
            print(tag_a);
        tag_940="0 a"+tag_a+" "+tag_b+"";
        print("tag 940 : ",tag_940);
        
        marc[num]=marc[num][:-2];
        marc[num]=marc[num]+tag_940+"";
               
        len_total = len_total + len(tag_940);
        len_total=str(len_total);
        len_total_str=len_total.zfill(5);
        print("len_total : ",len_total_str);
        
        start_data_str=str(start_data+12);
        start_data_str=start_data_str.zfill(5);
        print("start_data : ",start_data_str);
        
        
        header = len_total_str + marc[num][5:12]+start_data_str;
        
        print("header :",header);
        
        marc[num]=marc[num][17:];
        marc[num]=header+marc[num];
        
        
        tmp_1=marc[num][:start_data-1];
        tmp_2=marc[num][start_data-1:];
        
        print("tmp1 ---",tmp_1);
        print("tmp2 ---",tmp_2);
        len_940_str = str(len(tag_940));
        len_940_str = len_940_str.zfill(4);
        
        #마지막 디렉토리 길이
        last_dir_len=int(marc[num][start_data-10:start_data-6]);
        #마지막 디렉토리 시작위치
        last_dir_start=int(marc[num][start_data-6:start_data-1]);
        creat_dir_start = last_dir_len+last_dir_start;
        creat_dir_start = str(creat_dir_start);
        creat_dir_start = creat_dir_start.zfill(5);
        print(last_dir_len);
        print(last_dir_start);
        
        marc[num] = tmp_1 +"940"+ len_940_str +creat_dir_start+ tmp_2;
        
        change_marc.append(num);
    
    NewFile.writelines(marc[num]);
    
    print (marc[num]);
    print ('------------------------------------------------------'); 
    
    num = num+1;

print("change_marc : ",change_marc);

oFile.close();
NewFile.close();

print("created by hojnam23@gmail.com");

