#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<int> nums(N);
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }
    
    int xor_all = 0;
    for (int num : nums) {
        xor_all ^= num;
    }
    
    int result = 0;
    for (int num : nums) {
        result = max(result, xor_all ^ num);
    }
    result = max(result, xor_all); // 0과의 XOR은 원래 값과 같음
    
    cout << result << result << "\n";
    
    return 0;
}