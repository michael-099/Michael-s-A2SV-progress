/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> v;
        vector<int> v2;
        bool flag=true;
       // cout<< head->val<<"''";
    ListNode*mynode=head;
    //cout<< mynode->val;
    int i=0;
    while(mynode!=NULL){
        v.push_back(mynode->val);
        mynode=mynode->next;
        i++;
       // cout<<i;
    }

   
    // for(int k : v){
    //     cout<<k;
    // }
    for(int i=v.size()-1;i>=0;i--)
    {
v2.push_back(v[i]);
 }
    // for(int k : v2){
    //     cout<<k;
    // }
    for (int i=0;i<=v.size()-1;i++){
        if(v[i]!=v2[i]){
            flag=false ;
        }
    }
    return flag;}
};
