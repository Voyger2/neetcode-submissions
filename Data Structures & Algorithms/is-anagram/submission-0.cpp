class Solution {
public:
    bool isAnagram(string s, string t) {
        int n1=s.size();
        int n2=t.size();
       if(n1 != n2){
        return false;
       }
        unordered_map <char,int> mpp1;
        unordered_map <char,int> mpp2;
       for(int i=0; i<n1; i++){
        mpp1[s[i]]++;
       }
       for(int i=0; i<n2;i++){
        mpp2[t[i]]++;
       }
       if(mpp1==mpp2){
        return true;
       }
       else{
        return false;
       }
        
       
    }
};
