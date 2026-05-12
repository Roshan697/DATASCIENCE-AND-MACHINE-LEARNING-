#include<bits/stdc++.h>
using namespace std;

int maxSum(vector<int> &a, int k){
    int current_sum = 0;
    int best_sum = 0;

    for(int i = 0; i < k; i++){
        current_sum += a[i];
        best_sum = current_sum;
    }

    for(int i = k; i<a.size(); i++){
        current_sum += a[i] -a[i-k];
        best_sum = max(best_sum,current_sum);
    }
    return best_sum;
}

int main(){
    
    vector<int> a = {2,1,5,1,3,2};
    int k = 3;
    cout<<"Maximum sum is: "<<maxSum(a,k)<<endl;
}