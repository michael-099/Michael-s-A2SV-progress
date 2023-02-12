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
    ListNode* reverseList(ListNode* head) {
        if(head==nullptr){
            return head;
        }
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next = curr->next;
        while(curr!=nullptr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> v;
        if(head==nullptr || head->next==nullptr){
            v.push_back(0);
            return v;
        }
        stack<int> s;
        s.push(0);
        head = reverseList(head);
        while(head!=nullptr){
            if(head->val < s.top()){
                v.push_back(s.top());
                s.push(head->val);
            }
            else{
                while(s.size()>1 && head->val>=s.top()){
                    s.pop();
                }
                v.push_back(s.top());
                s.push(head->val);
            }
            head = head->next;
        }
        reverse(v.begin(),v.end());
        return v;

    }
};
