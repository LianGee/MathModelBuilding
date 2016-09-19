#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <sstream>


using namespace std;

void takeSubstring(string &str, string takens[]){
    stringstream ss;
    string subStr;
    ss.str(str);
    int length = 0;
    while(getline(ss, subStr, ' ')){
        takens[length++]= subStr;
    }
}


/*
	TT:0 TC:1 CC:2
*/
bool isSame(string s){
	if(s[0] == s[1]){
		//cout << "isSame"  << endl;
		return true;
	}else return false;
}

void encoder(string* genoType[1001], string *rs){//genoType 1000*9445
	bool first = true;
	string firstSame = "";
	int* genoCode[9445];//一共9445个位点，每个位点有1000个编码 
	for(int i = 0; i < 9445; i++){
		genoCode[i] = new int[1000];
	}	
	
	for(int i = 0; i < 9445; i++){
		first = true;
		for(int j = 0; j < 1000; j++){//跳过rs头部 
			if(genoType[j][i] == "ID" || genoType[j][i] == "II") {//脏数据 
				genoCode[i][j] = -1;
			}
			if(isSame(genoType[j][i])){
				if(first){//如果第一次读到重复标记为0 
					genoCode[i][j] = 0;
					firstSame = genoType[j][i];
					first = false;
				}else if(genoType[j][i] == firstSame){ //和第一次重复的一样的重复对标记为0 
					genoCode[i][j] = 0;
				}else{//再出现重复对标记为2 
					genoCode[i][j] = 2;
				}
			}else{//如果不是重复对标记为1 
				genoCode[i][j] = 1;	
			} 
		}
	}
	
	//写入文件
	freopen("data.txt", "w+", stdout);
	
	//写入头信息 
	cout << "ID		Chr 	Pos 		";
	for(int i = 0; i < 1000; i++){
		if(i < 500){
			cout << 1 << " ";
		}else if(i < 999) cout << 0 <<" ";
		else cout << 0 << endl;
	}
	
	//写入code
	for(int i = 0; i < 9445; i++) {
		cout << rs[i] << "	chr1 	4924223 	";
		for(int j = 0; j < 999; j++){
			cout << genoCode[i][j] << " ";
		}
		cout << genoCode[i][999] << endl;
	}

}

int fun(){
    string **genoType;
    genoType = new string* [1001];    
    for(int i=0; i<1000; i++){
        genoType[i] = new string[9445];
    }
    
    ifstream in;
    string str;
    string takens[9445];
    string rs;
    string header[9445];
    
    in.open("genotype.dat");
    if(!(in.is_open())){
        cout<<"The file can't be open!"<<endl;
        return -1;
    }
    getline(in, rs);//位点信息读入 
    takeSubstring(rs, header);
    
    for(int i=0; i<1000; i++){
        getline(in, str);        
        takeSubstring(str, takens);
        for(int j=0; j<9445;j++){
            genoType[i][j]=takens[j];
        }
    }
    in.close();
    encoder(genoType, header);
    
}

int main()
{

	fun();
    
    return 0;
}

