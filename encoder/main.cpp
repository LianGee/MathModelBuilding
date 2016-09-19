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


int getcode(string s){
	string code[16] = {"AA", "AC", "AG", "AT",
						"CA", "CC", "CG", "CT",
						"GA", "GC", "GG", "GT",
						"TA", "TC", "TG", "TT",
	};
	for(int i = 0; i < 16; i++){
		if(code[i] == s)return i;
	}
	return -1;
}


int main()
{
    string **genoType;
    genoType = new string* [1001];    
    for(int i=0; i<1001; i++){
        genoType[i] = new string[9445];
    }
    
    int** statistic;
    statistic = new int* [9445];
    for(int i = 0; i < 9445; i++){
		statistic[i] = new int[16];
		for(int j = 0; j < 16; j++){
			statistic[i][j] = 0;
		}
	}
    
    ifstream in;
    string str;
    string takens[9445];
    string rs;
    string header[9445];
    int code = 0;
    
    
    
    in.open("genotype.dat");
    if(!(in.is_open())){
        cout<<"The file can't be open!"<<endl;
        return -1;
    }
    getline(in, rs);//位点信息读入 
    takeSubstring(rs, header);
    
    for(int i=0; i<500; i++){//统计编码对  前500 个样本 
        getline(in, str);        
        takeSubstring(str, takens);
        for(int j=0; j<9445;j++){
        	code = getcode(takens[j]);
        	if(code != -1){//没有脏数据时 
				statistic[j][code] += 1;
			}
            //genoType[i][j]=takens[j];
        }
    }
    freopen("healthy.txt", "w+", stdout);
    for(int i = 0; i < 9445; i++){
    	//cout << header[i] << " ";
		for(int j = 0; j < 16; j++){
			cout << statistic[i][j] << " ";
		}
		cout << endl;
	}
    
    
    for(int i=0; i<500; i++){//统计编码对 后500个样本 
        getline(in, str);        
        takeSubstring(str, takens);
        for(int j=0; j<9445;j++){
        	code = getcode(takens[j]);
        	if(code != -1){//没有脏数据时 
				statistic[j][code] += 1;
			}
            //genoType[i][j]=takens[j];
        }
    }
    freopen("unhealthy.txt", "w+", stdout);
    for(int i = 0; i < 9445; i++){
    	//cout << header[i] << " ";
		for(int j = 0; j < 16; j++){
			cout << statistic[i][j] << " ";
		}
		cout << endl;
	}
    in.close();
    

    
    return 0;
}

