class Solution {
 public:
  vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    vector<float> v1;
    vector<vector<int>> v2;
    for (int i = 0; i < points.size(); i++) {
      int j = 0;
      float x = sqrt((pow(points[i][j], 2)) + (pow(points[i][j + 1], 2)));
      v1.push_back(x);
    }
   
    for (int j = 0; j < v1.size() - 1; j++) {
      for (int i = 0; i < v1.size() - 1; i++) {
        if (v1[i] > v1[i + 1]) {
          float temp;
          temp = v1[i];
          v1[i] = v1[i + 1];
          v1[i + 1] = temp;
          vector<int> temp2;
          temp2 = points[i];
          points[i] = points[i + 1];
          points[i + 1] = temp2;
        }
      }
    }
    //    for (int i = 0; i < v1.size(); i++) {
    //   cout << v1[i] << " ";
    // }
  
    // for (int j = 0; j < v1.size(); j++) {
    //   for (int i = 0; i < points.size(); i++) {
    //     cout << points[j][i] << " ";
    //   }
    //   cout << endl;
    // }
    for (int j = 0; j < k; j++) {
      v2.push_back(points[j]);
    }

    return v2;
  }
};
