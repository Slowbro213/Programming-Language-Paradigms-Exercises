// memory saving String class
// overload assignment and copy constructor

#include <iostream>
#include <cstring>
#include <unordered_map>

using namespace std;

struct MyHashFunction {
    size_t operator()(const char* key) const {
        size_t hashValue = 0;
        for (int i = 0; key[i] != '\0'; i++) {
            hashValue = 37 * hashValue + key[i];
        }
        return hashValue;
    }

};

struct MyEqualFunction {
    bool operator()(const char* str1, const char* str2) const {
        return strcmp(str1, str2) == 0;
    }
};

class StrCount {
private:
    int count;
    char* str;
    explicit StrCount(char* s) {
        str = s;
        count = 1;
    }
    ~StrCount() {
        cout<<"Deleting string: "<<str<<endl;
        delete[] str;
    }
    friend class String;
    friend class Pstring;
};

class String {
protected:
    StrCount* pStrCnt;
    static unordered_map<const char*, StrCount*,MyHashFunction,MyEqualFunction> strMap;
public:
    String() {
        char* key = new char[1];
        *key = '\0';
        if(strMap.find(key) == strMap.end()){
            pStrCnt = new StrCount(key);
            strMap[key] = pStrCnt;
        }
        else {
            pStrCnt = strMap[key];
            pStrCnt->count += 1;
        }
    }
    String(char* s) {
        if(strMap.find(s) == strMap.end()){
            char* key = new char[strlen(s)+1];
            strcpy(key,s);
            pStrCnt = new StrCount(key);
            strMap[key] = pStrCnt;
        }
        else {
            pStrCnt = strMap[s];
            pStrCnt->count += 1;
        }
    }
    String(String& s) { // copy constructor
        pStrCnt = s.pStrCnt;
        pStrCnt->count += 1;
    }
    virtual ~String() {
        cout<<"deleting String obj with StrCount object: "<<pStrCnt<<" "<<pStrCnt->str<<endl;
        if(pStrCnt -> count == 1){ // we are its last user
            strMap.erase(pStrCnt->str);
            delete pStrCnt;
        }
        else
            pStrCnt->count -= 1;
    }
    void display() {
        cout << pStrCnt->str;
        cout << " (addr=" << pStrCnt << ")" << endl;
    }

    String& operator = (String& s) { // assignment operator
        if(this == &s) return *this;
        if(pStrCnt==s.pStrCnt) return *this;
        if(pStrCnt->count == 1){
            strMap.erase(s.pStrCnt->str);
            delete pStrCnt;
        }
        else
            pStrCnt->count -= 1;
        pStrCnt = s.pStrCnt;
        pStrCnt->count += 1;
        return *this;
    }

    bool operator == (String& s) {
        return pStrCnt==s.pStrCnt;
    }
    bool operator != (String& s) {
        return pStrCnt!=s.pStrCnt;
    }
    bool operator < (String& s) {
        return strcmp(pStrCnt->str, s.pStrCnt->str) < 0;
    }
    bool operator > (String& s) {
        return strcmp(pStrCnt->str, s.pStrCnt->str) > 0;
    }
    bool operator <= (String& s) {
        return strcmp(pStrCnt->str, s.pStrCnt->str) <= 0;
    }
    bool operator >= (String& s) {
        return strcmp(pStrCnt->str, s.pStrCnt->str) >= 0;
    }
    char operator [] (int i) {
        if(i < 0 || i > strlen(pStrCnt->str)-1) throw out_of_range("index out of range");
        return pStrCnt->str[i];
    }
    String operator + (String& s) {
        char* newStr = new char[strlen(pStrCnt->str) + strlen(s.pStrCnt->str) + 1];
        strcpy(newStr, pStrCnt->str);
        strcat(newStr, s.pStrCnt->str);
        String toreturn(newStr);
        delete[] newStr;
        return toreturn;
    }

};

unordered_map<const char*, StrCount*,MyHashFunction,MyEqualFunction> String::strMap = unordered_map<const char*, StrCount*,MyHashFunction,MyEqualFunction>();

class Pstring : public String {

private:

    void DoTheRest(char* newStr)
    {
        StrCount* pstrcnt = this->pStrCnt;
            if(strMap.find(newStr) == strMap.end()){
               char* key = new char[strlen(newStr)+1];
                strcpy(key,newStr);
                pStrCnt = new StrCount(key);
                strMap[key] = pStrCnt;
            }
            else {
                pStrCnt = strMap[newStr];
                pStrCnt->count += 1;
            }
            delete[] newStr;
            pstrcnt->count-=1;
            if(pstrcnt->count==0){
                strMap.erase(pstrcnt->str);
                delete pstrcnt;}
    }

public:

    Pstring() : String() {}
    Pstring(char* s) : String(s) {}

    void assignLeftMost(Pstring& s1, int n)
    {
        char* newStr = new char[n+1];
        for(int i=0;i<n;i++)
            newStr[i] = s1[i];
        newStr[n] = '\0';
        DoTheRest(newStr);
    }

    void assignRightMost(Pstring& s1, int n)
    {
        char* newStr = new char[n+1];
        for(int i=0;i<n;i++)
            newStr[i] = s1[strlen(s1.pStrCnt->str)-n+i];
        newStr[n] = '\0';
        DoTheRest(newStr);
    }

    void assignMid(Pstring& s1, int start, int n)
    {
        char* newStr = new char[n+1];
        for(int i=0;i<n;i++)
            newStr[i] = s1[start+i];
        newStr[n] = '\0';
        DoTheRest(newStr);
    }
};

int main() {

    String s1("hello");
    String s2("hello");
    String s3("Hello");
    String s4;
    String s5;
    String s6("hel");
    String s7("lo");
    String s8 = s6 + s7;
    String s9 = s3;
    s1.display();
    s2.display();
    s3.display();
    s4.display();
    s5.display();
    s6.display();
    s7.display();
    s8.display();
    s9.display();
    s9=s8;
    s9.display();
    Pstring S1("hello567hello345hello");
    Pstring S2;
    S2.assignLeftMost(S1, 4);
    S2.display();
    S2.assignMid(S1,8,6);
    S2.display();
    S2.assignRightMost(S1,6);
    S2.display();
}
