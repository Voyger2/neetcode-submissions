class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n= nums.size();
       unordered_map<int, int> mpp;
        for(int i=0 ; i<n ; i++){
            mpp[nums[i]]++; //count
        }
        for(int i=0 ; i<n; i++){
            if(mpp[nums[i]]>1){
                return 1;
            }
        }
        return 0;
    }
};