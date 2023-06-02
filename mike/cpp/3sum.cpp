#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

vector<vector<int>> threeSum(vector<int> &nums) {
    vector<vector<int>> triplets;
    int n = nums.size();
    sort(nums.begin(), nums.end());
    int zero_idx = -1;
    int pos_idx = -1;
    unordered_set<int> s;
    for (int i = 0; i < n; i++) {
        s.insert(nums[i]);
        if (zero_idx == -1 && nums[i] == 0) zero_idx = i;
        if (pos_idx == -1 && nums[i] > 0) pos_idx = i;
    }
    if (zero_idx > -1 &&
        ((pos_idx - zero_idx > 2) || (pos_idx == -1 && n - zero_idx > 2))) {
        triplets.push_back({0, 0, 0});
    }

    return triplets;
}

int main() {
    vector<int> nums = {-1, 0, 0, 0, 1, 2, -1, -4};
    vector<vector<int>> res = threeSum(nums);
    for (auto v : res) {
        for (int num : v) {
            cout << num << ' ';
        }
        cout << endl;
    }
}