#include<bits/stdc++.h>
using namespace std;

pair<int,int> twosum(vector<int> nums, int target){

    int L = 0;
    int R = nums.size()-1;
    while (L < R){
        int s = nums[L]+nums[R];
        if(s == target){
            return {nums[L],nums[R]};
        }

        else if(s<target){
            L++;
        }
        else{
            R--;
        }
    }
}

int main(){

    vector<int> nums = {1,2,3,4};
    int target = 5;
    pair<int,int> answer = twosum(nums,target);
    cout<<answer.first<<" "<<answer.second<<endl;
}